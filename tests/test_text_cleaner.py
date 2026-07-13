

from app.services.text_cleaner import clean_text

text = """
JOHN SMITH!!!

Python      Developer

Skills:
Python, SQL, FastAPI, Docker!!!

Email: john@email.com
"""

cleaned_text = clean_text(text)

print(cleaned_text)