import re

SECTION_PATTERNS = {
    "abstract": r"\babstract\b",
    "introduction": r"\bintroduction\b",
    "related_work": r"related work",
    "method": r"\bmethod\b|\bapproach\b|\bmodel\b",
    "experiment": r"\bexperiment\b|\bresults\b|\bevaluation\b",
    "conclusion": r"\bconclusion\b|\bdiscussion\b"
}


def detect_section(text):

    text_lower = text.lower()

    for section, pattern in SECTION_PATTERNS.items():
        if re.search(pattern, text_lower):
            return section

    return "other"