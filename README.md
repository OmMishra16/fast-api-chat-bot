# FastAPI Chatbot Project

A robust chatbot API built with FastAPI and OpenAI's GPT-3.5 Turbo, featuring conversation management and context retention.

## 🚀 Features

- RESTful API endpoints for chat interactions
- Conversation management with history tracking
- Context retention for more coherent conversations
- OpenAI GPT-3.5 Turbo integration
- Environment-based configuration
- Error handling and validation

## 📋 Prerequisites

- Python 3.7+
- OpenAI API key

## 🛠️ Installation

1. Clone the repository:
2. cd chatbot-project
3. Install dependencies: pip3 install -r requirements.txt
4. Create a `.env` file in the root directory and add your OpenAI API key: OPENAI_API_KEY=your_api_key_here
5. Start the FastAPI server:  ``uvicorn app.main:app --reload``
   


The API will be available at `http://localhost:8000`

## 🔍 API Endpoints

### Root Endpoint
- `GET /`: Welcome message
  - Returns: `{"message": "Welcome to the Chatbot API"}`

### Chat Endpoints
- `POST /api/chat/send`: Send a message to the chatbot
  - Parameters:
    - `message` (string, required): The user's message
    - `conversation_id` (integer, optional): ID of existing conversation
  - Returns:
    ```json
    {
        "conversation_id": 1,
        "user_message": "Hello",
        "bot_response": "Hi! How can I help you today?"
    }
    ```

## 💡 Project Structure

## ⚙️ Configuration

The project uses pydantic-settings for configuration management. Key settings:
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `MAX_CONTEXT_MESSAGES`: Maximum number of messages retained for context (default: 10)

## 🔒 Environment Variables

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key

## 📦 Dependencies

Key dependencies include:
- FastAPI
- Uvicorn
- Python-dotenv
- Pydantic
- OpenAI
- Pytest


## 🔗 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Pydantic Documentation](https://docs.pydantic.dev/)
