# tstring

[![main](https://github.com/maxwelllevin/tstring/actions/workflows/pytest.yml/badge.svg)](https://github.com/maxwelllevin/tstring/actions/workflows/pytest.yml)
[![codecov](https://codecov.io/github/maxwelllevin/tstring/branch/main/graph/badge.svg?token=W6D5FN6AUA)](https://codecov.io/github/maxwelllevin/tstring)
[![build](https://github.com/maxwelllevin/tstring/actions/workflows/pypi.yml/badge.svg)](https://github.com/maxwelllevin/tstring/actions/workflows/pypi.yml)
![PyPI](https://img.shields.io/pypi/v/tstring)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tstring)

Curly-brace string templates in Python.

```shell
pip install tstring
```

## Usage

```python
from tstring import Template

template = Template("{a}.{b}.{c}")
print(template.substitute(a="d", b="e", c="f"))
>>> "d.e.f"
```

Support for optional variable substitutions is also included:

```python
template = Template("{a}.{b}[.{c}]")
print(template.substitute(a="d", b="e", c="f"))
>>> "d.e.f"
print(template.substitute(a="d", b="e"))
>>> "d.e"
```
