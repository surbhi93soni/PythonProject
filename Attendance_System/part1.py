import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
from train import Train
from face_recognition import face_detection
from Attendence import Attendance
import cv2
class Face_Recognition_System:
    def __init__(self,root):
       self.root = root
       self.root.title("Face_Recognition_System")
       self.root.geometry("1920x1800+0+0")
#first image
       img=Image.open('img1.png')
       image=img.resize((300,130),Image.ANTIALIAS)
       self.photoimg1=ImageTk.PhotoImage(img)
       f_lb1=Label(self.root,image=self.photoimg1)
       f_lb1.place(x=0,y=0,width=300,height=130)
#second image
       img = Image.open('img2.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg2)
       f_lb1.place(x=300, y=0, width=400, height=130)

# fourth  image
       img = Image.open('studentimg.jpg')
       image = img.resize((500, 130), Image.ANTIALIAS)
       self.photoimg3 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg3)
       f_lb1.place(x=700, y=0, width=650, height=130)

#Label
       title_lb1=Label(text="Face Recognition System ",font=("Arial ",25,"bold"),bg="white",fg="red")
       title_lb1.config(anchor=CENTER)
       title_lb1.pack()
       title_lb1.place(x=0,y=130,width=1920,height=45)


       #Student detail button
       img = Image.open('stud.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg4 = ImageTk.PhotoImage(img)

       b1=Button(image=self.photoimg4,command=self.student_details,cursor="hand2")
       b1.place(x=100,y=200,width=120,height=120)
       b2 = Button( text="Student_Detail",command=self.student_details, cursor="hand2",font=("times new roman ",10,"bold"),bg="Blue",fg="red")
       b2.place(x=100, y=300, width=120, height=20)
#Face Detect button
       img = Image.open('detect.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg6 = ImageTk.PhotoImage(img)

       b3=Button(image=self.photoimg6,cursor="hand2",command=self.face_data)
       b3.place(x=100,y=400,width=120,height=120)
       b4 = Button( text ="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman ",10,"bold"),bg="Blue",fg="red")
       b4.place(x=100, y=500, width=120, height=20)
#Attendance button
       img = Image.open('attend.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg7 = ImageTk.PhotoImage(img)

       b5 = Button(image=self.photoimg7, cursor="hand2",command=self.attendance_data)
       b5.place(x=240, y=400, width=120, height=120)
       b6 = Button(text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman ", 10, "bold"), bg="Blue",
                   fg="red")
       b6.place(x=240, y=500, width=120, height=20)

#TrainSet button
       img = Image.open('download.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg9 = ImageTk.PhotoImage(img)

       b9=Button(image=self.photoimg9,cursor="hand2",command=self.train_data)
       b9.place(x=240,y=200,width=120,height=120)
       b10 = Button(text="Train Face", cursor="hand2",command=self.train_data,font=("times new roman ",10,"bold"),bg="Blue",fg="red")
       b10.place(x=240, y=300, width=120, height=20)
#photo train button
       img = Image.open('photo.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg10 = ImageTk.PhotoImage(img)

       b11=Button(image=self.photoimg10,cursor="hand2",command=self.open_img)
       b11.place(x=380,y=200,width=120,height=120)
       b12= Button(text="Photo", cursor="hand2",command=self.open_img,font=("times new roman ",10,"bold"),bg="Blue",fg="red")
       b12.place(x=380, y=300, width=120, height=20)

    def open_img(self):
       os.startfile("data")

##################### FUNCTION ############################
    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
#################### Function Train###########
    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)
#################### Function Train###########
    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=face_detection(self.new_window)
#################### Function Attendance###########
    def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)


if __name__ == '__main__':
    root= Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()






