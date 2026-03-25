def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    
    cleaned = ""
    for ch in text:
        if ch.isalnum() or ch == " ":
            cleaned += ch
    
    return cleaned.strip()