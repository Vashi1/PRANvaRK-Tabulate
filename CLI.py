def authorisation(a, b):
    # FixedTODO Fix the bug regarding non-admin users in authorisation
    # flag is for ADMIN and chkr is for password
    import mysql.connector as sql
    flag = 0
    chkr = 0
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor(buffered=True)
    cur.execute("select Password from payroll where Uid = {}".format(a))
    data = cur.fetchone()
    if data is None:
        print("login not authorised! Please try again")
    elif data is not None:
        for c in data:
            data = c
        if data == b:
            ad = 0
            print("login authorised")
            chkr = 1
            cur.execute("select ADMIN from payroll where Uid = {0}".format(a))
            admin = cur.fetchone()
            for a in admin:
                ad = a
            if ad is None:
                flag = 0
            elif ad is not None:
                flag = 1
        elif data != b:
            print("The Password is incorrect")
    # FixedTODO remove debugging prints after this
    return flag, chkr


def list_user():
    import mysql.connector as sql
    from tabulate import tabulate
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="Medical_store")
    cur = myql.cursor()
    cur.execute("select Uid, Name from payroll")
    data = cur.fetchall()
    headers = ["Uid", "Name"]
    print(tabulate(data, headers, tablefmt="grid"))


def user_manage_main():
    while True:
        print("\t\t\t1.Add User")
        print("\t\t\t2.Edit User Information")
        print("\t\t\t3.Search User")
        print("\t\t\t4.Delete User")
        print("\t\t\t5.List All Users")
        print("\t\t\t6.Back to Main Menu")
        choi_usr = input("Enter your choice : ")
        if choi_usr == '1':
            add_usr()
        elif choi_usr == '2':
            editusr()
        elif choi_usr == '3':
            srch_usr()
        elif choi_usr == '4':
            del_usr()
        elif choi_usr == '6':
            break
        elif choi_usr == "5":
            list_user()
        else:
            print("Please input a valid input")


def add_usr():
    while True:
        import mysql.connector as sql
        myql = sql.connect(host='localhost', user='Rakshith', password='Rakshith1@', database="medical_store")
        print("Please input the following data!")
        f = open("uid.txt", "r+")
        data = int(f.read())
        #        uid = int(input("Enter the Uid : "))
        name = input("Enter the name : ")
        d_o_j = input("Enter the Date of joining : ")
        salary = int(input("Enter the salary : "))
        address = input("Enter the address : ")
        mobile_no = int(input("Enter the mobile number : "))
        email = input("Enter the email address:")
        adm_right = input("Do you want to grant user rights(leave blank if no) : ")
        pa_wd = input("Enter the password for the user : ")
        cur = myql.cursor()
        cur.execute(
            "insert into payroll values ({}, '{}', '{}', {}, '{}', {}, '{}','{}','{}')".format(data, name, d_o_j,
                                                                                               salary,
                                                                                               address, mobile_no,
                                                                                               email, adm_right, pa_wd))
        f.write(str(data+1))
        f.close()
        print(cur.rowcount, "User was added")
        myql.commit()
        cho1 = input("Do you wan to continue(y/n)")
        if cho1 == "y":
            pass
        elif cho1 == "n":
            myql.close()
            break
        else:
            print("Please enter a valid input")


def editusr():
    from tabulate import tabulate
    while True:
        print("Uid\tName\tD_O_J\tSalary\tAddress\tMobile_number\tE_mail\tADMIN\tPassword")
        clmn = input("Enter the column name : ")
        vlue = input("Enter the new value : ")
        uid = int(input("Enter the UID for the user : "))
        if clmn in ["Uid", "Salary", "Mobile_number"]:
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database='medical_store')
            cur = myql.cursor()
            cur.execute("update payroll set {0} = {1} where Uid = {2}".format(clmn, vlue, uid))
            print(cur.rowcount, "column was modified")
            myql.commit()
            cho2 = input("Do you want to continue(y/n) : ")
            if cho2 == 'y':
                pass
            elif cho2 == "n":
                myql.close()
                break
        elif clmn in ["Name", "D_O_J", "Address", "E_mail", "ADMIN", "Password"]:
            if clmn in ["Uid", "Salary", "Mobile_number"]:
                import mysql.connector as sql
                myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database='medical_store')
                cur = myql.cursor()
                cur.execute("update payroll set {0} = '{1}' where Uid = {2}".format(clmn, vlue, uid))
                print(cur.rowcount, "column was modified")
                myql.commit()
                cho2 = input("Do you want to continue(y/n) : ")
                if cho2 == 'y':
                    pass
                elif cho2 == "n":
                    myql.close()
                    break
            # fixedTODO fix the problem with edit module for different datatypes


