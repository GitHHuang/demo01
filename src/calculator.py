import tkinter as tk
from tkinter import messagebox
import re
from PIL import Image, ImageTk  # 用于加载和显示图像

# 假设的eval_expr模块实现（出于安全考虑，不建议直接使用eval）
# 在实际应用中，你应该使用更安全的方法来解析和计算表达式
# 例如，使用第三方库如 sympy 或自己实现一个解析器
# 下面的代码仅作为示例，并不安全！
def safe_eval(expr):
    # 只允许数字、小数点、加减乘除、括号和空格
    if not re.match(r'^[\d\.\+\-*/\(\) ]+$', expr):
        return None, "Invalid characters in expression"
    try:
        # 使用eval，但限制全局和局部命名空间来减少安全风险
        # 注意：这仍然不是完全安全的！
        result = eval(expr, {"__builtins__": None}, {})
        return result, None
    except Exception as e:
        return None, str(e)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("一个简单的计算器")
        self.root.geometry("400x600")  # 设置窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小

        # 设置窗口背景颜色
        self.root.configure(bg='#f0f0f0')

        # 加载窗口图标（确保有一个名为'calculator_icon.png'的图像文件在同一目录下）
        icon = Image.open("calculator_icon.png")
        icon = ImageTk.PhotoImage(icon.resize((32, 32), Image.ANTIALIAS))
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon)

        self.result_var = tk.StringVar()
        self.entry = tk.Entry(
            root, textvariable=self.result_var, font=('Arial', 24, 'bold'),
            bd=10, insertwidth=4, width=20, borderwidth=4,
            bg='#ffffff', fg='#000000', highlightbackground='#d3d3d3',
            highlightcolor='black'
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=20)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            btn = tk.Button(
                self.root, text=button, padx=20, pady=20, font=('Arial', 18, 'bold'),
                command=action, bg='#e0e0e0', fg='#000000', borderwidth=3,
                relief='ridge', cursor='hand2'
            )
            btn.grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        try:
            if key == "=":
                expression = self.result_var.get()
                result, error = safe_eval(expression)
                if result is not None:
                    self.result_var.set(str(result))
                else:
                    messagebox.showerror("Error", error)
            elif key == "C":
                self.result_var.set("")
            else:
                self.result_var.set(self.result_var.get() + key)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            # 你也可以选择在这里显示一个消息框来通知用户
            # messagebox.showerror("Unexpected Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()