# 🎵 Music Recommender System

A **Python-based music recommendation system** that analyzes user purchase patterns and provides personalized music recommendations.

---

## 📂 Project Structure

| File / Folder         | Description                          |
|----------------------|--------------------------------------|
| `main.py`            | Main application entry point          |
| `music_data.py`      | Data models and storage functions     |
| `queries.py`         | Recommendation query engine           |
| `tests/`             | Comprehensive test suite              |
| `tests/__init__.py`  | Test package initialization           |
| `tests/test_music_data.py` | Unit tests for data models       |
| `tests/test_queries.py`    | Unit tests for query engine       |
| `README.md`          | Project documentation                 |

---

## ⚙️ How It Works

This system consists of **two main components**:

### 1️⃣ Data Management
- **Users:** Stores demographic info (age, city) and purchased albums  
- **Albums:** Complete info including name, artist, genre, and track count  

### 2️⃣ Query Engine
The system analyzes user purchase patterns using queries:  
- By user & artist  
- By user & genre  
- By age group & artist  
- By age group & genre  
- By city & artist  
- By city & genre  

---

## 🛠 Technical Implementation

**Performance Optimizations:**  
- Uses **Generator Expressions** for memory-efficient processing  
- Utilizes **dictionary data structures** for O(1) data access  
- **Modular design** for separation of concerns  

---

## 💻 Example Execution


```text
=== Music Recommender Menu ===

1. Add a new user
2. Add a new album
3. Query by user & artist
...
Choose an option: 2

Album name: The Dark Side of the Moon
Artist: Pink Floyd
Genre: Progressive Rock
Number of tracks: 10

Album 'The Dark Side of the Moon' added.

Choose an option: 1

Username: john_doe
Age: 28
City: New York
Enter purchased albums (comma separated, e.g., album1:2,album2:1): dark_side:2,wish_you_were_here:1

User 'john_doe' added.

Choose an option: 3

Username: john_doe
Artist: Pink Floyd

john_doe purchased 25 tracks by Pink Floyd.
```

---

## 🌟 Key Technical Features

- Implementation of **functional programming** concepts  
- Comprehensive **unit testing**  
- **Modular & extensible design**  
- Interactive **command-line interface**  
- Efficient data processing using **generators**  

> This project not only implements a practical recommendation system but also demonstrates advanced Python techniques and software engineering principles.
