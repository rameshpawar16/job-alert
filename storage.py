import os

FILE = "seen_jobs.txt"

def is_new(job_id):
    if not os.path.exists(FILE):
        open(FILE, "w").close()

    with open(FILE, "r") as f:
        seen = f.read().splitlines()

    if job_id in seen:
        return False

    with open(FILE, "a") as f:
        f.write(job_id + "\n")

    return True
