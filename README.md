# 📝 Django + Vue + GraphQL Blog App

Welcome to my full-stack blog project! This is a simple yet powerful blogging platform built using **Django** (for the backend), **GraphQL** (for the API), and **Vue.js** (for the frontend). I built this app to explore modern web technologies and how they can work together seamlessly.

---

## 📖 What’s This All About?

This app lets you:
- Browse blog posts
- Create, edit, and delete your own posts (if you're logged in)
- Interact with a GraphQL API
- Enjoy a fast, smooth, and responsive frontend experience with Vue

It's designed to show how a traditional backend (Django) can be paired with a modern frontend and API layer.

---

## 🧩 What’s Inside?

Here’s what makes this app tick:

### Frontend:
- **Vue.js** – for building a reactive, smooth user experience
- **Axios** – handles HTTP requests to the API
- **Tailwind CSS** (optional) – for quick styling (if used)

### Backend:
- **Django** – the powerful Python web framework
- **Graphene-Django** – lets us use GraphQL with Django
- **JWT Auth** – for secure user authentication

---

## 🛠️ Setting It Up

Here’s how you can get it running locally:

### 🐍 Backend (Django)

```bash
# Clone the repo
git clone https://github.com/yourusername/django_vue_graphql_blog.git
cd django_vue_graphql_blog/backend

# Create a virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
