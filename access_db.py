import sqlite3 as sql
# products tablosu bağlantısı
con = sql.connect("main.db")
# sales tablosu bağlantısı
salescon = sql.connect("sales.db")
# cost tablosu bağlantısı
purccon = sql.connect("cost.db")
db = con.cursor()
dbsales = salescon.cursor()
dbpurc = purccon.cursor()
def newProductTotheDb():
   print(("Please enter to product information;"))
   name = input("What's new product name?")
   cost = input("How much does your product cost?")
   sale = input("How much does your product sale?")
   db.execute(
       "INSERT INTO products (name,cost,sale)  VALUES ('{}', {},'{}')".format(name,cost,sale))
   print("New product is created successfully! Thank you!")
   con.commit()
   getProducts()
def newSalesTotheDb():
    print("Did you make a new sale? Search for product name")
    getProducts()
    name = input("Search Product Name : ")
    db.execute(f"SELECT * FROM products WHERE name='{name}'")
    rows = db.fetchall()
    if len(rows)==0:
        print("Error: The product does not exist!")
    else:
        row = rows[0]
        productName = row[0]
        cost = row[1]
        sale = row[2]
        profit = int(sale)
        count = input("How many were sold? ")
        print(f"Total sale price is {int(count) * profit}TL ")
        print(f"Do you confirm the sale of {count} {productName}? ")
        confirm = input("If you are accept this sales press 1 opposite press 0 : ")
        if (confirm == "1"):
            dbsales.execute(
                "INSERT INTO sales (productName,price,count)  VALUES ('{}', {}, {})".format(productName, profit,                                                                                  count))
            print("New sales is created successfully! Thank you!")
            salescon.commit()
            getSalesList()


def getCostList():
    dbpurc.execute(f"SELECT * FROM cost")
    rows = dbpurc.fetchall()
    if len(rows) == 0:
        print("Error:4 You don't have any costs!")
        return 0
    else:
        print(f"You have {len(rows)} costs!")
        totalCount = 0
        totalPrice = 0
        for x in rows:
            totalPrice +=x[2] * x[1]
            totalCount +=x[2]
            print(f"You have cost {x[2]} items of {x[0]} product. Total cost is {x[1] * x[2]} TL")
        print(f"A total of {totalCount} items were cost. Total money is {totalPrice} TL")
        return totalPrice
def getCostSingleList(product):
    dbpurc.execute(f"SELECT * FROM cost WHERE productName='{product}'")
    rows = dbpurc.fetchall()
    if len(rows) == 0:
        print("Error:4 You don't have any costs!")
        return 0
    else:
        print(f"You have {len(rows)} costs!")
        totalCount = 0
        totalPrice = 0
        for x in rows:
            totalPrice +=x[2] * x[1]
            totalCount +=x[2]
            print(f"You have cost {x[2]} items of {x[0]} product. Total cost is {x[1] * x[2]} TL")
        print(f"A total of {totalCount} items were cost. Total money is {totalPrice} TL")
        return totalPrice
def getSalesSingleList(product):
    dbsales.execute(f"SELECT * FROM sales WHERE productName='{product}'")
    rows = dbsales.fetchall()
    if len(rows) == 0:
        print("Error: You don't have any sales!")
        return 0
    else:
        print(f"You have {len(rows)} sales!")
        totalCount = 0
        totalPrice = 0
        for x in rows:
            totalPrice += x[2] * x[1]
            totalCount += x[2]
            print(f"You have sold {x[2]} items of {x[0]} product. Total sales is {x[1] * x[2]}TL")
        print(f"A total of {totalCount} items were sold. Total money is {totalPrice}TL")
        return totalPrice
def getSalesList():
    dbsales.execute(f"SELECT * FROM sales")
    rows = dbsales.fetchall()
    if len(rows) == 0:
        print("Error: You don't have any sales!")
        return 0
    else:
        print(f"You have {len(rows)} sales!")
        totalCount = 0
        totalPrice = 0
        for x in rows:
            totalPrice += x[2] * x[1]
            totalCount += x[2]
            print(f"You have sold {x[2]} items of {x[0]} product. Total sales is {x[1] * x[2]}TL")
        print(f"A total of {totalCount} items were sold. Total money is {totalPrice}TL")
        return totalPrice
