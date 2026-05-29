class ReportGenerator:

    def generate(
        self,
        transcript,
        translation,
        summary,
        keywords
    ):

        report = f"""
==================================================
MEETING REPORT
==================================================

SUMMARY
--------------------------------------------------

{summary}


KEYWORDS
--------------------------------------------------

"""

        for keyword, score in keywords:
            report += f"- {keyword}\n"

        report += f"""

TRANSLATION
--------------------------------------------------

{translation}


TRANSCRIPT
--------------------------------------------------

{transcript}

"""

        return report