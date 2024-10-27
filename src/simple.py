import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    if user_input == "Hello":
        messagebox.showinfo("Success", "You entered the correct text!")
    else:
        messagebox.showwarning("Failed", "Incorrect text. Please try again.")

    # 创建主窗口
root = tk.Tk()
root.title("Simple Desktop Client")

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设定窗口尺寸（例如300x200）
window_width = 300
window_height = 200

# 计算窗口在屏幕中央的位置
window_x_position = (screen_width // 2) - (window_width // 2)
window_y_position = (screen_height // 2) - (window_height // 2)

# 设定窗口尺寸和位置
root.geometry(f'{window_width}x{window_height}+{window_x_position}+{window_y_position}')

# 创建一个标签
label = tk.Label(root, text="Enter 'Hello':")
label.pack(pady=10)

# 创建一个文本框
entry = tk.Entry(root)
entry.pack(pady=10)

# 创建一个按钮
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()