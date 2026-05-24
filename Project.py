# -*- coding: utf-8 -*-
"""
@author: Rohit Sah
"""
import csv
import os
from os import system
from getpass import getpass
system('cls')

def ADD():
    print("=========To add new record=========== ")
    csv_w=open('student.csv','a',newline='')
    obj=csv.writer(csv_w)
    ID=input("Enter the Student id:")
    SName=input("Enter the Student Name:")
    Attendence=int(input("Total attendence:"))
    CS=float(input("Enter the marks of student in CS:"))
    PH=float(input("Enter the marks of student in physics:"))
    CH=float(input("Enter the marks of student in Chemistry:"))
    MA=float(input("Enter the marks of student in Maths:"))
    PE=int(input("Enter the marks of student in Physical Education:"))
    record=[]
    record.append(ID)
    record.append(SName)
    record.append(Attendence)
    record.append(CS)
    record.append(PH)
    record.append(CH)
    record.append(MA)
    record.append(PE)
    
    obj.writerow(record)
    del obj
    csv_w.close


    input("\n press any key to continue...")

def TRAVERSE():
    try:
        csv_r=open('Student.csv','r')
        obj=csv.reader(csv_r)
        print("\n\t ID \t NAME \t ATTENDENCE \t COMPUTERSCI \t    PHYSICS \t    CHEMISTRY\t    MATHS\tPT")
        print("________________________________________________________________________________________________")
        a=0
        for row in obj:
                if row:
                      print("\t %s    \t %s      \t %s    \t %s     \t %s    \t %s     \t%s   \t%s"%(row[0] ,row[1] ,row[2], row[3], row[4], row[5], row[6], row[7]))

                else:
                    print("\n\t No Record,file is empty....")
        del obj
        csv_r.close()
            
    except FileNotFoundError:
        print("No Such file found...")
        input("\n press any key to continue...")
    
def SEARCH(ID):
    val=0
    try:
        csv_r=open('Student.csv','r')
        obj=csv.reader(csv_r)
        for row in obj:
            if row :
                if row [0]==ID:
                    print("\n\t ID \t NAME \t ATTENDENCE \t COMPUTERSCI \t PHYSICS \t CHEMISTRY\t MATHS\t  PT")
                    print("___________________________________________________________________________________________________")
                    print("\t %s    \t %s      \t %s    \t %s \t %s    \t %s     \t%s   \t%s"%(row[0] ,row[1] ,row[2], row[3], row[4], row[5], row[6], row[7]))
                    val=1
                    break
            else:
                print("\n\t No Record,file is empty....")
                val=-1
                
        del obj
        csv_r.close()
            
    except FileNotFoundError:
        print("no such file found")
    if val==0:
        print("No matching record found..")
    input("\n press any key to continue...")
    return val
           
def DELETE():
    print("Delelting a record")
    found=0
    c=input("Enter the Student ID to delete :")
    try:
        csv_r=open('student.csv','r')
        csv_w=open('temp.csv','w',newline='')
        objr=csv.reader(csv_r)
        objw=csv.writer(csv_w)
        for row in objr:
            if row[0]==c:
                found=1
                print("Record deleted successfully...!")
            else:
                objw.writerow(row)
                
        del objr
        del objw
        
        csv_r.close()
        csv_w.close()   
            
    except FileNotFoundError:
        print("unexpected erroe generated....")
    os.remove("student.csv")
    os.rename("temp.csv","student.csv")
def USER():
     c=input("Enter the your id :")
     print("========your details============")
     try:
        csv_r=open('Student.csv','r')
        obj=csv.reader(csv_r)
        a=0
        for row in obj:
            if row[0]==c:
                print("\n\t ID \t NAME \t ATTENDENCE \t COMPUTERSCI \t PHYSICS \t CHEMISTRY\t MATHS\t  PT")
                print("__________________________________________________________________________________________________________")
                print("\t %s    \t %s   \t %s    \t %s  \t %s    \t %s    \t%s    \t%s    "%(row[0] ,row[1] ,row[2], row[3], row[4], row[5], row[6], row[7]))
                break
        else:
            print("no such record")
        del obj
        csv_r.close()
     except FileNotFoundError:
         print("No Such file found...")
         input("\n press any key to continue...")
def ADMIN():
    system('cls')
    loop=True
    while loop:
        print("\t           Welcome to admin account..")
        print("\n\t\t STUDENT REPORT MANAGMENT")
        print("\n\t\t1. ADD a new record")
        print("\n\t\t2.Delete a Record")
        print("\n\t\t3.Display  all records")
        print("\n\t\t4.to dispaly a particular record")
        print("\n\t\t5.Return to main menu")
        val=int(input("\n\n\tEnter your choice(1 - - - 5)?"))
        if val==1:
            ADD()
        elif val==2:
            DELETE()
        elif val==3:
            TRAVERSE()
        elif val==4:
            c = input("Enter the ID to be searched:")
            SEARCH(c)
        else:
            loop=False
def mainMenu():
    opt='y'
    while opt in ['y','y']:
        system('cls')
        print("\n\t\tWelcome to   Student Report Managment System")
        print("\n\n\t 1.login as administrator")
        print("\n\n\t 2.login as user")
        print("\n\n\t 3.Exit")
        choice=input("\n\n\t\t Enter your choice (1,2 or 3):")
        if choice=='1':
            count=3
            while count >0:
                count=count-1
                username=input("Enter the username:")
                password=input("Enter the password:")
                if username=='rohit'and password=='report123':
                    print("LOGIN SUCCESSFUL")
                    count=0
                    ADMIN()
                else:
                    print(" invaled username or password.")
                    print()
                    print("you have  %d valid attempts left now"%(count))
                    print()
                    print()
            print("press enter for other login option")

        elif choice=='2':
            USER()
        elif choice=='3':
            input("Press any key now will terminate the program")
            exit()
        else:
            print("invaled choice entered")
            opt=input("Do u wish to continue (y/n)?")
mainMenu()

        
