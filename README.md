# AI Hub Backend

This repository contains a minimal Django backend for creating ChatGPT assistants.

## Setup

1. Install Python 3.11+ and Django:
   ```bash
   pip install -r requirements.txt
   ```

2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API exposes a single endpoint to create assistants:

- `POST /assistants/create/` with JSON body `{"name": "Your assistant name", "instructions": "..."}`.

This will create a new assistant entry in the database and return its details as JSON.
