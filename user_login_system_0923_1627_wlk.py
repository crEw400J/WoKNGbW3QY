# 代码生成时间: 2025-09-23 16:27:24
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
import hashlib

# 用户登录验证系统
class UserLoginSystem(BoxLayout):
    def __init__(self, **kwargs):
        super(UserLoginSystem, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        # 创建用户名输入框
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)
        
        # 创建密码输入框
        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)
        
        # 创建登录按钮
        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)
        
    # 登录验证函数
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        # 检查用户名和密码是否为空
        if not username or not password:
            self.show_error_popup("Username and password cannot be empty.")
            return
        
        # 这里使用简单的哈希函数进行密码验证，实际应用中应使用更安全的验证方式
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # 假设我们有一个有效的用户名和密码哈希值
        valid_username = "admin"
        valid_password_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
        
        # 验证用户名和密码
        if username == valid_username and hashed_password == valid_password_hash:
            self.show_success_popup("Login successful!")
        else:
            self.show_error_popup("Invalid username or password.")
            
    # 显示成功登录弹窗
    def show_success_popup(self, message):
        popup = Popup(title="Success", content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()
        
    # 显示错误信息弹窗
    def show_error_popup(self, message):
        popup = Popup(title="Error", content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# Kivy应用类
class UserLoginApp(App):
    def build(self):
        return UserLoginSystem()

if __name__ == "__main__":
    UserLoginApp().run()
