#Salwa Fayyad 1200430
#Sondos Ashraf 1200905

import datetime
productList=[[]]
from enum import Enum


class Product:

    Product_id=0 
    Product_name=""
    Product_category=""
    Price=0
    Inventory=0 # number of items available for sale from the product
    Supplier=""
    Has_on_offer=0
    offerPrice=0
    validDate=datetime.date(1900,1,1)

    def __init__(self, Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_on_offer, offerPrice,validDate):
        self.Product_id = Product_id
        self.Product_name = Product_name
        self.Product_category = Product_category
        self.Price = Price
        self.Inventory = Inventory
        self.Supplier = Supplier
        self.Has_on_offer = Has_on_offer
        self.offerPrice=offerPrice
        self.validDate=validDate
        



    def addProducts(self, Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_on_offer, offerPrice,validDate):
        productList.append([ Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_on_offer, offerPrice,validDate])

    def printlist(self):
        print(productList)
        
    def getlist(self):
        return productList

