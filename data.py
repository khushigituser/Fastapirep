from pydantic import BaseModel        # Pydantic checks whether incoming data matches the expected data types.
class product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int

    # def __init__(self,id, name, description, price,quantity ):   #constructor
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.price=price
    #     self.quantity=quantity

        
