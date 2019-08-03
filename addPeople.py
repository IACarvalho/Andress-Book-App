from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur = con.cursor()


class AddPeope(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add People')
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/addperson.png')
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
        self.entry_name.insert(0,'Please enter a name')
        self.entry_name.place(x=150, y=45)

        #Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.insert(0,'Please enter a surname')
        self.entry_surname.place(x=150, y=85)

        # E-mail
        self.lbl_email = Label(self.bottomFrame, text='E-mail:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.insert(0,'Please enter a E-mail')
        self.entry_email.place(x=150, y=125)

        # Phone number
        self.lbl_phone = Label(self.bottomFrame, text='Phone:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.insert(0,'Please enter a Phone Number')
        self.entry_phone.place(x=150, y=165)

        # Address

        self.lbl_address = Label(self.bottomFrame, text='Address:', font='arial 15 bold', fg='white',
                            bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=31, height=20, wrap=WORD)
        self.address.place(x=150, y=200)

        #Button

        button = Button(self.bottomFrame, text='Add Person', command=self.addPerson)
        button.place(x=215, y=460)

    def addPerson(self):
        name = self.entry_name.get()
        surName = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.address.get(1.0,'end-1c')

        if(name and surName and email and phone and address != ""):
            try:
                query="INSERT INTO 'persons' (Person_Name, person_surname, person_email, person_phone, person_address) VALUES(?,?,?,?,?)"
                cur.execute(query, (name, surName, email, phone, address))
                con.commit()
                messagebox.showinfo("Succsess", "Succsessfuly! Person already in your adress book", icon="info")
                self.destroy()
            except:
                messagebox.showerror('Error', "can't add to database\n\nPlease call suport", icon="warning")
                self.destroy()
        else:
            messagebox.showerror('Error', "Please don't let any field empity", icon="warning")