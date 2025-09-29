# 代码生成时间: 2025-09-29 15:38:53
from kivy.network.urlrequest import UrlRequest
from kivy.network.urlrequest import UrlResponse
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.network import buffers
from collections import deque
import socket
import threading
import json

# 定义一个客户端类，用于处理多人游戏网络通信
class GameClient:
    def __init__(self, app):
        self.app = app
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.buffer = deque()
        self.callbacks = {}
        self.lock = threading.Lock()
        self.running = False
        self.url = "http://localhost:8080"  # 服务器地址

    def start(self):
        """启动客户端，连接到服务器"""
        self.running = True
        self.socket.connect((self.url.split(':')[0], int(self.url.split(':')[1])))
        threading.Thread(target=self.receive).start()

    def receive(self):
        """接收服务器发送的数据"""
        while self.running:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                with self.lock:
                    self.buffer.append(data)
            except Exception as e:
                print(f"Error receiving data: {e}")
                break

    def send(self, data):
        """发送数据到服务器"""
        try:
            self.socket.sendall(data.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")

    def process_buffer(self):
        """处理缓冲区中的数据"""
        while self.buffer:
            data = self.buffer.popleft()
            try:
                message = json.loads(data.decode('utf-8'))
                if message['type'] in self.callbacks:
                    self.callbacks[message['type']](message['data'])
            except Exception as e:
                print(f"Error processing buffer: {e}")

    def register_callback(self, message_type, callback):
        "