def srch_usr():
    while True:
        print("\t\t\t1.Do you search by Uid")
        print("\t\t\t2.Search by Username")
        print("\t\t\t3.Back(User Management)")
        cho3 = int(input("\t\t\tEnter your input : "))
        if cho3 == 1:
            uid1 = int(input("Enter the userid you want to search : "))
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database='medical_store')
            cur = myql.cursor()
            cur.execute("select * from payroll where Uid = {0}".format(uid1))
            data = cur.fetchone()
            if data is None:
                print("The user does not exists")
            elif data is not None:
                print("The user exists")
                # The admi will tell whether the logged in user has admin rights
                cho4 = input("Do you want to view further details(y/n) : ")
                if cho4 == "y":
                    if admi == 1:
                        print("Uid", "Name", "D_O_J", "Salary", "Address", "Mobile_number", "E_mail", sep='\t\t')
                        print(
                            "-----------------------------------------------------------------------------------------")
                        uid = data[0]
                        name = data[1]
                        doj = data[2]
                        salary = data[3]
                        address = data[4]
                        mobile = data[5]
                        email = data[6]
                        print(uid, name, doj, salary, address, mobile, email, sep='\t\t')
                    elif admi == 0:
                        print("You need ADMIN Rights to view further details")
        elif cho3 == 3:
            break
        # fixedTODO fix the bug in search by mname and saltname
        elif cho3 == 2:
            uid2 = input("Enter the Username : ")
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database='medical_store')
            cur = myql.cursor()
            cur.execute("select * from payroll where Name = '{}'".format(uid2))
            data = cur.fetchone()
            if data is None:
                print("The user does not exists")
            elif data is not None:
                print("The user exists")
                # Again ask for the user for his choice
                cho5 = input("Do you want to view more details(y/n) : ")
                if cho5 == "y":
                    if admi == 1:
                        print("Uid", "Name", "D_O_J", "Salary", "Address", "Mobile_number", "E_mail", sep='\t\t')
                        print(
                            "-----------------------------------------------------------------------------------------")
                        uid = data[0]
                        name = data[1]
                        doj = data[2]
                        salary = data[3]
                        address = data[4]
                        mobile = data[5]
                        email = data[6]
                        print(uid, name, doj, salary, address, mobile, email, sep="\t\t")
                        # fixedTODO it shows address insted of mobile number
                        print(
                            '-----------------------------------------------------------------------------------------')
                    elif admi == 0:
                        print("You need ADMIN Rights to view further details")
                        print()


def del_usr():
    while True:
        uid = int(input("Enter the user_id to be deleted : "))
        import mysql.connector as sql
        myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database='medical_store')
        cur = myql.cursor()
        cur.execute("delete from payroll where Uid = {}".format(uid))
        myql.commit()
        print(cur.rowcount, "user was deleted")
        print("""\n
                         \n
                         \n""")
        chi = input("Do you want to continue(y/n) : ")
        if chi == "y":
            pass
        elif chi == "n":
            myql.close()
            break


def add_order():
    a = open("Sales_id.txt", "r+")
    f = int(a.read())
    from datetime import date
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    print("Enter the following data :-")
    sid = f + 1
    # fixedTODO to store sid in a text file
    c_name = input("Enter the customer name : ")
    # D_O_s = input("Enter the date : ")
    # gst = int(input("Enter the GST Percentage : "))
    # discount = int(input("Enter the discount per piece(if any) : "))
    while True:
        tp = 0
        gtp = 0
        """cur.execute("Select Mname, Quantity from stocks")
        data = cur.fetchall()
        print("Available Stock")
        print("Mname", "Quantity", sep="\t")"""
        # for i in data:
        # print(i)
        mid = input("Enter the Mid of the product : ")
        cur.execute("select Quantity from stocks where Mid = {}".format(mid))
        daa = cur.fetchall()
        cur.execute("select GST from stocks where Mid = {}".format(mid))
        daaa = cur.fetchall()
        gst = daaa[0][0]
        a = daa[0][0]
        cur.execute("select discount from stocks where Mid = {}".format(mid))
        daa1 = cur.fetchall()
        discount = daa1[0][0]
        print("Quantity available is ", a)
        quan = int(input("Enter the quantity : "))
        if quan <= a:
            cur.execute("update stocks set Quantity = Quantity - {} where Mid = {}".format(quan, mid))
            myql.commit()
            cur.execute("select Price from stocks where Mid = {}".format(mid))
            price = cur.fetchall()
            idprice = price[0][0] * quan
            # itemgst = idprice *
            tp = (idprice + ((gst * idprice) / 100))
            gtp = tp - ((discount * tp) / 100)
            ch = input("Do you want to continue(y/n)?")
            if ch == "y" or ch == "Y":
                cur.execute(
                    "insert into bill_detail values({}, '{}', '{}', {}, {}, {}, {}, {})".format(sid, d1, c_name, mid,
                                                                                                gst, discount, gtp,
                                                                                                quan))
                myql.commit()
                pass
            elif ch == "n" or ch == "N":
                # tp = tp - ((discount * tp) / 100)
                cur.execute(
                    "insert into bill_detail values({}, '{}', '{}', {}, {}, {}, {}, {})".format(sid, d1, c_name, mid,
                                                                                                gst, discount, gtp,
                                                                                                quan))
                myql.commit()
                cur.execute(
                    "insert into Sales values({}, '{}', '{}', {}, {}, {})".format(sid, c_name, d1, tp, gst, discount))
                f = open("Sales_id.txt", "w")
                f.write(str(sid))
                f.close()
                myql.commit()
                break

        else:
            print("Please check the stocks again!")
    #   #Tp = int(input("Enter the Total Price"))


