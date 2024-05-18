#Write a library class with no_of_books as two instance variables.
#Write a program to create a library class and show how you can print all books.
#Add a book, and get the number of books using diffrent methods.
#Show that your program doesn't persist the books after the program is stopped.
class Library:
    def __init__(self):
        self.no_Books = 0
        self.Books = []
    def addbook(self,Book):
        self.Books.append(Book)
        self.no_Books = len(self.Books)
    def showinfo(self):
        print(f"The library has {self.no_Books} books. The books are")
        for Book in self.Books:
           print(Book)
l1 = Library()
l1.addbook("The Ministry of utmost happiness")
l1.addbook("The Kite Runner")
l1.addbook("War and Peace")
l1.showinfo()


    