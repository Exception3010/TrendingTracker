# Demo Flow & Recording Script

**Total Duration:** \~2–3 minutes

1. **0:00–0:10 — Title & Overview**

    * **Visual:** Title slide “GitHub Trending Repositories Tracker”.
    * **Narration:** “Hi, I’m Hazem. This demo shows a Django app that scrapes GitHub Trending daily, stores data in a database, and exposes it via a REST API.”

2. **0:10–0:30 — Project Walkthrough**

    * **Visual:** IDE file explorer (PyCharm/VSCode).
    * **Highlight:** `trending/models.py`, `management/commands/scrape_trending.py`, `trending_tracker/celery.py`.
    * **Narration:** “Here’s the structure: data model, scraper command, and Celery configuration for scheduling.”

3. **0:30–0:45 — Database Setup**

    * **Command:** `python manage.py migrate` in terminal.
    * **Narration:** “This creates our `TrendingRepo` table.”

4. **0:45–1:00 — Running the Scraper**

    * **Command:** `python manage.py scrape_trending`.
    * **Narration:** “The scraper fetches today’s trending GitHub repos and saves them to the database.”

5. **1:00–1:15 — Inspecting Data**

    * **Command:**

      ```bash
      python manage.py shell
      >>> from trending.models import TrendingRepo
      >>> TrendingRepo.objects.filter(scraped_date=date.today()).count()
      ```
    * **Narration:** “We now have entries for today.”

6. **1:15–1:40 — API Demo**

    * **Visual:** Browser or Postman at `http://localhost:8000/api/trending/`.
    * **Narration:** “Here’s the JSON output, sorted by date and star count.”

7. **1:40–2:00 — Scheduling Tasks**

    * **Visual:** Show `crontab -e` entry or Windows Task Scheduler screenshot.
    * **Narration:** “On Linux, we use a cron job at midnight; on Windows, Task Scheduler runs the same command daily.”

8. **2:00–2:20 — Celery Beat (Optional)**

    * **Visual:** Open `trending_tracker/celery.py` and highlight `beat_schedule`.
    * **Narration:** “Alternatively, Celery Beat handles periodic execution within Django.”

9. **2:20–2:30 — Conclusion**

    * **Visual:** Display GitHub repo link or README.
    * **Narration:** “That’s it! Check out the code at \[GitHub link]. Thanks for watching

**Title Slied Layout:**

* **Title (centered):** GitHub Trending Repositories Tracker
* **Subtitle (below title):** By Hazem
* **Visual Element:** GitHub logo or trending icon (optional)
