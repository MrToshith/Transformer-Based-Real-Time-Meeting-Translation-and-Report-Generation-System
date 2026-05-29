from transformers import BartTokenizer
from transformers import BartForConditionalGeneration

class Summarizer:
    def __init__(self):
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text):
        input_text = "summary: " + text
        inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, max_length=1024)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=60, min_length=20, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary