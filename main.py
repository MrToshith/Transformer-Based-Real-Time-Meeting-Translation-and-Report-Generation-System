from stt.whisper_engine import WhisperEngine
from translation.translator import Translator

engine = WhisperEngine()
audio_path = "data/audio/meeting-clip1.wav"
result = engine.transcribe(audio_path)

print(result.keys())
print()
print(result["text"])

print()

translator = Translator()
translated = translator.translate(result["text"])

print("\nHindi:\n")
print(translated)