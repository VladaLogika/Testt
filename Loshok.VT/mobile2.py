from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


#class Click_but(Button):
#    def __init__(self, Screen, direction = "right", goal = "main", **kwargs):
#        super().__init__(**kwargs)
#        self.screen = Screen
#        self.direction = direction
#        self.goal = goal
#    def on_press(self):
#        self.screen.manager.transition.direction = self.direction
#        self.screen.manager.current = self.goal



class Firsrcreen(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name=name)
        v1 = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'Перейти на інший екран')
        but = Button(text = 'Кнопка два!', size_hint=(.2,1), pos_hint={'left':4})
        btn.on_press = self.next
        v1.add_widget(btn)
        v1.add_widget(but)
        ti = TextInput(text='Hello', halign='right', focus=True,multiline=False)
        self.add_widget(v1)
        v1.add_widget(ti)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name=name)
        btn = Button(text = 'Повернися, повернися!')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'thre'

class ThreScr(Screen):
    def __init__(self, name = 'thre'):
        super().__init__(name=name)
        btn = Button(text = 'далі! ')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'firth'

class FirthScr(Screen):
    def __init__(self, name = 'firth'):
        super().__init__(name=name)
        btn = Button(text = 'ще трохи!')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Firsrcreen())
        sm.add_widget(SecondScr())
        sm.add_widget(ThreScr())
        sm.add_widget(FirthScr())

        return sm

app = MyApp()
app.run()