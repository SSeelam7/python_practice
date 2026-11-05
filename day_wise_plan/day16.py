
#1:
class student:
    pass

class car:
    pass

class book:
    pass

class bankaccount:
    pass


#2:

student1 = student()
student2 = student()

car1 = car()
car2 = car()
car3 = car()

book1 = book()
book2 = book()

bank_account1 = bankaccount()
bank_account2 = bankaccount()

print(book1)
#just printing 1 object bcz, all are similar.


#3:
class student():
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = student("trinadh", 27, "python")
student2 = student("sairam", 27, "pyspark")
student3 = student("ramesh", 27, "SQL")
student4 = student("yashwanth", 27, "ABAP")

print(f"name: {student1.name}, age: {student1.age}, course: {student1.course}")
print(f"name: {student2.name}, age: {student2.age}, course: {student2.course}")
print(f"name: {student3.name}, age: {student3.age}, course: {student3.course}")
print(f"name: {student4.name}, age: {student4.age}, course: {student4.course}")

#4:
class employee():
    def __init__(self,name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

employee1 = employee("Trinadh", 1111, "IT", 90000)
employee2 = employee("ramesh", 2222, "IT", 70000)
employee3 = employee("Sekhar", 3333, "Non-IT", 60000)

print(f"Employee Name: {employee1.name}, Employee ID: {employee1.employee_id}, Department: {employee1.department}, Salary: {employee1.salary}")

#self will store the details into the respective object.

#5:
class book():
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = book("maths", "ramanujan", 150)
book2 = book("science", "abdhul_kalam", 250)
book3 = book("social", "hitler", 100)
print("====== Before price change ======")
print(f"Title: {book1.title}, Author: {book1.author}, Price: {book1.price}")
print(f"Title: {book2.title}, Author: {book2.author}, Price: {book2.price}")
print(f"Title: {book3.title}, Author: {book3.author}, Price: {book3.price}")

book3.price = 300

print("====== After price change ======")
print(f"Title: {book3.title}, Author: {book3.author}, Price: {book3.price}")



#6:
class bankaccount():
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw_amount(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount



account1 = bankaccount("sairam", 25000)
account2 = bankaccount("trinadh", 30000)


print(account1.check_balance())
account1.deposit(25000)
print(account1.check_balance())
account1.withdraw_amount(60000)
account1.withdraw_amount(40000)
print(account1.check_balance())



#7:
class GameCharacter():
    def __init__(self, name, health, level,coins):
        self.name = name
        self.health = health
        self.level = level
        self.coins = coins

    def take_damage(self,amount):
        self.health -= amount
        return self.health

    def collect_coins(self,amount):
        self.coins += amount
        return self.coins

    def level_up(self):
        self.level += 1
        return self.level

player1 = GameCharacter("Thor", 100, 1, 100)

print(f"Character Name: {player1.name}, Health: {player1.health}, Level: {player1.level}, Coins: {player1.coins}")
player1.take_damage(10)
print(f"Character Name: {player1.name}, Health: {player1.health}, Level: {player1.level}, Coins: {player1.coins}")
player1.collect_coins(50)
print(f"Character Name: {player1.name}, Health: {player1.health}, Level: {player1.level}, Coins: {player1.coins}")
player1.level_up()
print(f"Character Name: {player1.name}, Health: {player1.health}, Level: {player1.level}, Coins: {player1.coins}")



#8:

class Student():
    def __init__(self,name, age, course):
        self.name = name
        self.age = age
        self.course = course

students_list = [
    Student("Rahul", 25, "Python"),
    Student("Priya", 23, "Data Science"),
    Student("Arjun", 24, "Java"),
    Student("Trinadh", 27, "Python"),
    Student("Sairam", 27, "Python"),
    Student("Ramesh", 27, "SQL")
]
ages = []
for student in students_list:
    ages.append(student.age)
    print(f"Student Name: {student.name}")



print("========= Student Enrolled For Python =========")
cnt = 0
for student in students_list:
    if student.course == "Python":
        cnt += 1
        print(f"Python Student Name: {student.name}")
print(f"{cnt} Students Enrolled For Python")


oldest_students = []
for student in students_list:
    if student.age == max(ages):
        oldest_students.append(student.name)
print(f"Oldest Student: {oldest_students}")


#9:
class Book():
    def __init__(self,title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

class Member():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def borrow_book(self, book):
        if book.is_available == "Yes":
            print(f"Book '{book.title}' is available. Granted to {self.name}")
            book.is_available = "No"
        else:
            print(f"Book '{book.title}' is already borrowed")


# -------------------------
# Books in the library
# -------------------------

maths_book = Book("Maths", "Ramanujan", "Yes")
Biology_book = Book("Biology", "Aristotle", "Yes")
constitution = Book("Indian Constitution", "Ambedkar", "No")



# -------------------------
# Library members
# -------------------------

sairam = Member("Sairam", 1111)
yashwanth = Member("Yashwanth", 2222)


sairam.borrow_book(maths_book)
print(maths_book.is_available)
yashwanth.borrow_book(maths_book)
yashwanth.borrow_book(constitution)
yashwanth.borrow_book(Biology_book)



#Mini Project
# Creating Class PRODUCT
class Product():
    def __init__(self,name, price):
        self.name = name
        self.price = price

# Shopping Cart
class ShoppingCart():
    def __init__(self):
        self.products = []

    #to add the products int cart
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} has been added to shopping cart")

    #to display the cart
    def display_cart(self):
        if len(self.products) == 0:
            print("Cart is empty")
            return

        for product in self.products:
            print(f"{product.name} - ₹{product.price}")

    #to remove the products from cart
    def remove_product(self,product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"{product.name} Removed from Cart")
                return

    #to calculate the total price of cart items
    def calculate_total(self):
        total_price = 0

        for product in self.products:
            total_price += product.price

        return total_price

cart = ShoppingCart()

while True:
    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. Display Cart")
    print("3. Remove Product")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add product
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))

        product = Product(name, price)
        cart.add_product(product)


    elif choice == "2":
        # Display cart
        cart.display_cart()

    elif choice == "3":
        # Remove product
        product_name = input("Enter product name which you want to remove: ")
        cart.remove_product(product_name)

    elif choice == "4":
        # Calculate total
        total_price = cart.calculate_total()
        print(f"Total Price: {total_price}")

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")




