# tstring

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
