list1=[]
id_inc=0
def menu():
    print("""0: exit
1:Add book
2:View Catalog
3:Search books
4:update details
5: delete book
6: save to file
7:load from file         
          """)
    try:
        choice=int(input("Enter your choice:"))
    except:
        return -1
    return choice
def add_book():
    global list1, id_inc
    title=input("Enter Title of Book :")
    author=input("Enter Author Name :")
    genre=input("Enter Genre of Book :")
    price=float(input("Enter price of Book :"))
    copies=int(input("Enter number of copies :"))
    dict1={'ID':id_inc+1,'Title':title,'Author':author,'Genre':genre,'Price':price,'Copies':copies}
    list1.append(dict1)
    id_inc+=1
            
def view_book():
    if not list1:
        print("List is Empty!")
        return
    if len(list1)==1:
        print('-'*90)
        for book in list1:
            print(f"'ID'    :             {book['ID']}")
            print(f"'Title' :             {book['Title']}")
            print(f"'Author':             {book['Author']}")
            print(f"'Genre' :             {book['Genre']}")
            print(f"'Price' :             {book['Price']}")
            print(f"'Copies':             {book['Copies']}")
        print('-'*70)
    else:        
        print(f"{'ID':^5}{'Title':<20}{'Author':<20}{'Genre':<20}{'Price':>10}{'Copies':>10}")
        print('-'*90)
        for book in list1:
            print(f"{book['ID']:^5}{book['Title']:<20}{book['Author']:<20}{book['Genre']:<20}{book['Price']:>10.2f}{book['Copies']:>10}")
        print('-'*90)
        
def search_book():
    book_id=(input("Enter book id or title or author  :"))
    for b in list1:
        if book_id.isdigit() and int(book_id)==b['ID']:
            print(b)
            return
        elif book_id==b['Title']:
            print(b)
            return 
        elif book_id==b['Author']:
            print(b)
            return
    else:
        print("No data found from this ID!")
        
def update_book():
    book_id=(input("Enter book id :"))
    for b in list1:
        if int(book_id)==b['ID']:
            _price=float(input("Edit Price :"))
            _copies=int(input("Edit Copies :"))
            b['Price']=_price
            b['Copies']=_copies
            
def delete_book():
    book_id=(input("Enter book id :"))
    for b in list1:
        if int(book_id)==b['ID']:
            list1.remove(b)
            print("Deleted Successfully!")
     

def save_to_file():
    try:   
        filename=input("enter filename :")       
        with open(filename,'w') as f:
            for b in list1:
                a= f'{b['ID']}|{b['Title']}|{b['Author']}|{b['Price']}|{b['Copies']}'
                f.write(a)
    except:
        print("something went wrong!")
    
def load_from_file():
    try:
        filename=input("Enter Text Filename :")
        with open(filename,'r') as f:
            print(f.read())
    except :
        print("Somethinf went wrong!")

def main():
    while True:
        choice=menu()
        if choice==0:
            break
        match choice:
            case 1:
                add_book()
            case 2:
                view_book()
            case 3:
                search_book()
            case 4:
                update_book()
            case 5:
                delete_book()
            case 6:
                save_to_file()
            case 7:
                load_from_file()
            case _:
                print("Invalid choice")
main()