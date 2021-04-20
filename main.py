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
    print_menu()
    list_book = []
    with open('books.csv', 'r+') as book_file:
        while user_input != "Q":
            user_input = input(">>>").upper()
            if user_input == "L":
                for i in list_of_books(book_file):
                    list_book.append(i)
                for j in list_book:
                    print("{:<40} by {:<18} {:>5} pages".format(j[0], j[1], j[2]))
            elif user_input == "A":
                pass
            elif user_input == "M":
                pass
            elif user_input not in CHOICES:
                print("Invalid menu choice.")
        quit_program()


def list_of_books(csv_file):
    book_list = csv.reader(csv_file)
    books = []
    for row in book_list:
        books.append(row)
    return books


def print_menu():
    print("Menu:\n L - List all books\n A - Add new book \n M - Mark book as completed\n Q - Quit")


def quit_program():
    print("Bye")


if __name__ == '__main__':
    main()
