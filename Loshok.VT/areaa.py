from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 

class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=8, size_hint = (0.3, None) ,height='200sp', pos_hint={'center_x':0.5, 'center_y':0.5})
        self.text_input = TextInput(multiline = False, size_hint=(0.4, 0.07), pos_hint={'center_x': 0.5, 'y': 0})
        lineV.add_widget(self.text_input)

        but = Button(text='Розпочати', size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'y': 0}, background_color=(2, 0, 0, 0.7))
        lineV.add_widget(but)
        self.add_widget(lineV)
        but.on_press = self.next_window 

    def next_window(self):
        if self.text_input.text == "так":
            self.manager.current = 'first'
            self.manager.transition.direction = "left"

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=8, size_hint = (0.3, None) ,height='200sp', pos_hint={'center_x':0.5, 'center_y':0.5})
        lab = Label(text = "Введи першу сторону")
        lineV.add_widget(lab)
        self.text_input2 = TextInput(multiline = False, size_hint=(0.4, 0.07), pos_hint={'center_x': 0.5, 'y': 0})
        lineV.add_widget(self.text_input2)

        but = Button(text='нанананана', size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'y': 0}, background_color=(2, 0, 0, 0.7))
        lineV.add_widget(but)
        self.add_widget(lineV)
        but.on_press = self.next_window

    def next_window(self):
        self.manager.current = 'second'
        self.manager.transition.direction = "right"

class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=8, size_hint = (0.3, None) ,height='200sp', pos_hint={'center_x':0.5, 'center_y':0.5})
        lab = Label(text = "Введи першу сторону")
        lineV.add_widget(lab)
        self.text_input3 = TextInput(multiline = False, size_hint=(0.4, 0.07), pos_hint={'center_x': 0.5, 'y': 0})
        lineV.add_widget(self.text_input3)

        but = Button(text='Розмір Б', size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'y': 0}, background_color=(2, 0, 0, 0.7))
        lineV.add_widget(but)
        self.add_widget(lineV)
        but.on_press = self.next_window

    def next_window(self):
        self.manager.current = 'three'
        self.manager.transition.direction = "down"

class Three(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation='vertical', padding=8, spacing=8, size_hint = (0.3, None) ,height='200sp', pos_hint={'center_x':0.5, 'center_y':0.5})

        lab = Label(text = str(s), color = 'black')
        lineV.add_widget(lab)
        s = int(self.text_input2) * int(self.text_input3)
        


        but = Button(text='ПОВЕРНУТИ НАЗАД!!!', size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'y': 0}, background_color=(2, 0, 0, 0.7))
        lineV.add_widget(but)
        self.add_widget(lineV)
        but.on_press = self.next_window

    def next_window(self):
        self.manager.current = 'main'
        self.manager.transition.direction = "down"

class Win(App):
    def build(self):
        Window.size = (400,600)
        Window.clearcolor = (2, 0, 1 ,1)
        main_screen = ScreenManager()
        main_screen.add_widget(Main(name = 'main'))
        main_screen.add_widget(First(name = 'first'))
        main_screen.add_widget(Second(name = 'second'))
        main_screen.add_widget(Three(name = 'main'))
        return main_screen
    
app = Win()
app.run()

