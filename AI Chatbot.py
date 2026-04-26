# AI CHATBOT

from groq import Groq

client = Groq(api_key="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")

print("🤖 AI Chatbot Ready!")
print("Type your message and press Enter")
print("Type 'quit' to exit")
print("=" * 40)

# Store conversation history [DICTIONARY]
messages = [
    {
        "role": "system", #instruction,
        "content": "You are a helpful assistant who gives short and clear answers."
    }
]

while True:
    # Get user input
    user_input = input("\nYou: ")

    # Exit if user types quit
    if user_input.lower() == "quit":
        print("👋 Goodbye!")
        break

    # Add user message to history
    messages.append({
        "role": "user", #Human
        "content": user_input
    })

    # Send to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Get AI reply
    ai_reply = response.choices[0].message.content

    # Add AI reply to history
    messages.append({
        "role": "assistant", #AI
        "content": ai_reply
    })

    # Print AI reply
    print(f"\n🤖 AI: , {ai_reply}")