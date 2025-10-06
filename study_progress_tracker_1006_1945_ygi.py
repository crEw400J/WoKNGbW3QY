# 代码生成时间: 2025-10-06 19:45:02
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.properties import ListProperty, StringProperty
from kivy.clock import Clock
import json

"""
学习进度跟踪器，使用KIVY框架创建一个简单的GUI应用程序。
用户可以添加和跟踪学习课程的进度。
"""

class Course:
    """学习课程类"""
    def __init__(self, name):
        self.name = name
        self.progress = 0  # 进度百分比

    def update_progress(self, value):
        "