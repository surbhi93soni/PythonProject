import csv
from tkinter import filedialog
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from face_recognition import face_detection
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

mydata=[]


class Attendance:
    def __init__(self,root):
       self.root = root
       self.root.title("Attendance details")
       self.root.geometry("1920x1800+0+0")
######################## Variable ##########
       self.var_id=StringVar()
       self.var_name = StringVar()
       self.var_Dept = StringVar()
       self.var_Course = StringVar()
       self.var_time = StringVar()
       self.var_date = StringVar()
       self.var_attendance = StringVar()


       # first Image
       img = Image.open('p1.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg1 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg1)
       f_lb1.place(x=0, y=0, width=300, height=130)
       # second image
       img = Image.open('img2.jpg')
       image = img.resize((300, 130), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg2)
       f_lb1.place(x=300, y=0, width=300, height=90)
       # third image
       img = Image.open('img3.jpg')
       image = img.resize((500, 130), Image.ANTIALIAS)
       self.photoimg3 = ImageTk.PhotoImage(img)
       f_lb1 = Label(self.root, image=self.photoimg3)
       f_lb1.place(x=600, y=0, width=550, height=90)
       # background image
       img = Image.open('bgimg.jpg')
       image = img.resize((1920, 1200), Image.ANTIALIAS)
       self.photoimg5 = ImageTk.PhotoImage(img)
       bg_img = Label(self.root, image=self.photoimg5)
       bg_img.place(x=0, y=90, width=1920, height=1000)
       # Label
       title_lb1 = Label(bg_img, text="Attendance System ", font=("Arial ", 25, "bold"), bg="white", fg="red")
       title_lb1.config(anchor=CENTER)
       title_lb1.pack()
       title_lb1.place(x=0, y=0, width=1920, height=40)
       # main frame
       main_frame = Frame(bg_img, bd=2)
       main_frame.place(x=0, y=50, width=1920, height=650)

       # left frame
       left_frame = LabelFrame(main_frame,bd=2, bg="White", relief=RIDGE, text="Student Attendance Details",
                               font=("times new roman", 12, "bold"))
       left_frame.place(x=10, y=10, width=600, height=530)
       # Class Student Detail
       Class_frame = LabelFrame(left_frame, bd=2, bg="White", relief=RIDGE, text="Class Student Information",
                                font=("times new roman", 12, "bold"))
       Class_frame.place(x=10, y=120, width=600, height=380)
       # Student iD
       AttendanceID_label = Label(Class_frame, text="Attendance ID", font=("times new roman", 12, "bold"))
       AttendanceID_label.grid(row=0, column=0, padx=3, pady=10, sticky=W)
       AttendanceID_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_id,
                                   font=("times new roman", 12, "bold"))
       AttendanceID_Entry.grid(row=0, column=1, padx=3, pady=10, sticky=W)
       # Name
       Name_label = Label(Class_frame, text="Name", font=("times new roman", 12, "bold"))
       Name_label.grid(row=0, column=2, padx=3, pady=10, sticky=W)
       Name_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_name,
                                      font=("times new roman", 12, "bold"))
       Name_Entry.grid(row=0, column=3, padx=3, pady=10, sticky=W)

       #Department
       AttendanceID_label = Label(Class_frame, text="Department", font=("times new roman", 12, "bold"))
       AttendanceID_label.grid(row=1, column=0, padx=3, pady=10, sticky=W)
       AttendanceID_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_Dept,
                                      font=("times new roman", 12, "bold"))
       AttendanceID_Entry.grid(row=1, column=1, padx=3, pady=10, sticky=W)
       # Course
       AttendanceID_label = Label(Class_frame, text="Course", font=("times new roman", 12, "bold"))
       AttendanceID_label.grid(row=1, column=2, padx=3, pady=10, sticky=W)
       AttendanceID_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_Course,
                                      font=("times new roman", 12, "bold"))
       AttendanceID_Entry.grid(row=1, column=3, padx=3, pady=10, sticky=W)
       # Date
       Date_label = Label(Class_frame, text="Time", font=("times new roman", 12, "bold"))
       Date_label.grid(row=2, column=0, padx=3, pady=10, sticky=W)
       Date_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_time,
                                      font=("times new roman", 12, "bold"))
       Date_Entry.grid(row=2, column=1, padx=3, pady=10, sticky=W)
       ##TIME
       AttendanceID_label = Label(Class_frame, text="Date", font=("times new roman", 12, "bold"))
       AttendanceID_label.grid(row=2, column=2, padx=3, pady=10, sticky=W)
       AttendanceID_Entry = ttk.Entry(Class_frame, width=15,textvariable=self.var_date,
                                      font=("times new roman", 12, "bold"))
       AttendanceID_Entry.grid(row=2, column=3, padx=3, pady=10, sticky=W)

      ## Status
       status_label = Label(Class_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
       status_label.grid(row=3, column=0)

       status_combo = ttk.Combobox(Class_frame,textvariable=self.var_attendance, font=("times new roman", 12, "bold"),
                                state="read only", width=17)
       status_combo["values"] = ("Status ", "Absent", "Present")
       status_combo.current(0)
       status_combo.grid(row=3, column=1, padx=3, pady=10, sticky=W)
       #  button
       btnframe = Frame(Class_frame, bd=2, relief=RIDGE, bg="white")
       btnframe.place(x=0, y=200, width=600, height=350)
       Photobtn = Button(btnframe, text="Import.csv",command=self.importCsv, font=("arial", 13, "bold"),
                         bg="Blue", fg="White")
       Photobtn.grid(row=0, column=0)
       upphotobtn = Button(btnframe, text="Export.csv",command=self.ExportCsv, font=("arial", 13, "bold"), bg="Blue", fg="White")
       upphotobtn.grid(row=0, column=1)


       resetbtn = Button(btnframe, text="Reset",command= self.reset,font=("arial", 13, "bold"), bg="Blue",
                         fg="White")
       resetbtn.grid(row=0, column=2)


       # left frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Attendance Details",
                               font=("times new roman", 12, "bold"))
       Right_frame.place(x=610, y=10, width=600, height=530)

       Table_frame = LabelFrame(Right_frame, bd=2, bg="White", relief=RIDGE, text="Table",
                                font=("times new roman", 12, "bold"))
       Table_frame.place(x=0, y=135, width=600, height=250)
       scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
       self.Attendance_table = ttk.Treeview(Table_frame, column=(
       "id", "name","Dept", "Course","time","date","attendance"),
                                         xscrollcommand=scroll_x, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command=self.Attendance_table.xview)
       scroll_y.config(command=self.Attendance_table.yview)
       self.Attendance_table.heading("id", text="StudentID")
       self.Attendance_table.heading("name", text="Name")
       self.Attendance_table.heading("Dept", text="Department")
       self.Attendance_table.heading("Course", text="Course")
       self.Attendance_table.heading("time", text="Time")
       self.Attendance_table.heading("date", text="Date")
       self.Attendance_table.heading("attendance", text="Attendance")
       self.Attendance_table["show"] = "headings"
       self.Attendance_table.column("id", width=100)
       self.Attendance_table.column("name", width=100)
       self.Attendance_table.column("Dept", width=100)
       self.Attendance_table.column("Course", width=100)
       self.Attendance_table.column("time", width=100)
       self.Attendance_table.column("date", width=100)
       self.Attendance_table.column("attendance", width=100)
       self.Attendance_table.pack(fill=BOTH,expand=1)
       self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)

