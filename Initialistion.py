# TODO fix the initialisation script
try:
    with open("Flag.dat", "r") as a:
        data = a.read()
        if a == "1":
            import mysql.connector as sql

            myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@", database="Medical_store")
            cur = myql.cursor()
            cur.execute("create database if not exists Medical_Store")
            myql.commit()
            cur.execute("use Medical_store")
            cur.execute("""Create table if not exists Payroll
            (Uid int,
                Name char(20),
                D_O_J date,
                Salary int,
                Address char(30),
                Mobile_number int,
                E_mail char(30),
                ADMIN char(5),
                Password char(20)
             )""")
            myql.commit()
            cur.execute("""Create table if not exists Stocks
            (
               Mid int,
            Mname char(40),
            Saltname char(40),
            Brandname char(40),
            Quantity int,
            Price int,
            Location char(30),
            Exp_date date,
            D_O_P date  
            )""")
            myql.commit()
            cur.execute("""reate table if not exists Sales
            (
                S_id int,
                C_name char(40),
                Date_of_sale date,
                Total_price int,
                GST char(20),
                Discount int
            )""")
            myql.commit()


except FileNotFoundError:
    with open("Flag.dat", "w") as f:
        import mysql.connector as sql

        myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@")
        cur = myql.cursor()
        cur.execute("Create database if not exists Medical_store")
        myql.commit()
        cur.execute("Use Medical_store")
        cur.execute("""Create table if not exists Payroll
                        (Uid int,
                        Name char(20),
                        D_O_J date,
                        Salary int,
                        Address char(30),
                        Mobile_number int,
                        E_mail char(30),
                        ADMIN char(5),
                        Password char(20)
                        )""")
        myql.commit()
        cur.execute("""Create table if not exists Stocks
                        (
                       Mid int,
                        Mname char(40),
                        Saltname char(40),
                        Brandname char(40),
                        Quantity int,
                        Price int,
                        Location char(30),
                        Exp_date date,
                        D_O_P date  
                        )""")
        myql.commit()
        cur.execute("""create table if not exists Sales
                        (
                        S_id int,
                        C_name char(40),
                        Date_of_sale date,
                        Total_price int,
                        GST char(20),
                        Discount int
                        )""")
        myql.commit()
        cur.execute("insert into Payroll(Uid, ADMIN, Password) values(1, 'yes', 'pass')")
        myql.commit()
        print("Uid = 1, Password = pass")
        a = open("Default.txt", "w")
        data = "Uid = 1, Password = pass"
        a.write(data)
        a.close()
        # fixedTODO find the bug in the code when flag.dat exists
        a = open("Sales_id.txt", "w")
        a.write("0")
        a.close()
