import os
from dotenv import load_dotenv
from google import genai

# Load Environment variables :

load_dotenv()

# connect to OpenAI :

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_ai(question):
    try:
        response = client.interactions.create(
            model="Gemini-3.5-flash-lite",
            input=question
        )

        return response.output_text

    except Exception as e:
        return f"Something went wrong: {e}"




def main():
    print("🤖 AI Research Agent")
    print("--------------------")
    
    question = input("what would you like to ask? ")

    answer = ask_ai(question)

    print("\nAI Response:")
    print(answer)

if __name__ == "__main__":
    main()