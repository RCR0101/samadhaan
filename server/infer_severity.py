# from transformers import AutoModelForCausalLM, pipeline
from ctransformers import AutoModelForCausalLM
from transformers import pipeline

class TextProcessor:
    def __init__(self):
        # Initialize the LLM and summarizer only once upon creating an instance of TextProcessor
        self.llm = AutoModelForCausalLM.from_pretrained(f'models/hf-zephyr', model_file="zephyr-7b-beta.Q4_K_M.gguf", model_type="mistral", temperature=0.1, gpu_layers=50)
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def get_summary_text(self, txt_msg):
        # Use the preloaded summarizer to generate a summary
        summarized_text = self.summarizer(txt_msg, max_length=512, min_length=30, do_sample=False)[0]['summary_text']
        return summarized_text

    def get_severity(self, txt_msg):
        # Use the preloaded LLM to evaluate severity
        prompt_txt = "provide severity value from the list 'Critical', 'Endanger', 'Exam Related', 'Malpractice', 'Suggestion' for text: " + txt_msg
        response_text = self.llm(prompt_txt)
        return response_text

# # Example usage
# text_processor = TextProcessor()

# # Now you can call get_summary_text and get_severity multiple times without re-initializing the LLM and summarizer
# txt_msg = "Your text message here."
# summary = text_processor.get_summary_text(txt_msg)
# print("Summary:", summary)

# severity = text_processor.get_severity(txt_msg)
# print("Severity:", severity)