#Day16 Challenge:
#Creating Movie class

class Movie():

    def __init__(self,title,genre,rating,watched):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watched = watched

class Watchlist():

    def __init__(self):
        self.movies = []

    #function to add the movies to watchlist
    def add_movie(self,movie):

        for mov in self.movies:

            if mov.title.lower() == movie.title.lower():
                print(f"{movie.title} is already in watchlist")
                #Intentionally added this part, bcz in real time(prime, netflix, youtube) we don't see duplicates in watchlist
                return

        self.movies.append(movie)
        print(f"{movie.title} added to watchlist")

    def display_movies(self):
        if len(self.movies) == 0:
            print("Watch list is empty")

        else:
            for movie in self.movies:
                print(f"{movie.title} | {movie.genre} | {movie.rating} | {movie.watched}")


    def mark_watched(self,movie_title):

        for mov in self.movies:
            if mov.title.lower() == movie_title.lower():

                if not mov.watched:
                    print(f"{movie_title} already marked as watched")
                    return

                else:
                    mov.watched = True
                    print(f"{movie_title} marked as watched")
                    return

        else:
            print(f"{movie_title} not found")
            return

    def remove_movie(self,movie_title):
        for mov in self.movies:
            if mov.title.lower() == movie_title.lower():
                self.movies.remove(mov)
                print(f"{movie_title} removed from watchlist")
                return

        else:
            print(f"{movie_title} not found in watch list")

    def get_unwatched_movies(self):

        if len(self.movies) == 0:
            print("Watch list is empty")

        else:

            for mov in self.movies:
                if mov.watched == False:
                    print(f"{mov.title} to be watched")

watchlist = Watchlist()


while True:
    print("----------------------")
    print("Please Choose the option")
    print("----------------------")
    print("1. Add Movie To watch List")
    print("2. Display The Watchlist")
    print("3. Mark Movie As Watched")
    print("4. Remove Movie From Watchlist")
    print("5. Get Unwatched Movies List")
    print("6. Exit")
    print("----------------------")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        title = input("Enter the movie title: ")
        genre = input("Enter the genre: ")
        rating = input("Enter the rating: ")
        watched = input("Did you watch the movie?: ")

        # Other than True or true I want to mark every other inpu as Bool False
        watched = watched.lower() == "true"

        movie = Movie(title, genre, rating, watched)
        watchlist.add_movie(movie)

    elif choice == "2":

        watchlist.display_movies()

    elif choice == "3":

        movie_title = input("Enter The Movie Title Which You Want To Mark: ")
        watchlist.mark_watched(movie_title)

    elif choice == "4":

        movie_title = input("Enter The Movie Title Which You Want To Remove: ")
        watchlist.remove_movie(movie_title)

    elif choice == "5":

        watchlist.get_unwatched_movies()

    elif choice == "6":
        print("Thanks You...!")
        break

    else:
        print("Invalid Selection, Please Choose Right One")










