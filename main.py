from scraper import scrape_jobs
from job_filters import is_relevant
from storage import is_new
from notifier import notify
import os

BOT_TOKEN = os.getenv("8016462484:AAGSm9Aw73VrvC3BGnVC_XX60evEMuUJ2-U")
CHANNEL = os.getenv("@ai_ds_job_updates")

def run():
    # Heartbeat (confirms CI/CD + Telegram)
    notify("✅ CI/CD is running successfully. Bot is alive.")

    jobs = scrape_jobs()

    for job in jobs:
        if is_new(job["id"]) and is_relevant(
            job["title"], job["desc"], job["location"]
        ):
            msg = f"""
🚨 New Job Alert – AI / Data Science Intern

🏢 Company: {job['company']}
💼 Role: {job['title']}
📍 Location: {job['location']}
"""
            notify(msg)

if __name__ == "__main__":
    run()
    print("✅ Script finished")
