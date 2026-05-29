from translator import Translator

translator = Translator()

transcript = """
Hello everyone.
Welcome to today's meeting.
"""

translated_text = translator.translate(transcript)

with open("meeting_translation.txt", "w", encoding="utf-8") as file:
    file.write("Original Transcript : ")
    file.write(transcript)

    file.write("\nHindi Translation : \n")
    file.write(translated_text)