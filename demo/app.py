import gradio as gr
from src.pipeline import run_pipeline

def voice_rag_pipeline(audio_file):
    # Pass uploaded audio to your pipeline
    answer = run_pipeline(audio_file)
    return answer

# Gradio Interface
demo = gr.Interface(
    fn=voice_rag_pipeline,
    inputs=gr.Audio(sources=["microphone", "upload"], type="filepath"),
    outputs="text",
    title="🎤 Voice-Enabled RAG Demo",
    description="Speak or upload a voice query. The system transcribes, retrieves context, and generates an answer."
)

if __name__ == "__main__":
    demo.launch()
