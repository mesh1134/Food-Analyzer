import os
from google import genai
from dotenv import load_dotenv

# Load the hidden API key
load_dotenv()
client = genai.Client()

def analyze_food(image, progress=None):
    if image is None:
        return "Please upload an image first."

    if progress:
        progress(0.2, desc="Preparing image and prompt...")

    # The upgraded prompt with guardrails
    prompt = """
    You are an expert AI nutritionist. 
    
    FIRST RULE: Determine if the image contains food. If it does NOT contain food, ignore all formatting and simply reply with: "⚠️ **This does not appear to be a food item.** Please upload a clear image of food." Do not provide calorie estimates for non-food items.
    
    SECOND RULE: If it IS food, analyze it and return the information EXACTLY in the following structured Markdown format:
    
    ### 🍱 Food Name
    [Identify the specific food or dish]
    
    ### 🔥 Estimated Calories
    [Provide an approximate calorie count based on the visible portion size]
    
    ### 🥦 Health Benefits
    * [Benefit 1]
    * [Benefit 2]
    
    ### ⚠️ Possible Health Risks
    * [List 1-2 potential risks, such as high sodium, allergens, or high sugar content]
    """

    if progress:
        progress(0.6, desc="Gemini is analyzing... this takes a few seconds ⏳")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image, prompt]
        )

        if progress:
            progress(1.0, desc="Analysis Complete!")

        return response.text

    except Exception as e:
        return f"An error occurred during analysis: {e}"