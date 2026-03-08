import gradio as gr
from google import genai
import os
from dotenv import load_dotenv

# This automatically loads the variables from the .env file
load_dotenv()

# Initialize the Gemini Client
# It will automatically look for the GEMINI_API_KEY environment variable
client = genai.Client()

def analyze_food(image):
    if image is None:
        return "Please upload an image first."

    # 1. The Prompt Engineering
    prompt = """
    You are an expert AI nutritionist. Analyze the provided image of food and return the information EXACTLY in the following structured Markdown format:
    
    ### 🍱 Food Name
    [Identify the specific food or dish]
    
    ### 🔥 Estimated Calories
    [Provide an approximate calorie count based on the visible portion size]
    
    ### 🥦 Health Benefits
    * [Benefit 1]
    * [Benefit 2]
    * [Benefit 3]
    
    ### ⚠️ Possible Health Risks
    * [List 1-2 potential risks, such as high sodium, allergens, or high sugar content]
    """

    # 2. The API Call
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image, prompt]
        )
        return response.text
    except Exception as e:
        return f"An error occurred during analysis: {e}"

# 3. The Gradio UI (Simple and clean)
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🍱 AI Food Calorie & Health Analyzer")
    gr.Markdown("Upload an image of your food to get instant nutritional insights.")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Food Image")
            submit_btn = gr.Button("Analyze Food", variant="primary")

        with gr.Column():
            text_output = gr.Markdown(label="Analysis Results")

    # Connect the button to the function
    submit_btn.click(fn=analyze_food, inputs=image_input, outputs=text_output)

if __name__ == "__main__":
    demo.launch()