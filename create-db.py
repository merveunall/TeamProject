import sqlite3 as sql
con = sql.connect("cost.db")
db = con.cursor()
# Databasei sıfırlamak için önce proje dosyasından main.db , cost.db ve sales.db i sil
# daha sonra 2. satırdaki koda main.db yaz ve createTable() fonksiyonunnu çalıştır
# daha sonra 2. satırdaki koda cost.db yaz ve createCost() fonksiyonunnu çalıştır
# daha sonra 2. satırdaki koda sales.db yaz ve createSales() fonksiyonunnu çalıştır
# Databaseler oluşturulmadan access_db.py çalışmaz!
def createTable():
    db.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, cost INT,sale INT)");
    con.commit()
    con.close()
def createSales():
    db.execute("CREATE TABLE IF NOT EXISTS sales (productName TEXT,price INT,count INT)")
    con.commit()
    con.close()
def createCost():
    db.execute("CREATE TABLE IF NOT EXISTS cost (productName TEXT,price INT,count INT)")
    con.commit()
    con.close()

#createTable()
#createSales()
createCost()