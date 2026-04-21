# ShortLink

A modern URL shortener built with **Python, Flask, and SQLite**.  
LinkSleek lets users create short links from long URLs, use custom aliases, track clicks, and manage links from a dashboard.

---

## Features

- Shorten long URLs into shareable links
- Custom alias support
- Automatic redirection to original URL
- Click tracking
- Dashboard to view all created links
- Analytics page for total links and clicks
- Persistent SQLite database storage
- Clean and responsive UI

---

## Tech Stack

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Migrate

**Frontend**
- HTML
- CSS
- Jinja2 Templates

**Database**
- SQLite

**Testing**
- Pytest

---

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