# TODO add order recieve order

def sales_manage_main():
    while True:
        print("1.Generate e-Bill")
        print("2.View all bills")
        print("3.Search bills")
        print("4.Back(Main Menu)")
        ch = input("Enter your choice : ")
        if ch == "1":
            add_order()
        elif ch == "2":
            view_order()
        elif ch == "3":
            search_order()
        elif ch == "4":
            break
        else:
            print("Please enter a valid input")


def view_order():
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute("Select bill_id, Cust_name, bill_date, mid, GST_val, DIS, tp, Quantity  from bill_detail")
    data = cur.fetchall()
    if data is None or data == []:
        print("No orders exist")
    elif data is not None:
        headers = ["Bill_id", "C_name", "dataofsale", "mid" ,"GST", "Discount", "Price", "Quantity"]
        print("Bill_id", "C_name", "dateofsale", "mid", "GST", 'Discount', "Price", "Quantity", sep="\t\t")
        print("-----------------------------------------------------------------------------------------")
        for i in data:
            print(i[0], i[1] + "  ", i[2], i[3], i[4], i[5], "   ", i[6], i[7], sep="\t\t")
            print('-----------------------------------------------------------------------------------------')


def search_order():
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    print("1.Search by bill_id")
    print("2.Search by C_name")
    ch = input("Enter your choice : ")
    if ch == "1":
        sid = int(input("Enter the bill_id : "))
        cur.execute(
            "select bill_id, Cust_name, bill_date, mid, GST_val, DIS, Quantity from bill_detail where bill_id = {}".format(
                sid))
        data = cur.fetchall()
        if data is None or data == []:
            print("The Order does not exists")
        elif data is not None:
            print("bill_id", "C_name", "dateofsale", "mid", "GST", 'Discount', "Quantity", sep="\t\t\t")
            print(
                "---------------------------------------------------------------------------------------------------------")
            for i in data:
                print(i[0], ' ', i[1] + "  ", i[2], ' ', i[3], ' ', i[4], ' ', i[5], "   ", i[6], sep="\t\t")
                print(
                    '---------------------------------------------------------------------------------------------------------')
            cur.execute(
                "select sum(tp) as 'Total price' from bill_detail group by bill_id having bill_id = {}".format(sid))
            a = cur.fetchall()
            print("\n")
            print("Total Price")
            print("-----------")
            print(a[0][0])
            print("-----------")
            print("\n")
    elif ch == "2":
        cname = input("Enter the C_name : ")
        cur.execute(
            "select bill_id, Cust_name, bill_date, mid, GST_val, DIS, Quantity from bill_detail where Cust_name = '{}'".format(
                cname))
        data = cur.fetchall()
        if data is None or data == []:
            print("The order does not exists")
        else:
            print("bill_id", "C_name", "dateofsale", "mid", "GST", 'Discount', "Quantity", sep="\t\t\t")
            print(
                "---------------------------------------------------------------------------------------------------------")
            for i in data:
                print(i[0], ' ', i[1] + "  ", i[2], ' ', i[3], ' ', i[4], ' ', i[5], "   ", i[6], sep="\t\t")
                print(
                    '---------------------------------------------------------------------------------------------------------')
            cur.execute(
                "select sum(tp) as 'Total price' from bill_detail group by Cust_name having Cust_name = '{}'".format(
                    cname))
            a = cur.fetchall()
            print("\n")
            print("Total Price")
            print("-----------")
            print(a[0][0])
            print("-----------")
            print("\n")


