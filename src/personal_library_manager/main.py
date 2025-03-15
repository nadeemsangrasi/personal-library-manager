from typing import Union
import random
from personal_library_manager.config import load_books, add_data,validate_string,validate_integer,check_status

class ValidationError(Exception):
    pass

def main() -> None:
    books: list[dict[str, Union[str, int, bool]]] = load_books()
    isExit = False

    def add_book():
        print("")
        print("Add book...!")
        print("")
        try:
            random_id = random.randint(1111, 2222)
            book_name = validate_string(input("Book Title:\t"), "please enter valid book title")
            book_author = validate_string(input("Book Author:\t"), "please enter valid book author")
            book_publication = validate_integer(input("Book Publication:\t"), "please enter valid book publication e.g(2025,2024)")
            book_genre = validate_string(input("Book Genre:\t"), "please enter valid book genre")
            book_status = check_status(validate_string(input("Book Status e.g(yes/no):\t"), "please enter valid book status"))
            book = {"id": random_id, "title": book_name, "author": book_author, "publication": book_publication, "genre": book_genre, "status": book_status}
            books.append(book)
            add_data(books)
            print("Book added successfully...!")
            print("")
            moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
            if moreAction:
                main()
        except ValidationError:
            return False

    def remove_book():
        print("")
        print("Remove Book...!")
        print("")
        try:
            if len(books)==0:
                print("No books found please add books first")
                print("")
                moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                if moreAction:
                    main()
                return
            isRemovedBook=False
            title = validate_string(input("Enter book title to remove...!\t"),"please enter valid book title")
            for index in range(len(books)):
                if books[index]["title"]==title:
                    isRemovedBook=True
                    books.pop(index)
                    add_data(books)
                    print("Book removed successfully...!")
                    print("")
                    moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                    if moreAction:
                        main()
                    return
            if not isRemovedBook:
                print("Book not found...!")

            print("")
            moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
            if moreAction:
                main()
        except ValidationError:
            return False
    def search_book():
        print("")
        print("Search for a book...!")
        print("")
        try:
            if len(books)==0:
                print("No books found please add books first")
                print("")
                moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                if moreAction:
                    main()
                return
            isFound=True
            book_title_or_author = validate_string(input("Enter book by title and author :\t"), "please enter valid author name")
            for book in books:
                if book["title"] == book_title_or_author or book["author"] == book_title_or_author:
                    isFound=False
                    print(f"""id : {book["id"]}\ntitle : {book["title"]}\nauthor : {book["author"]}\npublication : {book["publication"]}\ngenre : {book["genre"]}\nstatus : {book["status"]} """)
                    print("")
                    moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                    if moreAction:
                        main()
                    return
            if isFound:
                print("Book not found...!")
                print("")
            moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
            if moreAction:
                main()
        except ValidationError:
            return False
    def display_books():
        print("")
        print("All books...!")
        print("")
        try:
            if len(books)==0:
                print("No books found please add books first")
                print("")
                moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                if moreAction:
                    main()
                return
            for book in books:
                print(f"""Id : {book["id"]}\nTitle : {book["title"]}\nAuthor : {book["author"]}\nPublication : {book["publication"]}\nGenre : {book["genre"]}\nStatus : {book["status"]} 
""")
            print("")
            moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
            if moreAction:
                main()
        except ValidationError:
            return False
    def display_statistics():
        print("")
        print("Statistics...!")
        print("")
        try:
            if len(books)==0:
                print("No books found please add books first")
                print("")
                moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
                if moreAction:
                    main()
                return
            total_books = len(books)
            readed_books = len(set(book["status"] for book in books))
            print(f"Total books: {total_books}")
            print(f"Readed books Percentage: {round(readed_books/total_books*100)}%")
            print("")
            moreAction = check_status(validate_string(input("Want to continue? (yes,no)...!\t"),"please enter valid action"))
            if moreAction:
                main()
        except ValidationError:
            return False
        
    def exitLibrary():
        nonlocal isExit
        isExit = True

    options = [
        {"index": 1, "title": "Add a book", "action": add_book},
        {"index": 2, "title": "Remove a book", "action": remove_book},
        {"index": 3, "title": "Search for a book", "action": search_book},
        {"index": 4, "title": "Display all books", "action": display_books},
        {"index": 5, "title": "Display statistics", "action": display_statistics},
        {"index": 6, "title": "Exit", "action": exitLibrary},
    ]

    def display_options():
        for item in options:
            print(f"""{item["index"]} {item["title"]}""")

    while not isExit:
        print(100 * "#")
        print("")
        print(f" Welcome to Personal Library Manager")
        print("")
        print(100 * "#")
        print("")
        display_options()
        print("")
        try:
            choice = int(validate_integer(input("Perform desired action from 1 to 6 e.g(1)\t"),"please enter valid number"))
            match choice:
                case 1:
                    if not options[choice - 1]["action"]():
                        break
                case 2:
                    if not options[choice - 1]["action"]():
                        break
                case 3:
                    if not options[choice - 1]["action"]():
                        break
                case 4:
                    if not options[choice - 1]["action"]():
                        break
                case 5:
                    if not options[choice - 1]["action"]():
                        break
                case 6:
                    if not options[choice - 1]["action"]():
                        break
        except ValidationError:
            print("Please enter valid action")
        except Exception:
            isExit = True

if __name__ == "__main__":
    main()