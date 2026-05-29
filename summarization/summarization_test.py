from summarization import Summarizer

summarizer = Summarizer()

text = """
The team discussed plans for flexible working hours.
Paul presented progress updates.
A presentation from Miss Reyes is scheduled later.
Further discussion will occur after the presentation.
"""

summary = summarizer.summarize(text)

print(summary)