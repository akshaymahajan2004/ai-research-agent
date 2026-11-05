from google.genai import types

def conduct_research(client,model,research_plan):
    prompt= f"""
    You are an expert web research assistant.

    Investigate the following research questions:

    {research_plan}

    Instructions:
    1. Research each question carefully.
    2. Use reliable and relevant online sources.
    3. Provide factual and detailed findings.
    4. Include source names and URLs where available.
    5. Organize the findings under clear headings.
    6. Do not invent facts or sources.
    """

    # Enable google search:

    search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    # Configure Gemini with Google search 

    config = types.GenerateContentConfig(
        tools=[search_tool]
    )

    # Send research request

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config
    )

    return response.text