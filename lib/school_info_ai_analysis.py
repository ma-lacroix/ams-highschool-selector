# Prepares prompts to use to send to OpenAI

import os
from enum import Enum
from typing import List

from lib.openAI_tools import OpenAIClient

class PromptDataType(str, Enum):
    DISTANCE = "distance"
    ENROLLMENT_NUMBERS = "enrollment_numbers"
    SUMMARY = "summary"

    @classmethod
    def get_all_types(cls) -> List[str]:
        return [e.value for e in cls]


def get_prompt_string(key: str, school_name: str) -> str:
    BASE_ADDRESS = os.environ['BASE_POSTAL_CODE']

    base_prompt = """You speak Dutch and return answers in Dutch. 
        You are a city high school councelor giving advice to parents.
                    """
    prompts = {
        "distance": f"""
        {base_prompt}
        Give me a rough estimate of the distance between {school_name} and {BASE_ADDRESS} in Amsterdam. 
        Return just the value in kilometers in your response.     
            """,
        "enrollment_numbers": f"""
        {base_prompt}
        Give me the yearly enrolment numbers of {school_name} in Amsterdam. Keep only the numbers and years in your
        concise response.  
            """,
        "summary": f"""
        {base_prompt}
        Give me a 2 sentence summary of {school_name} in Amsterdam. Then give me 3 advantages and 3 disadvantages. 
        All bulletpoints should be concise and short.  
            """
    }
    return prompts.get(key)

def get_ai_data(openai_client: OpenAIClient, prompt_type: str, school_name: str) -> str:
    return openai_client.get_text_response(
        prompt=get_prompt_string(prompt_type, school_name)
    )