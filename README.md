<h1 align="center">📚 Library Management System — Django REST API</h1>

<p align="center">
  <strong>A powerful and modular backend API for managing libraries, books, members, and transactions.</strong>
</p>

<p align="center">
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white"/></a>
  <a href="https://www.django-rest-framework.org/"><img src="https://img.shields.io/badge/DRF-3.16+-ff1709?style=for-the-badge&logo=django&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Docs-Swagger-brightgreen?style=for-the-badge&logo=swagger"/></a>
</p>

---

## 🧩 Overview

**Library Management System (LMS)** is a backend API built with **Django REST Framework (DRF)**.  
It helps libraries manage **books, authors, members, borrowing, and returning transactions** in a simple yet powerful way.  
Authentication is handled using **JWT tokens (Djoser)** and the project includes **Swagger API documentation** for developers.

---

## ✨ Features

- 📖 **Book & Author Management**  
- 👤 **Member Management**  
- 🔄 **Borrowing / Returning System**   
- 📘 **Interactive Swagger API Docs**  
- ⚙️ **Scalable RESTful Architecture**

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5 + Django REST Framework |
| **Authentication** | Djoser + JWT |
| **Database** | SQLite / PostgreSQL |
| **API Docs** | drf_yasg (Swagger & ReDoc) |
| **Language** | Python 3.11+ |

---

## 📁 Project Structure

Library_Management_System/
│
├── manage.py
├── myproject/ # Main project config
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── api / #Book,Author,Member,Category,Borrow Date Management 
│
└── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/fardin-05/Library_Management_System.git
cd phimart
```
### 2️⃣ Create Virtual env
```bash
Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
```
### 3️⃣Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply migrations
```bash
python manage.py migrate
```
### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```
### 6️⃣ Run the development server
```bash
python manage.py runserver
```
### Now open your browser at : 
```bash
http://127.0.0.1:8000/
```
---

### 🧾 API Documentation

**Library Management includes interactive API documentation generated via drf_yasg.**




| Tool | URL |
| ----------- | ----------- |
| Swagger | http://127.0.0.1:8000/swagger/ |
| ReDoc | http://127.0.0.1:8000/redoc/ |

---




### 🧪 Example Environment Variables

**Create a .env file in the root directory:**
```
ini

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### 📄 License
---

This project is licensed under the MIT License — feel free to use and modify it.

---

### Author

**Fardin Khan**

*Django Backend Developer*

📧 fardinazim7@gmail.com

🌐 https://fardin-05.github.io


⭐ If you like this project, consider giving it a star on GitHub!
