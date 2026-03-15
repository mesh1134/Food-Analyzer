import gradio as gr
from ai_engine import analyze_food

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🍱 AI Food Calorie & Health Analyzer")
    gr.Markdown("Upload an image of your food to get instant nutritional insights.")
    
    with gr.Row():
        with gr.Column():
            # The input image component
            image_input = gr.Image(type="pil", label="Upload Food Image")
            
            # Adding clickable examples!
            gr.Examples(
                examples=["examples/burger.jpg", "examples/kerala_sadya.jpg","some_item.jpg"],
                inputs=image_input,
                label="Or click an example to test:"
            )
            
            # Primary action button
            submit_btn = gr.Button("Analyze Food", variant="primary")
        
        with gr.Column():
            # Text output area where results will render
            text_output = gr.Markdown(label="Analysis Results")
            
    
    submit_btn.click(fn=analyze_food, inputs=image_input, outputs=text_output)

if __name__ == "__main__":
    demo.launch()