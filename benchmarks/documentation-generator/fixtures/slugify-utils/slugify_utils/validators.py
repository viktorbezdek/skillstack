"""Slug validation utilities."""

import re


class SlugError(ValueError):
    """Raised when a string is not a valid slug or violates constraints."""


_SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_MAX_SLUG_LENGTH = 255


def validate_slug(slug: str, separator: str = "-", max_length: int = _MAX_SLUG_LENGTH) -> None:
    """Assert that *slug* is a valid URL slug.

    A valid slug contains only lowercase ASCII letters, digits, and the
    specified separator.  It must not start or end with the separator, and
    it must not contain consecutive separators.

    Args:
        slug: The string to validate.
        separator: Expected separator character.  Defaults to '-'.
        max_length: Maximum allowed length.  Defaults to 255.

    Raises:
        SlugError: If any constraint is violated, with a descriptive message.
    """
    if not slug:
        raise SlugError("slug must be a non-empty string")
    if len(slug) > max_length:
        raise SlugError(f"slug length {len(slug)} exceeds maximum {max_length}")
    if separator != "-":
        # Rebuild pattern for custom separator
        esc = re.escape(separator)
        pattern = re.compile(rf"^[a-z0-9]+(?:{esc}[a-z0-9]+)*$")
        if not pattern.match(slug):
            raise SlugError(
                f"slug '{slug}' is invalid: must be lowercase alphanumeric "
                f"words joined by '{separator}'"
            )
    else:
        if not _SLUG_PATTERN.match(slug):
            raise SlugError(
                f"slug '{slug}' is invalid: must match [a-z0-9]+(-[a-z0-9]+)*"
            )


def is_valid_slug(slug: str, separator: str = "-", max_length: int = _MAX_SLUG_LENGTH) -> bool:
    """Return True if *slug* is a valid slug, False otherwise.

    Convenience wrapper around :func:`validate_slug` that never raises.

    Args:
        slug: The string to test.
        separator: Expected separator character.
        max_length: Maximum allowed length.

    Returns:
        ``True`` if valid, ``False`` otherwise.
    """
    try:
        validate_slug(slug, separator=separator, max_length=max_length)
        return True
    except SlugError:
        return False
