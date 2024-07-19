# Django Blog Project

This is a simple blog application built with Django. It allows users to create, edit, and delete blog posts, as well as add comments to posts.

## Features

- User authentication
- Create, edit, delete blog posts
- Add comments to posts
- Approve or remove comments

## Requirements

- Python 3.6+
- Django 3.2+
- SQLite (default) or any other relational database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/stolbikova/blog.git
   cd blog
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser:

   ```
   python manage.py createsuperuser

   ```

6. python manage.py runserver

## Testing

    python manage.py test
