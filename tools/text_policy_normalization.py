import unicodedata


def normalize_for_policy_match(text: str) -> str:
    nfkc_text = unicodedata.normalize('NFKC', text)
    casefolded_text = nfkc_text.casefold()
    words = casefolded_text.split()
    normalized_text = " ".join(words)
    return normalized_text

print(normalize_for_policy_match("  ＨＥＬＬＯ    WORLD  "))
