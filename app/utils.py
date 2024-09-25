import re

def clean_website_text(text):
    # Remove HTML tags
    clean_text = re.sub(r'<.*?>', '', text)
    
    # Remove URLs
    clean_text = re.sub(r'http\S+|www\S+', '', clean_text)
    
    # Remove any non-alphanumeric characters except spaces
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', clean_text)
    
    # Remove extra spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    return clean_text