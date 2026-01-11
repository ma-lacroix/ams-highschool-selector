# A class containing relevant school data

from typing import List


class School:

    def __init__(self, name: str, link: str, school_type: str, vwo: bool):
        self.name = name
        self.link = link
        self.school_type = school_type
        self.vwo = vwo
        self.distance = 0
        self.enrollment = []
        self.ai_summary = ""

    def update_all_ai_attributes(self, new_values: List[str]):
        self.distance = new_values[0]
        self.enrollment = new_values[1]
        self.ai_summary = new_values[2]

    def print_all_attributes(self):
        print(f"School: {self.name}")
        print(f"Link: {self.link}")
        print(f"Type: {self.school_type}")
        print(f"VWO: {self.vwo}")
        print(f"Distance from home: {self.distance}")
        print(f"Enrolement numbers: {self.enrollment}")
        print(f"AI summary: {self.ai_summary}")
        print("-" * 40)

    def turn_into_row(self) -> dict:
        return {
            "name": self.name,
            "link": self.link,
            "school_type": self.school_type,
            "vwo": self.vwo,
            "distance": self.distance,
            "enrollment": self.enrollment,
            "ai_summary": self.ai_summary,
        }
