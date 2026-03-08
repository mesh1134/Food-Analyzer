import gradio as gr
from ai_engine import analyze_food

# FIX: Removed the theme parameter from here
with gr.Blocks() as demo:
    gr.Markdown("# 🍱 AI Food Calorie & Health Analyzer")
    gr.Markdown("Upload an image of your food to get instant nutritional insights.")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Food Image")

            gr.Examples(
                examples=["examples/burger.jpg", "examples/salad.jpg"],
                inputs=image_input,
                label="Or click an example to test:"
            )

            submit_btn = gr.Button("Analyze Food", variant="primary")

        with gr.Column():
            text_output = gr.Markdown(label="Analysis Results")

    submit_btn.click(fn=analyze_food, inputs=image_input, outputs=text_output)

if __name__ == "__main__":
    # FIX: Moved the theme parameter down here to demo.launch()
    demo.launch(theme=gr.themes.Soft())