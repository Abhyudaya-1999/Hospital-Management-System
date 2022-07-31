from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.nameoftablets=StringVar()
        self.ref=StringVar()
        self.dailydose=StringVar()
        self.dose=StringVar()
        self.patientname=StringVar()
        self.patientid=StringVar()
        self.medication=StringVar()
        self.issuedate=StringVar()
        self.expirydate=StringVar()
        self.nhsnumber=StringVar()
        self.lot=StringVar()
        self.sideeffects=StringVar()
        self.nooftablets=StringVar()
        self.furtherinfo=StringVar()
        self.bloodpressure=StringVar()
        self.storageadvice=StringVar()
        self.dob=StringVar()
        self.followup=StringVar()
        self.patientadd=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #  =============================Data frame================================================ #
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                               font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)   

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                               font=("times new roman",12,"bold"),text="Prescription")                                   
        DataFrameRight.place(x=990,y=5,width=460,height=350)





        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)




        lblNameTablet=Label(DataFrameLeft,font=("arial",13,"bold"),text="Names of Tablet:",padx=2,pady=4)
        lblNameTablet.grid(row=0,column=0)
        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.nameoftablets,font=("times new roman",12,"bold"),width=33)
        comNameTablet["values"]=("nice","corona vaccines","calpol","serodin","becosule b-12")
        comNameTablet.grid(row=0,column=1)  

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No.:",padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.ref,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)   

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblnooftablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="Number of Tablets:",padx=2,pady=4)
        lblnooftablets.grid(row=3,column=0,sticky=W)
        txtnooftablets=Entry(DataFrameLeft,textvariable=self.nooftablets,font=("arial",13,"bold"),width=35)
        txtnooftablets.grid(row=3,column=1)    

        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="lot:",padx=2,pady=4)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.lot,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)  

        lblissuedate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=4)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate=Entry(DataFrameLeft,textvariable=self.issuedate,font=("arial",13,"bold"),width=35)
        txtissuedate.grid(row=5,column=1)  

        lblexpdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=4)
        lblexpdate.grid(row=6,column=0,sticky=W)
        txtexpdate=Entry(DataFrameLeft,textvariable=self.expirydate,font=("arial",13,"bold"),width=35)
        txtexpdate.grid(row=6,column=1)  

        lbldailydose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lbldailydose.grid(row=7,column=0,sticky=W)
        txtdailydose=Entry(DataFrameLeft,textvariable=self.dailydose,font=("arial",13,"bold"),width=35)
        txtdailydose.grid(row=7,column=1)  

        lblsideeffects=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=4)
        lblsideeffects.grid(row=8,column=0,sticky=W)
        txtsideeffects=Entry(DataFrameLeft,textvariable=self.sideeffects,font=("arial",13,"bold"),width=35)
        txtsideeffects.grid(row=8,column=1)  

        lblfurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Info:",padx=2,pady=4)
        lblfurtherinfo.grid(row=9,column=0,sticky=W)
        txtfurtherinfo=Entry(DataFrameLeft,textvariable=self.furtherinfo,font=("arial",13,"bold"),width=35)
        txtfurtherinfo.grid(row=9,column=1) 

        lblbloodpressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=4)
        lblbloodpressure.grid(row=1,column=2,sticky=W)
        txtbloodpressure=Entry(DataFrameLeft,textvariable=self.bloodpressure,font=("arial",13,"bold"),width=35)
        txtbloodpressure.grid(row=1,column=3) 

        lblstorageadvice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=4)
        lblstorageadvice.grid(row=2,column=2,sticky=W)
        txtstorageadvice=Entry(DataFrameLeft,textvariable=self.storageadvice,font=("arial",13,"bold"),width=35)
        txtstorageadvice.grid(row=2,column=3)

        lblmedication=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=4)
        lblmedication.grid(row=3,column=2,sticky=W)
        txtmedication=Entry(DataFrameLeft,textvariable=self.medication,font=("arial",13,"bold"),width=35)
        txtmedication.grid(row=3,column=3)

        lblpatientid=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=4)
        lblpatientid.grid(row=4,column=2,sticky=W)
        txtpatientid=Entry(DataFrameLeft,textvariable=self.patientid,font=("arial",13,"bold"),width=35)
        txtpatientid.grid(row=4,column=3)

        lblnhsnumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=4)
        lblnhsnumber.grid(row=5,column=2,sticky=W)
        txtnhsnumber=Entry(DataFrameLeft,textvariable=self.nhsnumber,font=("arial",13,"bold"),width=35)
        txtnhsnumber.grid(row=5,column=3)

        lblpatientname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=4)
        lblpatientname.grid(row=6,column=2,sticky=W)
        txtpatientname=Entry(DataFrameLeft,textvariable=self.patientname,font=("arial",13,"bold"),width=35)
        txtpatientname.grid(row=6,column=3)   

        lbldob=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=4)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob=Entry(DataFrameLeft,textvariable=self.dob,font=("arial",13,"bold"),width=35)
        txtdob.grid(row=7,column=3) 

        lblpatientadd=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=4)
        lblpatientadd.grid(row=8,column=2,sticky=W)
        txtpatientadd=Entry(DataFrameLeft,textvariable=self.patientadd,font=("arial",13,"bold"),width=35)
        txtpatientadd.grid(row=8,column=3)   

        lblfollowup=Label(DataFrameLeft,font=("arial",12,"bold"),text="Follow Up:",padx=2,pady=4)
        lblfollowup.grid(row=9,column=2,sticky=W)
        txtfollowup=Entry(DataFrameLeft,textvariable=self.followup,font=("arial",13,"bold"),width=35)
        txtfollowup.grid(row=9,column=3)     

        #===========================dataframeright===========================================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=4)
        self.txtPrescription.grid(row=0,column=0)

        #=============================buttons==============================
        btnPrescription=Button(ButtonFrame,command=self.iPrescription,text="Precription",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnPrescription.grid(row=0,column=0)

        btnprescriptiondata=Button(ButtonFrame,text="Prescription Data",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnprescriptiondata.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,command=self.update_data,text="Update",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,command=self.idelete,text="Delete",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,command=self.clear,text="Clear",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.iExit,text="Exit",bg='green',fg='white',font=("arial",7,"bold"),width=40,height=7,padx=2,pady=4)
        btnExit.grid(row=0,column=5)

        #==========================table===============================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","no of tablets","issue date",
        "expiry date","patient id","patient name","nhs number","medication","lot","sideeffects"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftable",text="Name of tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("no of tablets",text="No. of Tablets")
        self.hospital_table.heading("issue date",text="Issue Date")
        self.hospital_table.heading("expiry date",text="Expiry Date")
        self.hospital_table.heading("sideeffects",text="Side Effects")
        self.hospital_table.heading("patient id",text="Patient ID")
        self.hospital_table.heading("nhs number",text="NHS Number")
        self.hospital_table.heading("medication",text="Medication")
        self.hospital_table.heading("lot",text="LOT")
        self.hospital_table.heading("patient name",text="Patient Name")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("no of tablets",width=100)
        self.hospital_table.column("issue date",width=100)
        self.hospital_table.column("expiry date",width=100)
        self.hospital_table.column("sideeffects",width=100)
        self.hospital_table.column("patient id",width=100)
        self.hospital_table.column("nhs number",width=100)
        self.hospital_table.column("medication",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("patient name",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


#=========================functionality========================
    def iPrescription(self):
        if (self.nameoftablets.get()==" " or self.ref.get()==" "):
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="Abhyudaya Yadav",password="Datatash@123",database="abhyudaya")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.nameoftablets.get(),
                                                                                        self.ref.get(),
                                                                                        self.dose.get(),
                                                                                        self.nooftablets.get(),
                                                                                        self.issuedate.get(),
                                                                                        self.expirydate.get(),
                                                                                        self.sideeffects.get(),
                                                                                        self.patientid.get(),
                                                                                        self.nhsnumber.get(),
                                                                                        self.medication.get(),
                                                                                        self.lot.get(),
                                                                                        self.patientname.get(),
                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="Abhyudaya Yadav",password="Datatash@123",database="abhyudaya")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set nameoftablets=%s,ref=%s,dose=%s,nooftablets=%s,issuedate=%s,expirydate=%s,sideeffects=%s,patientid=%s,nhsnumber=%s,medication=%s,lot=%s,patientname=%s"),(
                                                      self.nameoftablets.get(),
                                                      self.ref.get(),
                                                      self.dose.get(),
                                                      self.nooftablets.get(),
                                                      self.issuedate.get(),
                                                      self.expirydate.get(),
                                                      self.sideeffects.get(),
                                                      self.patientid.get(),
                                                      self.nhsnumber.get(),
                                                      self.medication.get(),
                                                      self.lot.get(),
                                                      self.patientname.get(),
                                                )
        conn.commit()
        self.fetch_data()
        conn.close()  
        messagebox.showinfo("Success","Record has been inserted")
                                      


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="Abhyudaya Yadav",password="Datatash@123",database="abhyudaya")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
           self.hospital_table.delete(*self.hospital_table.get_children())
           for i in rows:
                self.hospital_table.insert(" ",END,values=i)
           conn.commit()
        conn.close() 
           

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.nooftablets.set(row[3])
        self.issuedate.set(row[4])
        self.expirydate.set(row[5])
        self.sideeffects.get(row[6])
        self.patientid.get(row[7])
        self.nhsnumber.get(row[8])
        self.medication.get(row[9])
        self.lot.get(row[10])
        self.patientname.get(row[11])

    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.nameoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Reference No.:\t\t\t"+self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.dose.get()+"\n")
        self.txtPrescription.insert(END,"no of tablets:\t\t\t"+self.nooftablets.get() + "\n")
        self.txtPrescription.insert(END,"issue Date:\t\t\t"+self.issuedate.get() + "\n")
        self.txtPrescription.insert(END,"expiry date:\t\t\t"+self.expirydate.get() + "\n")
        self.txtPrescription.insert(END,"side effects:\t\t\t"+self.sideeffects.get() + "\n")
        self.txtPrescription.insert(END,"patient id:\t\t\t"+self.patientid.get() + "\n")
        self.txtPrescription.insert(END,"nhs number:\t\t\t"+self.nhsnumber.get() + "\n")
        self.txtPrescription.insert(END,"medication:\t\t\t"+self.medication.get() + "\n")
        self.txtPrescription.insert(END,"lot:\t\t\t"+self.lot.get() + "\n")
        self.txtPrescription.insert(END,"patient name:\t\t\t"+self.patientname.get() + "\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="Abhyudaya Yadav",password="Datatash@123",database="abhyudaya")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.nameoftablets.set("")
        self.ref.set("")
        self.dose.set("")
        self.nooftablets.set("")
        self.issuedate.set("")
        self.expirydate.set("")
        self.sideeffects.set("")
        self.patientid.set("")
        self.nhsnumber.set("")
        self.medication.set("")
        self.lot.set("")
        self.patientname.set("")
        self.bloodpressure.set("")
        self.furtherinfo.set("")
        self.patientadd.set("")
        self.storageadvice.set("")
        self.followup.set("")
        self.dailydose.set("")
        self.dob.set("")
    
    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return    


root=Tk()
ob=hospital(root)
root.mainloop()
