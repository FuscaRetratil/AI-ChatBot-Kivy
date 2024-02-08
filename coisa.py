from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button.button import MDRaisedButton
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from openai import OpenAI
import os
Window.size = (350, 550)

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class Comando (MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class Response (MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17

class ChatBot(MDApp):

    def mudar_tela(self, nome):
        screen_manager.current = nome

    def build(self):
         global screen_manager
         screen_manager = ScreenManager ()
         screen_manager.add_widget(Builder.load_file("Main.kv"))
         screen_manager.add_widget(Builder.load_file("Chats.kv"))
         return screen_manager
    
    def enviar_mensagem(mensagem):
        resposta = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": mensagem} ],
        )
        return resposta.choices[0].message.content.strip() 

if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
