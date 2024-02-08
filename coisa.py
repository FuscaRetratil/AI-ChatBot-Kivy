from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button.button import MDRaisedButton
from kivy.core.text import LabelBase
from openai import OpenAI
import openai
import os
Window.size = (350, 550)

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

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
                {"role": "user", "content": mensagem}
            ],
        )
        return resposta ["choices"][0]["message"]
    
print(enviar_mensagem("Quando foi construída a estátua da liberdade?"))

if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
