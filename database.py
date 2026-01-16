import mysql.connector as sql
from data import product
 
conn=sql.connect(host='localhost', user='root', password='root')

conn.autocommit=True
cur=conn.cursor()
cur.execute('use data')

def getData():
    products=[]
    cur.execute('select *from bckndb;')
    data=cur.fetchall()
    for i in data:
        products.append(product(id=i[0], name=i[1], description=i[2], price=i[3], quantity=i[4]))
    return products

def add_data(product:product):
     query=f"insert into bckndb values({product.id},'{product.name}','{product.description}',{product.price},{product.quantity});"
     cur.execute(query)
     return "record added successfully"

def update_data(id:int, product:product):
    query=f"update bckndb set name='{product.name}',description='{product.description}',price={product.price}, quantity={product.quantity} where id={id};"
    cur.execute(query)
    return "record added successfully"


def delete_data(id:int):
    query=f"delete from bckndb where id={id}"
    cur.execute(query)
    return "record deleted successfully"
