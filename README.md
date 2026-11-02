# 🎬 Movie Database API

### 🍿 A simple Movie Database API built with Python, FastAPI, and SQLite.

## 📌 About The Project

This project is a simple **Movie Database API** developed using Python and SQLite.

It allows users to manage movie information through a RESTful API built with FastAPI.

Each movie contains information such as its title, IMDb rating, release year, country, and image URL.

The main purpose of this project is to practice database operations and API development using Python.

## ✨ Features

- 🎥 Add new movies to the database.
- 📋 Retrieve all movie records.
- 🔍 Search for a movie by its ID.
- ⭐ Store IMDb ratings.
- ✏️ Update movie information by ID.
- 🗑️ Delete movies by ID.
- 🖼️ Store movie poster URLs or image paths.
- 🌐 Create and test API endpoints.
- 📡 Send HTTP requests using the Requests library.

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| 🐍 Python | Main programming language |
| ⚡ FastAPI Offline | API development |
| 🗄️ SQLite3 | Database management |
| 📡 Requests | Sending HTTP requests |
| 🚀 Uvicorn | Running the API server |

## 📂 Project Structure

```text
Fastapi_Project/
│
├── src2/
│   ├── api.py
│   ├── database.py
│   └── call_api_db.py
│
├── MoviesData.db
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Install the required packages**

```bash
pip install fastapi-offline requests uvicorn
```

**3. Navigate to the project folder**

```bash
cd src2
```

**4. Run the API server**

```bash
uvicorn api:app --reload
```

## 🔗 API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/getmovies/` | Get all movies |
| POST | `/addmovie/` | Add a new movie |
| DELETE | `/deleteid?id={id}` | Delete a movie by ID |
| PUT | `/updatemovie?id={id}` | Update a movie by ID |

## 📖 API Documentation

After starting the server, open the following URL in your browser to explore and test the API endpoints:

🌐 **Swagger Documentation:**

http://127.0.0.1:8000/docs

## 🗃️ Database Structure

The project uses an SQLite database named `MoviesData.db`.

The `movies` table contains the following fields:

| Column | Data Type | Description |
|---|---|---|
| `id` | INTEGER | Unique movie ID |
| `title` | TEXT | Movie title |
| `imdb_rate` | REAL | IMDb rating |
| `year` | TEXT | Release year |
| `country` | TEXT | Movie country |
| `image` | TEXT | Movie image URL or path |

## 🎯 Project Goals

Through this project, I practiced:

- Working with SQLite databases.
- Writing SQL queries.
- Implementing CRUD operations.
- Building REST APIs with FastAPI.
- Sending HTTP requests using Python Requests.
- Connecting a Python application to a database.

---

### 💻 Developed with Python ❤️

⭐ If you find this project interesting, feel free to explore the code!
