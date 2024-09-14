# *********************** Project on Hotel Management **************************
import os
import datetime as dt
import mysql.connector as ms

def welcome():
    print("---------------------------------------------------------------------------------------")
    print("\n\n****************** W E L C O M E ************************\n\n ")
    print(" HOTEL  MANAGEMENT  SYSTEM ")
    print(" \n D E V E L O P E D  B Y :\n")
    print(" Faaiz Ali Ahmad\n\n\ ")
      
def introduction():
    intro = '''
    ---------------------------------------------------------------------------
                 W E L C O M E     T O      H O T E L    T A J
              ___________________________________________________
                
    WELCOME TO THE HOTEL TAJ. WE HAVE INCLUDED THREE TYPES OF ROOM IN OUR HOTEL.
    WE HAVE ALSO INCLUDED MANY FACILITES IN OUR  HOTEL FOR THE  CONVENEINCE FOR
    OUR  GUESTS.
    WE HAVE TOTAL 300 ROOMS IN OUR HOTEL.THE LIST OF ROOMS THAT WE HAVE ARE
    AS UNDER:-
     TYPES OF ROOM                TOTAL NO. OF ROOMS         CHARGES(per day)
    ****************             ********************      *******************
         AC                              100                        $100/-
         AC DELUXE                       100                        $200/-
         SUPER DELUXE                    50                         $300/-
         EXECUTIVE                       50                         $400/-
   THE LIST OF FACILITIES THAT WE OFFER TO OUR GUESTS ARE AS UNDER:-
         1. ROOM  SERVICES     (10% extra charges)
         2. RESTAURANT  AND  BAR
         3. TAXI               ($50/- per hour)
         4. SWIMMING POOL      (Open from 06:00 am to 18:00 pm)
         5. STEAM BATH         ($20 per hour)
    ---------------------------------------------------------------------------
    '''
    print(intro)
  
def ADDGUEST():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        i   = input("Enter Guest ID   : ")
        nm  = input("Enter Name       : ")
        add = input("Enter Address    : ")
        mob = input("Enter Mobile No. : ")
        try:
            st = "insert into guest values( {}, '{}', '{}', '{}', null, '--', 0, 0, 0, 0, 0, 0, 0)".format(i, nm, add, mob)
            cursor.execute(st)
            conobj.commit()
            print("\n\nData added successfully\n")
        except ms.ProgrammingError:
            print('[ NO TABLE EXIST ]')
            return
        ch = input("Press y to add more records : ")
    conobj.close()
    
def DISPLAYGUEST():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        st = "select * from guest order by id"
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    f = 0
    print("\n\t\t\t\tLIST  OF  GUESTS\n")
    while d is not None:
        f = 1
        print("---------------------------------------------------------------------------------------")
        print("Guest ID : ", d[0], end = ' ')
        print("Name : ", d[1], end = ' ')
        print("Address : ", d[2], end = ' ')
        print("Mobile No. : ", d[3])
        print("Date of Booking : ", d[4])
        print("Room Type : ", d[5], end = ' ')
        print("No. of Rooms : ", d[6], end = ' ')
        print("No. of Days  : ", d[7], end = ' ')
        print("Room Charges : ", d[8], end = ' ')
        print("Restaurant Bill : ", d[9], end = ' ')
        print("Taxi Charges : ", d[10], end = ' ')
        print("Steam Bath Charges: ", d[11])
        print("Grand Total: ", d[12])
        print("---------------------------------------------------------------------------------------")
        d = cursor.fetchone()
    conobj.close()
    if f == 0:
        print("\n\nNo Record Exist\n")
    
def SEARCHGUEST():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print(d)
        print("\n\t\t\t\t[ SEARCH  RESULT ... ]\n")
        print("---------------------------------------------------------------------------------------")
        print("Guest   ID         : ", d[0])
        print("Name               : ", d[1])
        print("Address            : ", d[2])
        print("Mobile No.         : ", d[3])
        print("Date of Booking    : ", d[4])
        print("Room Type          : ", d[5])
        print("Number of Rooms    : ", d[6])
        print("Number of Days     : ", d[7])
        print("Room Charges       : ", d[8])
        print("Restaurant Bill     : ", d[9])
        print("Taxi Charges       : ", d[10])
        print("Steam Bath Charges : ", d[11])
        print("Grand Total        : ", d[12])
        print("---------------------------------------------------------------------------------------")
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
    
