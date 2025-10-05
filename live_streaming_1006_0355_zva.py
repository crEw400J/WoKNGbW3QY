# 代码生成时间: 2025-10-06 03:55:24
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.clock import Clock
# NOTE: 重要实现细节
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
import requests
import json
import cv2
import numpy as np
import queue
import threading
# 添加错误处理

"""
直播推流系统

功能：
- 从摄像头捕获视频流
- 将视频流编码为H.264格式
- 推流到指定的RTMP服务器
"""

class LiveStreamingWidget(Widget):
    def __init__(self, **kwargs):
        super(LiveStreamingWidget, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        self.texture = Texture.create(size=(640, 480), colorfmt='bgr')
        self.texture.bind(on_texture=self.on_texture)
# 添加错误处理
        self.push_stream_url = "rtmp://live.hkstv.hk.lxdns.com/live/hks"  # 推流地址
        self.encoder = cv2.VideoWriter_fourcc(*'H264')
        self.out = cv2.VideoWriter('output.h264', self.encoder, 20.0, (640, 480))
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.push_stream)
        self.thread.start()

    def on_touch_down(self, touch):
        return super(LiveStreamingWidget, self).on_touch_down(touch)

    def on_texture(self, instance, value):
        self.canvas.before.clear()
        self.canvas.add(Color(1, 1, 1, 1))
        self.canvas.add Rectangle(size=(640, 480), texture=self.texture)
# 扩展功能模块

    def push_stream(self):
        while True:
            if not self.queue.empty():
                frame = self.queue.get()
                if frame is None:
                    break
                self.out.write(frame)
                data = frame.tobytes()
                url = f"{self.push_stream_url}?frame={data.hex()}"
# TODO: 优化性能
                response = requests.post(url, data=data)
                if response.status_code != 200:
# NOTE: 重要实现细节
                    print(f"推流失败：{response.text}")
            else:
                time.sleep(0.01)

    def capture_frame(self):
        ret, frame = self.capture.read()
# 增强安全性
        if ret:
            self.out.write(frame)
            self.queue.put(frame)
        else:
            print("捕获失败")
        Clock.schedule_once(self.capture_frame, 1 / 25)

    def on_close(self):
        self.capture.release()
        self.out.release()
        self.queue.put(None)
# FIXME: 处理边界情况
        self.thread.join()
# TODO: 优化性能

class LiveStreamingApp(App):
    def build(self):
        return LiveStreamingWidget()

if __name__ == '__main__':
    LiveStreamingApp().run()