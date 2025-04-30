#library management system#
class book:
    def __init__(self):
        self.Name=input("enter name of the book")
        self.Serial_number=int(input("enter serial number"))
        self.Authors_name=input("enter name of the author")
        self.Quantity=int(input("enter quantity of the book"))
        self.Price=int(input("enter price of the book"))
        #get reteives the value#
    def getName(self):
        return self.Name
    def getSerial_number(self):
        return self.Serial_number
    def getAuthors_name(self):
        return self.Authors_name
    def getQuantity(self):
        return self.Quantity
    def getPrice(self):
        return self.Price
        #set updates the value
    def setName(self,Name):
        return self.Name
    def setSerial_number(self,Serial_number):
        return self.Serial_number
    def setAuthors_name(self,Authors_name):
        return self.Authors_name
    def setQuantity(self,Quantity):
        return self.Quantity
    def setPrice(self,Price):
        return self.Price

class show_all_book():
    def __init__(self):
        self.book_lists=[]
        self.s=0
            
    def add_books(self):
        b=book()
        self.book_lists.append(b)

    def display_books(self):
        for book in self.book_lists:
            print("Name:",book.getName(),"Serial Number:",book.getSerial_number(),
                  "Author:",book.getAuthors_name(),"Quantity:",book.getQuantity(),"Price:",book.getPrice())
                       
    def search_book_name(self):
        a=input("enter name of the book")
        for book in self.book_lists:
            if book.getName()==a:
                print("Name:",book.getName(),"Serial Number:",book.getSerial_number(),
                  "Author:",book.getAuthors_name(),"Quantity:",book.getQuantity(),"Price:",book.getPrice())
            else:
                print("No Book Found")
    def search_Authors_Name(self):
        a=input("enter name of the author")
        for author in self.book_lists:
            if author.getAuthors_name() == a:
                print("Name:",author.getName(),"Serial Number:",author.getSerial_number(),
                  "Author:",author.getAuthors_name(),"Quantity:",author.getQuantity(),"Price:",author.getPrice())
            else:
                print("no author found")

    def upgrade_quantity(self):
            serial_number = int(input("Enter the serial number of the book to update quantity "))
            for book in self.book_lists:
                if book.getSerial_number() == serial_number:
                    self.Quantity = int(input("Enter the new quantity: "))
                    book.setQuantity(book.getQuantity() + self.Quantity)
                    print("Quantity updated successfully!")
                else:
                    print("Book with given serial number not found.")

    def borrow(self,a):
        n=int(input("enter roll no"))
        if(a.isstudent(n)):
            b=int(input("enter the book serial no"))
            for book in self.book_lists:
                if book.getSerial_number() == b:
                    book.setQuantity(book.getQuantity()-1)
                    print("successfully borrow")
            
                    
class college:
    def __init__(self):
        self.name = input("enter name")
        self.rollno = int(input("enter rollno"))
        self.dept= input("enter department")
        self.year= int(input("enter year"))
        #get reteives the value#

        
    def getname(self):
        return self.name
    def getrollno(self):
        return self.rollno
    def getdept(self):
        return self.dept
    def getyear(self):
        return self.year
        #set updates the value
    def setname(self,name):
        self.name = name
    def setrollno(self,rollno):
        self.rollno = rollno
    def setdept(self,dept):
        self.dept = dept
    def setyear(self,year):
        self.year = year
        
class student():
    def __init__(self):
        self.student_list=[]
        self.c=0

    def add(self):
        a=college()
        self.student_list.append(a)
    def display(self):
        for i in self.student_list:
            print("Name:", i.getname(), "Roll No:", i.getrollno(),
                  "Department:", i.getdept(), "Year:", i.getyear())
    def search(self):
        n=input("enter Department")
        for i in  self.student_list:
              if i.getdept()==n:
                  print("Name:", i.getname(), "Roll No:", i.getrollno(),
                  "Department:", i.getdept(), "Year:", i.getyear())

    def isstudent(self,n):
        s=0
        for i in  self.student_list:
           if i.getrollno()==n:
               s=1

        if s==0:
            return False
        else:
            return True
          
             
s=show_all_book()
d=student()
a=1
while a!=0:
    a=int(input("Enter 1 for Add_Books,2 for Display Books,3 for Name of the books,"
                "4 for authors name,5 for upgrade Quantity,enter the 6 for add,7 display and 8 for search,9 for borrow book ,0 for exit"))
    if a==1:
          s.add_books()
    elif a==2:
        s.display_books()
    elif a==3:
        s.search_book_name()
    elif a==4:
        s.search_Authors_Name()
    elif a==5:
        s.upgrade_quantity()
    elif a==6:
        d.add()
    elif a==7:
        d.display()
    elif a==8:
        d.search()
    elif a==9:
        s.borrow(d)
    

