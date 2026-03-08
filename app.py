import gradio as gr
from ai_engine import analyze_food

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🍱 AI Food Calorie & Health Analyzer")
    gr.Markdown("Upload an image of your food to get instant nutritional insights.")

    with gr.Row():
        with gr.Column():
            # 1. The Input
            image_input = gr.Image(type="pil", label="Upload Food Image")

            # 2. The Clickable Examples
            # Make sure you actually save two images in an 'examples' folder!
            gr.Examples(
                examples=["examples/burger.jpg", "examples/salad.jpg"],
                inputs=image_input,
                label="Or click an example to test:"
            )

            # 3. The Button
            submit_btn = gr.Button("Analyze Food", variant="primary")

        with gr.Column():
            # 4. The Output
            text_output = gr.Markdown(label="Analysis Results")

    # Connect everything together
    submit_btn.click(fn=analyze_food, inputs=image_input, outputs=text_output)

if __name__ == "__main__":
    demo.launch()