def getProducts():
    db.execute(f"SELECT * FROM products")
    rows = db.fetchall()
    if len(rows) == 0:
        print("Error: You don't have any products!")
    else:
        print("Your all product list : ")
        print(f"You have {len(rows)} products!")
        for x in rows:
            print(f"product name : {x[0]} cost : {x[1]} sale : {x[2]}")
def newCostTotheDb():
    print("Did you make a new cost? Search for product name")
    getProducts()
    name = input("Search Product Name : ")
    db.execute(f"SELECT * FROM products WHERE name='{name}'")
    rows = db.fetchall()
    if len(rows) == 0:
        print("Error: The product does not exist!")
    else:
        row = rows[0]
        productName = row[0]
        cost = row[1]
        sale = row[2]
        profit =  int(cost)
        count = int(input("How many were purchased?"))
        print(f"Total cost price is {int(count) * profit}TL ")
        print(f"Do you confirm the cost of {count} {productName}? ")
        confirm = input("If you are accept this cost press 1 opposite press 0")
        if (confirm == "1"):
             dbpurc.execute("INSERT INTO cost (productName,price,count)  VALUES ('{}', {}, {})".format(productName, profit,count))
             print("New cost is created successfully! Thank you!")
             purccon.commit()
             getCostList()
def SingleProductCostAndSaleInfo():
    name = input("Search Product Name : ")
    cost = getCostSingleList(name)
    sale = getSalesSingleList(name)
    print(f"{name} product profit cost is {sale - cost}TL")


def UpdateProduct():
    name = input("Search Product Name : ")
    db.execute(f"SELECT * FROM products WHERE name='{name}'")
    rows = db.fetchall()
    if len(rows)==0:
        print("Error : The product does not exist!")
    else:
        row = rows[0]
        productName = row[0]
        cost = row[1]
        sale = row[2]
        profit = int(cost)
        getProducts()
        print(f"Product Name : {productName} sale : {sale} cost : {cost}")
        print(f"Do you want to update {productName}?")
        confirm = input("Press 1 if you want to update product, press 0 for cancel")
        if(confirm=="1"):
            uName = input(f"Old Product Name : ({productName}), Product Name : ")
            uCost = input(f"Old Cost {cost}, Cost : ")
            uSale = input(f"Old Sale {sale}, Sale : ")
            db.execute(f"UPDATE products SET name = '{uName}', cost= '{uCost}', sale = '{uSale}' WHERE name = '{productName}';")
            con.commit()
            print("Product is updated successfully! Thank You!")
            getProducts()


def getProfit():
    rent = 3000
    waterBill = 250
    electricityBill = 1500
    internet=200
    salary=4200
    total = rent + waterBill + electricityBill + internet + salary
    cost = getCostList()
    sales = getSalesList()
    print(f"Total sales is {sales}TL")
    print(f"Total cost is {cost}TL")
    print(f"Total Fixed Cost is {total} TL")
    total += cost
    print(f"Total Profit Cost is {sales - total} TL")


print("Press 1 for new product to the database")
print("Press 2 for new sales to the database")
print("Press 3 for new cost to the database")
print("Press 4 for see the sales list")
print("Press 5 for see the cost list")
print("Press 6 for total profit cost")
print("Press 7 for product list")
print("Press 8 for update product")
print("Press 9 for total product profit cost")
choose = input("What's your choose?")

if(choose=="1"):
    newProductTotheDb()
elif(choose=="2"):
    newSalesTotheDb()
elif(choose=="3"):
    newCostTotheDb()
elif(choose=="4"):
    getSalesList()
elif(choose=="5"):
    getCostList()
elif(choose=="6"):
    getProfit()
elif(choose=="7"):
    getProducts()
elif(choose=="8"):
    UpdateProduct()
elif(choose=="9"):
    SingleProductCostAndSaleInfo()
else:
    print("Your choose is wrong. Please start project again.")