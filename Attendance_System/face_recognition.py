from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import numpy as np
import os
class face_detection:
    def __init__(self,root):
       self.root = root
       self.root.title("Face Detection")
       self.root.geometry("1920x1800+0+0")

       title_lb1=Label(self.root,text="Face Detection and Recognition ",font=("Arial ",25,"bold"),bg="pink",fg="green")
       title_lb1.place(x=0,y=0,width=1920,height=45)


       #######Button########

       # second image
       img = Image.open('face1.jpg')
       image = img.resize((200, 60), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg2)
       f_lb1.place(x=0, y=60, width=200, height=500)
       Photobtn = Button(self.root, text="Detect Face", command=self.face_recog, font=("arial", 25, "bold"),
                         bg="red", fg="White")
       Photobtn.grid(row=0, column=0)
       Photobtn.place(x=0, y=300, width=200, height=45)
       # second image
       img = Image.open('face2.png')
       image = img.resize((1000, 50), Image.ANTIALIAS)
       self.photoimg1 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg1)
       f_lb1.place(x=200, y=50, width=1000, height=600)
########################AttendNCE Mark #########
    def mark_attendance(self,i,n,d,c):
        with open("Mark.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list) and (c not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{c},{dtString},{d1},Present")




################ Face detection and recognition ##########
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="soni@1234",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select id from student where id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dept from student where id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Course from student where id=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)


                if confidence>77:
                    cv2.putText(img, f"id{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"name{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img,f"Dept{d}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img, f"Course{c}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,n,d,c)

                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]
            return coord
############## function #########
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,0,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Attendace Captured!!!")


if __name__ == '__main__':
    root= Tk()
    obj = face_detection(root)
    root.mainloop()
