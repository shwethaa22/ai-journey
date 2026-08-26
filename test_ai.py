import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
URL="https://api.groq.com/openai/v1/chat/completions"

print(f"Key starts with: {API_KEY[:8]}")

response=requests.post(
    URL,
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "messages": [
            {"role": "user", "content": "How old is Lord Shiva? Answer with Proof in 4 lines"}
        ],
        "model": "openai/gpt-oss-20b"
    },
    timeout=10
)

print(f"Response status code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print("Response Answer:", data["choices"][0]["message"]["content"])
    print("No. of tokens used:", data["usage"]["total_tokens"])

else:
    print("Error:", response.text)    