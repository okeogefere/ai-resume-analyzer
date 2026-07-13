from app.services.resume_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text



text = extract_text_from_pdf("uploads/OkeOgefere_M.pdf")
cleaned_text = clean_text(text)

print(cleaned_text)
