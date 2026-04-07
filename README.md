# 🍰 Dessert Shop – Django Advanced Final Project

A fully featured, production‑ready Django web application built for the **Django Advanced Course @ SoftUni**.  
The project demonstrates real‑world backend architecture, modular design, REST APIs, asynchronous processing, background tasks, permissions, and clean, maintainable code.

---

## 🌐 Live Demo

🔗 **https://dessertshop-h0hwemhhbjgzcgas.spaincentral-01.azurewebsites.net/**

---

# 📌 Project Overview

**Dessert Shop** is a complete dessert management platform where customers can browse desserts, place orders, leave reviews, and manage their profiles — while staff members can manage the entire catalog, orders, and ingredients through a permission‑based admin interface.

The project includes:

- Full CRUD for Desserts, Categories, Ingredients  
- Customer order system with Order Items  
- Review system (1 review per user per dessert)  
- Staff dashboard  
- REST API (DRF)  
- Asynchronous tasks (Django‑Q)  
- Cloud deployment (Azure App Service)  
- PostgreSQL database  
- Cloudinary media storage  
- Authentication, authorization, permissions  
- Custom template filters  
- Signals  
- Pagination, search, responsive UI  
- 25+ automated tests  

---

# 🧩 Features

## 🍰 Desserts
- List all available desserts  
- Dessert details page  
- Create / edit / delete desserts (staff only)  
- Upload dessert images  
- Assign categories & ingredients  
- Search desserts by name  
- Pagination  

## 🗂 Categories
- List categories  
- Category details  
- Full CRUD (staff only)  

## 🧾 Ingredients
- List ingredients  
- Mark allergens  
- Full CRUD (staff only)  

## 🛒 Orders
- Customers can create orders  
- Add / edit / delete order items  
- Automatic total price calculation  
- Custom validation  
- “My Orders” page  
- Staff can manage all orders  

## ⭐ Reviews (UGC)
- One review per dessert per user  
- Edit/delete only your own review  
- Reviews displayed on dessert detail page  

## 🔐 Authentication & Authorization
- Registration, login, logout  
- Profile page & profile editing  
- Two user groups: **Customers** & **Staff**  
- Permissions via `PermissionRequiredMixin`  
- Dynamic navigation based on role  
- Signals for automatic profile creation  

## 📡 REST API (DRF)
- Endpoints for desserts, categories, ingredients, orders, reviews  
- ViewSets + Routers  
- Nested serializers  
- Permission classes  
- JSON responses  

## ⚡ Asynchronous Processing (Django‑Q)
- Background email sending on new order  
- Daily cron job: order summary report  
- Worker cluster with multiprocessing  

## 📊 Staff Dashboard
- Total users  
- Total desserts  
- Total orders  
- Pending orders  
- Clean Bootstrap UI  

## 🧰 Additional Features
- Custom template filter (`euro`)  
- Custom 404 page  
- Responsive Bootstrap design  
- Template inheritance  
- Signals  
- Environment variables (`.env`)  

---

# 🔑 User Roles & Permissions

## 👤 Customers
- Browse desserts  
- Create orders  
- Leave reviews  
- Access “My Orders”  

## 👨‍🍳 Staff
- Full CRUD for desserts, categories, ingredients  
- Manage orders  
- Access staff dashboard  
- Extended API permissions  

## 🔔 Automatic Group Assignment
A Django signal assigns new users to the **Customers** group and creates a Profile.

---

# 📡 API Documentation

**Base URL:** `/api/`

## Available Endpoints
- `/desserts/`
- `/categories/`
- `/ingredients/`
- `/orders/`
- `/reviews/`

## Authentication
- Session authentication  
- Staff users have elevated permissions  

## Response Format
- JSON  

---

# 🛠 Technologies Used

- Python 3.9  
- Django 4.2  
- Django REST Framework  
- Django‑Q (async tasks + cron)  
- PostgreSQL  
- Bootstrap 5  
- Pillow  
- python‑dotenv  
- Cloudinary (media storage)  
- Azure App Service  

---

# 🔐 Environment Variables (.env)

Create a `.env` file in the project root:

```env
SECRET_KEY=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

DEBUG=

EMAIL_HOST_PASSWORD=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
