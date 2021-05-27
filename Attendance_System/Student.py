from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
       self.root = root
       self.root.title("Student Details")
       self.root.geometry("1920x1800+0+0")
################variable######################
       self.var_Dept=StringVar()
       self.var_Course = StringVar()
       self.var_Year = StringVar()
       self.var_sem = StringVar()
       self.var_id = StringVar()
       self.var_EmailID = StringVar()
       self.var_Phone = StringVar()
       self.var_DOB = StringVar()
       self.var_Gender = StringVar()
       self.var_Address = StringVar()
       self.var_name = StringVar()

       #first Image
       img = Image.open('p1.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg1 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg1)
       f_lb1.place(x=0, y=0, width=300, height=130)
#second image
       img = Image.open('img2.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg2)
       f_lb1.place(x=300, y=0, width=300, height=90)
#third image
       img = Image.open('img3.jpg')
       image = img.resize((500, 130), Image.ANTIALIAS)
       self.photoimg3 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg3)
       f_lb1.place(x=600, y=0, width=550, height=90)
#background image
       img = Image.open('bgimg.jpg')
       image = img.resize((1920, 1200), Image.ANTIALIAS)
       self.photoimg5 = ImageTk.PhotoImage(img)
       bg_img= Label(self.root, image=self.photoimg5)
       bg_img.place(x=0, y=90, width=1920, height=1000)
#Label
       title_lb1=Label(bg_img,text="Student Management System ",font=("Arial ",25,"bold"),bg="white",fg="red")
       title_lb1.config(anchor=CENTER)
       title_lb1.pack()
       title_lb1.place(x=0,y=0,width=1920,height=40)
#main frame
       main_frame=Frame(bg_img,bd=2)
       main_frame.place(x=0,y=50,width=1920,height=650)
#left frame
       left_frame=LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
       left_frame.place(x=10,y=10,width=600,height=530)

       CurrentCourse_frame = LabelFrame(left_frame, bd=2, bg="White", relief=RIDGE, text="Current Course Information",
                               font=("times new roman", 12, "bold"))
       CurrentCourse_frame.place(x=10, y=0, width=600, height=120)
       # Department
       dep_label=Label(CurrentCourse_frame,text="Department",font=("times new roman", 12, "bold"),bg="white")
       dep_label.grid(row=0 , column=0)

       dep_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_Dept , font=("times new roman", 12, "bold"),state="read only",width=17)
       dep_combo["values"]=("Select Department ","CSE","IT","CIVIL","ME","EC","biotech","CSA")
       dep_combo.current(0)
       dep_combo.grid(row=0, column=1,padx=3,pady=10,sticky=W)
    # Course
       dep_label = Label(CurrentCourse_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
       dep_label.grid(row=0, column=2)
       dep_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_Course , font=("times new roman", 12, "bold"),
                                state="read only", width=17)
       dep_combo["values"] = ("Select Course","B.Tech","M.Tech","BioTech","MCA")
       dep_combo.current(0)
       dep_combo.grid(row=0, column=3, padx=0, pady=2,sticky=W)
       # Semster
       dep_label = Label(CurrentCourse_frame,  text="Semster", font=("times new roman", 12, "bold"), bg="white")
       dep_label.grid(row=1, column=0)
       dep_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_sem, font=("times new roman", 12, "bold"),
                                state="read only", width=17)
       dep_combo["values"] = ("Select Semester", " 1", "2", " 3", "4", " 5"," 6", " 7", " 8")
       dep_combo.current(0)
       dep_combo.grid(row=1, column=1, padx=3, pady=10,sticky=W)
       # Year
       year_label = Label(CurrentCourse_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
       year_label.grid(row=1, column=2)
       year_combo = ttk.Combobox(CurrentCourse_frame, textvariable=self.var_Year, font=("times new roman", 12, "bold"),
                                state="read only", width=17)
       year_combo["values"] = ("Select Year","I", "II", "III", "IV")
       year_combo.current(0)
       year_combo.grid(row=1, column=3, padx=3, pady=10,sticky=W)

#Right Frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Search Student",
                               font=("times new roman", 12, "bold"))
       Right_frame.place(x=620, y=10, width=600, height=430)
