from tkinter import *
from tkinter import font

root = Tk()

def bold_it():
    bold_font=font.Font(T,T.cget("font"))
    bold_font.configure(weight="bold")
    
    T.tag_configure("bold",font=bold_font)
    current_tags=T.tag_names("sel.first")
    
    if "bold" in current_tags:
        T.tag_remove("bold","sel.first","sel.last")
    else:
        T.tag_add("bold","sel.first","sel.last")

def itatics_it():
    italics_font=font.Font(T,T.cget("font"))
    italics_font.configure(slant="italic")
    
    T.tag_configure("italic",font=italics_font)
    current_tags=T.tag_names("sel.first")
    
    if "italic" in current_tags:
        T.tag_remove("italic","sel.first","sel.last")
    else:
        T.tag_add("italic","sel.first","sel.last")

# specify size of window. 
root.geometry("350x350")
root.title('PyNotepad') 

#scrollbar
scrollbar=Scrollbar(root)

#label
l=Label(root,text='Trial version',font=('Broadway'))
  
# Create text widget and specify size. 
T = Text(root,yscrollcommand=scrollbar.set,height = 10, width = 250,font=('Rockwell'),bg='light blue') 
 
# Create an Exit button. 
b2 = Button(root, text = "Exit",fg='red', command = root.destroy)  


#bold button
bold_button=Button(root,text='Bold',command=bold_it)
bold_button.pack()

#italics_button
italics_button=Button(root,text='Italics',command=itatics_it)
italics_button.pack()


scrollbar.pack(side=RIGHT,fill=Y)
l.pack()
T.pack() 
b2.pack()


root.mainloop()