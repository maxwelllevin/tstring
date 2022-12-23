from typing import Dict
import pytest

from src.tstring import Template


@pytest.mark.parametrize(
    ("expected", "template", "mapping"),
    (
        ("", "", dict()),
        ("a", "a", dict()),
        ("a", "{b}", dict(b="a")),
        ("a", "[{b}]", dict(b="a")),
        ("", "[{b}]", dict()),
        ("ab", "{a}[{b}]", dict(a="a", b="b")),
        ("a.b", "{a}[.{b}]", dict(a="a", b="b")),
        ("defg", "{a}{b}{c}g", dict(a="d", b="e", c="f")),
        ("d.e-gf", "{a}.{b}[-g{c}]", dict(a="d", b="e", c="f")),
        ("d.e-gf", "{a}.{b}[-g{c}][-{d}]", dict(a="d", b="e", c="f")),
    ),
)
def test_correctness(expected: str, template: str, mapping: Dict[str, str]):
    assert Template(template).substitute(mapping, True) == expected


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
