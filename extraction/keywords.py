from keybert import KeyBERT

class KeywordExtractor:
    def __init__(self):
        self.model = KeyBERT()

    def extract(self, text, top_n=10):
        keywords = self.model.extract_keywords(text, top_n=top_n, stop_words="english", keyphrase_ngram_range=(1,3))
        return keywords