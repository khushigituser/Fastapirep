from fastapi import FastAPI
from data import product

app=FastAPI()

products=[
    product(id=1, name="laptop", description='dell', price=120, quantity=23),
    product(id=1, name="mobile", description="moto", price=234, quantity=34)
]



@app.get('/')
def getData():
    return "welcome to home.."

@app.get('/new page')
def newPageData():
    return "welcome to new page.."

@app.get('/products')
def get_products():
    return products