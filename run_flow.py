from aijson import register_action
import re

@register_action
def extract_personal_info(text: str) -> dict:
    personal_info = {
        'name': re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', text),  #
        'email': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
        'phone': re.findall(r'\b\d{10}\b', text)
    }
    return personal_info

@register_action
def anonymize_text(text: str, personal_info: dict) -> str:
 
    anonymized_text = text
    for info in personal_info.values():
        for item in info:
            anonymized_text = anonymized_text.replace(item, "[REDACTED]")
    return anonymized_text
