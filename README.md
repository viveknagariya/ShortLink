ShortLink GitHub Download and Setup Guide

This guide explains how to download the ShortLink project from GitHub and set it up on your computer step by step.

Repository URL
https://github.com/viveknagariya/ShortLink.git


1. Requirements

Before starting, make sure these are installed on your system:

- Python 3.x
- Git
- VS Code or any code editor
- Internet connection

To check Python:
python --version

If python does not work, try:
py --version

To check Git:
git --version


2. Download the Project from GitHub

Open Command Prompt, PowerShell, or VS Code Terminal.

Run this command:
git clone https://github.com/viveknagariya/ShortLink.git

After cloning, move into the project folder:
cd ShortLink


3. Open the Project in VS Code

If you want to open it in VS Code, run:
code .

If the code command does not work, open VS Code manually and choose:
File > Open Folder > ShortLink


4. Create a Virtual Environment

In the terminal, run:
python -m venv venv

If python does not work, use:
py -m venv venv

This will create a virtual environment folder named venv.


5. Activate the Virtual Environment

On Windows:
venv\Scripts\activate

If PowerShell blocks it, run this first:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then activate again:
venv\Scripts\activate

On Mac/Linux:
source venv/bin/activate

After activation, you should see (venv) in the terminal.


6. Install Project Dependencies

Run:
pip install -r requirements.txt

This will install all required packages such as Flask and SQLAlchemy.


7. Run the Project

Start the project using:
python app.py

If needed, you can also use:
py app.py

or:
flask run

If the application starts correctly, you should see something like:
Running on http://127.0.0.1:5000


8. Open the Project in the Browser

Open this URL in your browser:
http://127.0.0.1:5000


9. How to Use the Project

- Enter a long URL on the homepage
- Optionally enter a custom alias
- Generate the short link
- Copy the generated short URL
- Open the short URL to test redirection
- Open Dashboard to view all created links
- Open Analytics to see total links and click information


10. Database Details

This project uses SQLite database.

Database file:
instance/app.db

Important points:
- Data stays saved in the database unless you manually delete it
- Short links remain available as long as their records exist in the database
- If you stop and restart the app, saved data remains available


11. Exact First-Time Setup Commands

Run these commands one by one:

git clone https://github.com/viveknagariya/ShortLink.git
cd ShortLink
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Then open:
http://127.0.0.1:5000


12. Common Problems and Fixes

Problem: python is not recognized
Use:
py -m venv venv
py app.py

Problem: venv activation is blocked in PowerShell
Run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then:
venv\Scripts\activate

Problem: No module named flask
Run:
pip install -r requirements.txt

Problem: Port already in use
Stop the old running server or close the terminal using that port, then run the app again.

Problem: Git is not recognized
Install Git from the official Git website, then restart terminal.


13. Useful Commands

Check Git status:
git status

Activate virtual environment:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run project:
python app.py

Run tests:
pytest


14. Project Summary

ShortLink is a Flask-based URL shortener project built using Python and SQLite.
It allows users to:
- shorten long URLs
- create custom aliases
- track clicks
- manage links from dashboard
- view statistics in analytics

This project is useful for learning Flask, routing, database integration, form validation, and basic web application architecture.


15. Folder Structure Overview

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
    └── templates/


16. Final Note

Whenever you want to use the project again later:

1. Open terminal in the project folder
2. Activate virtual environment
3. Run:
python app.py

Then open:
http://127.0.0.1:5000
