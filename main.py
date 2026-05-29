from stt.whisper_engine import WhisperEngine

engine = WhisperEngine()
audio_path = "data/audio/meeting-clip1.wav"
result = engine.transcribe(audio_path)

print(result.keys())
print()
print(result["text"])