from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
#from text import *
sq1,sq2 = 0,0
class Main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=18,size_hint=(0.5, None) 
                          ,height='300sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.text_input = TextInput(multiline=False, size_hint=(0.4, 0.07), 
                                    pos_hint={'center_x': 0.5, 'y': 0})

        lineV.add_widget(self.text_input)

        but = Button(text="Розпочати",size_hint=(0.8, 0.5), 
                     pos_hint={'center_x': 0.5, 'y': 0}, background_color=(0, 1, 0, 0.7) )
        lineV.add_widget(but)

        self.add_widget(lineV)
        but.on_press = self.next_win
    def next_win(self):
        if self.text_input.text == "так":
            self.manager.current = 'first'
            self.manager.transition.direction = "up"
            
class First(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=18,size_hint=(0.5, None) 
                          ,height='500sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        lab = Label(text="Введи першу сторону", color="black")
        lineV.add_widget(lab)
        
        self.text_input2 = TextInput(multiline=False, size_hint=(0.4, 0.07), 
                                    pos_hint={'center_x': 0.5, 'y': 0})

        lineV.add_widget(self.text_input2)

        but = Button(text="Розмір А",size_hint=(0.8, 0.5), 
                     pos_hint={'center_x': 0.5, 'y': 0}, background_color=(0, 1, 0, 0.7) )
        lineV.add_widget(but)

        self.add_widget(lineV)
        but.on_press = self.next_win
    def next_win(self):
        global sq1
        sq1= int(self.text_input2.text)
        self.manager.current = 'second'
        self.manager.transition.direction = "left"


class  Second(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=18,size_hint=(0.5, None) 
                          ,height='500sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        lab = Label(text="Введи другу сторону", color="black")
        lineV.add_widget(lab)
        
        self.text_input3 = TextInput(multiline=False, size_hint=(0.4, 0.07), 
                                    pos_hint={'center_x': 0.5, 'y': 0})

        lineV.add_widget(self.text_input3)

        but = Button(text="Розмір B",size_hint=(0.8, 0.5), 
                     pos_hint={'center_x': 0.5, 'y': 0}, background_color=(0, 1, 0, 0.7) )
        lineV.add_widget(but)

        self.add_widget(lineV)
        but.on_press = self.next_win
    def next_win(self):
        global sq2
        sq2= int(self.text_input3.text)
        self.manager.current = 'three'
        self.manager.transition.direction = "left"


class  Three(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=18,size_hint=(0.5, None) 
                          ,height='500sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        global sq1
        print(sq1)
        lab = Label(text=str(sq1), color="black")
        lineV.add_widget(lab)
        

        but = Button(text="ПОВЕРНУТИ НАЗАД",size_hint=(0.8, 0.5), 
                     pos_hint={'center_x': 0.5, 'y': 0}, background_color=(0, 1, 0, 0.7) )
        lineV.add_widget(but)

        self.add_widget(lineV)
        but.on_press = self.next_win
    def next_win(self):
        self.manager.current = 'main'
        self.manager.transition.direction = "left"

class Win(App):
    def build(self):
        Window.size = (400, 600)
        Window.clearcolor= (1, 1, 0, 1) 
        main_screen= ScreenManager()
        main_screen.add_widget(Main(name='main'))
        main_screen.add_widget(First(name='first'))
        main_screen.add_widget(Second(name='second'))
        main_screen.add_widget(Three(name='three'))
        return main_screen

app = Win()
app.run()