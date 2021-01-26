from tkinter import *
from tkinter import font
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import urllib.request

root = Tk()

#WordMeaning function button
def WordMeaning():
    word=T.get('sel.first','sel.last')
    #word=input('Enter a word to find meaning: ')
    url = "https://www.vocabulary.com/dictionary/" + word
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')

    soup1 = soup.find(class_="short")
    soup1 = soup1.get_text()
    print('Meaning of given word:\n',soup1)

#new_file definition
#def new_file():
#    T.delete("1.0",END)
    
#open_file definiton
def open_file():
    T.delete("1.0",END)
    open_textfile=filedialog.askopenfilename(initialdir="C:/Users/Ilangoven/Documents/PyTraining",title="Open File",
    filetypes=(("Text Files","*.txt"),("Python File","*.py"),("Word File","*.docx"),("All files","*.*")))
    
    open_textfile=open(open_textfile,"r")
    content=open_textfile.read()
    T.insert(END,content)
    open_textfile.close()

#function definition for bold text
def bold_it():
    bold_font=font.Font(T,T.cget("font"))
    bold_font.configure(weight="bold")
    
    T.tag_configure("bold",font=bold_font)
    current_tags=T.tag_names("sel.first")
    
    if "bold" in current_tags:
        T.tag_remove("bold","sel.first","sel.last")
    else:
        T.tag_add("bold","sel.first","sel.last")

#function definition for italic text
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

#toobar creation
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

#widgettoobar creation
widgettoolbar_frame=Frame(root)
widgettoolbar_frame.pack(fill=X)

#creating a Menu
my_menu=Menu(root)
root.config(menu=my_menu)


#Adding file operation menu
#file_menu=Menu(my_menu,tearoff=False)
#my_menu.add_cascade(Label="File",menu=file_menu)
#file_menu.add_command(Label="NewFile",command=new_file) 
#file_menu.add_command(Label="Open",command=open_file) 


#bold button
bold_button=Button(widgettoolbar_frame,text='Bold',command=bold_it)
bold_button.grid(row=0,column=0,padx=5,sticky=W)

#italics_button
italics_button=Button(widgettoolbar_frame,text='Italics',command=itatics_it)
italics_button.grid(row=0,column=1,padx=5)

#openfile button
openfile_button=Button(toolbar_frame,text='OpenFile',command=open_file)
openfile_button.grid(row=0,column=2,padx=5)

#Wikibutton
wikibutton=Button(widgettoolbar_frame,text="WordMeaning",command=WordMeaning)
wikibutton.grid(row=0,column=3,padx=5)

scrollbar.pack(side=RIGHT,fill=Y)
l.pack()
T.pack() 
b2.pack()


root.mainloop()


















