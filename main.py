import os
from dotenv import load_dotenv
from google import genai
from agent.planner import create_research_plan
# Load Environment variables :

load_dotenv()

# connect to OpenAI :

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
model = "gemini-3.5-flash-lite"


def main():
    print("🤖 AI Research Agent")
    print("--------------------")
    
    topic = input("Enter your research topic:  ")

    print("\nGenerating your research plan...\n")

    plan = create_research_plan(client,model,topic)

    print("===== RESEARCH PLAN =====")
    print(plan)

if __name__ == "__main__":
    main()