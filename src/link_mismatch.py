import re

def detect_link_mismatch(text: str) -> bool:
    urls = re.findall(r'https?://\S+', text)
    return len(urls) >= 1