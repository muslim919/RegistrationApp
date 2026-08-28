from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class RegistrationForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        title = Label(text="Create Account", font_size=28, size_hint_y=None, height=60)

        self.first_name = TextInput(
            hint_text="First Name", multiline=False, size_hint_y=None, height=50
        )

        self.last_name = TextInput(
            hint_text="Last Name", multiline=False, size_hint_y=None, height=50
        )

        self.email = TextInput(
            hint_text="Email", multiline=False, size_hint_y=None, height=50
        )

        self.password = TextInput(
            hint_text="Password",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50,
        )

        register_button = Button(text="Register", size_hint_y=None, height=55)

        register_button.bind(on_press=self.register)

        self.message = Label(text="", font_size=18)

        self.add_widget(title)
        self.add_widget(self.first_name)
        self.add_widget(self.last_name)
        self.add_widget(self.email)
        self.add_widget(self.password)
        self.add_widget(register_button)
        self.add_widget(self.message)

    def register(self, instance):

        first_name = self.first_name.text.strip()
        last_name = self.last_name.text.strip()
        email = self.email.text.strip()
        password = self.password.text

        if not first_name or not last_name:
            self.message.text = "Please enter your name."
            return

        if not email:
            self.message.text = "Please enter your email."
            return

        if not password:
            self.message.text = "Please enter your password."
            return

        self.message.text = f"Welcome, {first_name} {last_name}!"


class RegistrationApp(App):
    def build(self):
        return RegistrationForm()


if __name__ == "__main__":
    RegistrationApp().run()
