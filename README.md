# Running CP Topic Locally

This project is built using Django. Follow these steps to set it up and run it on your local machine.

## Prerequisites

- **Python 3.9+** (Download from [python.org](https://www.python.org/downloads/))
- **Git** (Download from [git-scm.com](https://git-scm.com/))
- (Optional) **Virtualenv** or use Python’s built-in `venv` module

## Installation

1. **Clone the repository:**

   Open your terminal and run:

   ```bash
   git clone https://github.com/IbrahimCp/cp-topic.git
   cd cp-topic
   ```

2. **Create and activate a virtual environment:**

   Using Python’s built-in `venv`:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   If a `requirements.txt` file exists:

   ```bash
   pip install -r requirements.txt
   ```

   If not, install Django manually:

   ```bash
   pip install django
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **(Optional) Create a superuser for the Django admin:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the site:**

   Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your project running locally.

## Additional Tips

- **Deactivating the Virtual Environment:**

  When you're done working, you can exit the virtual environment by running:

  ```bash
  deactivate
  ```

- **Further Documentation:**

  For more details on Django, please refer to the [Django documentation](https://docs.djangoproject.com/en/4.2/).

- **Troubleshooting:**

  If you encounter issues, check that all prerequisites are installed correctly and that your virtual environment is activated. For further assistance, feel free to open an issue on GitHub.

---
