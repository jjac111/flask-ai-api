# AI Flask API

A powerful Flask-based RESTful API that provides various AI-powered text processing and analysis endpoints using OpenAI's GPT models.

## Features

- Text Summarization
- Question Answering
- Content Rewriting
- Code Explanation
- Idea Generation
- Language Translation
- Mood/Emotion Analysis
- Keyword Extraction
- Learning Resource Recommendations
- Writing Prompt Generation

## Prerequisites

- Python 3.8+
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai_flask_api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   SECRET_KEY=your-secret-key-here
   ```

## Running the Application

Start the Flask development server:
```bash
python run.py
```


The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Text Summarization
- **Endpoint**: `POST /summarize`
- **Payload**:
  ```json
  {
      "text": "Your long text to summarize"
  }
  ```

### 2. Question Answering
- **Endpoint**: `POST /ask`
- **Payload**:
  ```json
  {
      "question": "Your question here",
      "context": "Optional context for the question"
  }
  ```

### 3. Content Rewriting
- **Endpoint**: `POST /rewrite`
- **Payload**:
  ```json
  {
      "text": "Text to rewrite",
      "tone": "formal/casual/persuasive"
  }
  ```

### 4. Code Explanation
- **Endpoint**: `POST /explain`
- **Payload**:
  ```json
  {
      "code": "Your code snippet here"
  }
  ```

### 5. Idea Generation
- **Endpoint**: `POST /generate`
- **Payload**:
  ```json
  {
      "topic": "Your topic for ideas"
  }
  ```

### 6. Language Translation
- **Endpoint**: `POST /translate`
- **Payload**:
  ```json
  {
      "text": "Text to translate",
      "target_language": "Spanish"
  }
  ```

### 7. Mood Analysis
- **Endpoint**: `POST /analyze`
- **Payload**:
  ```json
  {
      "text": "Text to analyze for mood"
  }
  ```

### 8. Keyword Extraction
- **Endpoint**: `POST /keywords`
- **Payload**:
  ```json
  {
      "text": "Text to extract keywords from"
  }
  ```

### 9. Learning Resources
- **Endpoint**: `POST /recommend`
- **Payload**:
  ```json
  {
      "topic": "Topic to learn",
      "difficulty": "beginner/intermediate/advanced"
  }
  ```

### 10. Writing Prompts
- **Endpoint**: `POST /prompt`
- **Payload**:
  ```json
  {
      "genre": "mystery/sci-fi/romance/etc"
  }
  ```


