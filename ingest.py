import requests
from minsearch import Index


def load_faq_data():
    """
    Load FAQ data from a remote source and return it as a list of dictionaries.
    Each dictionary contains 'question' and 'answer' keys.
    """
    doc_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(doc_url)
    courses_raw = response.json()

    documents = []
    url_prefix = "https://datatalks.club/faq"

    for course in courses_raw:
        course_url = f"""{url_prefix}{course["path"]}"""
        #print(course_url)
    
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()
    
        documents.extend(course_data)
    
        return documents
    
    
def build_index():
    """
    Build a MinSearch index from the loaded FAQ data.
    """
    index = Index(
        text_fields = ["question", "section", "section"],
        keyword_fields = ["course"]
    )

    index.fit(documents)
    
    return index