def EDITGUEST():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\t\t\t\t[ MODIFYING  RECORDS ]\n")
        n = input("Enter new Name or press 0 to unchange : ")
        if n !='0':
            st = "update guest set name = '{}' where id = {}".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Address or press 0 to unchange : ")
        if n !='0':
            st = "update guest set address = '{}' where id = {}".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Mobile No. or press 0 to unchange : ")
        if n !='0':
            st = "update guest set mobile = '{}' where id = {}".format(n, i)
            cursor.execute(st)
            conobj.commit()
        conobj.close()
        print("\n\nRecord Modified Successfully\n")
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
def REMOVEGUEST():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        st = "delete from guest where id = {}".format(i)
        cursor.execute(st)
        conobj.commit()
        conobj.close()
        print("\n\nRecord Deleted Successfully\n")
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
def BOOKING():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        ch = 1
        while ch !=5:
            print(" MAKE  YOUR  BOOKING ")
            print("______________________")
            print("SELECT A ROOM")
            print("Press 1 FOR AC")
            print("Press 2 FOR AC DELUXE")
            print("Press 3 FOR SUPER DELUXE")
            print("Press 4 FOR EXECUTIVE")
            print("Press 5 FOR EXIT BOOKING")
            ch = int(input("Enter your choice : "))
            if ch == 1 :
                r = 'AC'
                n = int(input("Enter Number of Rooms : "))
                nd = int(input("Enter Number of Days : "))
                b = n*4000*nd
                break
            elif ch == 2:
                r = 'AC DELUXE'
                n = int(input("Enter Number of Rooms : "))
                nd = int(input("Enter Number of Days : "))
                b = n*5000*nd
                break
            elif ch == 3:
                r = 'SUPER DELUXE'
                n = int(input("Enter Number of Rooms : "))
                nd = int(input("Enter Number of Days : "))
                b = n*8000*nd
                break
            elif ch == 4:
                r = 'EXECUTIVE'
                n = int(input("Enter Number of Rooms : "))
                nd = int(input("Enter Number of Days : "))
                b = n*12000*nd
                break
            elif ch == 5:
                print("Booking Exit")
                r = '--'
                n = 0
                nd = 0
                b = 0
                break
            else:
                print("Invalid Choice of Room")
        da = dt.date.today()
        amt = b + d[9]+ d[10]+ d[11]
        st = "update guest set dob = '{}', roomtype = '{}', norooms = {}, nod = {}, bill = {}, total = {} where id = {}".format(da, r, n, nd, b, amt, i )
        cursor.execute(st)
        conobj.commit()
        st = "select id , name, address, mobile, dob, roomtype, norooms , bill from guest where id = {}".format(i)
        cursor.execute(st)
        d = cursor.fetchone()
        print("\n\n              [ BOOKING  CONFIRMED")
        print("---------------------------------------------------------------------------------------")
        print("\t\tHOTEL  TAJ\n")
        print("Guest   ID      : ", d[0])
        print("Name            : ", d[1])
        print("Address         : ", d[2])
        print("Mobile No.      : ", d[3])
        print("Date of Booking : ", d[4])
        print("Room Type       : ", d[5])
        print("Number of Rooms : ", d[6])
        print("Booking Amount  : ", d[7])
        print("---------------------------------------------------------------------------------------")
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
def CANCELLATION():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        ch = input("Are You Sure To Cancel This Booking (y/n) : ")
        if ch == 'y' or ch == 'Y':
            print("\n\n              [ BOOKING  CANCELLED")
            print("---------------------------------------------------------------------------------------")
            print("\t\tHOTEL  TAJ\n")
            print("Guest   ID        : ", d[0])
            print("Name              : ", d[1])
            print("Address           : ", d[2])
            print("Mobile No.        : ", d[3])
            print("Booking Date      : ", d[4])
            print("Cancellation Date : ", dt.date.today())
            print("Room Type         : ", d[5])
            print("Number of Rooms   : ", d[6])
            print("Refund  Amount    : ", d[7])
            print("---------------------------------------------------------------------------------------")
            print("Amount will be credit in your account within 24 hours.")
            st = "update guest set roomtype = '--', norooms = 0, bill = 0, rest = 0, taxi = 0, steam = 0, total = 0  where id = {}".format(i)
            cursor.execute(st)
            conobj.commit()
        else:
            print("\n\n[ CANCELLATION EXIT . . . ] \n")
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
def PAYBILL():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\n                [ BILLING DESK ]")
        print("---------------------------------------------------------------------------------------")
        print("                     HOTEL  TAJ\n")
        print("Guest   ID            : ", d[0])
        print("Name                  : ", d[1])
        print("Address               : ", d[2])
        print("Mobile No.            : ", d[3])
        print("Booking Date          : ", d[4])
        print("Room Type             : ", d[5])
        print("Number of Rooms       : ", d[6])
        print("Number of Days        : ", d[7])
        print("Booking Amount        : ", d[8])
        print("---------------------------------------------------------------------------------------")
        r = int(input("Enter Restaurant Bill  : "))
        t = int(input("Enter Taxi Bill       : "))
        s = int(input("Enter Steam Bath Bill : "))
        g = d[8] + r + t + s
        st = "update guest set rest = {}, taxi = {}, steam = {}, total = {}  where id = {}".format(r, t, s, g, i)
        cursor.execute(st)
        conobj.commit()
        PRINTBILL(i)
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()
def PRINTBILL(i = -999):
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        if i == -999:
            i = int(input("Enter Guest ID : "))
        st = "select * from guest where id = {}".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\n     HOTEL  TAJ\n")
        print("BILL (GSTN : A93BJ783343)\n")
        print("---------------------------------------------------------------------------------------")
        print("Guest   ID         : ", d[0])
        print("Name               : ", d[1])
        print("Address            : ", d[2])
        print("Mobile No.         : ", d[3])
        print("Booking Date       : ", d[4])
        print("Room Type          : ", d[5])
        print("Number of Rooms    : ", d[6])
        print("Number of Days     : ", d[7])
        print("----------------------------------------------------")
        print("Room Charges       : ", d[8])
        print("Restaurant Bill     : ", d[9])
        print("Taxi Charges       : ", d[10])
        print("Steam Bath Charges : ", d[11])
        print("Total Amount       : ", d[12])
        print("----------------------------------------------------")
        print("      CGST (6%)    : ", d[12] * 0.6)
        print("      SGST (6%)    : ", d[12] * 0.6)
        print("      Grand Total  : ", d[12] + d[12] * 0.12)
    else:
        print("\n\nRecord Not Found For This Guest ID\n")
    conobj.close()  
    
def CHANGEPASSWORD():
    try:
        file = open('pass.txt', 'r')
    except FileNotFoundError:
        print("Your OTP is   123")
        n = input("Enter OTP : ")
        if n == '123':
            a = input("Enter New Password : ")
            b = input("Re-Enter New Password : ")
            if a == b:
                with open('pass.txt', 'w') as file2:
                    file2.write(a)
                    print("\n[ PASSWORD  RESET  SUCCESSFULLY ]")
        return
    try:
        n = input("Enter Old Password : ")
        data = file.read()
        if n == data:
            a = input("Enter New Password : ")
            b = input("Re-Enter New Password : ")
            if a == b:
                with open('temp.txt', 'w') as file2:
                    file2.write(a)
                    print("\n[ PASSWORD  RESET  SUCCESSFULLY ]")
                file.close()
                os.remove('pass.txt')
                os.rename('temp.txt','pass.txt')
    except EOFError :
        file.close()
def ADMIN():
    try:
        file = open('pass.txt', 'r')
    except FileNotFoundError:
        CHANGEPASSWORD()
    try:
        file = open('pass.txt', 'r')
        d = file.read()
        file.close()
        n = input("Enter Password : ")
        if n == d:
            ch = '1'
            while ch != '0':
                print("---------------------------------------------------------------------------------------")
                print("1.  FOR  INSTRUCTIONS")
                print("2.  ENTER  GUEST  DETAILS")
                print("3.  DISPLAY GUEST  DETAILS")
                print("4.  SEARCH  A  GUEST")
                print("5.  EDIT  GUEST  RECORDS")
                print("6.  DELETE  GUEST RECORDS")
                print("7.  BOOKING")
                print("8.  CANCELLATION")
                print("9.  PAY  BILL")
                print("10. PRINT BILL")
                print("11. CHANGE PASSWORD")
                print("0.  TO EXIT")
                ch = input("Enter your choice : ")
                print("---------------------------------------------------------------------------------------")
                if ch == '1' :
                    introduction()
                elif ch == '2':
                    ADDGUEST()
                elif ch == '3':
                    DISPLAYGUEST()
                elif ch == '4':
                    SEARCHGUEST()
                elif ch == '5':
                    EDITGUEST()
                elif ch == '6':
                    REMOVEGUEST()
                elif ch == '7':
                    BOOKING()
                elif ch == '8':
                    CANCELLATION()
                elif ch == '9':
                    PAYBILL()
                elif ch =='10':
                    PRINTBILL()
                elif ch == '11':
                    CHANGEPASSWORD()
                elif ch == '0':
                    break
                else:
                    print("Invalid Choice")
        else:
            print("[ ACCESS  DENIED ]")
    except EOFError :
        file.close()
conobj = ms.connect(host="localhost", user="root", passwd="pass")
cursor = conobj.cursor()
try:
    st = "create database hotel"
    cursor.execute(st)
    conobj.commit()
except ms.DatabaseError:
    conobj.close()
try:
    conobj = ms.connect(host="localhost", user="root", passwd="pass", database="hotel")
    cursor = conobj.cursor()
    st = "create table guest( id integer primary key, name varchar(100) not null, address varchar(200), mobile varchar(20), dob date, roomtype varchar(20) default '--', norooms integer default 0, nod integer default 0, bill integer default 0, rest integer default 0, taxi integer default 0, steam integer default 0, total integer default 0)"
    cursor.execute(st)
    conobj.commit()
    conobj.close()
except ms.ProgrammingError:
    conobj.close()
welcome()
ADMIN()

print("\n\n Thank You \n\n")
