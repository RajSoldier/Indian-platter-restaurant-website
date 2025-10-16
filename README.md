# Indian Platter Restaurant (Django)

A Django web app for an Indian restaurant with menus, events, and feedback.

## Quick start
1) Create and activate a virtual environment
   python -m venv .venv
   .venv\Scripts\activate

2) Install dependencies
   pip install -r requirements.txt

3) Apply migrations and run
   python manage.py migrate
   python manage.py runserver

## Project layout
- Django project: hello/
- App: home/
- Templates: home/templates/
- Static files: static/
- Media uploads: media/

## Notes
- Do not commit db.sqlite3 or media/ (already in .gitignore).
- Add your secrets via environment variables or a .env (ignored).
