from tkinter import *
import sqlite3
import addPeople
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My People")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My Persons', font='arial 15 bold',
                            fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # Scrollbar
        self.sb=Scrollbar(self.bottomFrame, orient=VERTICAL)

        # Listbox
        self.listBox = Listbox(self.bottomFrame, width=60, height=42)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.sb.config(command= self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        persons = con.execute("SELECT * FROM persons").fetchall()
        count = 0
        for person in persons:
             self.listBox.insert(count, str(person[0])+"-"+person[1]+" "+person[2])
             count +=1

        # Buttons
        btnadd = Button(self.bottomFrame, text='Add', width=12, font='Sans 12 bold',
                        command=self.funcAddPeople)
        btnadd.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        btnupdate = Button(self.bottomFrame, text='Update', width=12, font='Sans 12 bold',
                            command=self.funcUpdatePeople)
        btnupdate.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        btndisplay = Button(self.bottomFrame, text='Display', width=12, font='Sans 12 bold',
                            command = self.funcDisplayPerson)
        btndisplay.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btndelete = Button(self.bottomFrame, text='Delete', width=12, font='Sans 12 bold',
                        command=self.funcDeletePerson)
        btndelete.grid(row=0, column=2, sticky=N, padx=10, pady=130)
    
    def funcAddPeople(self):
        addpage = addPeople.AddPeope()
        self.destroy()

    def funcUpdatePeople(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]
        updateapge = Update()
        self.destroy()
    
    def funcDisplayPerson(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]
        displaypage = Dispay()
        self.destroy

    def funcDeletePerson(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]
        
        mbox = messagebox.askquestion("Warning", "You realy want to delete this person?",
                                    icon='warning')
        
        if mbox == 'yes':
            try:
                cur.execute("DELETE FROM persons WHERE person_id = ?", (person_id))
                con.commit()
                messagebox.showinfo("Success", "Person has been deleted")
                self.destroy()
            except:
                messagebox.showinfo("Error", "Person has not been deleted")
                self.destroy()

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Update Person")
        self.resizable(False, False)

        # get person from database
        global  person_id
        person_info = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id,)).fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/update.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My Persons', font='arial 15 bold',
                            fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # Labels and Entries
        #name
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.insert(0,self.person_name)
        self.entry_name.place(x=150, y=45)

        #Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0,self.person_surname)
        self.entry_surname.place(x=150, y=85)

        # E-mail
        self.lbl_email = Label(self.bottomFrame, text='E-mail:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0,self.person_email)
        self.entry_email.place(x=150, y=125)

        # Phone number
        self.lbl_phone = Label(self.bottomFrame, text='Phone:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.place(x=150, y=165)

        # Address

        self.lbl_address = Label(self.bottomFrame, text='Address:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=31, height=20, wrap=WORD)
        self.address.insert('1.0', self.person_address)
        self.address.place(x=150, y=200)

        #Button

        button = Button(self.bottomFrame, text='Update Person', command = self.updatePerson)
        button.place(x=215, y=460)
    def updatePerson(self):
        person_id = self.person_id
        person_name = self.entry_name.get()
        person_surname = self.entry_surname.get()
        person_email = self.entry_email.get()
        person_phone = self.entry_phone.get()
        person_address = self.address.get(1.0, 'end-1c')

        if(person_name and person_surname and person_email and person_phone and person_address != ""):
            try:
                query = '''UPDATE persons set person_name =?,
                    person_surname = ?,person_email = ?,
                    person_phone = ?,person_address = ?
                    WHERE person_ID = ?'''
                con.execute(query, (person_name, person_surname, person_email,
                            person_phone, person_address, person_id))
                con.commit()
                messagebox.showinfo("Success", "Your update is already done", icon="info")
                self.destroy()
            except:
                messagebox.showerror('Error', "can't add to database\n\nPlease call suport", icon="warning")
                self.destroy()
        else:
            messagebox.showerror('Error', "Please don't let any field empity", icon="warning")

class Dispay(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Display Person")
        self.resizable(False, False)
     # get person from database
        global  person_id
        person_info = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id,)).fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

    # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

    # Heading, image and date
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My Persons', font='arial 15 bold',
                            fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

    # Labels and Entries
    #name
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.insert(0,self.person_name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150, y=45)

    #Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0,self.person_surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=150, y=85)

    # E-mail
        self.lbl_email = Label(self.bottomFrame, text='E-mail:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0,self.person_email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=150, y=125)

    # Phone number
        self.lbl_phone = Label(self.bottomFrame, text='Phone:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=150, y=165)

    # Address

        self.lbl_address = Label(self.bottomFrame, text='Address:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=31, height=20, wrap=WORD)
        self.address.insert('1.0', self.person_address)
        self.address.config(state=DISABLED)
        self.address.place(x=150, y=200)