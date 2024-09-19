from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        
        # Define labels with appropriate Kivy properties
        head_label = Label(text="Python User Registration App", font_size='26sp', bold=True, height=40)
        name_label = Label(text="Name:", font_size='18sp')
        self.name_input = TextInput(multiline=False, font_size='18sp')
        email_label = Label(text="Email_ID:", font_size='18sp')
        self.email_input = TextInput(multiline=False, font_size='18sp')
        phone_label = Label(text="Phone no.:", font_size='18sp')
        self.phone_input = TextInput(multiline=False, font_size='18sp')
        password_label = Label(text="Password:", font_size='18sp')
        self.password_input = TextInput(multiline=False, font_size='18sp', password=True)
        confirm_label = Label(text="Confirm Password:", font_size='18sp')
        self.confirm_input = TextInput(multiline=False, font_size='18sp', password = True)

        #  Button
        submit_button =Button(text='Register', font_size=18, on_press=self.register)

        # Adding labels to the layout
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(phone_label)
        layout.add_widget(self.phone_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)
        
        return layout
    def register(self, instance):
        # collect information
        name =self.name_input.text
        email = self.email_input.text
        phone = self.phone_input.text
        password =self.password_input.text
        confirm_password =self.confirm_input.text

        #  validation
        if name.strip() ==''or email.strip() == '' or phone.strip()=='' or password.strip()=='' or confirm_password.strip()=='':
           message = "Please fill all the fields\n made by Anant gupta"
        elif password != confirm_password:
            message= "Passwords do not match\n made by Anant gupta"
        else:
            filename =name + '.txt'
            with open(filename, 'w')as file:
                file.write('Name: {}\n'.format(name))    
                file.write('email: {}\n'.format(email))    
                file.write('phone: {}\n'.format(phone))    
                file.write('Password: {}\n'.format(password))  
            message= "Registration successfully completed!\n made by Anant gupta\n Name: {}\nEmail: {}".format(name, email)  

            # popup
        popup = Popup(title= "Registration Status", content=Label(text=message), size_hint=(None,None), size=(400,200))
        popup.open()




if __name__ == "__main__":
    RegistrationApp().run()
