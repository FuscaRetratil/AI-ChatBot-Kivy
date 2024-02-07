from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button.button import MDRaisedButton
from kivy.core.text import LabelBase
import openai
Window.size = (350, 550)

chave_api = "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"
openai.api_key = chave_api

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
        resposta = openai.client.chat.completions.create (
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": mensagem}
            ],
        )
        return resposta ["choices"][0]["message"]



if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
