'''Assignment 4: Atomic E-Commerce Order Processor
Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products 
must be processed atomically: either the entire order completes successfully, or the entire 
transaction fails. If one item in the order is out of stock or is unrecognized, no stock 
should be deducted for any other item (rollback).'''


class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass
def process_order(catalog,order):
    for k,v in order.items():
        if k not in catalog:
            raise ProductNotFoundError(f"Product {k} is not found in catalog! ")
        stk=catalog[k]["stock"]
        if v>stk:
            raise OutOfStockError( f"Product '{k}' is out of stock. " f"Requested: {v}, Available: {stk}." )
    total=0.0
    for k,v in order.items(): 
        price = catalog[k]["price"] 
        catalog[k]["stock"] -= v 
        total += price * v 
    return total

def main():
    catalog = {
    "P01": {"price": 100.0, "stock": 5},
    "P02": {"price": 50.0, "stock": 2}}
    order={"P01": 2, "P02": 1}
    try:
        total=process_order(catalog,order)
        print('Total Cost :',total)
        print('Updated Catalog :',catalog)
    except ProductNotFoundError as e:
        print(e)
    except OutOfStockError as e:
        print(e)
main()