#Class Student Detail
       Class_frame = LabelFrame(left_frame, bd=2, bg="White", relief=RIDGE, text="Class Student Information",
                               font=("times new roman", 12, "bold"))
       Class_frame.place(x=10, y=120, width=600, height=380)
       # Student iD
       StudentID_label=Label(Class_frame,text="Student ID",font=("times new roman", 12, "bold"))
       StudentID_label.grid(row=0 , column=0,padx=3, pady=10,sticky=W)
       StudentID_Entry=ttk.Entry(Class_frame,textvariable=self.var_id,width=15, font=("times new roman", 12, "bold"))
       StudentID_Entry.grid(row=0, column=1,padx=3, pady=10,sticky=W)
       #student name
       StudentName_label = Label(Class_frame, text="Student Name", font=("times new roman", 12, "bold"))
       StudentName_label.grid(row=0, column=2, padx=3, pady=10, sticky=W)
       StudentName_Entry = ttk.Entry(Class_frame,textvariable=self.var_name, width=15, font=("times new roman", 12, "bold"))
       StudentName_Entry.grid(row=0, column=3, padx=3, pady=10, sticky=W)
       #Student Address
       StudentAddress_label = Label(Class_frame, text="Student Address", font=("times new roman", 12, "bold"))
       StudentAddress_label.grid(row=1, column=0, padx=3, pady=10, sticky=W)
       StudentAddress_Entry = ttk.Entry(Class_frame,textvariable=self.var_Address, width=15, font=("times new roman", 12, "bold"))
       StudentAddress_Entry.grid(row=1, column=1, padx=3, pady=10, sticky=W)
       # Student Gender
       StudentGender_label = Label(Class_frame, text="Student Gender", font=("times new roman", 12, "bold"))
       StudentGender_label.grid(row=1, column=2, padx=3, pady=10, sticky=W)
       Gender_combo=ttk.Combobox(Class_frame,textvariable=self.var_Gender,font=("times new roman", 12, "bold"))
       Gender_combo["values"]=("Male","Female","Others")
       Gender_combo.grid(row=1, column=3, padx=3, pady=10, sticky=W)
       ## Student Contact
       StudentContact_label = Label(Class_frame, text="Student Contact", font=("times new roman", 12, "bold"))
       StudentContact_label.grid(row=2, column=0, padx=3, pady=10, sticky=W)
       StudentContact_Entry = ttk.Entry(Class_frame,textvariable=self.var_Phone, width=15, font=("times new roman", 12, "bold"))
       StudentContact_Entry.grid(row=2, column=1, padx=3, pady=10, sticky=W)
       # Student Email
       StudentEmail_label = Label(Class_frame, text="Student EmailId", font=("times new roman", 12, "bold"))
       StudentEmail_label.grid(row=2, column=2, padx=3, pady=10, sticky=W)
       StudentEmail_Entry = ttk.Entry(Class_frame,textvariable=self.var_EmailID, width=15, font=("times new roman", 12, "bold"))
       StudentEmail_Entry.grid(row=2, column=3, padx=3, pady=10, sticky=W)
       # Student DateofBirth
       StudentDOB_label = Label(Class_frame, text="Student DOB", font=("times new roman", 12, "bold"))
       StudentDOB_label.grid(row=3, column=0, padx=3, pady=10, sticky=W)
       StudentDOB_Entry = ttk.Entry(Class_frame,textvariable=self.var_DOB, width=15, font=("times new roman", 12, "bold"))
       StudentDOB_Entry.grid(row=3, column=1, padx=3, pady=10, sticky=W)
       #Radio button
       self.var_radio1=StringVar()
       radiobtn1=ttk.Radiobutton(Class_frame,variable=self.var_radio1,text="Take Photo Sample",value='yes')
       radiobtn1.grid(row=4,column=0)

       radiobtn2 = ttk.Radiobutton(Class_frame, variable=self.var_radio1,text="Dont take Photo Sample", value='No')
       radiobtn2.grid(row=4, column=1)
#buttonframe
       btnframe=Frame(Class_frame,bd=2,relief=RIDGE,bg="white")
       btnframe.place(x=0,y=200,width=600,height=350)
       Photobtn = Button(btnframe, text="Take Photo Sample",command=self.generate_dataset, font=("arial", 13, "bold"), bg="pink", fg="Black")
       Photobtn.grid(row=0, column=4)
       savebtn=Button(btnframe,text="Save",command=self.add_data,font=("arial",13,"bold"),bg="blue",fg="White")
       savebtn.grid(row=0,column=0)
       Updatebtn = Button(btnframe, text="Update",command=self.update_data, font=("arial", 13, "bold"), bg="Green", fg="White")
       Updatebtn.grid(row=0, column=1)
       resetbtn = Button(btnframe, text="Reset",command=self.reset_data,font=("arial", 13, "bold"), bg="red", fg="White")
       resetbtn.grid(row=0, column=2)
       Delbtn = Button(btnframe, text="Delete",command=self.delete_data, font=("arial", 13, "bold"), bg="yellow", fg="Black")
       Delbtn.grid(row=0, column=3)
#Right Frame Search Student
#Class Student Detail


