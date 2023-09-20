
searched_book = input()
current_search = ""
books_checked = 0

while current_search != searched_book:
    current_search = input()

    if current_search == searched_book:
        print(f"You checked {books_checked} books and found it.")

    if current_search == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break
    books_checked += 1
