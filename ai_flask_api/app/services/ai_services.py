from openai import OpenAI
from flask import current_app


class AIServices:
    def __init__(self):
        self.client = OpenAI(api_key=current_app.config['OPENAI_API_KEY'])

    def summarize_text(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a text summarization expert."},
                {"role": "user", "content": f"Please summarize the following text:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def answer_question(self, question, context=''):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
        if context:
            messages[0]["content"] += f"\nContext: {context}"

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content

    def rewrite_content(self, text, tone):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a content rewriter. Rewrite in a {
                    tone} tone."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    def explain_code(self, code):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a code explanation expert."},
                {"role": "user", "content": f"Please explain this code in simple terms:\n{code}"}
            ]
        )
        return response.choices[0].message.content

    def generate_ideas(self, topic):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an creative idea generator."},
                {"role": "user", "content": f"Generate 5 creative ideas related to: {topic}"}
            ]
        )
        return response.choices[0].message.content

    def translate_text(self, text, target_language):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a language translator."},
                {"role": "user", "content": f"Translate this text to {
                    target_language}:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def analyze_mood(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a mood analysis expert."},
                {"role": "user", "content": f"Analyze the mood of this text:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def extract_keywords(self, text):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a keyword extraction expert."},
                {"role": "user", "content": f"Extract key topics and keywords from this text:\n{
                    text}"}
            ]
        )
        return response.choices[0].message.content

    def get_learning_resources(self, topic, difficulty):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an educational resource expert."},
                {"role": "user", "content": f"Recommend learning resources for {
                    topic} at {difficulty} level"}
            ]
        )
        return response.choices[0].message.content

    def generate_writing_prompt(self, genre):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative writing prompt generator."},
                {"role": "user", "content": f"Generate a writing prompt for the {
                    genre} genre"}
            ]
        )
        return response.choices[0].message.content