############# fetch data ###########
    def fetchData(self,rows):
      self.Attendance_table.delete(*self.Attendance_table.get_children())
      for i in rows:
         self.Attendance_table.insert("",END,values=i)

    def importCsv(self):
       global mydata

       fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV files","*csv"),("All File","*.*")),
                                      parent=self.root)
       with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
             mydata.append(i)
          self.fetchData(mydata)
######### Export
    def ExportCsv(self):
      try:
          if len(mydata)<1:
             messagebox.showerror("No Data","No Data found to Export",parent=self.root)
             return False

          fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV files", "*csv"), ("All File", "*.*")),
                                             parent=self.root)
          with open(fln,mode="w",newline="") as myfile:
               exp_write = csv.writer(myfile, delimiter=",")
               for i in mydata:
                   exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+"Sucessfully")
      except Exception as es:
           messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
       cursor_focus=self.Attendance_table.focus()
       content=self.Attendance_table.item(cursor_focus)
       rows=content["values"]
       self.var_id.set(rows[0])
       self.var_name.set(rows[1])
       self.var_Dept.set(rows[2])
       self.var_Course.set(rows[3])
       self.var_time.set(rows[4])
       self.var_date.set(rows[5])
       self.var_attendance.set(rows[6])

    def reset(self):

       self.var_id.set("")
       self.var_name.set(" ")
       self.var_Dept.set(" ")
       self.var_Course.set(" ")
       self.var_time.set(" ")
       self.var_date.set(" ")
       self.var_attendance.set("Status")


if __name__ == '__main__':
    root= Tk()
    obj = Attendance(root)
    root.mainloop()