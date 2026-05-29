from stt.whisper_engine import WhisperEngine
from translation.translator import Translator
from storage.transcript_store import TranscriptStore
from summarization.summarization import Summarizer
from extraction.keywords import KeywordExtractor
from reporting.report_generator import ReportGenerator

engine = WhisperEngine()
audio_path = "data/audio/meeting-clip1.wav"
transcript = engine.transcribe(audio_path)
transcript_text = transcript["text"]

store = TranscriptStore()
store.save_text("transcript.txt", transcript_text)

translator = Translator()
translated = translator.translate(transcript["text"])
store.save_text("hindi_translation.txt", translated)

summarizer = Summarizer()
summary = summarizer.summarize(transcript_text)

extractor = KeywordExtractor()
keywords = extractor.extract(transcript_text)

generator = ReportGenerator()
report = generator.generate(
    transcript=transcript_text,
    translation=translated,
    summary=summary,
    keywords=list(keywords)
)
print(report)

print("Done")