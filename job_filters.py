KEYWORDS = [
    "ai intern", "data science intern", "ml intern", "python intern"
]

SKILLS = [
    "python", "sql", "machine learning", "nlp", "deep learning",
    "power bi", "excel", "genai", "big data"
]

LOCATIONS = ["pune", "hyderabad", "bengaluru"]

def is_relevant(title, desc, location):
    text = (title + desc).lower()

    return (
        any(k in text for k in KEYWORDS) and
        any(s in text for s in SKILLS) and
        any(l in location.lower() for l in LOCATIONS)
    )
