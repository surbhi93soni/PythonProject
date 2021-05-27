from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
class Train:
    def __init__(self,root):
       self.root = root
       self.root.title("Train dataset")
       self.root.geometry("1920x1800+0+0")

       title_lb1=Label(self.root,text="Train Dataset ",font=("Arial ",35,"bold"),bg="pink",fg="green")
       title_lb1.place(x=0,y=0,width=1920,height=45)

       # first image
       img = Image.open('top.jpg')
       image = img.resize((500, 130), Image.ANTIALIAS)
       self.photoimg1 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg1)
       f_lb1.place(x=0, y=45, width=500, height=230)
       #######Button########
       Photobtn = Button(self.root,command=self.train_classifier, text="Train Photo Sample", font=("arial", 35, "bold"),
                         bg="Blue", fg="White")
       Photobtn.grid(row=0, column=0)
       Photobtn.place(x=0, y=280, width=500, height=100)
       # second image
       img = Image.open('bottom.jpg')
       image = img.resize((500, 130), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg2)
       f_lb1.place(x=0, y=380, width=500, height=230)

       #######Function###########

    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

###### Train the classifier #########
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")

if __name__ == '__main__':
    root= Tk()
    obj = Train(root)
    root.mainloop()
