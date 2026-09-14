import json
patients=[]
pid=len(patients)

def menu():
    print("""1.Add Patient
2.View Records
3.Search Patients
4.Update Details
5.Delete Patient
6.Save to json
7.load from json
8.Exit""")
    try:
        choice=int(input("Enter Your Choice :"))
    except:
        return -1
    return choice

def add_patient():
    global pid,patients
    name=input("Enter Patient's Name :")
    age=int(input("Enter Patient's Age :"))
    disease=input("Enter Patient's Disease :")
    doctor=input("Enter Patient's Doctor :")
    fee=float(input("Enter Patient's Fee :"))
    pid=pid+1
    list1=[pid,name,age,disease,doctor,fee]
    patients.append(list1)
    print(patients)

def view_record():
    if not patients:
        print("No Record Found!")
        return
    if len(patients)==1:
        print('-'*60)
        for p in patients:
            print(f"ID       :     {p[0]}")
            print(f"Name     :     {p[1]}")
            print(f"Age      :     {p[2]}")
            print(f"Disease  :     {p[3]}")
            print(f"Doctor   :     {p[4]}")
            print(f"Fee      :     {p[5]}")
        print('-'*60)
    if len(patients)>1:
        print('-'*90)
        print(f"{'ID':^5}{'Name':<20}{'Age':<10}{'Disease':<20}{'Doctor':<20}{'Fee':>10}")
        print('-'*90)
        for p in patients:
            print(f"{p[0]:^5}{p[1]:<20}{p[2]:<10}{p[3]:<20}{p[4]:<20}{p[5]:>10.2f}")
        print('-'*90)

def search_record():
    patient_id=input("Enter Patients Id or Name or Doctor :")
    for p in patients:
        if patient_id.isdigit() and int(patient_id)==p[0]:
            print(p)
            return
        elif patient_id==p[1]:
            print(p)
            return
        elif patient_id==p[4]:
            print(p)
            return
    print("ID not found!")

def update_record():
    patient_id=int(input("Enter Patients Id :"))
    for p in patients:
        if patient_id==p[0]:
            _disease=input("Edit disease :")
            _doctor=input("Edit doctor :")
            _fee=float(input("Edit fee :"))
            p[3]=_disease
            p[4]=_doctor
            p[5]=_fee
            return
    print("ID not found")

def delete_patient():
    patient_id=int(input("Enter Patients Id :"))
    for p in patients:
        if patient_id==p[0]:
            ans=input("do you want to delete record(y/n)").lower()
            if ans=='y':
                patients.remove(p)
                return
            else:
                print("Not Deleting!")
                return
    print("ID not Found!")

def save_record():
    try:
        with open('patient.json','w')as f:
            json.dump(patients,f,indent=4)
            print("Dumped successfully!")
    except OSError:
        print("Error while saving JSON file!")
        
def load_record():
    global patients,pid
    try:
        with open('patient.json','r')as f:
            patient=json.load(f)
            if patient:
                pid=max(p[0] for p in patient)
                patients=patient
            else:
                pid=0
        print("Records loaded successfully")
    except FileNotFoundError: 
        print("JSON file not found!") 
    except json.JSONDecodeError: 
        print("JSON file contains invalid data!") 
    except OSError: 
        print("Error while reading JSON file!")

def main():
    while True:
        choice=menu()
        if choice==1:
            add_patient()
        elif choice==2:
            view_record()
        elif choice==3:
            search_record()
        elif choice==4:
            update_record()
        elif choice==5:
            delete_patient()
        elif choice==6:
            save_record()
        elif choice==7:
            load_record()
        elif choice==8:
            break
        else:
            print("Invalid Choice!")
if __name__=='__main__':main()
