# 代码生成时间: 2025-09-24 15:45:06
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random


class RandomNumberGeneratorApp(App):
    """主应用程序类，负责界面布局和随机数生成逻辑"""
    def build(self):
        # 创建水平布局
        layout = BoxLayout(orientation='horizontal')
        
        # 创建标签显示随机数
        self.random_number_label = Label(text='Random Number:', size_hint=(0.2, None), height=50)
        layout.add_widget(self.random_number_label)
        
        # 创建随机数按钮
        random_button = Button(text='Generate Random Number', size_hint=(0.8, None), height=50)
        random_button.bind(on_press=self.generate_random_number)
        layout.add_widget(random_button)
        
        return layout
    
    def generate_random_number(self, instance):
        """生成随机数并更新标签文本"""
        try:
            # 假设我们生成0到100之间的随机数
            random_number = random.randint(0, 100)
            # 更新标签的文本
            self.random_number_label.text = f'Random Number: {random_number}'
        except Exception as e:
            # 错误处理
            self.random_number_label.text = f'Error: {str(e)}'

if __name__ == '__main__':
    RandomNumberGeneratorApp().run()