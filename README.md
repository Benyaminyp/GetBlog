# GetBlog

**GetBlog** is a simple and functional blog application built with the Django framework. It supports user authentication, blog post management, category filtering, and includes a fully-featured admin panel.

## Features

- User registration, login, and logout
- Create, edit, and delete blog posts
- Categorize posts by topic
- Admin panel using Django's built-in admin
- Clean and minimal user interface
- Organized project structure for easy maintenance

## Prerequisites

- Python 3.x (recommended: Python 3.10+)
- `pip` package manager
- (Optional) `virtualenv` for managing virtual environments

## Installation (Windows)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Mohammadparsa1384/GetBlog.git
   cd GetBlog
 GetBlog


2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application in your browser**:

   * Home page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

```text
GetBlog/
├── accounts/       # Handles user authentication and profiles
├── blog/           # Manages blog posts and categories
├── dashboard/      # User/admin dashboard components
├── templates/      # HTML templates for rendering views
├── static/         # Static files (CSS, JS, images)
├── media/          # Uploaded user content
├── manage.py       # Django’s command-line utility
└── requirements.txt # Project dependencies
```
Contributing
Contributions are welcome! To contribute:

Fork the repository.

Create a new branch: git checkout -b your-feature-name

Make your changes and commit: git commit -m "Add your feature"

Push to your fork: git push origin your-feature-name

Open a Pull Request

## Developers
[Mohammadparsa1384](https://github.com/Mohammadparsa1384) – Developer

[ArmanBahriSource](https://github.com/ArmanBahriSource) – Developer

[Benyaminyp](https://github.com/Benyaminyp) – Developer


