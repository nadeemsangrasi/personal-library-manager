
# 📚 Personal Library Manager

The **Personal Library Manager** is a Python-based console application that allows users to manage their personal book collection. It provides functionalities to add, remove, search, and display books, along with statistics on the library's contents.

---

## 🚀 Features

✅ Add new books with details like title, author, publication year, genre, and status  
✅ Remove books by title  
✅ Search for books by title or author  
✅ Display all books in the library  
✅ View library statistics (total books and percentage of read books)  
✅ Simple user-friendly console interface  

---

## 🏗️ Project Structure
```
personal_library_manager/
├── config.py
├── main.py
└── README.md
```

---

## 📂 Configuration
The `config.py` file contains helper functions for:
- `load_books()` – Loads existing books from a data source.
- `add_data()` – Adds new book data to the collection.
- `validate_string()` – Validates input strings.
- `validate_integer()` – Validates input integers.
- `check_status()` – Checks the book status (read/unread).

---

## 🛠️ Installation
1. **Clone the repository:**
```bash
git clone https://github.com/your-username/personal-library-manager.git
```

2. **Navigate to the project folder:**
```bash
cd personal-library-manager
```

3. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 💡 Usage

To start the Personal Library Manager, run:
```bash
python main.py
```

### ➡️ Options:

1. **Add a book** – Add a new book with details  
2. **Remove a book** – Remove a book by title  
3. **Search for a book** – Search for a book by title or author  
4. **Display all books** – Show a list of all books  
5. **Display statistics** – Show total books and read percentage  
6. **Exit** – Exit the program  

---

## 🚦 Input Validation

- Book title, author, genre, and status require valid non-empty strings.  
- Publication year must be a valid integer.  
- Status must be either `"yes"` or `"no"`.  

---

## 🏆 Example
```bash
Welcome to Personal Library Manager
######################################

1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit

Perform desired action from 1 to 6 e.g.(1): 1
Book Title: Clean Code
Book Author: Robert C. Martin
Book Publication: 2008
Book Genre: Programming
Book Status (yes/no): yes

Book added successfully!
```

---

## 🚧 Error Handling

- Invalid inputs are handled with custom `ValidationError` exceptions.  
- Appropriate error messages are shown for incorrect inputs.  

---

## 📝 Contributing

Feel free to contribute by opening issues or submitting pull requests.

---

## 📄 License

This project is licensed under the **MIT License**.

---

👨‍💻 Developed with ❤️ by [Nadeem Khan](https://github.com/nadeemsangrasi)
```

This version should work without any markdown rendering issues. 👍
