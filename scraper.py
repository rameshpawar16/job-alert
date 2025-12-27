import feedparser

def scrape_jobs():
    url = "https://www.foundit.in/srp/results?query=ai%20intern&locations=India&rss=true"
    feed = feedparser.parse(url)

    print("RSS entries found:", len(feed.entries))

    jobs = []
    for entry in feed.entries:
        jobs.append({
            "id": entry.id,
            "title": entry.title,
            "company": "Foundit",
            "location": "India",
            "desc": entry.summary
        })

    return jobs
