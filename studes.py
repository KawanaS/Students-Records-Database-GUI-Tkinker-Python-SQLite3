from tkinter import*
import sqlite3

root=Tk()
root.title('Students Records')

#create a database or connect to one
conn=sqlite3.connect('studes.db')      #creates a database file in the same  directory
#create a cursor
cur=conn.cursor()
#create table in the database
cur.execute("""CREATE TABLE students(
name text,
studentid text,
score integer
)""")

#create the submit function
def submit():
    conn = sqlite3.connect('studes.db')
    cur = conn.cursor()
    #insert into database
    cur.execute("INSERT INTO students VALUES(:name,:studentid,:score)",
                {
                    'name':name_entry.get(),
                    'studentid':studentid_entry.get(),
                    'score':score_entry.get()

                }
                )
    conn.commit()
    conn.close()
    name_entry.delete(0,END)
    studentid_entry.delete(0,END)
    score_entry.delete(0,END)

#create the show records function
def show():
    conn = sqlite3.connect('studes.db')
    cur = conn.cursor()
    #search the database
    cur.execute("SELECT *, oid FROM students")
    records=cur.fetchall()
    print_records=''
    for record in records:
        print_records += str(record) + '\n'
    print_label=Label(root,text=print_records)
    print_label.grid(row=5,column=1)
    conn.commit()
    conn.close()

#create the delete function
def delete():
    conn = sqlite3.connect('studes.db')
    cur = conn.cursor()
    cur.execute("DELETE from students WHERE oid=" + OID_entry.get())
    OID_entry.delete(0,END)
    conn.commit()
    conn.close()

#create the save fucntion
def save():
    conn = sqlite3.connect('studes.db')
    cur = conn.cursor()
    cur.execute("""UPDATE students SET 
            name=:name1,
            studentid=:studentid1,
            score=:score1
            WHERE oid=:oid """,
                   {
        'name1':nameupdate_entry.get(),
        'studentid1':studentidupdate_entry.get(),
        'score1':scoreupdate_entry.get(),
        'oid': OID_entry.get()
       }     )

    conn.commit()
    conn.close()

#create input lables
name_label=Label(root,text='Name',padx=10)
name_label.grid(row=0,column=0)
name_entry=Entry(root,width=30)
name_entry.grid(row=0,column=1)

studentid_label=Label(root,text='Student ID',padx=10)
studentid_label.grid(row=1,column=0)
studentid_entry=Entry(root,width=30)
studentid_entry.grid(row=1,column=1)

score_label=Label(root,text='Score',padx=10)
score_label.grid(row=2,column=0)
score_entry=Entry(root,width=30)
score_entry.grid(row=2,column=1)

#create submit button
submit_btn=Button(root,text='Submit',command=submit)
submit_btn.grid(row=3,column=1)

#create the show records button
showrecords_btn=Button(root,text='Show Records',command=show)
showrecords_btn.grid(row=4,column=1)

#create the delete button
delete_btn=Button(root,text='Delete',command=delete)
delete_btn.grid(row=9,column=1)

#create the update entries
OID_label=Label(root,text='Update OID',padx=10)
OID_label.grid(row=8,column=0)
OID_entry=Entry(root,width=30)
OID_entry.grid(row=8,column=1)
nameupdate_label=Label(root,text='Name Update',padx=10)
nameupdate_label.grid(row=11,column=0)
nameupdate_entry=Entry(root,width=30)
nameupdate_entry.grid(row=11,column=1)

studentidupdate_label=Label(root,text='Student ID Update',padx=10)
studentidupdate_label.grid(row=12,column=0)
studentidupdate_entry=Entry(root,width=30)
studentidupdate_entry.grid(row=12,column=1)

scoreupdate_label=Label(root,text='Score Update',padx=10)
scoreupdate_label.grid(row=13,column=0)
scoreupdate_entry=Entry(root,width=30)
scoreupdate_entry.grid(row=13,column=1)

#create the update button
update_btn=Button(root,text='Save',command=save)
update_btn.grid(row=14,column=1)

conn.commit()
conn.close()

root.mainloop()
