from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIConn:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OpenAI_API"))

    def get_feedback(self,question):
        feedback = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return feedback