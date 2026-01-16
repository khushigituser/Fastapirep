# FASTAPI

# CRUD operations :
# uvicorn server port -8000 fix

# create -> post decorator
# read-> get decorator
# update -> put decorator
# delete -> delete decorator



from fastapi import FastAPI
from data import product
from database import getData, add_data, update_data, delete_data
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000"],   # we can also use star here for all ports
                   allow_methods=["*"])

listofproducts=[
    product(id=1, name="laptop", description='dell', price=120, quantity=23),
    product(id=2, name="mobile1", description="moto11", price=234, quantity=34),
    product(id=3, name="mobile2", description="moto12", price=235, quantity=35),
    product(id=4, name="mobile3", description="moto13", price=236, quantity=36)
]



# @app.get('/')
# def getData():
#     return "welcome to home.."

@app.get('/new page')
def newPageData():
    return "welcome to new page.."

@app.get('/products')
def getproducts():
    return getData()

@app.get('/products/{id}')   # this id is optional when we are not using frontend
def get_products(id:int):
    for i in listofproducts:
        if i.id==id:
            return i
    return '404 product not found'

# @app.post('/products')
# def add_product(product:product):
#     listofproducts.append(product)
#     return "data added successfully"


@app.post('/products')
def add_product(product:product):
    return add_data(product)


# @app.put("/products")
# def update_product(id:int, product:product):
#     for i in range(len(listofproducts)):
#         if listofproducts[i].id==id:
#             listofproducts[i]=product
#             return "product update successfully"
#     return "product not found"


@app.put("/products/{id}")
def update_product(id:int, product:product):
    return update_data(id, product)


# @app.delete("/products")
# def delete_product(id:int):
#     for i in range(len(listofproducts)):
#         if listofproducts[i].id==id:
#             del listofproducts[i]
#             return "product deleted sucessfully"
#     return "product not found"

@app.delete("/delete_products")
def delete_product(id:int):
    products=getData()
    for i in products:
        if i.id == id:
            return delete_data(id)
    return "product not found"

