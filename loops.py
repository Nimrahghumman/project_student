for i in range(5):
    print(i)

bankcode = "200nh"
usercode = ""

while bankcode != usercode:
    bankcode = ("enter your bank code")
    print("your bank code is incorrect")

print("your bank code is correct")

useremail1 ="nimrah@gmail.com"
userpassword1 = "123456"
useremai = ""
userpassword = ""
while useremail1 != useremai and userpassword1 != userpassword:
    useremail = input("enter your email")
    userpassword = input("enter your password")
    print("useremail & userpassword is wrong")  
print("your email or password is correct") 

#  
email = "ghuman@gmail.com"
password = "123456"

while True:
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")

    if (email == user_email and password == user_password):
       
        break
    print("Invalid credentials, try again.\n")

print("login successfull")

# set work
a = {1,2,3,4,5,6,7,8,9}

a.update([30, "color","red"])

print(a)

data = {10,20,30,40,50,60}
# data.remove(20)
# data.discard(100)
# data.update([200])
data.add(100)

print(data)

student = {"ali","nimra","sara","iqra","hamza","neha", "samra"}
a,b,*c, = student
print(b)
print("hello" in student)
print(student)



# ref and copy
a = [1,2,3,4]
b = a.copy()
b.append(5)
print(a)



def user(id,Name,age, ):
   print(f"{id} hello {Name} your age {age}") 

user(1,"nimra",22)
user(2,"sara", 22)
a = 10
def data():
    print(a)
data()
# tuple imutable***********
data = (500)
print(id(data))
marks = (500)
print(id(marks))

# tow varebal same id********** arange 500
# ****** mutablt data list,setor tapul********

# # set work 
a = {500}
print(id(a))


b = {500}
print(id(b))


class car:
    def __ini__(self,brand, model):
        self.brand = brand
        self.model = model

newcar = car ("tesla","xr")
print(newcar.brand)



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old") student1 = Student("Ali", 20)
student1.introduce()

   
class student:
 def __init__(self,rollnumber, name, age):
        self.rollnumber = rollnumber
        self.name = name
        self.age = age


newstudent = student(101 ,"ali", 20) 
print(f"{newstudent.rollnumber}my name is  {newstudent.name} and my age is {newstudent.age}")       

class bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
newbank = bank("nimra", 123456789, 1000.0)
print(newbank.name)
print(newbank.account_number)
print(newbank.balance)