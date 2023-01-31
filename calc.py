import tkinter as tk
from tkinter import messagebox
from re import split


def add_digit(digit):
    value = display.get()
    if value == '0':
        value = value[1:]
    display['state'] = tk.NORMAL
    display.delete(0, tk.END)
    display.insert(0, value + digit)
    display['state'] = tk.DISABLED


def add_operation(operation):
    value = display.get()
    if value[-1] in '/*+-':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value or '√' in value:
        calculate()
        value = display.get()
    display['state'] = tk.NORMAL
    display.delete(0, tk.END)
    display.insert(0, value + operation)
    display['state'] = tk.DISABLED


def calculate():
    display['state'] = tk.NORMAL
    value = display.get()
    if value[0] == '0':
        value = value[1:]
        display.delete(0, tk.END)
    elif value[-1] in '/*+-':
        value = value + value[:-1]
    elif value[0] in '√':
        value = value[:]
    display.delete(0, tk.END)
    try:
        if value[0] == '√':
            value = value[1:]
            try:
                if float(value) < 0:
                    messagebox.showinfo('Error', 'Не число!')
                    display.delete(0, tk.END)
                    display.insert(0, 0)
                display.insert(0, round(pow(float(value), 0.5), 12))
            except ValueError:
                messagebox.showinfo('Error', 'Неверный формат ввода!')
                display.insert(0, 0)
        else:
            display.insert(0, round(eval(value), 12))

    except (NameError, SyntaxError):
        messagebox.showinfo('Error', 'Нужно вводить только цифры и знаки операций!!!')
        display.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'На ноль делить нельзя!!!')
        display.insert(0, 0)
    display['state'] = tk.DISABLED


def sqrt_func(sqrt_arg):
    display['state'] = tk.NORMAL
    display.delete(0, tk.END)
    display.insert(0, sqrt_arg)
    display['state'] = tk.DISABLED


def clear():
    display['state'] = tk.NORMAL
    display.delete(0, tk.END)
    display.insert(0, 0)
    display['state'] = tk.DISABLED


def press_key(event):
    display['state'] = tk.NORMAL
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '/+*-':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\b':
        clear_simbol()
    display['state'] = tk.DISABLED


def clear_simbol():
    display['state'] = tk.NORMAL
    display.delete(len(display.get()) - 1)
    if display.get() == '':
        display.insert(0, 0)
    display['state'] = tk.DISABLED


def procent():
    display['state'] = tk.NORMAL
    try:
        value = float(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, value / 100)
    except SyntaxError:
        messagebox.showinfo('Error', 'Неверное выражение!!!')
        display.delete(0, tk.END)
        display.insert(0, 0)
    display['state'] = tk.DISABLED


def add_point(point):
    display['state'] = tk.NORMAL
    value = display.get() + '.'
    array = split("([+|-|/|*])", value)
    print(array)
    for element in array:
        if element.count('.') > 1:
            messagebox.showinfo('Error', 'Неверное выражение!!!')
            display.delete(0, tk.END)
            display.insert(0, 0)
        else:
            display.delete(0, tk.END)
            display.insert(0, value)
    display['state'] = tk.DISABLED


def press_point(event):
    display['state'] = tk.NORMAL
    if event.char == '.':
        add_point(event.char)
    display['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Pocket Calculator', 14), height=2, width=4,
                     command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Pocket Calculator', 14), fg='red', height=2, width=4,
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=clear)


def make_sqrt_button(sqrt_arg):
    return tk.Button(text=sqrt_arg, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=lambda: sqrt_func(sqrt_arg))


def make_clear_simbol_button(operation):
    return tk.Button(text=operation, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=clear_simbol)


def make_procent_button(operation):
    return tk.Button(text=operation, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=procent)


def make_point_button(point):
    return tk.Button(text=point, bd=5, font=('Pocket Calculator', 14), fg='red',
                     command=lambda: add_point(point))


root = tk.Tk()
root.title('Calculator')

root.bind('<Key>', press_key)
root.bind('.', press_point)
photo = tk.PhotoImage(file='images/calculator.png')
root.iconphoto(False, photo)
root['bg'] = '#828282'

display = tk.Entry(root, justify=tk.RIGHT, font=('Pocket Calculator', 15, 'bold'), width=15)
display.insert(0, '0')
display['state'] = tk.DISABLED
display.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_button('7').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('1').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=1, stick='wens', padx=5, pady=5)

make_operation_button('/').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=4, column=3, stick='wens', padx=5, pady=5)


make_calc_button('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)

make_clear_button('AC').grid(row=1, column=0, stick='wens', padx=5, pady=5)

make_clear_simbol_button('<').grid(row=1, column=1, stick='wens', padx=5, pady=5)

make_procent_button('%').grid(row=1, column=2, stick='wens', padx=5, pady=5)

make_sqrt_button('√').grid(row=5, column=0, stick='wens', padx=5, pady=5)

make_point_button('.').grid(row=5, column=2, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)

root.resizable(False, False)
w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()