#table Frame
       Table_frame = LabelFrame(Right_frame, bd=2, bg="White", relief=RIDGE, text="Table",
                                 font=("times new roman", 12, "bold"))
       Table_frame.place(x=0, y=0, width=600, height=350)
       scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
       self.student_table=ttk.Treeview(Table_frame,column=("Dept","Course","Year","sem","id","name","Phone","Address","DOB","Gender","EmailID","PhotoSample"),xscrollcommand=scroll_x,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)
       self.student_table.heading("Dept",text="Department")
       self.student_table.heading("Course", text="Course")
       self.student_table.heading("Year", text="Year")
       self.student_table.heading("sem", text="Semester")
       self.student_table.heading("id", text="StudentID")
       self.student_table.heading("name", text="Student Name")
       self.student_table.heading("Address", text="Address")
       self.student_table.heading("Phone", text="Contact")
       self.student_table.heading("DOB", text="Date of Birth")
       self.student_table.heading("EmailID", text="EmailID")
       self.student_table.heading("Gender", text="Gender")
       self.student_table.heading("PhotoSample", text="PhotoSampleStatus")
       self.student_table["show"] = "headings"
       self.student_table.column("Dept",width=100)
       self.student_table.column("Course", width=100)
       self.student_table.column("Year", width=100)
       self.student_table.column("sem", width=100)
       self.student_table.column("id", width=100)
       self.student_table.column("name",width=100)
       self.student_table.column("Address",width=100)
       self.student_table.column("Phone", width=100)
       self.student_table.column("DOB", width=100)
       self.student_table.column("EmailID",width=100)
       self.student_table.column("Gender", width=100)
       self.student_table.column("PhotoSample", width=150)
       self.student_table.pack(fill=BOTH,expand=1)
       self.student_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()
################3Function Declaration###############
    def add_data(self):
       if self.var_Dept.get()=="Select Department" or self.var_Dept.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All field required",parent=self.root)
       else:
           try:
               conn=mysql.connector.connect(host="localhost",username="root",password="soni@1234",database="face_recognition")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_Dept.get(),
                                                                self.var_Course.get(),
                                                                self.var_sem.get(),
                                                                self.var_Year.get(),
                                                                self.var_id.get(),
                                                                self.var_name.get(),
                                                                self.var_Address.get(),
                                                                self.var_Gender.get(),
                                                                self.var_Phone.get(),
                                                                self.var_EmailID.get(),
                                                                self.var_DOB.get(),
                                                                self.var_radio1.get()

                     ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("sucess","Student details has been addded sucessfully ",parent=self.root)
           except Exception as es:
               messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
####################### Function ################
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="soni@1234",database="face_recognition")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
               self.student_table.insert("",END,values=i)
            conn.commit()
      conn.close()
        ############## get cursor ################
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]
       self.var_Dept.set(data[0]),
       self.var_Course.set(data[1]),
       self.var_sem.set(data[2]),
       self.var_Year.set(data[3]),
       self.var_id.set(data[4]),
       self.var_name.set(data[5]),
       self.var_Address.set(data[6]),
       self.var_Gender.set(data[7]),
       self.var_Phone.set(data[8]),
       self.var_EmailID.set(data[9]),
       self.var_DOB.set(data[10]),
       self.var_radio1.set(data[11])
    #update function############




    def update_data(self):
        if self.var_Dept.get() == "Select Department" or self.var_Dept.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All field required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="soni@1234",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,sem=%s,Year=%s,name=%s,Address=%s,Gender=%s,Phone=%s,EmailID=%s,DOB=%s,PhotoSample=%s where id=%s", (
                        self.var_Dept.get(),
                        self.var_Course.get(),
                        self.var_sem.get(),
                        self.var_Year.get(),
                        self.var_name.get(),
                        self.var_Address.get(),
                        self.var_Gender.get(),
                        self.var_Phone.get(),
                        self.var_EmailID.get(),
                        self.var_DOB.get(),
                        self.var_radio1.get(),
                        self.var_id.get()



                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess", "Student details has been updated sucessfully ", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
############Delete function##############
    def delete_data(self):
       if self.var_id.get()=="":
           messagebox.showerror("Error","Student id must require",parent=self.root)
       else:
           try:
               delete=messagebox.askyesno("Student page delete","Do you want to delete",parent=self.root)
               if delete>0:
                   conn = mysql.connector.connect(host="localhost", username="root", password="soni@1234",
                                                  database="face_recognition")
                   my_cursor = conn.cursor()
                   sql="delete from student where id=%s"
                   val=(self.var_id.get(),)
                   my_cursor.execute(sql,val)
               else:
                   if not delete:
                       return
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("sucess", "Student details has been deleted sucessfully ", parent=self.root)
           except Exception as es:
               messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
#############Reset##################
    def reset_data(self):
        self.var_Dept.set("Select Department ")
        self.var_Course.set("Select Course")
        self.var_sem.set("Select Semester")
        self.var_Year.set("Select Year")
        self.var_id.set("")
        self.var_name.set("")
        self.var_Address.set("")
        self.var_Gender.set("Male")
        self.var_Phone.set("")
        self.var_EmailID.set("")
        self.var_DOB.set("")
        self.var_radio1.set("")
################ generate dataset or take photo ##################
    def generate_dataset(self):
        if self.var_Dept.get() == "Select Department" or self.var_Dept.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All field required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="soni@1234", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,sem=%s,Year=%s,name=%s,Address=%s,Gender=%s,Phone=%s,EmailID=%s,DOB=%s,PhotoSample=%s where id=%s",(
                                                                                            self.var_Dept.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_Address.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Phone.get(),
                                                                                            self.var_EmailID.get(),
                                                                                            self.var_DOB.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get() == id+1
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

        ################# load predefined data on face frontals from op[encv]##################
                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    #Minimum Neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h ,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)






if __name__ == '__main__':
    root= Tk()
    obj = Student(root)
    root.mainloop()
