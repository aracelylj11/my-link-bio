# my-link-bio

## Project Overview

A personal link-in-bio page built with Python and Flask. Add, edit, or remove links and share a simple contact page with visitors.

## Features

- Create, update, and delete link cards from the home page.
- View link preview metadata when a URL provides Open Graph tags.
- See a warning after adding a link when a preview cannot be retrieved; cards with incomplete preview metadata are visibly marked.
- Visit `/about` for a short introduction.
- Visit `/contact` to see a contact message and send an email to `hello@example.com`.

## Setup

1. Create and activate a Python virtual environment (optional but recommended).
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in a browser. The contact page is available at `http://127.0.0.1:5000/contact`.

## Dependencies

- `Flask` provides the web application and routes.
- `gunicorn` serves the application in production.
- `requests` retrieves link metadata.
- `beautifulsoup4` parses retrieved Open Graph metadata.
