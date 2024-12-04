import tkinter as tk

# функция принимающая введённые значения
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


#  функция ответа(удаление предыдущего и вывод нового)
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

#  функция сложения
def add():
    num1, num2 = get_values()
    result_add = num1 + num2
    insert_values(result_add)


# функция вычитания
def sub():
    num1, num2 = get_values()
    result_add = num1 - num2
    insert_values(result_add)


#  функция умножения
def mult():
    num1, num2 = get_values()
    result_mult = num1 * num2
    insert_values(result_mult)


# функция деления
def div():
    num1, num2 = get_values()
    result_div = num1 / num2
    insert_values(result_div)

# окно
window = tk.Tk()
window.title('Калькулятор') # название окна
window.geometry('370x350')  #размер окна
window.resizable(False, False)
# кнопки
button_add = tk.Button(window, text = '+', width= 4, height=2, command=add)
button_add.place(x=100, y=100)

button_sub = tk.Button(window, text= '-', width= 4, height=2, command=sub)
button_sub.place(x=200, y=100)

button_mult = tk.Button(window, text= '*', width= 4, height=2, command=mult)
button_mult.place(x=100, y=200)

button_div = tk.Button(window, text= ':', width= 4, height=2, command=div)
button_div.place(x=200, y=200)

# поля для ввода
number1_entry = tk.Entry(window, width= 28)
number1_entry.place(x=150, y=20)

number2_entry = tk.Entry(window, width= 28)
number2_entry.place(x=150, y=50)

answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=280)

# текст
number1 = tk.Label(window, text= 'Введите первое число: ')
number1.place(x= 1, y=20)

number2 = tk.Label(window, text= 'Введите второе число: ')
number2.place(x= 1, y=50)

number3 = tk.Label(window, text= 'Ответ: ')
number3.place(x= 1, y=280)

window.mainloop()
