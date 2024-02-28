from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button.button import MDRaisedButton
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from openai import OpenAI
import os
import pyttsx3

Window.size = (350, 550)

class Comando(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17
class AudioScreen(Screen):
    pass

class ChatBot(MDApp):
    engine = pyttsx3.init("sapi5")
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.built = False

    def mudar_tela(self, nome):
        self.screen_manager.current = nome

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file("Main.kv"))
        self.screen_manager.add_widget(Builder.load_file("chats.kv"))
        self.screen_manager.add_widget(Builder.load_file("Audio.kv"))
        self.screen_manager.add_widget(Builder.load_file("botname.kv"))
        self.screen_manager.add_widget(AudioScreen())
        self.built = True
        return self.screen_manager

    def falar(self):
        self.engine.setProperty("voice", "brazil")
        text_input = self.root.get_screen("audio").ids.text
        texto = text_input.text
        self.engine.say(texto)
        self.engine.runAndWait()

    def bot_name(self):
        if self.screen_manager.get_screen("main").bot_name.text != "":
            self.screen_manager.get_screen("chats").bot_name.text = (
                self.screen_manager.get_screen("main").bot_name.text
            )
            self.screen_manager.current = "chats"

    def enviar_mensagem(self, mensagem):
        resposta = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                # {"role": "system", "content": "You are a highly skilled AI, answer the questions given within a maximum of 500 characters"}
                {"role": "user", "content": mensagem}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return resposta.choices[0].message.content.strip()

    def enviar(self):
        user_input = self.screen_manager.get_screen("chats").ids.user_input.text
        self.screen_manager.get_screen("chats").ids.chat_list.add_widget(
            Comando(text=user_input, size_hint_x=0.2, halign="right")
        )
        resposta = self.enviar_mensagem(user_input)
        self.screen_manager.get_screen("chats").ids.chat_list.add_widget(
            Response(text=resposta, size_hint_x=0.8, halign="left")
        )
        self.screen_manager.get_screen("chats").ids.user_input.text = ""

if __name__ == "__main__":
	LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
	ChatBot().run()