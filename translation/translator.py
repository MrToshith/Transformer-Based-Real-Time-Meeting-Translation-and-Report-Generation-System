from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

class Translator:
    def __init__(self):
        model_name = "facebook/nllb-200-distilled-600M"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, text, source_lang="eng_Latn", target_lang="hin_Deva"):
        self.tokenizer.src_lang = source_lang
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        translated_tokens = self.model.generate(**inputs, forced_bos_token_id = self.tokenizer.convert_tokens_to_ids(target_lang), max_length=512)
        translated_text = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        return translated_text