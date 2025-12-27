from scraper import scrape_jobs
from job_filters import is_relevant
from storage import is_new
from notifier import notify

def run():
    jobs = scrape_jobs()
    print("Total jobs found:", len(jobs))
    
    for job in jobs:
        if is_new(job["id"]) and is_relevant(
            job["title"], job["desc"], job["location"]
        ):
            msg = f"""
🚨 New Job Alert – AI / Data Science Intern

🏢 Company: {job['company']}
💼 Role: {job['title']}
📍 Location: {job['location']}

🔗 Apply on Indeed
"""
            notify(msg)

if __name__ == "__main__":
    run()
    print("✅ Script started")
    

