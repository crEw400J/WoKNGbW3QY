# 代码生成时间: 2025-09-21 19:18:19
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import StringProperty
from random import randint, choice
from string import ascii_letters, digits


# 测试数据生成器应用类
class TestDataGeneratorApp(App):
    def build(self):
        # 创建一个垂直布局
        layout = BoxLayout(orientation='vertical')

        # 创建输入框，让用户输入生成数据的数量
        self.num_input = TextInput(multiline=False)
        layout.add_widget(self.num_input)

        # 创建按钮，用户点击后生成测试数据
        generate_button = Button(text='Generate')
        generate_button.bind(on_press=self.generate_test_data)
        layout.add_widget(generate_button)

        # 创建标签，显示生成的测试数据
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        return layout

    def generate_test_data(self, instance):
        # 获取用户输入的生成数量
        try:
            num = int(self.num_input.text)
        except ValueError:
            self.result_label.text = 'Invalid input! Please enter a number.'
            return
        
        # 生成测试数据
        test_data = ''
        for _ in range(num):
            # 随机生成一个字符串，包含字母和数字
            test_string = ''.join(choice(ascii_letters + digits) for _ in range(10))
            test_data += test_string + '
'
        
        # 显示生成的测试数据
        self.result_label.text = test_data


# 运行应用
if __name__ == '__main__':
    TestDataGeneratorApp().run()