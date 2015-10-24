# -*- coding:utf-8 -*-
'''
Created on 2015年10月24日

@author: luke
'''
from Tkinter import *
root = Tk()
root.title('Notepad')
# x not *
root.geometry("500x500+100+100")

# Create Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='new', accelerator='Ctrl + N')
filemenu.add_command(label='open', accelerator='Ctrl + O')
filemenu.add_command(label='save', accelerator='Ctrl + S')
filemenu.add_command(label='save other', accelerator='Ctrl +Shift + S')
menubar.add_cascade(label='file', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='undo', accelerator='Ctrl + Z')
editmenu.add_command(label='redo', accelerator='Ctrl + Y')
editmenu.add_separator()
editmenu.add_command(label='cut', accelerator='Ctrl + X')
editmenu.add_command(label='copy', accelerator='Ctrl + C')
editmenu.add_command(label='paste', accelerator='Ctrl + V')
editmenu.add_separator()
editmenu.add_command(label='find', accelerator='Ctrl + F')
editmenu.add_command(label='select all', accelerator='Ctrl + A')
menubar.add_cascade(label='edit', menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label='author')
aboutmenu.add_command(label='copyright')
menubar.add_cascade(label='about', menu=aboutmenu)

#toorbar
toorbar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toorbar, text='open')
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toorbar, text='save')
shortButton.pack(side=LEFT)
toorbar.pack(expand = NO,fill=X)

#Statusbar
status=Label(root,text='Ln20',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

#Linenumber&text
linelabel=Label(root,width=2,bg='antique white')
linelabel.pack(side=LEFT,fill=Y)

textPad =Text(root,undo=True)
textPad.pack(expand=YES,fill=BOTH)
#scrollbar
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command = textPad.yview)
scroll.pack(side=RIGHT,fill=Y)

# main
root.mainloop()

