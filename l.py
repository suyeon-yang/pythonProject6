"""
Replace the contents of this module docstring with your own details
Name: Suyeon Yang
Date started: 17 April 2021
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---reading-tracker-suyeon-yang
"""

import csv

CHOICES = ["L", "A", "M", "Q"]


def main():
    """..."""
    print("Reading Tracker 1.0 - by Suyeon Yang")
    user_input = ""
    list_book = []
    print_menu()
    with open('books.csv', 'r+') as book_file:
        while user_input != "Q":
            user_input = input(">>>").upper()
            if user_input == "L":
                for i in list_of_books(book_file):
                    list_book.append(i)
                a = 0
                for j in list_book:
                    a += 1
                    print("{}. {:<40} by {:<18} {:>5} pages".format(a, j[0], j[1], j[2]))
                print_menu()
            elif user_input == "A":
                for i in list_of_books(book_file):
                    list_book.append(i)
                book_title, book_author, book_pages = user_input_validation()
                list_book.append(add_book(book_author, book_title, book_pages))
                print_menu()
            elif user_input == "M":
                pass
            elif user_input not in CHOICES:
                print("Invalid menu choice.")
        quit_program()


def print_menu():
    print("Menu:\n L - List all books\n A - Add new book \n M - Mark book as completed\n Q - Quit")


def list_of_books(csv_file):
    book_list = csv.reader(csv_file)
    books = []
    for row in book_list:
        books.append(row)
    return books


def user_input_validation():
    book_title = input("Title: ")
    while book_title == "":
        print("Input can not be blank")
        book_title = input("Title: ")
    book_author = input("Author: ")
    while book_author == "":
        print("Input can not be blank")
        book_author = input("Author: ")
    while True:
        try:
            book_pages = int(input("Pages: "))
            assert book_pages > 0
            break
        except ValueError:
            print("Invalid input; enter a valid number")
        except AssertionError:
            print("Number must be > 0")

    return book_title, book_author, book_pages


def add_book(book_title, book_author, book_pages):
    user_added_book = [book_title, book_author, book_pages]
    return user_added_book


def quit_program():
    pass


if __name__ == '__main__':
    main()

