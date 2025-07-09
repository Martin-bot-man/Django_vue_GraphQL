# 📝 Django + Vue + GraphQL Blog App

A full-stack blog application built with **Django** (backend), **GraphQL** (API), and **Vue.js** (frontend). This project showcases how to combine modern technologies to create a performant, modular, and interactive web application.

---

## 📚 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Author](#author)

---

## 🚀 About the Project

This is a simple, full-stack blog application where users can:
- Read blog posts
- Create, update, and delete their own posts (if authenticated)
- Interact with the API via GraphQL queries and mutations

The backend is powered by Django and **Graphene-Django** for a GraphQL API. The frontend uses **Vue.js** to consume this API and render a dynamic, interactive user experience.

---

## ✨ Features

- Full CRUD operations on blog posts
- GraphQL API with custom queries and mutations
- JWT-based authentication
- Responsive and reactive frontend with Vue.js
- Modern, clean UI
- Developer-friendly project structure

---

## 🛠️ Tech Stack

**Frontend:**
- [Vue.js](https://vuejs.org/) (Composition API)
- [Axios](https://axios-http.com/) for HTTP requests
- [Vue Apollo](https://v4.apollo.vuejs.org/) (if used)

**Backend:**
- [Django](https://www.djangoproject.com/)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
- [Django REST Framework](https://www.django-rest-framework.org/) (optional)
- [Django CORS Headers](https://pypi.org/project/django-cors-headers/)
- JWT Authentication

---

## ⚙️ Installation & Setup

### Backend (Django)

```bash
# Clone the repository
git clone https://github.com/yourusername/django_vue_graphql_blog.git
cd django_vue_graphql_blog/backend

# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

