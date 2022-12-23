from typing import Dict
import pytest

from src.tstring import Template


@pytest.mark.parametrize(
    ("expected", "template", "mapping", "allow_missing"),
    (
        ("", "", dict(), True),
        ("a", "a", dict(), True),
        ("a", "{b}", dict(b="a"), True),
        ("a", "[{b}]", dict(b="a"), True),
        ("", "[-{b}]", None, False),
        ("", "[{b}]", dict(), True),
        ("ab", "{a}[{b}]", dict(a="a", b="b"), True),
        ("a.b", "{a}[.{b}]", dict(a="a", b="b"), True),
        ("defg", "{a}{b}{c}g", dict(a="d", b="e", c="f"), True),
        ("d.e-gf", "{a}.{b}[-g{c}]", dict(a="d", b="e", c="f"), True),
        ("d.e-gf", "{a}.{b}[-g{c}][-{d}]", dict(a="d", b="e", c="f"), True),
    ),
)
def test_correctness(
    expected: str, template: str, mapping: Dict[str, str], allow_missing: bool
):
    assert Template(template).substitute(mapping, allow_missing) == expected


@pytest.mark.parametrize(
    ("error", "template", "mapping", "allow_missing"),
    (
        (ValueError, "{a}", dict(), False),
        (ValueError, "{a", dict(), False),
        (ValueError, "[a}]", dict(), False),
        (ValueError, "{a}{b}{c}", dict(), False),
    ),
)
def test_failures(
    error: Exception, template: str, mapping: Dict[str, str], allow_missing: bool
):
    with pytest.raises(error):
        Template(template).substitute(mapping, allow_missing=allow_missing)


def test_repr():
    template = Template("{a}{b}{c}")
    assert repr(template) == "Template('{a}{b}{c}')"


def test_str():
    template = Template("{a}{b}{c}")
    assert str(template) == "{a}{b}{c}"
