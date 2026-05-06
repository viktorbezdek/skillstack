"""Core slug generation logic."""

import re
import unicodedata
from typing import Sequence

from .languages import TRANSLITERATION_MAPS
from .validators import validate_slug, SlugError


def slugify(text: str, lang: str = "en", separator: str = "-", max_length: int = 80) -> str:
    """Convert text to a URL-safe slug.

    Normalises unicode, applies language-specific transliteration, strips
    non-alphanumeric characters, and collapses separators.

    Args:
        text: The input string to slugify.
        lang: ISO 639-1 language code for transliteration rules.
            Supported: 'en', 'ru', 'cs', 'de', 'tr'.  Defaults to 'en'.
        separator: Character used between slug words.  Defaults to '-'.
        max_length: Maximum length of the resulting slug.  Defaults to 80.

    Returns:
        A URL-safe slug string.

    Raises:
        ValueError: If ``text`` is empty after processing.
        SlugError: If the resulting slug exceeds platform constraints.

    Examples:
        >>> slugify("Hello World")
        'hello-world'
        >>> slugify("Привет мир", lang="ru")
        'privet-mir'
        >>> slugify("Café au lait")
        'cafe-au-lait'
    """
    if not text or not text.strip():
        raise ValueError("text must be a non-empty string")

    # Apply language transliteration before unicode normalisation
    result = _apply_transliteration(text, lang)

    # Unicode normalise: decompose then strip combining chars
    result = unicodedata.normalize("NFKD", result)
    result = "".join(c for c in result if not unicodedata.combining(c))

    # Lowercase and replace non-alphanumeric with separator
    result = result.lower()
    result = re.sub(r"[^\w\s-]", "", result)
    result = re.sub(r"[\s_-]+", separator, result)
    result = result.strip(separator)

    if not result:
        raise ValueError(f"text '{text}' produced an empty slug")

    if len(result) > max_length:
        result = result[:max_length].rstrip(separator)

    return result


def unslugify(slug: str, separator: str = "-") -> str:
    """Convert a slug back to a human-readable string.

    Replaces separators with spaces and title-cases each word.

    Args:
        slug: A slug string (e.g. 'hello-world').
        separator: The separator character used in the slug.  Defaults to '-'.

    Returns:
        A human-readable title string (e.g. 'Hello World').

    Raises:
        SlugError: If ``slug`` is not a valid slug (use :func:`validate_slug`
            to check first).
    """
    validate_slug(slug, separator=separator)
    return slug.replace(separator, " ").title()


def batch_slugify(texts: Sequence[str], lang: str = "en", separator: str = "-") -> list[str]:
    """Slugify multiple strings, skipping invalid inputs with a warning.

    Unlike :func:`slugify`, this function does not raise on individual failures
    — it returns an empty string for each text that cannot be slugified.

    Args:
        texts: Sequence of strings to slugify.
        lang: Language code applied to all inputs.
        separator: Separator character applied to all inputs.

    Returns:
        List of slugs in the same order as ``texts``.  Failed conversions
        produce an empty string at the corresponding index.
    """
    results = []
    for text in texts:
        try:
            results.append(slugify(text, lang=lang, separator=separator))
        except (ValueError, SlugError):
            results.append("")
    return results


def _apply_transliteration(text: str, lang: str) -> str:
    table = TRANSLITERATION_MAPS.get(lang, {})
    return "".join(table.get(c, c) for c in text)
