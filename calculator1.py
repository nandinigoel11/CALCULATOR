from tkinter import*
from tkinter.messagebox import*

font = ('Britannic Bold',22)

def clear():
    result.delete(0,END)

def back():
    z = result.get()
    z = z[0:len(z)-1]
    result.delete(0,END)
    result.insert(0,z)

def clickbtn(event):
    y = event.widget
    text= y['text']

    if text == '=':
        try:
            z = result.get()
            ans = eval(z)
            result.delete(0, END)
            result.insert(0, ans)
            return
        except Exception as e:
            showerror('error',e)

    result.insert(END, text)


scr = Tk()
scr.title('CALCULATOR')
scr.geometry('325x410')

heading = Label(scr, text = 'My Calculator', font=font)
heading.pack(side=TOP)

result = Entry(scr, font = font, justify=RIGHT)
result.pack(side = TOP, pady=10, fill=X, padx=10)

button_frame = Frame(scr)
button_frame.pack(side=TOP, pady=10, padx=10)

x = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(button_frame, text=str(x), font=font, width=4, relief='sunken')
        btn.grid(row=i, column=j, pady=2, padx=2)
        x = x+1
        btn.bind('<Button-1>',clickbtn)

btn1 = Button(button_frame, text='0', font=font, width=4, relief='sunken')
btn1.grid(row=3, column=1, pady=2, padx=2)
btn1.bind('<Button-1>', clickbtn)

btn2 = Button(button_frame, text='.', font=font, width=4, relief='sunken')
btn2.grid(row=3, column=0, pady=2, padx=2)
btn2.bind('<Button-1>', clickbtn)

btn3 = Button(button_frame, text='=', font=font, width=4, relief='sunken')
btn3.grid(row=3, column=2, pady=2, padx=2)
btn3.bind('<Button-1>', clickbtn)

btn4 = Button(button_frame, text='/', font=font, width=4, relief='sunken')
btn4.grid(row=0, column=3, pady=2, padx=2)
btn4.bind('<Button-1>', clickbtn)

btn5 = Button(button_frame, text='*', font=font, width=4, relief='sunken')
btn5.grid(row=1, column=3, pady=2, padx=2)
btn5.bind('<Button-1>', clickbtn)

btn6 = Button(button_frame, text='-', font=font, width=4, relief='sunken')
btn6.grid(row=2, column=3, pady=2, padx=2)
btn6.bind('<Button-1>', clickbtn)

btn7 = Button(button_frame, text='+', font=font, width=4, relief='sunken')
btn7.grid(row=3, column=3, pady=2, padx=2)
btn7.bind('<Button-1>', clickbtn)

btn8 = Button(button_frame, text='C', font=font, width=9, relief='sunken', command=back)
btn8.grid(row=4, column=0, columnspan=2)

btn9 = Button(button_frame, text='AC', font=font, width=9, relief='sunken', command=clear)
btn9.grid(row=4, column=2, columnspan=2)
scr.mainloop()
