import kivy
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        blayout= BoxLayout()
        btn1= Button(text= '1')
        btn2= Button(text= '2')
        btn3= Button(text= '3')
        btn4= Button(text= '4')
        blayout.add_widget(btn1)
        blayout.add_widget(btn2)
        blayout.add_widget(btn3)
        blayout.add_widget(btn4)
        return blayout
MyApp().run()