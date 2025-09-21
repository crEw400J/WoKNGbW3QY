# 代码生成时间: 2025-09-21 10:34:52
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserPopup
import os
import json

# 测试报告生成器类
class TestReportGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='测试报告生成器'))
        self.add_widget(Button(text='选择测试结果文件', on_press=self.open_file))
        self.add_widget(TextInput(multiline=True, readonly=True, hint_text='测试结果文件内容'))
        self.add_widget(Button(text='生成测试报告', on_press=self.generate_report))
        self.file_content = ''

    def open_file(self, instance):
        # 打开文件选择器并读取文件内容
        self.file_picker = FileChooserPopup(select=self.load_file)
        self.file_picker.open()

    def load_file(self, selection):
        # 加载文件内容
        if selection:
            file_path = selection[0]
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.file_content = file.read()
                    self.children[1].text = self.file_content
            except Exception as e:
                self.show_error(f'读取文件失败: {e}')

    def generate_report(self, instance):
        # 生成测试报告
        if not self.file_content:
            self.show_error('请先选择测试结果文件')
            return
        try:
            results = json.loads(self.file_content)
            report_content = self.create_report(results)
            self.save_report(report_content)
        except json.JSONDecodeError as e:
            self.show_error(f'解析测试结果失败: {e}')
        except Exception as e:
            self.show_error(f'生成测试报告失败: {e}')

    def create_report(self, results):
        # 创建测试报告内容
        report_content = '测试报告

'
        # 添加测试结果统计
        total = len(results)
        passed = sum(1 for result in results if result['status'] == 'passed')
        failed = total - passed

        report_content += f'总测试数: {total}
' \
            f'通过测试数: {passed}
' \
            f'失败测试数: {failed}

'
        # 添加测试结果详情
        for result in results:
            report_content += f'测试用例: {result[