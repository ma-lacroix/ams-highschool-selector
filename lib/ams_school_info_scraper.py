# Fetches the High School data from the City of Amsterdam

from typing import List

import requests
from bs4 import BeautifulSoup
from lib.school import School

BASE_URL = "https://schoolwijzer.amsterdam.nl"

def get_html_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python script)"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_meta_data(text: str) -> List[School]:
    soup = BeautifulSoup(text, "html.parser")
    selector = 'div[class*="styles_vestiging-card-content__"]'

    schools = []
    for a in soup.select(selector):
        name = "default"
        href = "default"
        school_type = "default"
        vwo = "No"

        sub_selector_one = 'a[class*="styles_vestiging-card-title__link__"]'
        sub_soup_one = a.select(sub_selector_one)
        for b in sub_soup_one:
            name = b.get_text(strip=True)
            href = b.get("href")

        sub_selector_two = (
            'ul[class*="styles_comma-separated-list__"]'
        )
        sub_soup_two = a.select(sub_selector_two)
        for c in sub_soup_two:
            school_type = c.get_text(strip=True)
            if 'vwo' in school_type.lower():
                vwo = "Yes"
        schools.append(School(name=name,
                              link=f"{BASE_URL}{href}",
                              school_type=school_type,
                              vwo=vwo)
                       )
    return schools[:2]

def fetch_school_data_from_city() -> List[School]:
    parent_text = get_html_text(f"{BASE_URL}/nl/vo/lijst/")
    return extract_meta_data(parent_text)