# Not working
def add_sup_order():
    while True:
        from datetime import date
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        print("Enter the following data!")
        # midi = int(input("Enter the Mid : "))
        f = open("Supply.txt", "r+")
        data = int(f.read())
        f.close()
        supid = input("Enter the supplier id: ")
        mid = input("Enter the Mid : ")
        import mysql.connector as sql
        myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
        cur = myql.cursor()
        cur.execute("select * from stocks where Mid = {}".format(mid))
        data_db = cur.fetchall()
        if data_db is None or data_db == []:
            mname = input("Enter the Mname : ")
            salt_nme = input("Enter the salt name : ")
            b_name = input("Enter the Brand name : ")
            quan = int(input("Enter the quantity : "))
            price = int(input("Enter the cost : "))
            # location = input("Enter the storage location : ")
            # TODO add the location as "Not specified" in the query
            location = "Not specified"
            expdate = input("Enter the expiry data : ")
            dod = input("Enter the Date_of_Delievery : ")
            GST = input("Enter the GST value : ")
            stat = 0
            discount = 0
            # TODO add the discount as 0 
            # supid = input("Enter the supplier id : ")
            # supname = input("Enter the supplier name : ")
            # sup_gst = input("Enter supplier's GST number")
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute(
                "insert into supplier_data values({},'{}',{},{},{},{},'{}','{}', '{}', '{}', '{}', '{}', {}, {}, {})".format(
                    data, d1, supid, mid, quan, price, dod, mname, salt_nme, b_name, location, expdate, GST, discount,
                    stat))
            myql.commit()
        elif data_db is not None or data_db != []:
            print("The data is shown below :-")
            print("Mid", "Mname", 'Sname', "Bname", "Existing quantity", "price", "location", "EXP_data",
                  'date of manufacturing',
                  sep='\t\t')
            for i in range(0, cur.rowcount):
                mname = data_db[i][1]
                sname = data_db[i][2]
                bname = data_db[i][3]
                quan = data_db[i][4]
                price = data_db[i][5]
                location = data_db[i][6]
                expdata = data_db[i][7]
                D_O_M = data_db[i][8]
                gst = data_db[i][9]
                discount = data_db[i][10]
                stat = 1
                # fixedTODO add the field name
                print(
                    "------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(mid, mname, sname, bname, quan, price, location, expdata, D_O_M, sep="\t\t")
            ch = int(input("Enter the quantity to be ordered : "))
            dod = input("Enter the date of delivery : ")
            cur.execute(
                "insert into supplier_data values({},'{}',{},{},{},{},'{}','{}', '{}', '{}', '{}', '{}', {}, {}, {})".format(
                    data, d1, supid, mid, ch, price, dod, mname, sname, bname, location, expdata, D_O_M, gst, discount,
                    stat))
            myql.commit()
        print(cur.rowcount, "Order was added")
        myql.commit()
        f = open("Supply.txt", "w+")
        data = data + 1
        f.write(str(data))
        f.close()
        ch = input("Do you want to continue(y/n) : ")
        if ch == "y":
            pass
        elif ch == "n":
            break
        else:
            print("Please enter a valid input!")


def recieve_sup_order():
    oid = int(input("Enter the order_id : "))
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute(
        "select orderid, order_date, supplier_id, Mid, Quantity, Price, Delievery_date from supplier_data where orderid = {}".format(
            oid))
    data = cur.fetchall()
    if data == None or data == []:
        print("The Table is empty")
    else:
        print("The data is shown below :-")
        print("orderid", "order_date", 'supplier_id', "Mid", "Quantity", "Price", "Delievery_date", sep='\t\t')
        for i in range(0, cur.rowcount):
            oid = data[i][0]
            odate = data[i][1]
            supid = data[i][2]
            mid = data[i][3]
            quan = data[i][4]
            price = data[i][5]
            Delievery_date = data[i][6]
            # fixedTODO add the field name
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(oid, odate, supid, mid, quan, price, Delievery_date, sep="\t\t")
        ch = input("Do you want to continue(y/n) : ")
        if ch == "y":
            cur.execute("select status from supplier_data where mid = {}".format(mid))
            data = cur.fetchall()
            if data[0][0] == 1:
                cur.execute('select Mid, Quantity from supplier_data')
                data_sup_data = cur.fetchall()
                for i in range(0, cur.rowcount):
                    mid = data_sup_data[i][0]
                    quan = data_sup_data[i][1]
                    cur.execute("update stocks set Quantity = Quantity + {} where Mid = {}".format(quan, mid))
                    myql.commit()
                    cur.execute("update supplier_data set status = 2 where mid = {}".format(mid))
                    myql.commit()
            elif data[0][0] == 0:
                cur.execute(
                    'select Mid, Mname, Saltname, Brandname, Quantity, Price, Location, Exp_date, order_date, GST, discount from supplier_data')
                data_sup_data = cur.fetchall()
                f = open("Mid.txt", "r")
                daa = int(f.read())
                print(daa, type(daa))
                f.close()
                for i in range(0, cur.rowcount):
                    mname = data_sup_data[i][1]
                    s_nme = data_sup_data[i][2]
                    bname = data_sup_data[i][3]
                    quant = data_sup_data[i][4]
                    pric = data_sup_data[i][5]
                    loca = data_sup_data[i][6]
                    expdata = data_sup_data[i][7]
                    order_da = data_sup_data[i][8]
                    gst = data_sup_data[i][9]
                    disco = data_sup_data[i][10]
                    print(disco)
                    cur.execute(
                        "insert into stocks values({}, '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', {}, {})".format(daa,
                                                                                                                   mname,
                                                                                                                   s_nme,
                                                                                                                   bname,
                                                                                                                   quant,
                                                                                                                   pric,
                                                                                                                   loca,
                                                                                                                   expdata,
                                                                                                                   order_da,
                                                                                                                   gst,
                                                                                                                   disco))
                    myql.commit()
                    print("cur.rowcount")
                    cur.execute("update supplier_data set status = 2 where mid = {}".format(daa))
                    myql.commit()
                f = open("Mid.txt", "w")
                daa += 1
                f.write(str(daa))
                f.close()
            elif data[0][0] == 2:
                print("The order is already added")
        if ch == "n":
            pass


def list_product():
    import mysql.connector as sql
    from tabulate import tabulate
    myql = sql.connect(host="localhost", user='Rakshith', password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute("select * from stocks")
    data = cur.fetchall()
    if data == ('None',):
        print("The Table is empty")
    else:
        print("The data is shown below :-")
        headers = ["Mid", "Mname", "Sname", "Bname", "quantity", "price", 'location', "EXP_data", 'date of manufacturing', "GST", "discount"]
        print(tabulate(data, headers, tablefmt="grid"))

        """for i in range(0, cur.rowcount):
            mid = data[i][0]
            mname = data[i][1]
            sname = data[i][2]
            bname = data[i][3]
            quan = data[i][4]
            price = data[i][5]
            location = data[i][6]
            expdata = data[i][7]
            D_O_M = data[i][8]
            # fixedTODO add the field name
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(mid, mname, sname, bname, quan, price, location, expdata, D_O_M, sep="\t\t")"""


def edit_product():
    while True:
        mid = input("Enter the Mid of the Product : ")
        print("Mid Mname Saltname Brandname Quantity Price Location Exp_date D_O_P GST discount")
        fname = input("Enter the field name : ")
        val = input("Enter the new value : ")
        char_fields = ['Saltname', 'Brandname', 'Location', "Exp_date"]
        if fname in char_fields:
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("update stocks set {0} = '{1}' where Mid = {2}".format(fname, val, mid))
            myql.commit()
            print(cur.rowcount, "user is modified.")

        elif fname == "Mname":
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("update stocks set {0} = '{1}' where Mid = {2}".format(fname, val, mid))
            myql.commit()
            print(cur.rowcount, "user is modified.")
        elif fname == "Quantity":
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor(buffered=True)
            cur.execute("update stocks set Quantity={0} where Mid={1}".format(val, mid))
            myql.commit()

        elif fname not in char_fields:
            import mysql.connector as sql
            myql = sql.connect(host="localhost  ", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("update stocks set {0} = {1} where Mid = {2}".format(fname, val, mid))
            myql.commit()
            print(cur.rowcount, "product is modified.")
        else:
            print("Please enter a valid input!")
        ch = input("Do you want to continue(y/n) : ")
        if ch == "y":
            pass
        elif ch == "n":
            break
        else:
            print("Please enter a valid input!")


def search_product():
    while True:
        print("\t\t\tDo you want to search by:-")
        print("\t\t\t1.Search by Mid")
        print("\t\t\t2.Search by Mname")
        print("\t\t\t3.Seach by Salt_name")
        print("\t\t\t4.Back(Main Menu)")
        ch = input("Enter your choice : ")
        if ch == "1":
            while True:
                inp = int(input("Enter the Mid :"))
                import mysql.connector as sql
                myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
                cur = myql.cursor()
                cur.execute("select * from stocks where Mid = {}".format(inp))
                data = cur.fetchone()
                # ad = 0
                # for i in data:
                #    ad = i
                if data == [] or data is None:
                    print("The product is not available in inventory")
                    break
                elif ad != 0:
                    print("The product is available in the inventory")
                    ch1 = input("Do you want to view more information(y/n) : ")
                    if ch1 == "y":
                        print("Mid", "Mname", "Saltname", "Brandname", "Quantity", "Price", "Location", "Exp_date",
                              "D_O_M", sep="\t\t\t")
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------")
                        mid = data[0]
                        mname = data[1]
                        saltname = data[2]
                        brandname = data[3]
                        quantity = data[4]
                        price = data[5]
                        location = data[6]
                        expdate = data[7]
                        dom = data[8]
                        print(mid, mname, saltname, brandname, quantity, price, location, expdate, dom, sep="\t\t\t")
                        break
                    if ch1 == "n":
                        break
                    else:
                        print("Please enter a valid input!")
        elif ch == '2':
            while True:
                mname = input("Enter the M_name : ")
                import mysql.connector as sql
                myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
                cur = myql.cursor()
                cur.execute("select * from stocks where Mname = '{}'".format(mname))
                data = cur.fetchall()
                # ad = 0
                # for i in data:
                #   ad = i
                if data is None or data == []:
                    print("The product is not available in inventory")
                    break
                elif data is not None:
                    print("The product is available in the inventory")
                    ch1 = input("Do you want to view more information(y/n) : ")
                    if ch1 == "y":
                        print("Mid", "Mname", "Saltname", "Brandname", "Quantity", "Price", "Location", "Exp_date",
                              "D_O_M", sep="\t\t\t")
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------")
                        """mid = data[0]
                        mname = data[1]
                        saltname = data[2]
                        brandname = data[3]
                        quantity = data[4]
                        price = data[5]
                        location = data[6]
                        expdate = data[7]
                        dom = data[8]
                        print(mid, mname, saltname, brandname, quantity, price, location, expdate, dom, sep="\t\t\t")"""
                        for i in data[0]:
                            print(i, end="\t\t\t")
                        break
                    if ch1 == "n":
                        break
                    else:
                        print("Please enter a valid input!")
        elif ch == "3":
            while True:
                msalt = input("Enter the salt name : ")
                import mysql.connector as sql
                myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
                cur = myql.cursor()
                cur.execute("select * from stocks where Saltname = '{}'".format(msalt))
                data = cur.fetchall()
                ad = 0
                for i in data:
                    ad = i
                if ad == 0:
                    print("The product is not available in inventory")
                    break
                elif ad != 0:
                    print("The product is available in the inventory")
                    ch1 = input("Do you want to view more information(y/n) : ")
                    if ch1 == "y":
                        print("Mid", "Mname", "Saltname", "Brandname", "Quantity", "Price", "Location", "Exp_date",
                              "D_O_M", sep="\t\t\t")
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------")
                        '''mid = data[0]
                        mname = data[1]
                        saltname = data[2]
                        brandname = data[3]
                        quantity = data[4]
                        price = data[5]
                        location = data[6]
                        expdate = data[7]
                        dom = data[8]
                        print(mid, mname, saltname, brandname, quantity, price, location, expdate, dom, sep="\t\t\t")'''
                        for i in data[0]:
                            print(i, end="\t\t\t")
                        break
                    if ch1 == "n":
                        break
                    else:
                        print("Please enter a valid input!")
        elif ch == "4":
            break
        else:
            print("Please enter a valid input!")


def del_product():
    print("\t\t\t1.Delete by Mname")
    print("\t\t\t2.Delete by Mid")
    ch = input("Enter your choice : ")
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    if ch == "1":
        mname = input("Enter the Mname : ")
        cur.execute("delete from stocks where Mname = '{0}'".format(mname))
        print(cur.rowcount, "item was deleted")
        myql.commit()
    elif ch == "2":
        mid = input("Enter the Mid : ")
        cur.execute("delete from stocks where Mid  = '{0}'".format(mid))
        print(cur.rowcount, "item was deleted")
        myql.commit()


def exp_product():
    import mysql.connector as sql
    from tabulate import tabulate
    # fixedTODO add for blank
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute("select * from stocks where Exp_date < curdate()")
    data = cur.fetchall()
    if data is None or data == []:
        print("No expired product exists")
    else:
        print("The details of expired products if given below : ")
        headers = ["Mid", "Mname", "Saltname", "Brandname", "Quantity", "Price", "Location", "Exp_date", "D_O_M"]
        print(tabulate(data, headers, tablefmt="grid"))
#        print("Mid", "Mname", "Saltname", "Brandname", "Quantity", "Price", "Location", "Exp_date", "D_O_M", sep="\t\t")
        for i in range(0, cur.rowcount):
            mid = data[i][0]
            mname = data[i][1]
            saltname = data[i][2]
            brandname = data[i][3]
            quantity = data[i][4]
            price = data[i][5]
            location = data[i][6]
            expdate = data[i][7]
            dom = data[i][8]
            print(
                "------------------------------------------------------------------------------------------------------------------------------------")
            print(mid, mname, saltname, brandname, quantity, price, location, expdate, dom, sep="\t\t\t")


# TODO fix the whole stock management module
def stock_manage_main():
    while True:
        print("\t\t\t1.Add Supply Order")
        print("\t\t\t2.List Products")
        print("\t\t\t3.Modify Product")
        print("\t\t\t4.Search Product")
        print("\t\t\t5.Delete Product ")
        # fixedTODO add a module to show all expired products
        print("\t\t\t6.Show Expired Products")
        print("\t\t\t7.Receive Supply Order")
        print("\t\t\t8.Back(Main Menu)")
        ch1 = input("\t\tEnter your choice : ")
        if ch1 == "1":
            # Doesn't Work anymore
            add_sup_order()
        elif ch1 == "2":
            list_product()
        elif ch1 == "3":
            edit_product()
        elif ch1 == "4":
            search_product()
        elif ch1 == "5":
            del_product()
        elif ch1 == "6":
            exp_product()
        elif ch1 == "8":
            break
        # Doesn't exist anymore
        elif ch1 == "7":
            recieve_sup_order()
        else:
            print("Please enter a valid input!")


def list_table():
    from tabulate import tabulate
    import mysql.connector as sql
    myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute("show tables")
    data = cur.fetchall()
    headers = ["Tables"]
    print(tabulate(data, headers, tablefmt="grid"))


def database_manage_main():
    while True:
        print("\t\t\t1.List Tables")
        print("\t\t\t2.Back(Main Menu)")
        cho = input("Enter your choice : ")
        if cho == "1":
            list_table()
        elif cho == "2":
            break
        else:
            print("Please enter a valid input!")


def user_manage_mini():
    while True:
        print("\t\t\t1.Search User")
        # fixedTODO Fix the edit user information and all other modules
        # fixedTODO FIX search User
        print("\t\t\t2.Back To Main Menu")
        cho_usr = input("Enter your choice :")
        if cho_usr == "1":
            srch_usr()
        elif cho_usr == "2":
            break
        else:
            print("Please enter a valid input")


def add_supplier():
    while True:
        print("Enter the following data!")
        f = open("Supplier.txt", "r+")
        data = int(f.read())
        f.close()
        #        sup_id = int(input("Enter the Supplier_id")
        sup_nme = input("Enter the supplier name : ")
        p_no = int(input("Enter the phone number : "))
        address = input("Enter the address : ")
        gst = input("Enter the Supplier GST number : ")
        import mysql.connector as sql
        myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
        cur = myql.cursor()
        cur.execute(
            "insert into supplier values({}, '{}', '{}', '{}', '{}')".format(data, sup_nme, p_no, address, gst))
        myql.commit()
        f = open("Supplier.txt", "w")
        data = data + 1
        f.write(str(data))
        f.close()
        ch = input("Do you want to continue(y/n)? : ")
        if ch == "y":
            pass
        elif ch == "n":
            break


def delete_supplier():
    print("1.Delete by supplier_id")
    print("2.Delete by Supplier_name")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        sid = int(input("Enter the supplier_id : "))
        import mysql.connector as sql
        myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
        cur = myql.cursor()
        cur.execute("delete from Supplier where supplier_id = {}".format(sid))
        myql.commit()
        print(cur.rowcount, "supplier was deleted")
    if ch == 2:
        supname = input("Enter the supplier_name : ")
        import mysql.connector as sql
        myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
        cur = myql.cursor()
        cur.execute("delete from Supplier where supplier_name ='{}'".format(supname))
        myql.commit()
        print(cur.rowcount, "supplier was deleted")


def list_supplier():
    from tabulate import tabulate
    headers = ["supplier_id", "supplier_name", "phone_number", "address", "supplier_gst"]
#    print('supplier_id', 'supplier_name', 'phone_number', 'address', 'supplier_gst', sep="\t\t")
#    print('-------------------------------------------------------------------------------------')
    import mysql.connector as sql
    myql = sql.connect(host='localhost', user="Rakshith", password="Rakshith1@", database="medical_store")
    cur = myql.cursor()
    cur.execute("Select * from supplier")
    data = cur.fetchall()
    if data is None or data == []:
        print("No record exists")
    else:
        print(tabulate(data, headers, tablefmt="grid"))
    """for i in range(0, cur.rowcount):
        supid = data[i][0]
        supname = data[i][1]
        phno = data[i][2]
        address = data[i][3]
        supgst = data[i][4]
        print(supid, supname, phno, address, supgst, sep="\t\t\t     ")
        print('-------------------------------------------------------------------------------------')
    """

def search_supplier():
    while True:
        print("1.Search by supplier_id")
        print("2.Search by supplier_name")
        print("3.Back(Main Menu)")
        ch = input("Enter your choice : ")
        if ch == "1":
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            sup_id = int(input("Enter the supplier_id : "))
            cur.execute("select * from supplier where supplier_id = {}".format(sup_id))
            data = cur.fetchall()
            if data is None or data == []:
                print("No such supplier exists")
            elif data is not None or data != []:
                print("The supplier exists!")
                print('supplier_id', 'supplier_name', 'phone_number', 'address', 'supplier_gst', sep="\t\t")
                print('-------------------------------------------------------------------------------------')
                print(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], sep="\t\t\t\t  ")
        elif ch == "2":
            sup_name = input("Enter the supplier_name : ")
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("select * from supplier where supplier_name = '{}'".format(sup_name))
            data = cur.fetchall()
            if data is None or data == []:
                print("No such supplier exists")
            elif data is not None or data != []:
                print('supplier_id', 'supplier_name', 'phone_number', 'address', 'supplier_gst', sep="\t\t")
                print('-------------------------------------------------------------------------------------')
                print(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], sep="\t\t\t\t  ")
        elif ch == '3':
            break
        else:
            print("Please enter a valid input")


def edit_supplier():
    while True:
        print('supplier_id supplier_name phone_number address supplier_gst')
        field = input("Enter the field_name : ")
        supid = input("Enter the Supplier_id : ")
        if field in ['phone_number']:
            value = input("Enter the new value : ")
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("update supplier set {} = {} where supplier_id = {}".format(field, value, supid))
            myql.commit()
            print(cur.rowcount, "supplier was modified")
        elif field in ['supplier_id']:
            print("You cannot change the supplier_id")
        elif field in ['supplier_name', 'address', 'supplier_gst']:
            value = input("Enter the new value : ")
            import mysql.connector as sql
            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="medical_store")
            cur = myql.cursor()
            cur.execute("update supplier set {} = '{}' where supplier_id = {}".format(field, value, supid))
            myql.commit()
            print(cur.rowcount, "supplier was modified")
        ch = input("Do you want to continue(y/n)")
        if ch == 'y':
            pass
        elif ch == "n":
            break
        else:
            print("Please enter a valid input")


