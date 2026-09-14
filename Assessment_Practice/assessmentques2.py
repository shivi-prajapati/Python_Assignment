emp_id=0
employees=[]
y=0.0
def menu():
    print("""1.Add Employee
2.View all Employee
3.Search Employee
4.Update Employee
5.Delete Employee
6.Exit""")
    try:
        choice=int(input("Enter Your Choice :"))
    except:
        return -1
    return choice

def net_salary(basic_salary,allowances,deduction):
    return basic_salary+allowances-deduction

def add_employee():
    global emp_id,employees
    name=input("Enter Employee Name :")
    department=input("Enter Employee Department :")
    basic_salary=float(input("Enter Employee Basic Salary :"))
    allowances=float(input("Enter Employee Allowances :"))
    deduction=float(input("Enter Employee Deduction :"))
    emp_dict={'ID':emp_id+1,'Name':name,'Department':department,'Basic Salary':basic_salary,'Allowances':allowances,'Deduction':deduction}
    employees.append(emp_dict)
    emp_id+=1
    print(employees)

def view_employee():
    global y
    if not employees:
        print("No Data Found!")
        return
    if len(employees)==1:
        print('-'*60)
        for e in employees:
            print(f"ID           :           {e['ID']}")
            print(f"Name         :           {e['Name']}")
            print(f"Department   :           {e['Department']}")
            print(f"Basic Salary :           {e['Basic Salary']}")
            print(f"Allowances   :           {e['Allowances']}")
            print(f"Deduction    :           {e['Deduction']}")
            y=net_salary(e['Basic Salary'],e['Allowances'],e['Deduction'])
            print(f"Net Salary   :           {y}")
            print('-'*60)
    elif len(employees)>1:
        print('-'*100)
        print(f"{'ID':^5}{'Name':<20}{'Department':<15}{'Basic Salary':>15}{'Allowances':>15}{'Deduction':>15}{'Net Salary':>15}")
        print('-'*100)
        for e in employees:
            y=net_salary(e['Basic Salary'],e['Allowances'],e['Deduction'])
            print(f"{e['ID']:^5}{e['Name']:<20}{e['Department']:<15}{e['Basic Salary']:>15.2f}{e['Allowances']:>15.2f}{e['Deduction']:>15.2f}{y:>15.2f}")
        print('-'*100)  
    
def search_employee():
    empid=input("Enter Employee Id or Name :")
    for e in employees:
        if empid.isdigit() and int(empid)==e['ID']:
            print(e)
            return
        elif empid==e['Name']:
            print(e)
            return
    else:
        print("Data not found for this ID")

def update_employee():
    global y
    empid=int(input("Enter Employee Id :"))
    for e in employees:
        if empid==e['ID']:
            _name=input("Edit Name :")
            _department=input("Edit Department :")
            _basic_salary=float(input("Edit Basic Salary :"))
            _allowance=float(input("Edit Allowance :"))
            _deduction=float(input("Edit Deduction :"))
            y=net_salary(_basic_salary,_allowance,_deduction)
            e['Name']=_name
            e['Department']=_department
            e['Basic Salary']=_basic_salary
            e['Allowances']=_allowance
            e['Deduction']=_deduction
            return
    print("ID not Found!")
           
def delete_employee():
    empid=int(input("Enter Employee Id :"))
    for e in employees:
        if empid==e['ID']:
            ans=input("Do you really want to delete(y/n) :")
            if ans=='y':
                employees.remove(e)
                return
    else:
        print("ID not found!")

def main():
    while True:
        choice=menu()
        if choice==1:
            add_employee()
        elif choice==2:
            view_employee()
        elif choice==3:
            search_employee()
        elif choice==4:
            update_employee()
        elif choice==5:
            delete_employee()
        elif choice==6:
            break
if __name__=='__main__':main()
