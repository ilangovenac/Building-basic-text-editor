from tkinter import *
import tkinter.font

root = Tk()
def bold_it():

    bold_font=font.Font(weight='bold')
    #bold_font=font.Font(font=T['font'])
    bold_font.configure(weight='bold')
    
    T.tag_configure('bold',font=bold_font)
    T.tag_add('bold', 'sel.first','sel.last')

   
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X) 

# specify size of window. 
root.geometry("350x350")
root.title('PyNotepad') 

#scrollbar
scrollbar=Scrollbar(root)

#label
l=Label(root,text='Trial version',font=('Broadway'))
  
# Create text widget and specify size. 
T = Text(root,yscrollcommand=scrollbar.set,height = 10, width = 250,font=('Rockwell'),bg='light blue',fg='dark blue') 
 
# Create an Exit button. 
b2 = Button(root, text = "Exit",fg='red', command = root.destroy)  

bold_button=Button(toolbar_frame,text='Bold',command=bold_it)
bold_button.grid(row=0,column=0,sticky=W,padx=5)


scrollbar.pack(side=RIGHT,fill=Y)
l.pack()
T.pack() 
b2.pack()


root.mainloop()