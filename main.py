from stt.whisper_engine import WhisperEngine
from translation.translator import Translator
from storage.transcript_store import TranscriptStore

engine = WhisperEngine()
audio_path = "data/audio/meeting-clip1.wav"
transcript = engine.transcribe(audio_path)
transcript_text = transcript["text"]

store = TranscriptStore()
store.save_text("transcript.txt", transcript_text)

translator = Translator()
translated = translator.translate(transcript["text"])
store.save_text("hindi_translation.txt", translated)

print("Done")