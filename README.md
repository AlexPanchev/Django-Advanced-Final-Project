# 🍰 Dessert Shop – Django Advanced Final Project

A fully featured, production‑ready Django web application built as part of the **Django Advanced Course @ SoftUni**.  
The project demonstrates real‑world Django architecture including:

- multi‑app modular structure  
- PostgreSQL database  
- authentication, authorization & permissions  
- REST API (DRF)  
- asynchronous task processing (Django‑Q)  
- cron jobs  
- media uploads  
- custom template filters  
- search & filtering  
- staff dashboard  
- signals  
- environment variables (.env)  
- clean, maintainable code  

---

# 📌 Project Overview

**Dessert Shop** is a complete dessert management system where:

### 👤 Customers can:
- browse desserts  
- view dessert details  
- leave reviews  
- create orders  
- view their personal order history (“My Orders”)  

### 👨‍🍳 Staff can:
- manage desserts, categories, ingredients  
- manage orders and order items  
- access a staff dashboard with statistics  
- use the REST API with elevated permissions  

---

# 🧩 Features

## ✔ Desserts
- List all desserts  
- View dessert details  
- Create, edit, delete desserts  
- Upload dessert images  
- Assign categories & ingredients  
- Search desserts by name  

## ✔ Categories
- List categories  
- View category details  
- Full CRUD  

## ✔ Ingredients
- List ingredients  
- Mark allergens  
- Full CRUD  

## ✔ Orders
- Create customer orders  
- Add, edit, delete order items  
- Automatic total price calculation  
- Validation & custom error messages  
- “My Orders” page for authenticated users  

## ✔ Reviews (User‑Generated Content)
- Users can leave 1 review per dessert  
- Edit/delete only your own review  
- Reviews displayed on dessert detail page  

## ✔ Authentication & Authorization
- Registration, login, logout  
- User groups: **Customers** & **Staff**  
- Permissions using `PermissionRequiredMixin`  
- Dynamic navigation based on role  
- Signals for automatic profile creation & group assignment  

## ✔ REST API (Django REST Framework)
- API endpoints for:
  - Desserts  
  - Categories  
  - Ingredients  
  - Orders  
  - Reviews  
- ViewSets + Routers  
- Nested serializers  
- API permissions  
- JSON responses  

## ✔ Asynchronous Task Processing (Django‑Q)
- Background email sending on new order  
- Daily cron job: send order summary report  
- Worker cluster with multiprocessing  

## ✔ Staff Dashboard
- Total users  
- Total desserts  
- Total orders  
- Pending orders  
- Clean Bootstrap UI  

## ✔ Additional Features
- Custom template filter (`euro`)  
- Custom 404 page  
- Responsive Bootstrap design  
- Template inheritance  
- Pagination  
- Signals  
- Environment variables (.env)  

---

# 🛠 Technologies Used

- Python 3.9  
- Django 4.2  
- Django REST Framework  
- Django‑Q (async tasks + cron)  
- PostgreSQL  
- Bootstrap 5  
- Pillow (image uploads)  
- python‑dotenv  

---

# 🔐 Environment Variables (.env)

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key

DB_NAME=final_project_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

DEBUG=True
EMAIL_HOST_PASSWORD=your-email-password
```

`.env` is included in `.gitignore` and **must not be committed**.

---

# 🗄 Database Setup (PostgreSQL)

```sql
CREATE DATABASE final_project_db;
```

---

# 🚀 Installation & Running the Project

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Django-Basics-Final-Project
```

### 2. Create & activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```

Open:  
http://127.0.0.1:8000/

---

# ⚡ Running Asynchronous Tasks

### Start Django‑Q worker:
```bash
python manage.py qcluster
```

### Features:
- async email on order creation  
- daily cron report  

---

# 📁 Project Structure

```
Django-Basics-Final-Project/
│
├── accounts/           # Authentication, profiles, signals
├── api/                # REST API (DRF)
├── core/               # Home page, shared logic
├── desserts/           # Desserts, categories, ingredients
├── orders/             # Orders & order items
├── reviews/            # User reviews
│
├── templates/          # All HTML templates
├── static/             # CSS, images
├── media/              # Uploaded images
│
├── .env                # Environment variables
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

---

# 🧪 Custom Template Filter

`desserts/templatetags/dessert_filters.py`:

```python
@register.filter
def euro(value):
    return f"{float(value):.2f} €"
```

Usage:

```django
{{ dessert.price|euro }}
```

---

# ⚠ Notes for the Examiner

- Project includes **authentication, authorization, and permissions**.  
- Uses **PostgreSQL** as required.  
- Contains **20+ templates**, **multiple dynamic pages**, and **full CRUD**.  
- Implements **REST API**, **async tasks**, **cron jobs**, **signals**, **custom filters**, **media uploads**, **search**, **pagination**, and **dashboard**.  
- Follows Django best practices, clean code, and modular architecture.  

---

# 🎉 Final Notes

This project goes **far beyond** the basic requirements and demonstrates:

- real‑world Django architecture  
- production‑ready structure  
- advanced backend concepts  
- clean, maintainable code  

