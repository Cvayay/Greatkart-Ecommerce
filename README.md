# Greatkart-Ecommerce

Greatkart is a Django-based e-commerce demo project that implements categories, products, carts, orders, user accounts and admin management.

## Quick overview
- Django 3.2 (project tested on Python 3.12)
- Apps: `accounts`, `store`, `carts`, `orders`, `category`
- Uses local `media/` for uploads and `static/` for assets

## Requirements
Install dependencies in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Environment
Create a `.env` file at the project root (not committed). Required entries:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

`SECRET_KEY` must be kept secret for production. `.env` is listed in `.gitignore` by default.

## Database setup and run
```powershell
#. apply migrations
.\.venv\Scripts\python manage.py migrate

#. create admin user
.\.venv\Scripts\python manage.py createsuperuser

#. run development server
.\.venv\Scripts\python manage.py runserver
```

## Running checks
- Apply migrations: `python manage.py migrate`
- Run server: `python manage.py runserver`

## Project structure (high-level)
- `greatkart/` — project settings and URLs
- `accounts/` — custom user model and profile
- `store/` — products, variations, galleries
- `carts/` — shopping cart and items
- `orders/` — order models and views
- `templates/` — HTML templates

## Notes & next steps
- We added a local stub `admin_thumbnails.py` to avoid a dependency conflict; replace or remove as needed.
- Secrets should never be committed. Keep `.env` out of version control.

If you'd like, I can expand this README with screenshots, endpoints, and example environment tokens.