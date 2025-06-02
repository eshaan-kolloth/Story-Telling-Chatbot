import openai
import os

openai.api_key = "sk......." #give your key
def generate_story(user_input, history=""):
    
    prompt = f"""
You are a creative and engaging storyteller. Continue the story based on the user's input.

Story so far:
{history}

User says: {user_input}
AI continues:
"""

    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a master storyteller."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=300,
    )

    
    return response.choices[0].message.content.strip()



if __name__ == "__main__":
    print("🧙 Welcome to StoryBot! Type 'exit' to quit.\n")
    story_history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        story = generate_story(user_input, story_history)
        story_history += f"\nYou: {user_input}\nAI: {story}\n"
        print(f"\nAI: {story}\n")