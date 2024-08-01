from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation
from dlatesty import *

#сонячна дощ хмарна сніг

class Mama(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = FloatLayout( size_hint=(1,1))
        anim = Animation(background_color=(.0,.255,.250,0.5), duration = 1.5)
        fotka = Image(source="fotka.png", size_hint=(0.4,0.4), pos_hint={"center_x":0.5, "y":0.3})

        blue = (.0, .255, .250,0.6)
        yellow = (.200, .0, .0,1)
        label1 = Label(text = "Це тест яка ви погода ок?", color=blue, font_size = 30, size_hint=(1,1.5))
        lineV.add_widget(label1)


        label2 = Label(text = "Нажміть кнопку нижче для того щоб почати", color=blue, size_hint=(1,0.5))
        lineV.add_widget(label2)


        but1 = Button(text="Почати тест", size_hint=(0.2,0.1), pos_hint={"center_x":0.5, "y":0.1}, font_size = 18)
        anim.start(but1)
        lineV.add_widget(but1)



        lineV.add_widget(fotka)
        self.add_widget(lineV)
        but1.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main2'
        self.manager.transition.direction = "up"

class Main2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        lineF = FloatLayout(size_hint=(1,1))
        blue = (.0, .255, .250,0.6)
        anim = Animation(background_color=(.0,.255,.250,0.5), duration = 1.5)

        name = Label(text = "Введіть ваше ім'я",color = blue, font_size = 30, size_hint=(1,1.5))
        name1 = TextInput(multiline = False, size_hint=(0.3,0.1), pos_hint={"center_x":0.5, "y":0.5})
        but2 = Button(text="Перейти до тесту", size_hint=(0.2,0.1), pos_hint={"center_x":0.5, "y":0.3})
        anim.start(but2)
        lineF.add_widget(but2)
        lineF.add_widget(name)
        lineF.add_widget(name1)


        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):

        self.manager.current = 'main3'
        self.manager.transition.direction = "up"

class Main3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineS = FloatLayout(size_hint=(1,1))
        sun = Image(source="sun.jpeg", size_hint=(0.2,0.2), pos_hint={"center_x":0.2, "y":0.6})
        rain = Image(source="rain.jpg", size_hint=(0.2,0.2), pos_hint={"center_x":0.5, "y":0.6})
        viter = Image(source="viter.jpg", size_hint=(0.2,0.2), pos_hint={"center_x":0.8, "y":0.6})


        blue = (.0, .255, .250,0.6)
        start = Label(text = "Що ж почнемо тест!",color = blue, font_size = 24, size_hint=(1,1.7))
        lineS.add_widget(start)
        question1 = Label(text = first, color = blue, font_size = 18, size_hint=(1,1))
        lineS.add_widget(question1)




        lineS.add_widget(viter)
        lineS.add_widget(rain)
        lineS.add_widget(sun)
        self.add_widget(lineS)
        

class Win(App):
    def build(self):
        white = (240, 248, 255,0)
        Window.clearcolor = white


        main_screen= ScreenManager()
        main_screen.add_widget(Mama(name='mama'))
        main_screen.add_widget(Main2(name ="main2"))
        main_screen.add_widget(Main3(name="main3"))

        return main_screen




app = Win()
app.run()
