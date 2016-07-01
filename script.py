import os, sys
from Tkinter import *
import tkMessageBox
import datetime
from PIL import Image      		 #PIL
from PIL import ImageTk          #PIL
now = datetime.datetime.now()
os.chdir("xxx/xxx/xx") #Go to the directory, where the pictures should are  		 #cd
print os.getcwd() #Print name of current directory
print os.listdir(os.getcwd()) #Print all Files in directory						 #ls
for file in os.listdir(os.getcwd()): #Print all files in current directory with .jpg file type
    if file.endswith(".jpg"):
        print(file)
      	file2 = file
for file in os.listdir(os.getcwd()): #Print all files in current directory with .jpg file type
    if file.endswith(".png"):
        print(file)
      	file2 = file

#save method
def save():
	neuerName = e1.get() + ".jpg"
	TEXT = e2.get()
	os.rename(file2, "xxx/xxx/xx" +neuerName) #Insert location where the file should go here
	tkMessageBox.showinfo("Fertig", "Datei wurde umbenannt in: " +neuerName)	#Messagebox feedback
	txt = open("xxx/xxx/xx" +e1.get() +".txt", "w") #Insert location where the file should go here
	txt.write("%s" %TEXT)	#Write the user input
	txt.write("#xx #abab #yay") #Insert hashtags, which will be added to the tweet every time
	txt.close()

def pic():		#open pic
	im = Image.open(file2) 		#define pic	
	im.show()	#open it

master = Tk()

Label(master, text="Heutiges Datum:").grid(row=1) #Label-Tosay s date
Label(master, text=now.strftime("%d.%m.%Y")).grid(row=1,column=1) #Actual Date
Label(master, text="Dateiname").grid(row=2) #Name of pic in folder Label
Label(master, text=file2).grid(row=2,column=1)	#Name of pic in folder
Label(master, text="Datum zum Posten").grid(row=3)	#Label-Date to post on
Label(master, text="Text dazu:").grid(row=4)	#Label-Test to post with the pic

e1 = Entry(master, width=8)	#Entry field for date of whised posting
e2 = Entry(master, width=24) #Entry field for text
e1.grid(row=3, column=1,columnspan=2)
e2.grid(row=4, column=1)

Button(master, text='Quit', command=master.quit).grid(row=0, column=0, sticky=W, pady=1)	#Quit button
Button(master, text='Save', command=save).grid(row=5, column=3, sticky=W, pady=4)		#Save the pic and text to post it
Button(master, text='ShowPic', command=pic).grid(row=5, column=1, sticky=W, pady=4)		#Show the pic to be shure it is the right

mainloop( )
