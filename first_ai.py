# MY FIRST AI PROGRAM
from groq import Groq

client = Groq(api_key="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")

#question = "What is prompt engineering and why is it important?"
question = input("Ask AI anything: ")

print("Sending:", question)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Always answer the user's question directly."
        },
        {
            "role": "user","content": question
        }
    ]
)

print("\nAI says:")
print(response.choices[0].message.content)