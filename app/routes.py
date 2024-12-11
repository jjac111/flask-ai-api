from flask import Blueprint, request, jsonify
from app.services.ai_services import AIServices

api = Blueprint('api', __name__)
ai_services = AIServices()


@api.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    summary = ai_services.summarize_text(data['text'])
    return jsonify({'summary': summary})


@api.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400

    context = data.get('context', '')
    answer = ai_services.answer_question(data['question'], context)
    return jsonify({'answer': answer})


@api.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    tone = data.get('tone', 'neutral')
    rewritten = ai_services.rewrite_content(data['text'], tone)
    return jsonify({'rewritten': rewritten})


@api.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400

    explanation = ai_services.explain_code(data['code'])
    return jsonify({'explanation': explanation})


@api.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({'error': 'No topic provided'}), 400

    ideas = ai_services.generate_ideas(data['topic'])
    return jsonify({'ideas': ideas})


@api.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    if not data or 'text' not in data or 'target_language' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    translated = ai_services.translate_text(
        data['text'], data['target_language'])
    return jsonify({'translated': translated})


@api.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    analysis = ai_services.analyze_mood(data['text'])
    return jsonify({'analysis': analysis})


@api.route('/keywords', methods=['POST'])
def keywords():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    keywords = ai_services.extract_keywords(data['text'])
    return jsonify({'keywords': keywords})


@api.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({'error': 'No topic provided'}), 400

    difficulty = data.get('difficulty', 'intermediate')
    recommendations = ai_services.get_learning_resources(
        data['topic'], difficulty)
    return jsonify({'recommendations': recommendations})


@api.route('/prompt', methods=['POST'])
def prompt():
    data = request.get_json()
    if not data or 'genre' not in data:
        return jsonify({'error': 'No genre provided'}), 400

    writing_prompt = ai_services.generate_writing_prompt(data['genre'])
    return jsonify({'prompt': writing_prompt})
