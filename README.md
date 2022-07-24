# djangoTask

Update project per [https://docs.djangoproject.com/en/4.0/intro/tutorial01/](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

In head project:
- `urls.py`
  - add `path('todo/', include('djangoTask.urls')),` (or whatever path you prefer)
- `settings.py`
  - add to `INSTALLED_APPS` the content `'djangoTask.apps.DjangotaskConfig',`
- [Update database](https://docs.djangoproject.com/en/4.0/intro/tutorial02/):
  - `python manage.py makemigrations djangoTask` (create new *migration*)
  - `python manage.py sqlmigrate djangoTask 0001` (view sql for migration. revise last argument to match whatever was generated)
  - `python manage.py migrate` (execute)


# Todo
[ ] make formatting cooler
  - bootstrap theme (themes are expensive - diy garbage)
  - [ ] dark mode (option later.  Fine right now)
  - dropdown "new menu" in index
  - navigation bar
[ ] about page
[ ] add history log
    - date changed
    - old value
    - new value
[ ] add delete button (changes status to 'deleted')
[ ] add 'comment' field
[ ] add 'complete' button
  - changes status to 'completed'
  - prompts user for message that will be added to "comment"
[ ] add attachment
  - if picture, display
[ ] metrics
  - tasks overdue
[ ] export/import tasks