def supplier_management():
    while True:
        print("\t\t\t1.Search Supplier")
        print("\t\t\t2.Add Supplier")
        print("\t\t\t3.List all Supplier")
        print("\t\t\t4.Modify Supplier")
        print("\t\t\t5.Remove Supplier")
        print("\t\t\t6.Back(Main Menu)")
        cho_sup = input("Enter your choice: ")
        if cho_sup == "1":
            search_supplier()
        elif cho_sup == "2":
            add_supplier()
        elif cho_sup == "3":
            list_supplier()
        elif cho_sup == "4":
            edit_supplier()
        elif cho_sup == "5":
            delete_supplier()
        elif cho_sup == "6":
            break
        else:
            print("Please enter a valid input")


def stock_manage_mini():
    while True:
        # FixedTODO Exp_product and list products
        print("Main True")
        print("\t\t\t1.Search Product")
        print("\t\t\t2.View all expired products")
        print("\t\t\t3.List all products")
        print("\t\t\t4.Back(Main Menu)")
        cho_stk = input("Enter your choice: ")
        if cho_stk == "1":
            search_product()
        elif cho_stk == "2":
            exp_product()
        elif cho_stk == "3":
            list_product()
        elif cho_stk == "4":
            break
        else:
            print("Please enter a valid input")


