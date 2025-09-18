# 代码生成时间: 2025-09-18 11:16:12
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# 用户权限管理系统
class PermissionManager:
    def __init__(self):
        self.permissions = {'admin': ['read', 'write', 'delete'],
                         'user': ['read']}
        self.users = {}

    def add_user(self, username, password, role='user'):
        """添加用户并分配权限"""
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = {'password': password, 
                            'role': role}

    def check_login(self, username, password):
        """检查用户登录"""
        if username not in self.users:
            return False
        if self.users[username]['password'] != password:
            return False
        return True

    def get_permissions(self, username):
        """获取用户权限"""
        if username not in self.users:
            raise ValueError("User not found")
        return self.permissions.get(self.users[username]['role'], [])

# Kivy主应用
class MainApp(App):
    def build(self):
        # 创建屏幕管理器
        self.screen_manager = ScreenManager()
        # 添加登录屏幕
        self.add_login_screen()
        # 添加主屏幕
        self.add_main_screen()
        return self.screen_manager

    def add_login_screen(self):
        # 创建登录屏幕布局
        login_screen = Screen(name='login')
        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
        # 创建用户名和密码输入框
        username_input = TextInput(hint_text='Username', multiline=False)
        password_input = TextInput(hint_text='Password', multiline=False, password=True)
        # 创建登录按钮
        login_btn = Button(text='Login', size_hint_y=None, height=dp(40))
        # 创建错误提示标签
        error_label = Label(text='Invalid username or password', size_hint_y=None, height=dp(30), color=[1, 0, 0, 1], halign='center')
        error_label.opacity = 0  # 默认隐藏错误提示
        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(login_btn)
        layout.add_widget(error_label)
        login_screen.add_widget(layout)
        # 设置登录按钮事件处理
        login_btn.bind(on_press=self.on_login)
        self.screen_manager.add_widget(login_screen)

    def add_main_screen(self):
        # 创建主屏幕布局
        main_screen = Screen(name='main')
        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
        # 创建退出按钮
        quit_btn = Button(text='Quit', size_hint_y=None, height=dp(40))
        layout.add_widget(quit_btn)
        main_screen.add_widget(layout)
        # 设置退出按钮事件处理
        quit_btn.bind(on_press=self.on_quit)
        self.screen_manager.add_widget(main_screen)

    def on_login(self, instance):
        # 登录事件处理
        username = self.root.ids['username_input'].text
        password = self.root.ids['password_input'].text
        try:
            if self.permission_manager.check_login(username, password):
                self.screen_manager.current = 'main'
                self.root.ids['error_label'].opacity = 0  # 隐藏错误提示
            else:
                self.root.ids['error_label'].opacity = 1  # 显示错误提示
        except Exception as e:
            print(f"Error: {e}")
            self.root.ids['error_label'].text = str(e)

    def on_quit(self, instance):
        # 退出事件处理
        self.stop()

if __name__ == '__main__':
    # 创建权限管理器实例
    permission_manager = PermissionManager()
    # 添加用户
    permission_manager.add_user('admin', 'admin123', 'admin')
    permission_manager.add_user('user1', 'user123')
    # 创建Kivy应用实例
    MainApp(permission_manager).run()