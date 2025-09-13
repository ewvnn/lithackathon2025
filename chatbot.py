import os
from pathlib import Path
import requests
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)


folder = Path("data")  
context_facts = ""
for file in folder.glob("*.txt"):   # use rglob("*.txt") for recursive
    all_text += file.read_text(encoding="utf-8", errors="replace") + "\n"

# System prompt constraining knowledge scope
system_prompt = (
    "You are a knowledgeable and professional law advisor specializing in divorce cases in Singapore. Your role is to provide clear, accurate, and practical legal advice to users based strictly on the facts and documents provided. Use plain language to explain complex legal concepts, statutes, and regulations so that non-lawyers can understand.  Always prioritize ethical, lawful, and responsible advice. Follow these contextual facts:\n\n"
    f"{context_facts}\n\n"
    "If a question falls outside the scope of the provided information, politely inform the user and give thoughtful, cautious guidance as an educated legal opinion, without overstepping legal boundaries. If detected input with confidential information, give warnings - “Possible client confidential information detected- consider redaction. Do you want to continue? If detected input with suicidal tendencies, direct to Singapore's SOS helpline. If detected input with personal safety risk, suggest protection order. Never make up an answer if questions is beyond the Data."
)

def run_chatbot():
    print("Welcome to the Law Education Chatbot! Ask me anything from the stories in the archive.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
        )

        reply = response.choices[0].message.content.strip()
        print(f"Chatbot: {reply}\n")



run_chatbot()