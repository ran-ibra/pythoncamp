'''
Contact Book Manager
1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Update Contact
6. Exit
Choice: 1
Name: John Doe
Phone: 555-1234
Email: john@example.com
Contact saved!
Choice: 2
--- All Contacts ---
1. John Doe | 555-1234 | john@example.com
2. Jane Smith | 555-5678 | jane@example.com
'''
import csv
import os
def add():
    name=input("name: ")
    phone= input("phone: ") 
    email=input("email: ")
    # return{
    #     'name':name,
    #     'phone':phone,
    #     'email':email
    # }
    with open('names.csv', 'a', newline='') as f:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
        if os.stat('names.csv').st_size == 0:
            writer.writeheader()
        writer.writerow({'name': name, 'phone': phone, 'email': email})
    print("Contact saved!")
def viewall():
    
    with open('names.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row['name']} | {row['phone']} | {row['email']}")

def search(f ):
    search=input("enter the searched ")
    found_rows = []
    with open(f, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter='|')
        for row in reader:
            for cell in row:
                if search in cell:
                    found_rows.append(row)
                    break  
    return found_rows



def update(f, col, value, colupdate,valueupdate):
    updated_rows = []
    with open(f, 'r', newline='') as inn:
        reader = csv.DictReader(inn,delimiter='|')
        fieldnames = reader.fieldnames
        for row in reader:
            if row[col] == value:
                row[colupdate] = valueupdate
            updated_rows.append(row)

    with open(f, 'w', newline='') as outt:
        writer = csv.DictWriter(outt, fieldnames=fieldnames,delimiter='|')
        writer.writeheader()
        writer.writerows(updated_rows)
def delete(f, col,value):

    remaining_rows = []
    with open(f, 'r', newline='')as inn :
        reader = csv.DictReader(inn,delimiter='|')
        fieldnames = reader.fieldnames
        for row in reader:
            if row[col] != value:
                remaining_rows.append(row)

    with open(f, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames,delimiter='|')
        writer.writeheader()
        writer.writerows(remaining_rows)


ch=1
while ch!=0:
    ch = input("choose one: \n1. Add Contact\n2. View All Contacts\n3. Search Contact\n4. Delete Contact\n5. Update Contact\n6. Exit")
    if ch == "1":
        add()
    elif ch == "2":
        viewall()
    elif ch=="3":
        results=search('names.csv')
        if results:
            print(f"Found in the following rows:")
            for row in results:
                print(row)
        else:
            print(f" not found in '{'names.csv'}'.")
    elif ch =="4":
        col= input("enter the col")
        val= input("enter the value you want to delete")
        delete('names.csv', col,val)

        
    elif ch=="5":
        col= input("enter the col")
        val= input("enter the value you want to update")
        
        upcol= input("enter the col you need to update the value in ")
        upval= input("enter the updated value")

        update('names.csv',col,val, upcol,upval)
        


# writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
# writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

