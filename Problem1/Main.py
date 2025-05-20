from BookRent import BookRent
from People import People
from Book import Book


Book1 = Book(1, 'Teszt Title', 'Teszt author', 2000, 123445)
Book2 = Book(2, 'Teszt Title', 'Teszt author', 1994, 123678)

member = People(1, 'Teszt member', 'teszt@gmail.com')

book_rent = BookRent(People, Book1, '2025-05-31')
