# GitHub Trending Repositories Tracker

**GitHub Trending Repositories Tracker** is a Django-based application that automatically scrapes GitHub’s trending 
repositories page once per day, stores repository metadata in a database, and exposes the data via a RESTful API.

## Features

* **Web Scraping**: Uses `requests` and BeautifulSoup to scrape GitHub Trending.
* **Django Models**: Defines a `TrendingRepo` model to store repository details.
* **REST API**: Serves data with Django REST Framework (DRF).
* **Scheduling**: Supports simple cron-based scheduling or in-app scheduling with Celery Beat.

## Tech Stack

* Python 3.10+
* Django 5.2
* Django REST Framework
* Requests
* BeautifulSoup4
* python-dotenv (loads `.env`)
* (Optional) Celery & Redis for task scheduling

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Exception3010/TrendingTracker.git
   cd TrendingTracker
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings**

   Copy `.env.example` to `.env` and fill in the values:

   ```bash
   cp .env.example .env    # on Windows: copy .env.example .env
   ```

   `.env` is git-ignored and is loaded automatically by `trending_tracker/settings.py`
   (via python-dotenv). Real environment variables take precedence over the file.

   | Variable | Default | Notes |
   | --- | --- | --- |
   | `DJANGO_SECRET_KEY` | dev-only fallback while `DJANGO_DEBUG` is true | **Required** when `DJANGO_DEBUG` is false. Generate one with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
   | `DJANGO_DEBUG` | `True` | Set to `False` in production |
   | `DJANGO_ALLOWED_HOSTS` | empty | Comma-separated hostnames, e.g. `example.com,www.example.com`. Required when `DJANGO_DEBUG` is false |

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

## Usage

### Scraping Trending Repos

Run the management command to scrape and save today’s trending repositories:

```bash
python manage.py scrape_trending
```

### API Endpoint

Once you have data, visit:

```
GET http://localhost:8000/api/trending/
```

* Returns JSON list of objects:

  ```json
  [
    {
      "id": 1,
      "name": "octocat/Hello-World",
      "url": "https://github.com/octocat/Hello-World",
      "description": "My first repository on GitHub!",
      "stars": 1234,
      "language": "Python",
      "scraped_date": "2025-07-22"
    },
    ...
  ]
  ```

### Scheduling

#### Cron (Linux/macOS)

1. Open your user crontab:

   ```bash
   crontab -e
   ```
2. Add the following line to run at midnight every day:

   ```cron
   0 0 * * * cd /path/to/project && /path/to/venv/bin/python manage.py scrape_trending
   ```

#### Windows Task Scheduler

Use Task Scheduler GUI or `schtasks`:

```powershell
schtasks /Create /SC DAILY /ST 00:00 /TN "ScrapeTrending" /TR "C:\path\to\venv\Scripts\python.exe
 C:\path\to\project\manage.py scrape_trending"
```

#### Celery Beat (Optional)

1. Install the Redis client (Celery itself is already in `requirements.txt`):

   ```bash
   pip install redis
   ```
2. Create `trending_tracker/celery.py` (already included).
3. Ensure `__init__.py` loads Celery app.
4. Run workers and beat:

   ```bash
   celery -A trending_tracker worker --loglevel=info &
   celery -A trending_tracker beat --loglevel=info
   ```

## Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: \`git commit -m "Add your feature"
4. Push to branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full terms, or view it online at 
[https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).
