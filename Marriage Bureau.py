CREATING  TABLES
 
import mysql.connector as sql
conn= sql.connect(host='localhost', user = 'root', password ='manager')
c1=conn.cursor()
c1.execute('create database marriage_bureaw_management')
 
c1.execute('create table legends_details(name varchar (200),address varchar(20),nationality varchar (100),appearence varchar(100),age bigint(55),profession varchar (255),phone_no  bigint(200)')
c1.execute('create girls_details(name varchar(100),address varchar(100),nationality varchar(50),appearence varchar(25),age int(4),profession varchar(65),phone_no varchar(15)')
c1.execute('create table user_id(user_name varchar(55),password varchar(55)')
conn.commit()

MAIN CODE
import  mysql . connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='marriage_bureaw_management')
cur = conn.cursor()
 
print('*****************************************************MARRIAGE   BUREAW MANAGEMENT**************************************************')
print('1.REGISTER')
print('2.LOGIN')
n=int(input('Enter your choice:'))
if n== 1:
    name=input('Enter your  User name:')
    passwd=int(input('Enter  your  Password(only numbers):'))
    print()
    V_SQLInsert="INSERT  INTO user_id (password,user_name) values (" +  str (passwd) + ",' " + name + " ') "
    cur.execute(V_SQLInsert)
    conn.commit()
    print()
    print('USER created succesfully')
 
if  n==2 :
    name=input('Enter your Username=')
    print()
    passwd=int(input('Enter your  Password='))
    V_Sql_Sel="select * from user_id where password='"+str (passwd)+"' and user_name=  ' " +name+ " ' "
    cur.execute(V_Sql_Sel)
    if cur.fetchone() is  None:
         print()
         print('Invalid username or password')
    else:
         print()
         import py
         c1=conn.cursor()
          print('________________________________________________________________WELCOME   TO  BSF  MARTIMONIAL  SERVICE              _______________________________________________________')
           c='y'
            while c.lower()=='y':
            print('=======================')
            print("1.provide details")
            print('2. in search of bridegroom')
         choice=int(input('enter the choice:'))
         if choice==1:
             print('==========================')
             print('5.Male customer details')
             print('6.Female customer details')
             choice=int(input('enter the choice:-'))
         if choice==2:
              print('========================')
              print('3. Handsome Bride ')
              print('4. Beautiful Groom ')
              choice=int(input('enter the choice-'))
         if choice == 5 :
              a=(input('enter the name:'))
              b=(input('enter the address:'))
              c=(input('enter the nationality:'))
              d=(input('enter the Appearence:'))
              e=(input('enter the age:'))
              f=(input('enter the profession:'))
              g=(input('enter the phone_no:'))
              c1=conn.cursor()
              sql_insert="insert into legends_details values( '{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
              c1.execute(sql_insert)
              conn.commit()
              print ('Data inserted')
              c=input('do you want to continue (y/[n]:)')
             
                   
         if choice==6:
              h=(input('enter the name:'))
              i=(input('enter the address:'))
              j=(input('enter the nationality:'))
              k=(input('enter the Appearence:'))
              l=(input('enter the age:'))
              m=(input('enter the profession:'))
              n=(input('enter the phone_no:'))
              c1=conn.cursor()
              sql_insert="insert into girls_details values( '{}','{}','{}','{}','{}','{}','{}')".format(h,i,j,k,l,m,n)
              c1.execute(sql_insert)
              conn.commit()
              print("Details are successfully inserted")
              c=input('do you want to continue (y/[n]:)')
              if c =='y' :
                      continue
              else:
                        print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                        print('VISIT  AGAIN')
         if choice==3:
              prof=(input('Enter the profession:'))
              c1.execute("select* from legends_details where profession='{}'". format(prof))
              data= c1.fetchall()
              print("name\t\t address\t\t nationality\t\t  Appearence\t\t  age\t\t  profession\t\t phone_no \t\t ")
              for i in data:
                 print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
                 c=input('do you want to continue (y/[n]:)')
                 if c =='y' :
                      continue
                 else:
                        print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                        print('VISIT  AGAIN')
              print('=========================')
         if choice==4:
              pro=(input('Enter the profession:'))
              c1.execute("select* from girls_details where profession='{}'". format(pro))
              data= c1.fetchall()
              print("name\t\t address\t\t nationality\t\t  Appearence\t\t  age\t\t  profession\t\t phone_no \t\t ")
              for i in data:
                 print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
                 c=input('do you want to continue (y/[n]:)')
                 if c =='y' :
                      continue
                 else:
                        print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                        print('VISIT  AGAIN')
