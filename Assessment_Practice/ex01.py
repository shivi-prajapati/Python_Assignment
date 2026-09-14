products = [ 
    {"ID": 1, "Name": "Laptop", "Category": "Electronics", "Price": 55000, "Quantity": 10}, 
    {"ID": 2, "Name": "Smartphone", "Category": "Electronics", "Price": 20000, "Quantity": 25} ,
    {"ID": 3, "Name": "Chair", "Category": "Furniture", "Price": 1500, "Quantity": 50}
] 

id_counter = len(products)

def menu():
    print('*'*80)
    print('''Select a option from the given menues
    1.Add Product
    2.View All Products
    3.Search Product
    4.Update Product
    5.Delete Product
    6.Exit
''')
    try:
        num=int(input("Enter Your Choice :"))
    except:
        num=-1
    return num

def add():
    global id_counter
    try:
        print('******** Add new product details ********')
        name=input("Enter product's Name you want to Add :").strip()
        if name=='':
            print('Name cannot be empty')
            return        
        category=input("Enter Product's Category :").strip()
        if category=='':
            print("Category cannot be empty")
            return
        price=float(input("Enter price of Product :"))
        if type(price)==str or price<0:
            print("Price needs to be a Positive Integer")
        quantity=int(input("Enter Quantity of product :"))
        if type(quantity)==str or quantity<0:
            print("Quantity needs to be a Positive Integer")
        products.append(dict(ID=id_counter+1,Name=name,Category=category,Price=price,Quantity=quantity))
        id_counter+=1
    except:
        ...

#-------------------------------------------------------------------------------------------------------------

def view():
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Quantity':>5}')
    for p in products:
        print('-'*60)
        pid,pname,pcategory,pprice,pqty=p.values()
        print(f'{pid:^5}{pname:<20}{pcategory:<20}{pprice:>10.2f}{pqty:>5}')
    print('-'*60)

#-------------------------------------------------------------------------------------------------------------

def search():
    y=int(input("Enter an Id you want to search :"))
    result=[i for i in products if i["ID"]==y]
    if not result:
        print("Data not found for the given ID")
        return None
    else:
        pid,pname,pcategory,pprice,pqty=result[0].values()
        print(f'Id           :{pid}')
        print(f'Name         :{pname}')
        print(f'Category     :{pcategory}')
        print(f'Price        :{pprice}')
        print(f'Quantity     :{pqty}')
        print('-'*60)

#-------------------------------------------------------------------------------------------------------------

def update():
    y=int(input("Enter Product Id you want to Update :"))
    result=[i for i in products if i['ID']==y]
    if not result:
        print("Data not found for the given ID")
        return None
    _,pname,pcategory,pprice,pqty=result[0].values()
    _pname=input(f'Name : ({pname})')
    _pcategory=input(f'Category : ({pcategory})')
    _pprice=int(input(f'Price : ({pprice})'))
    _pqty=int(input(f'Quantity : ({pqty})'))
    result[0]["Name"]=_pname
    result[0]["Category"]=_pcategory
    result[0]["Price"]=_pprice
    result[0]["Quantity"]=_pqty
    print("Updated Sucessfully !!")
    
#-------------------------------------------------------------------------------------------------------------

def delete():
    y=int(input("Enter Product Id you want to Update :"))
    result=[i for i in products if i['ID']==y]
    if not result:
        print("Data not found for the given ID")
        return None
    else:
        ans=input("Are you sure you want to delete (y/n) :")
        if ans=='y':
            products.remove(result[0])
            print("Deleted Sucessfully !!")

#-------------------------------------------------------------------------------------------------------------

def main():
    while True:
        choice=menu()
        if choice==6:
            break
        elif choice==1:
            add()
        elif choice==2:
            view()  
        elif choice==3:
            search()
        elif choice==4:
            update()
        elif choice==5:
            delete()
        else:
            print("Invalid Choice Please Try Again!!")    
if __name__=="__main__":main()
