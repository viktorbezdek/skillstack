"""Tests for slugify_utils.core."""

import pytest
from slugify_utils import slugify, unslugify, batch_slugify
from slugify_utils.validators import SlugError


class TestSlugify:
    def test_basic_ascii(self):
        assert slugify("Hello World") == "hello-world"

    def test_strips_special_chars(self):
        assert slugify("Hello, World!") == "hello-world"

    def test_collapses_whitespace(self):
        assert slugify("hello   world") == "hello-world"

    def test_russian_transliteration(self):
        assert slugify("Привет мир", lang="ru") == "privet-mir"

    def test_czech_diacritics(self):
        assert slugify("Česká republika", lang="cs") == "ceska-republika"

    def test_custom_separator(self):
        assert slugify("Hello World", separator="_") == "hello_world"

    def test_max_length_truncates(self):
        result = slugify("a" * 100, max_length=10)
        assert len(result) <= 10

    def test_empty_string_raises(self):
        with pytest.raises(ValueError, match="non-empty"):
            slugify("")

    def test_whitespace_only_raises(self):
        with pytest.raises(ValueError):
            slugify("   ")

    def test_accents_stripped_en(self):
        assert slugify("Café") == "cafe"


class TestUnslugify:
    def test_basic(self):
        assert unslugify("hello-world") == "Hello World"

    def test_single_word(self):
        assert unslugify("hello") == "Hello"

    def test_invalid_slug_raises(self):
        with pytest.raises(SlugError):
            unslugify("Hello-World")  # uppercase not valid in slug


class TestBatchSlugify:
    def test_all_valid(self):
        assert batch_slugify(["Hello", "World"]) == ["hello", "world"]

    def test_invalid_produces_empty_string(self):
        result = batch_slugify(["Hello", "", "World"])
        assert result == ["hello", "", "world"]

    def test_preserves_order(self):
        inputs = ["Café", "Наташа", "Güte"]
        result = batch_slugify(inputs, lang="en")
        assert len(result) == 3
