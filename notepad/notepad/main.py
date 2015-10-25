# -*- coding:utf-8 -*-
'''
Created on 2015年10月24日

@author: luke
'''
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os,re
from Tkconstants import SEL

filename = ''

def author():
    showinfo("author", "Made by Godning")
    
def copyright():
    showinfo("Copyright", "Belong to Godning")
    
def openfile():
    global filename
    #file object
    fileobj = askopenfile(defaultextension='.py')
    if fileobj == None:
        filename = None
    else:
        filename=fileobj.name
        root.title('File: '+os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()
        
def newfile():
    global filename
    root.title("New File")
    filename=None
    textPad.delete(1.0,END)
    
def save():
    global filename
    try:
        f=open(filename,'w')
        msg=textPad.get(1.0,END)
        f.write(msg)
        f.close()
    except:
        saveas()

def saveas():
    f = asksaveasfile(initialfile = 'newfile.py',defaultextension='.py')
    global filename
    filename = f.name
    file = open(filename,'w')
    msg = textPad.get(1.0,END)
    file.write(msg)
    file.close()
    root.title('File: '+os.path.basename(filename))
    
def cut():
    textPad.event_generate('<<Cut>>')

def copy():
    textPad.event_generate('<<Copy>>')
    
def paste():
    textPad.event_generate('<<Paste>>')
    
def redo():
    textPad.event_generate('<<Redo>>')
    
def undo():
    textPad.event_generate('<<Undo>>')
    
def selectall():
    textPad.tag_add('sel', '1.0',END)
    
def search():
    topsearch=Toplevel(root)
    topsearch.geometry('300x100+200+250')
    label = Label(topsearch,text='Find')
    label.grid(row=0,column=0,padx=5)
    entry=Entry(topsearch,width=20)
    entry.grid(row=0,column=1,padx=5)
    def genSearch():
        msg = entry.get()         
        where=textPad.search(msg, INSERT,END)
        if where:
            pastit=where + ('+%dc' % len(msg))
            textPad.tag_remove(SEL, '1.0', INSERT)
            textPad.tag_add(SEL,where ,pastit)  
            textPad.mark_set(INSERT, pastit)
            textPad.see(INSERT)
#         else:
#             showinfo("None", "Nothing could be found!")
    button=Button(topsearch,text="search",command=genSearch)
    button.grid(row=0,column=2) 
    
root = Tk()
root.title('Notepad')
# x not *
root.geometry("500x500+100+100")

# Create Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='new', accelerator='Ctrl + N',command=newfile)
filemenu.add_command(label='open', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='save', accelerator='Ctrl + S',command=save)
filemenu.add_command(label='save as', accelerator='Ctrl +Shift + S',command=saveas)
menubar.add_cascade(label='file', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='undo', accelerator='Ctrl + Z',command=undo)
editmenu.add_command(label='redo', accelerator='Ctrl + Y',command=redo)
editmenu.add_separator()
editmenu.add_command(label='cut', accelerator='Ctrl + X',command=cut)
editmenu.add_command(label='copy', accelerator='Ctrl + C',command=copy)
editmenu.add_command(label='paste', accelerator='Ctrl + V',command=paste)
editmenu.add_separator()
editmenu.add_command(label='find', accelerator='Ctrl + F',command=search)
editmenu.add_command(label='select all', accelerator='Ctrl + A',command=selectall)
menubar.add_cascade(label='edit', menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label='author', command=author)
aboutmenu.add_command(label='copyright', command=copyright)
menubar.add_cascade(label='about', menu=aboutmenu)

# toorbar
toorbar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toorbar, text='open',command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toorbar, text='save',command=save)
shortButton.pack(side=LEFT)
toorbar.pack(expand=NO, fill=X)

# Linenumber&text
linelabel = Label(root, width=2, bg='antique white')
linelabel.pack(side=LEFT, fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

# Statusbar
status = Label(root, text='Notepad v1.0', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# scrollbar
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# main
root.mainloop()

