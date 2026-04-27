# ShortLink

ShortLink is a modern URL shortener web application built with Flask and SQLite. It allows users to convert long URLs into short, shareable links, optionally create custom aliases, track click counts, and manage all generated links through a simple dashboard and analytics page.

## Features

- Shorten long URLs into compact links
- Create custom short aliases
- Redirect short links to original URLs
- Track click counts
- View all created links in a dashboard
- Basic analytics for total links and total clicks
- Clean and responsive user interface
- SQLite-based persistent data storage

## Tech Stack

**Backend**

- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Migrate

**Database**

- SQLite

**Frontend**

- HTML
- CSS
- Jinja2 Templates

**Testing**

- Pytest

## Project Structure

```bash
ShortLink/
├── app.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_app.py
├── instance/
│   └── app.db
└── urlshortener/
    ├── __init__.py
    ├── config.py
    ├── extensions.py
    ├── forms.py
    ├── models.py
    ├── routes.py
    ├── services.py
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── favicon.svg
    └── templates/
        ├── base.html
        ├── index.html
        ├── result.html
        ├── dashboard.html
        ├── analytics.html
        └── 404.html
```
