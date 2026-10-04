from dotenv import load_dotenv
load_dotenv()
from google import genai 

client = genai.Client()
msg = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what an AI agent is in 2 lines."
)
print(msg.text)
