import csv
student=[]
std_id=len(student)
def menu():
    print("""1.Enroll Student
2.Chort Directory
3.Query Records
4.Revise Payment
5.Purge Record
6.Save to CSV
7.Load from CSV
8.Exit""")
    try:
        choice=int(input("Enter Your Choice :"))
    except:
        return -1
    return choice

def enroll_student():
    global student,std_id
    name=input('Enter Student Name :').strip()
    if name=='':
        print("Name cannot be empty try again!")
        return
    course=input('Enter Course Name :').strip()
    if course=='':
            print("Course cannot be empty try again!")
            return
    try:
        total_fee=float(input('Enter Total Fee :'))
        if not total_fee>0:
            print("Total fee must be greater than zero")
            return
    except ValueError as e:
        print(e)
        return
    try:
        amount_paid=float(input('Enter the Amount Paid do far :'))
        if amount_paid<0 or amount_paid>total_fee:
            print("Amount must be greater than zero and less than total fee")
            return
    except ValueError as e:
        print(e)
        return
    std_dict={'ID':std_id+1,'Name':name,'Course':course,'Total Fee':total_fee,'Amount Paid':amount_paid}
    student.append(std_dict)
    std_id+=1

def status(total_fee,amount_paid):
    if amount_paid>=total_fee:
        return 'Fully Paid'
    elif 0<amount_paid<total_fee:
        return'Pending'
    elif amount_paid==0:
        return 'Unpaid'
    
def cohort_directory():
    if not student:
        print("No Record Found!")
        return
    if len(student)==1:
        print('-'*60)
        for p in student:
                print(f"ID          :     {p['ID']}")
                print(f"Name        :     {p['Name']}")
                print(f"Course      :     {p['Course']}")
                print(f"Total Fee   :     {p['Total Fee']}")
                print(f"Amount Paid :     {p['Amount Paid']}")
                _status=status(p['Total Fee'],p['Amount Paid'])
                print(f"Status      :     {_status}")
        print('-'*60)
    if len(student)>1:
            print('-'*90)
            print(f"{'ID':^5}{'Name':<20}{'Course':<20}{'Total Fee':<15}{'Amount Paid':<15}{'Status':<10}")
            print('-'*90)
            for p in student:
                _status=status(p['Total Fee'],p['Amount Paid'])
                print(f"{p['ID']:^5}{p["Name"]:<20}{p['Course']:<20}{p['Total Fee']:<10.2f}{p['Amount Paid']:<10.2f}{_status:<10}")
            print('-'*90)

def query_record():
    stud_id=input('Enter Id or name course :')
    for s in student:
        if stud_id.isdigit() and int(stud_id)==s['ID']:
            print(s)
            return
        if stud_id==s['Name']:
            print(s)
            return
        if stud_id==s['Course']:
            print(s)
            return
    print("NO data found for this ID")

def revise_payment():
    stud_id=int(input("Enter Student Id :"))
    for p in student:
            if stud_id==p[0]:
                _amount_paid=float(input("Edit Amount paid :"))
                p['Amount Paid']+=_amount_paid
                return
    print("ID not found")

def purge_record():
    stud_id=int(input("Enter Patients Id :"))
    for p in student:
        if stud_id==p[0]:
            ans=input("do you want to delete record(y/n)").lower()
            if ans=='y':
                student.remove(p)
                return
            else:
                print("Not Deleting!")
                return
    print("ID not Found!")

def save_to_csv():
    with open('student.csv','w')as f:
        writer=csv.DictWriter(f,fieldnames=['ID','Name','Course','Total Fee','Amount Paid','Status'])
        writer.writeheader()
        writer.writerows(student)

def load_from_csv():
    global student,std_id
    with open('student.csv','r')as f:
        reader=csv.DictReader(f)
        for r in reader:
            r['ID'] = int(r['ID'])
            r['Total Fee'] = float(r['Total Fee'])
            r['Amount Paid'] = float(r['Amount Paid'])
            student.append(r)
        if student:
            std_id = max(s['ID'] for s in student)
        else:
            std_id = 0

        print("Records loaded successfully!")


def main():
    while True:
        choice=menu()
        if choice==1:
            enroll_student()
        elif choice==2:
            cohort_directory()
        elif choice==3:
            query_record()
        elif choice==4:
            revise_payment()
        elif choice==5:
            purge_record()
        elif choice==6:
            save_to_csv()
        elif choice==7:
            load_from_csv()
        elif choice==8:
            break
        else:
            print("Invalid Choice!")
if __name__=='__main__':main()