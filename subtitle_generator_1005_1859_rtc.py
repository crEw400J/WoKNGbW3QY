# 代码生成时间: 2025-10-05 18:59:34
// subtitle_generator.py
# 这是一个使用Python和Kivy框架创建的字幕生成工具
# 它允许用户输入文本并生成对应的字幕文件

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserPopup
from kivy.core.window import Window
import os

class SubtitleGenerator(App):
    # 初始化方法
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text="字幕生成工具"))
        self.text_input = TextInput(multiline=True)
        self.layout.add_widget(self.text_input)
        self.generate_button = Button(text="生成字幕")
        self.generate_button.bind(on_press=self.generate_subtitles)
        self.layout.add_widget(self.generate_button)
        return self.layout

    def generate_subtitles(self, instance):
        # 获取输入文本
        input_text = self.text_input.text
        if not input_text.strip():
            # 空输入处理
            return

        # 创建文件选择器
        content = FileChooserPopup(select=self.save_file)
        content.open()
        
    def save_file(self, selection, button, touch, selection_x, selection_y):
        # 保存字幕文件
        file_path = selection[0] if selection else None
        if file_path and self.write_subtitles(file_path):
            self.show_message("字幕文件已保存！")
        else:
            self.show_message("保存字幕文件失败！")

    def write_subtitles(self, file_path):
        try:
            # 将输入文本保存到文件
            with open(file_path, 'w') as file:
                file.write(self.text_input.text)
            return True
        except Exception as e:
            # 错误处理
            print(f"保存字幕文件时发生错误: {e}")
            return False

    def show_message(self, message):
        # 显示消息
        Window.alert("字幕生成工具", message)

if __name__ == '__main__':
    SubtitleGenerator().run()