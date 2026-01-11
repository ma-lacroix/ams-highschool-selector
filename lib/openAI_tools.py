
import os
import openai

class OpenAIClient:

    def __init__(self):
        self.endpoint = ""
        self.model = "gpt-4.1-mini"
        self.env_variable_name = "OPENAI_API_KEY"
        self.client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    def get_prompt_text_response(self, prompt) ->  openai.types.responses.response:
        return self.client.responses.create(
            model = self.model,
            input = prompt
        )

    def get_text_response(self, prompt: str) -> str:
        response_object = self.get_prompt_text_response(prompt)
        return response_object.output[0].content[0].text
