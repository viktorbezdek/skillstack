"""slugify-utils: URL-safe slug generation with multilingual support."""

from .core import slugify, unslugify, batch_slugify
from .validators import validate_slug, SlugError

__version__ = "0.3.2"
__all__ = ["slugify", "unslugify", "batch_slugify", "validate_slug", "SlugError"]
