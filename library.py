#class => Library
#Layers of abstraction => display available books, to lend a book, to add a book

# class = Customer
# Layers of abstraction => request for a book, return a book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available books :")
        for book in self.availableBooks:
            print(book)

    def LendaBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print ("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)

        else:
            print ("Sorry, your book is not available in our library")



    def addaBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print ("You have reuturned the book successfully")



class Cutomer:

  def requestBook(self):
       print ("Enter the name of the book which you like to borrow:")
        self.book = input()
        return self.book

    def returnBook(self):
        print ("Enter the name of the book you want to return")
        self.book = input()
        return self.book


LibraryIT = Library([
    'Machine Learning basics', 'OOP with Python', 'Java Basics', 'Web development with Django and Falsk',
    'Building Algorithms', 'Cyber security', 'Computer engineering', '3D game development with Unity', 'Javascript basics'
])

customer = Cutomer()

while true:
    print ("Enter 1 to show all books at IT library")
    print("Enter 2 to lend a book")
    print ("Enter 3 to return a book")
    print ("Enter 4 for exit")

    userInput = int(input())
    if userInput == 1:
        LibraryIT.displayAvailableBooks()

    elif userInput == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)

    elif userInput == 3:
        returnBook = customer.returnBook()
        library.addBook(returnedBook)

    elif userInput == 4:
        quit()



