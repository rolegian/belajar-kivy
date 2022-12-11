import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.widget import Widget 

class MyApp(App):
    def build(self):
        wdg= Widget()
        lbl= Label(text= 'Hello world')
        lbl.pos= (200,0)
        btn= Button(text='tombol')
        wdg.add_widget(lbl)
        wdg.add_widget(btn)
        return wdg
MyApp().run()