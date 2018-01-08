import tkinter

def clear():
    global result
    entry.delete(0, len(entry.get()))
    result = ''

def backspace():
    global result
    entry.delete(0, len(entry.get()))
    result = result[0: len(result) - 1]
    entry.insert(len(entry.get()), result)
   
def eq():
    global result
    entry.delete(0, len(entry.get()))
    try:
        result = str(eval(result))
        entry.insert(len(entry.get()), result)
    except ArithmeticError:
        entry.insert(len(entry.get()), 'Error')
        result = ''

def bldExpr(x):
    global result
    if entry.get() == 'Error':
        entry.delete(0, len(entry.get()))
    entry.insert(len(entry.get()), str(x))
    result = result + x
    
def main():
    global entry, result
    result = ''
    master = tkinter.Tk()
    master.title("Calulator")
    master.geometry('%dx%d+%d+%d' % (124, 148, 1100, 180))
    entry = tkinter.Entry(master, justify = 'right')
    b0 = tkinter.Button(text = '0', command = lambda: bldExpr('0'))
    b1 = tkinter.Button(text = '1', command = lambda: bldExpr('1'))
    b2 = tkinter.Button(text = '2', command = lambda: bldExpr('2'))
    b3 = tkinter.Button(text = '3', command = lambda: bldExpr('3'))
    b4 = tkinter.Button(text = '4', command = lambda: bldExpr('4'))
    b5 = tkinter.Button(text = '5', command = lambda: bldExpr('5'))
    b6 = tkinter.Button(text = '6', command = lambda: bldExpr('6'))
    b7 = tkinter.Button(text = '7', command = lambda: bldExpr('7'))
    b8 = tkinter.Button(text = '8', command = lambda: bldExpr('8'))
    b9 = tkinter.Button(text = '9', command = lambda: bldExpr('9'))
    decButton = tkinter.Button(text = '.', command = lambda: bldExpr('.'))
    addButton = tkinter.Button(text = '+', command = lambda: bldExpr('+'))   
    subButton = tkinter.Button(text = '-', command = lambda: bldExpr('-'))
    multButton = tkinter.Button(text = 'x', command = lambda: bldExpr('*')) 
    divButton = tkinter.Button(text = '%', command = lambda: bldExpr('/'))
    lParButton = tkinter.Button(text = '(', command = lambda: bldExpr('('))
    rParButton = tkinter.Button(text = ')', command = lambda: bldExpr(')'))
    eqButton = tkinter.Button(text = '=', command = eq)  
    clrButton = tkinter.Button(text = 'C', command = clear)
    delButton = tkinter.Button(text = '<X', command = backspace)
    entry.grid(row = 0, column = 1, columnspan = 4)
    b0.grid(row = 5, column = 1, sticky = 'WENS')
    b1.grid(row = 4, column = 1, sticky = 'WENS')
    b2.grid(row = 4, column = 2, sticky = 'WENS')
    b3.grid(row = 4, column = 3, sticky = 'WENS')
    b4.grid(row = 3, column = 1, sticky = 'WENS')
    b5.grid(row = 3, column = 2, sticky = 'WENS')
    b6.grid(row = 3, column = 3, sticky = 'WENS')
    b7.grid(row = 2, column = 1, sticky = 'WENS')
    b8.grid(row = 2, column = 2, sticky = 'WENS')
    b9.grid(row = 2, column = 3, sticky = 'WENS')
    addButton.grid(row = 5, column = 4, sticky = 'WENS')
    eqButton.grid(row = 5, column = 3, sticky = 'WENS')
    subButton.grid(row = 4, column = 4, sticky = 'WENS')
    multButton.grid(row = 3, column = 4, sticky = 'WENS')
    divButton.grid(row = 2, column = 4, sticky = 'WENS')
    decButton.grid(row = 5, column = 2, sticky = 'WENS')
    lParButton.grid(row = 1, column = 1, sticky = 'WENS')
    rParButton.grid(row = 1, column = 2, sticky = 'WENS')
    clrButton.grid(row = 1, column = 3, sticky = 'WENS')
    delButton.grid(row = 1, column = 4, sticky = 'WENS')
    master.resizable(0,0)
    master.mainloop()

if __name__ == '__main__':
    main()    
