import sqlite3
from unicodedata import category

def create(dbname):
    """ Build's DataBase using the name passed to the function as a parameter """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE Store(idStore INT, SquareFeet INT, StoreType VARCHAR(45), LocationType CHAR(1), Address VARCHAR(45), City VARCHAR(45), StoreState VARCHAR(45), ZipCode VARCHAR(10));")
    c.execute("CREATE TABLE Store_Product(ProductID INT, StoreID INT, Quantity INT);")
    c.execute("CREATE TABLE Product(idProduct INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(30), Price DECIMAL(5,2), CategoryID INT, Description VARCHAR(90));")
    c.execute("CREATE TABLE Category(idCategory INT, Name VARCHAR(45), Description VARCHAR(90));")

    conn.commit()
    conn.close()


def fill(dbname):
    """ Fills the DataBase using the lists below """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # setup lists to be used to build DB
    categories = [(1, "CPU", "The Brain"), (2, "GPU", "The Brawn"), (3, "Memory", "The Beauty")]
    stores = [(1, 4000, "Retail", 'R', "2001 Blake St", "Denver", "Colorado", "80205"), (2, 1000, "Retail", 'R', "1 E 161 St", "The Bronx", "New York", "10451"), (3, 2000, "Retail", 'R', "24 Willie Mays Plaza", "San Francisco", "California", "94107")]
    products = [(1, 'RTX 3090', 960.99, 'GPU', 'Clock Speed 1.7 GHz, Memory 24 GB'), (2, 'RTX 3080', 740.99, 'GPU', 'Clock Speed 1.71 GHz, Memory 10 GB')]
    products += [(3, 'Intel Core i5-13600K', 329.99, 'CPU', 'Clock Speed 5.1 GHz, 14 cores and 20 threads'), (4, 'Intel Core i5-12600K', 277.99, 'CPU', 'Clock Speed 4.9 GHz, 10 cores and 16 threads')]
    products += [(5, 'Corsair Vengeance LPX', 67.99, 'Memory', '2 x 16GB'), (6, 'Corsair Dominator Platinum RGB', 349.99, 'Memory', '2 x 32GB')]

    # populate Category table
    for (catid, name, desc) in categories:
        c.execute("INSERT INTO Category VALUES(?, ?, ?);", (catid, name, desc)) 

    # populate Store table
    for (storeid, sqft, type, loc, add, city, state, zip) in stores:
        c.execute("INSERT INTO Store VALUES(?, ?, ?, ?, ?, ?, ?, ?);", (storeid, sqft, type, loc, add, city, state, zip))

    #----------------------------------------------------------------------------------------------------
    # My 'for' loop isn't working; 
    #
    #   File "/Users/brendanryan/Documents/School/CS_3308_Tools/Labs/Lab_7/storedb.py", line 36, in fill
    #   c.execute("INSERT INTO Product VALUES(?, ?, ?, ?, ?);", (prodid, name, price, catid, desc))
    #   sqlite3.InterfaceError: Error binding parameter 3 - probably unsupported type.
    #
    #----------------------------------------------------------------------------------------------------

    # for (prodid, name, price, catname, desc) in products:
    #     catid = c.execute("SELECT idCategory FROM Category WHERE Name = (?);", (catname,))             # because 'catname' came from a tuple, I had to indicate this with the comma. List literal is another option???
    #     c.execute("INSERT INTO Product VALUES(?, ?, ?, ?, ?);", (prodid, name, price, catid, desc))

    # # manually add items to Product table
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('RTX 3090', 960.99, (SELECT idCategory FROM Category WHERE Name = 'GPU'), 'Clock Speed 1.7 GHz, Memory 24 GB');")
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('RTX 3080', 740.99, (SELECT idCategory FROM Category WHERE Name = 'GPU'), 'Clock Speed 1.71 GHz, Memory 10 GB');")
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('Intel Core i5-13600K', 329.99, (SELECT idCategory FROM Category WHERE Name = 'CPU'), 'Clock Speed 5.1 GHz, 14 cores and 20 threads');")
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('Intel Core i5-12600K', 277.99, (SELECT idCategory FROM Category WHERE Name = 'CPU'), 'Clock Speed 4.9 GHz, 10 cores and 16 threads');")
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('Corsair Vengeance LPX', 67.99, (SELECT idCategory FROM Category WHERE Name = 'Memory'), '2 x 16GB');")
    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES('Corsair Dominator Platinum RGB', 349.99, (SELECT idCategory FROM Category WHERE Name = 'Memory'), '2 x 32GB');")

    # add products to store_product table
    c.execute("INSERT INTO Store_Product VALUES(1, 1, 32);")
    c.execute("INSERT INTO Store_Product VALUES(2, 1, 64);")
    c.execute("INSERT INTO Store_Product VALUES(3, 1, 128);")
    c.execute("INSERT INTO Store_Product VALUES(3, 2, 128);")
    c.execute("INSERT INTO Store_Product VALUES(4, 2, 256);")
    c.execute("INSERT INTO Store_Product VALUES(5, 2, 512);")
    c.execute("INSERT INTO Store_Product VALUES(5, 3, 512);")
    c.execute("INSERT INTO Store_Product VALUES(6, 3, 1024);")
    c.execute("INSERT INTO Store_Product VALUES(1, 3, 2048);")

    conn.commit()
    conn.close()

def addProduct(dbName, productName, price, categoryID, description):
    """ Inserts a product into the 'Product' table. Performs some error checking """
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    if not isinstance(productName, str) or len(productName) < 1:
        raise ValueError
    if not isinstance(description, str) or len(description) < 1:
        raise ValueError
    if isinstance(price, str):
        raise ValueError
    elif price < 0:
        raise ValueError

    # this section is driving the validation for test: 'test_catid'
    test_catid = c.execute("SELECT Name FROM Category WHERE idCategory= (?);", (categoryID,))   # Am I forcing this to be a tuple by wrapping the parameter in parens?
    test_catid = c.fetchone()
    if test_catid == None:
        raise ValueError

    c.execute("INSERT INTO Product (Name, Price, CategoryID, Description) VALUES(?, ?, ?, ?);", (productName, price, categoryID, description))
    
    conn.commit()
    conn.close()

create("StoreDB")
fill("StoreDB")