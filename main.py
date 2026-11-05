import os
from dotenv import load_dotenv
from google import genai
from agent.planner import create_research_plan
from agent.researcher import conduct_research

# Step 1: Load Environment variables :

load_dotenv()

# Step 2: connect to OpenAI :

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
model = "gemini-3.5-flash-lite"


def main():
    print("🤖 AI Research Agent")
    print("--------------------")
    
    try:
        # Step 3: Get research topic


        topic = input("Enter your research topic  ")

        print("\nGenerating your research plan..\n")

        # Step 4: Generate Research Plan
        research_plan = create_research_plan(client,model,topic)

        print("===== RESEARCH PLAN =====")
        print(research_plan)

        # Step 5: Conduct research according to planning

        print("\nResearching the topic using Google Search...\n")

        research_results = conduct_research(client,model,research_plan)

        print("===== RESEARCH FINDINGS =====")
        print(research_results)

    except Exception as e:
        return f"Something went wrong: {e}"

if __name__ == "__main__":
    main()