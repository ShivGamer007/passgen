import random #for random function
import tkinter #for GUI in Python

# Layout : 
window = tkinter.Tk()
window.title("Random Password Generator")#window name
window.geometry('520x350')
padding = 100
window['padx']=padding
title_text = tkinter.Label(text=' Hello ! Wellcome to Random Password Generator ',background='lime')#first line in window
title_text.grid(row=0,column=0)
tkinter.Label(text='').grid(row=1,column=0)#spacing
result = tkinter.Entry(border='2px')#generated password
result.grid(row=2,column=0)

# variables for checkboxes : 
chk1 = tkinter.IntVar()
chk2 = tkinter.IntVar()
chk3 = tkinter.IntVar()

# generating random password :
def password_generate(len):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@'
    password = "".join(random.sample(valid_char,len))
    result.delete(0,tkinter.END)
    result.insert(0,password)

# checkboxes for length of password :
def checkbox_check():
    if chk1.get()==6:
        password_generate(6)
    elif chk2.get()==10:
        password_generate(10)
    elif chk3.get()==12:
        password_generate(12)
    else:
        password_generate(8)


# working and on/off value of checkboxes :
tkinter.Label(text='').grid(row=3,column=0)#spacing
checkone = tkinter.Checkbutton(text=' 6  Characters',onvalue=6,offvalue=0,variable=chk1)
checkone.grid(row=4,column=0)
checktwo = tkinter.Checkbutton(text='10 Characters',onvalue=10,offvalue=0,variable=chk2)
checktwo.grid(row=5,column=0)
checkthree = tkinter.Checkbutton(text='12 Characters',onvalue=12,offvalue=0,variable=chk3)
checkthree.grid(row=6,column=0)

# Generate button : 
generate = tkinter.Button(text='Generate',command=checkbox_check,background='aqua')
generate.grid(row=7,column=0)

# thanks :
tkinter.Label(text=' ').grid(row=8,column=0)#spacing
tkinter.Label(text='Thanks for Using ... !!').grid(row=9,column=0)
tkinter.Label(text='-By SHIVANSHU SINGH ').grid(row=10,column=1)

window.mainloop()