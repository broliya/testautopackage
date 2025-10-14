import flet as ft

def main(page: ft.Page):
    # 设置页面标题
    page.title = "我的第一个 Flet 应用"
    
    # 添加一个文本控件
    page.add(ft.Text(value="你好，世界！"))

# 运行应用
ft.app(target=main)