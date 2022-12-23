# tstring

[![main](https://github.com/maxwelllevin/tstring/actions/workflows/pytest.yml/badge.svg)](https://github.com/maxwelllevin/tstring/actions/workflows/pytest.yml)
[![build](https://github.com/maxwelllevin/tstring/actions/workflows/pypi.yml/badge.svg)](https://github.com/maxwelllevin/tstring/actions/workflows/pypi.yml)
![PyPI](https://img.shields.io/pypi/v/tstring)

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
