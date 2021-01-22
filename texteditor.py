from tkinter import *
  
slate=Tk()

slate.geometry('300x300')
slate.title('PyNotepad')

scrollbar=Scrollbar(slate)
scrollbar.pack(fill=Y,side=RIGHT)

text=Text(slate,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

scrollbar.config(command=text.yview)


slate.mainloop()