user = int(input("Enter the Userid : "))
pass_chk = input("Enter the password : ")
admi, chk = authorisation(user, pass_chk)
if admi == 1 and chk == 1:
    while True:
        print("Main Menu")
        print("\t\t\t1.User Management")
        print("\t\t\t2.Bill Creation")
        print("\t\t\t3.Stock Management")
        print("\t\t\t4.Database Management")
        print("\t\t\t5.Supplier Management")
        print("\t\t\t6.Quit")
        cho_ini = input("Enter your choice : ")
        if cho_ini == '1':
            user_manage_main()
        elif cho_ini == '2':
            sales_manage_main()
        elif cho_ini == '3':
            stock_manage_main()
        elif cho_ini == "4":
            database_manage_main()
        elif cho_ini == "5":
            supplier_management()
        elif cho_ini == "6":
            print("Good Bye!")
            break

elif admi == 0 and chk == 1:
    while True:
        print("Main Menu")
        print("\t\t\t1.User Management")
        print("\t\t\t2.Stock Management")
        print("\t\t\t3.Quit")
        cho_ini = input("Enter your choice: ")
        if cho_ini == '1':
            user_manage_mini()
        elif cho_ini == '2':
            stock_manage_mini()
        elif cho_ini == "3":
            print("Bye")
            break
