import os
import gradio as gr
from google import genai
from dotenv import load_dotenv
import time

# Load key once. Decoupling ensures faster start-up and cleaner code.
load_dotenv()

# Initialize the Client once. 
client = genai.Client()

def analyze_food(image, progress=gr.Progress()):
    if image is None:
        return "Please upload an image first."

    # 1. Immediate visual confirmation (forces the bar to appear)
    progress(0.1, desc="Request received by AI Brain...")
    time.sleep(1.0) # Small intentional delay to let UI sync

    # 2. Update status and prepare inputs
    progress(0.3, desc="Preprocessing your image for Gemini 2.5...")
    time.sleep(1.0)
    
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
    
    # 3. Step 3 jumps directly into the model call
    progress(0.6, desc="Gemini is analyzing the food... almost there ⏳")
        
    try:
        # THE ACTUAL AI WORK HAPPENS HERE
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image, prompt]
        )
        
        # 4. Final step confirms completion
        progress(1.0, desc="Analysis Complete!")
            
        return response.text
        
    except Exception as e:
        return f"⚠️ **An error occurred during analysis:** {str(e)}"