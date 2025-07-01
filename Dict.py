#1.	Create a dictionary from two lists:
#a.	keys = ['id', 'name', 'age']
#b.	values = [101, 'John', 25]

v=dict([('name','Jhon'),('id',101),('age',25)])
print(v)

#2.	Create a dictionary to store student name and age.

v=dict([('Jhon',23),('Ramesh',25),('Suresh',24),('Vasu',28)])
print(v)

#3.	Create an empty dictionary and add key-value pairs one by one.

student = {}
student["name"] = "Alex"
student["age"] = 25
student["id"] = 101
print(student)

#4.	Get the value of key "salary" from this dictionary:
#EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}

employee={'name':'Akhila','age':28,'salary':50000}
print(employee)
print("Salary:",employee['salary'])
print("Salary:",employee.get('salary'))

#5.	 Remove the last inserted key-value pair from the dictionary using an appropriate method

employee={'name':'Akhila','city':'hyd','age':28,'salary':50000}
employee.popitem()
print(employee)

#6.	Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.

#Packing-
#Packing means collecting multiple values into a single variable (usually a tuple or list).

x=["Sunny",25,"CE"]
print(x)

#Unpacking-
#Unpacking means extracting values from a packed collection and assigning them to individual variables.

x=["Ravi",20,"Btech","CE"]
name,age,education,department=x
print(name)
print(age)
print(education)
print(department)

#example2
#*variable length aurgument

k=['python',101,True,'Good']
a,*b,c=k
print(a)
print(b)
print(c)