import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['mydb']
collection = db['users']

# name = input("Enter name\n")
# age = int(input('Enter age\n'))
# salary = float(input("Enter salary\n"))
# designation = input("Enter designation\n")

details = {
        # 'Name': name,
        # 'Age': age,
        # 'Salary': salary,
        # 'Designation': designation
    }

insert = collection.insert_one(details)

if insert.inserted_id:
    print("User Details inserted succesfully")
else:
    print('Error..')