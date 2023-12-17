from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
Window.size = (350, 550)

class ChatBot(MDApp):

    def mudar_tela(self, nome):
        screen_manager.current = nome



    def build(self):
         global screen_manager
         screen_manager = ScreenManager ()
         screen_manager.add_widget(Builder.load_file("Main.kv"))
         screen_manager.add_widget(Builder.load_file("Chats.kv"))
         return screen_manager
    
    



if __name__ == "__main__":
    ChatBot().run()
