class Library:
    def __init__(self, listOfBooksk):
        self.books = listOfBooksk

    def displayAvailableBooks(self):
        print("Books present in the library are: ")

        for books in self.books:
            print(books)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"Book {bookName} has been issued. ")
            self.books.remove(bookName)
            return True
        else:
            print("Book already been issued. Wait until the book is returned. ")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book. ")

class Student:
    def requestBook(self):
        self.book = input("Name of book you want to borrow  ")
        return self.book
    
    def returnBook(self):
        self.book = input("Name of book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["DSA", "WAD", "CNS", "M3", "HCI"])
    # centralLibrary.displayAvailableBooks()
    student = Student()

    while(True):
        welcomeMsg = """ ***** Welcome to Central Library ***** 
        Please choose an option:
        1. List of books
        2. Request a book
        3. Return a book
        4. Exit the library"""

        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            centralLibrary.borrowBooks(student.requestBook())
        
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thanks for using this library. ")
            exit()
        
        else:
            print("Invalid choice")
