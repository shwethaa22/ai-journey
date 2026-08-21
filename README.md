# AI Engineering — Learning Journey

Building toward AI engineering from first principles. Each project
adds one new capability.

## Projects

### Persistent Chatbot (`chatbot.py`)
A command-line chat application that remembers conversations
between sessions.

- Stores messages in the `{"role", "content"}` format used by
  LLM APIs (Groq, Gemini, OpenAI)
- Persists history to JSON, reloaded on startup
- Handles missing and corrupt history files gracefully

