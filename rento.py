import sqlite3
print('Welcome to E-Commerce Campaign')
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `products` (prod_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,ProdName TEXT, Category TEXT, SubCategory TEXT, Price INTEGER, CashBack INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `discounts` (Category TEXT, C_Discount INTEGER, SubCategory TEXT, S_Discount INTEGER)")
    #conn.commit
Database()
def user():
    e=input('search : ')
    cursor.execute("select * from `products` where ProdName = ?",(e,))
    r=cursor.fetchone()
    print('')
    print('Product ID : ',r[0])
    print('Product Name : ',r[1])
    print('Category : ',r[2])
    print('SubCategory : ',r[3])
    print('Product Price : ',r[4])
    print('Cashback on Purchase : ',r[5])
    
    cursor.execute("select C_Discount,S_Discount from `discounts` where Category = ? and SubCategory = ?",(r[2],r[3]))
    x=cursor.fetchone()
    print('Discount : ',x[0]+x[1],'%')
    print('1.Buy or 2.Search for another Product')
    i=int(input('select : '))
    if(i==1):
        print('pay with 1.CC(3% discount) 2.UPI(2% discount) 3.COD(no discount)')
        j=int(input('select : '))
        if(j==1):
            a=((x[0]+x[1]+3)*r[4])/100
        elif(j==2):
            a=((x[0]+x[1]+2)*r[4])/100
        else:
            a=((x[0]+x[1])*r[4])/100
        print('price : ',r[4])
        print('Cashback : ',r[5])
        print('Discount : ',a)
        print('Total Discount : ',a+r[5])
        print('Total Price : ',r[4]-a-r[5])
    else:
        user()
def updateDiscount():
    print('Category : 1.Electronics 2.Furniture 3.Home Appliances ')
    a=int(input('Select Category : '))
    if(a==1):
        pCategory = 'Electronics'
        print('Subcategory : Mobile Laptop Tv')
        subCtgry = input('Select(Type the word) : ')
    elif(a==2):
        pCategory = 'Furniture'
        print('Subcategory : Sofa  Tables  Chairs')
        subCtgry = input('Select(Type the word) : ')
    elif(a==3):
        pCategory = 'Home Appliances'
        print('Subcategory : Flowers  Kitchen  Cleaning')
        subCtgry = input('Select(Type the word) : ')
    cd=int(input('Category Discount : '))
    sd=int(input('SubCategory Discount : '))
    cursor.execute("select * from discounts where Category= ? and SubCategory= ?", (pCategory, subCtgry))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `discounts` (Category, C_Discount, SubCategory, S_Discount) VALUES(?, ?, ?, ?)", (pCategory, cd, subCtgry, sd))
        conn.commit()
    else:
        cursor.execute("update `discounts` set C_Discount= ?, S_Discount= ? where Category= ? and SubCategory= ?",(cd, sd, pCategory, subCtgry))
        conn.commit()



def campMangr():
    print('1.review product  2.Add product  3.Update Discounts 4.exit')
    y=int(input('select : '))
    if(y==1):
        print('review')
        e= input('search Product : ')
        cursor.execute("select * from `products` where ProdName = ?",(e,))
        r=cursor.fetchone()
        print('')
        print('Product ID : ',r[0])
        print('Product Name : ',r[1])
        print('Category : ',r[2])
        print('SubCategory : ',r[3])
        print('Product Price : ',r[4])
        print('Cashback on Purchase : ',r[5])
        print('')
        '''cursor.execute('select count(*) from products')
        r=cursor.fetchone()
        print(r)'''
        campMangr()
    elif(y==2):
        print('add')
        pName = input('Product Name :')
        cursor.execute("select * from `products` where ProdName = ?",(pName,))
        if cursor.fetchone() is not None:
            print('Product Already Exists')
            campMangr()
            return
        print('Category : 1.Electronics 2.Furniture 3.Home Appliances ')
        a=int(input('Select Category : '))
        if(a==1):
            pCategory = 'Electronics'
            print('Subcategory : Mobile Laptop Tv')
            subCtgry = input('Select(Type the word) : ')
        elif(a==2):
            pCategory = 'Furniture'
            print('Subcategory : Sofa  Tables  Chairs')
            subCtgry = input('Select(Type the word) : ')
        elif(a==3):
            pCategory = 'Home Appliances'
            print('Subcategory : Flowers  Kitchen  Cleaning')
            subCtgry = input('Select(Type the word) : ')
        price = int(input('Product Price : '))
        cashBack = int(input('Cash Back on Purchase : '))
        cursor.execute("INSERT INTO `products` (ProdName,Category, SubCategory, Price, CashBack) VALUES(?, ?, ?, ?, ?)", (pName, pCategory, subCtgry, price, cashBack))
        conn.commit()
        cd = 10
        sd = 5
        cursor.execute("select * from discounts where Category= ? and SubCategory= ?", (pCategory, subCtgry))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `discounts` (Category, C_Discount, SubCategory, S_Discount) VALUES(?, ?, ?, ?)", (pCategory, cd, subCtgry, sd))
            conn.commit()
        campMangr()
    elif(y==3):
        updateDiscount()
        campMangr()
    elif(y==4):
        return
    else:
        print('option not specified')
        campMangr()

def home():
    print('1.User 2.Campaign Manager 3.exit')
    x=int(input('select one of the options:'))
    if(x==1):
        user()
        home()
    elif(x==2):
        campMangr()
        home()
    elif(x==3):
        print('site closed')
        return
    else:
        print('option not specified')
        home()

home()
