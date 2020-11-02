import mysql.connector as sql
a = input("Enter the username for MYSQL : ")
b = input("Enter the password for MYSQL : ")
myql = sql.connect(host="localhost", user=a, password=b)
cur = myql.cursor()
cur.execute("create database if not exists medical_store")
myql.commit()
cur.execute("DROP TABLE IF EXISTS bill_detail")
myql.commit()
cur.execute("""create table bill_detail
                Bill_id int DEFAULT NULL,
                Cust_name char(100) DEFAULT NULL,
                bill_date date DEFAULT NULL,
                mid int DEFAULT NULL,
                GST_val int DEFAULT NULL,
                Dis int DEFAULT NULL,
                tp int DEFAULT NULL,
                Quantity int DEFAULT NULL""")
myql.commit()
cur.execute("DROP TABLE IF EXISTS payroll")
myql.commit()
cur.execute("""create table payroll
            Uid int DEFAULT NULL,
            Name char(30) DEFAULT NULL,
            D_O_J date DEFAULT NULL,
            Salary int DEFAULT NULL,
            Address char(40) DEFAULT NULL,
            Mobile_number int DEFAULT NULL,
            E_mail char(40) DEFAULT NULL,
            ADMIN char(5) DEFAULT NULL,
            Password char(40) DEFAULT NULL   
            """)
myql.commit()
cur.execute("insert into payroll values (5, 'ADMIN', '2020-09-01', 'jammu', 123,'admin','yes', '123')")
myql.commit()
cur.execute("insert into payroll values (6, 'noadmin','2020-09-01',123,'jam',123,'rak','no','123')")
myql.commit()
cur.execute("drop table if exists sales")
myql.commit()
cur.execute("""create table sales
            (sale_id int DEFAULT NULL,
            C_name char(10) DEFAULT NULL,
            tp int DEFAULT NULL,
            d_o_s date DEFAULT NULL
            """)
myql.commit()
cur.execute("drop table if exists stocks")
myql.commit()
cur.execute("""create table stocks
           Mid int DEFAULT NULL,
           Mname char(30) DEFAULT NULL,
           Saltname char(40) DEFAULT NULL,
           Brandname char(40) DEFAULT NULL,
           Quantity int DEFAULT NULL,
           price int DEFAULT NULL,
           Location char(20) DEFAULT NULL,
           Exp_date date DEFAULT NULL,
           D_O_M date DEFAULT NULL,
           GST int DEFAULT NULL,
          discount int DEFAULT NULL 
            """)
myql.commit()
cur.execute("""drop table if exists supplier""")
myql.commit()
cur.execute("")