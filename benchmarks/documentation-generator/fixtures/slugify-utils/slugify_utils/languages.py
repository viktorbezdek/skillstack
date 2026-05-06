"""Language transliteration tables.

Each table maps Unicode characters to their ASCII equivalents for a specific
language/script.  Characters not in the table are passed through unchanged.
"""

# Russian / Cyrillic → Latin
_RU = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
    "е": "e", "ё": "yo", "ж": "zh", "з": "z", "и": "i",
    "й": "j", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "shch", "ъ": "", "ы": "y", "ь": "",
    "э": "e", "ю": "yu", "я": "ya",
    # Uppercase handled by core.py lowercasing first; included for safety
    "А": "a", "Б": "b", "В": "v", "Г": "g", "Д": "d",
    "Е": "e", "Ё": "yo", "Ж": "zh", "З": "z", "И": "i",
    "Й": "j", "К": "k", "Л": "l", "М": "m", "Н": "n",
    "О": "o", "П": "p", "Р": "r", "С": "s", "Т": "t",
    "У": "u", "Ф": "f", "Х": "kh", "Ц": "ts", "Ч": "ch",
    "Ш": "sh", "Щ": "shch", "Ъ": "", "Ы": "y", "Ь": "",
    "Э": "e", "Ю": "yu", "Я": "ya",
}

# Czech diacritics → ASCII
_CS = {
    "á": "a", "č": "c", "ď": "d", "é": "e", "ě": "e",
    "í": "i", "ň": "n", "ó": "o", "ř": "r", "š": "s",
    "ť": "t", "ú": "u", "ů": "u", "ý": "y", "ž": "z",
    "Á": "a", "Č": "c", "Ď": "d", "É": "e", "Ě": "e",
    "Í": "i", "Ň": "n", "Ó": "o", "Ř": "r", "Š": "s",
    "Ť": "t", "Ú": "u", "Ů": "u", "Ý": "y", "Ž": "z",
}

# German umlauts → ASCII digraphs
_DE = {
    "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
    "Ä": "ae", "Ö": "oe", "Ü": "ue",
}

# Turkish specific mappings
_TR = {
    "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u",
    "Ç": "c", "Ğ": "g", "İ": "i", "Ö": "o", "Ş": "s", "Ü": "u",
}

#: Map of ISO 639-1 language code → transliteration character table.
TRANSLITERATION_MAPS: dict[str, dict[str, str]] = {
    "en": {},   # English: no transliteration needed (unicode normalisation handles it)
    "ru": _RU,
    "cs": _CS,
    "de": _DE,
    "tr": _TR,
}

SUPPORTED_LANGUAGES: list[str] = list(TRANSLITERATION_MAPS.keys())
