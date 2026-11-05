def create_research_plan(client,model,topic):
    """
    Create a research plan for the given topic using Gemini.
    """

    prompt = f"""
    You are an expert research planner.

    Your task is to create a research plan
    for the following topic:

    Topic: {topic}

    Instructions:
    1. Create exactly 5 research questions.
    2. Cover different aspects of the topic.
    3. Make questions clear and specific.
    4. Avoid repeating similar questions.
    5. Return the result as a numbered list.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text