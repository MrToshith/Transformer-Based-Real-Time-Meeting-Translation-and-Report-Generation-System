from pathlib import Path

class TranscriptStore:
    def __init__(self, output_dir="data/transcripts"):
        self.output_dir = Path(output_dir)
    
    def save_text(self, filename, text):
        file_path = self.output_dir / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        return file_path