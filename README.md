# jpsy
Enforcing Language Naming Conventions

## What is it?
jpsy (pronounced like Gypsy), is a tool for naming convention purists, who don't like seeing other languages' naming 
conventions messing around their code's look and feel.

It comes in handy when your python code handles JSONs created in a JavaScript component, 
or just when you have people in your project who don't play by the book when it comes to naming conventions. 

## Installation
`pip install jpsy`

or

`pip install -e git+git://github.com/RomAviad/jpsy.git`

## What's with the name?
Obviously, it's a mash-up between JS and Py(thon).

## Usage Example
```python
from jpsy import pythonify, jsify

sample = {"abc_pep8": 123, "dictKey": {"PascalCase": "whatever", "camelCaseLongKEY": "woot"}}

pythonified = pythonify(sample)
print(pythonified)
# >>> {'abc_pep8': 123, 'dict_key': {'pascal_case': 'whatever', 'camel_case_long_key': 'woot'}}

jsified = jsify(sample)
print(jsified)
# >>> {'abcPep8': 123, 'dictKey': {'PascalCase': 'whatever', 'camelCaseLongKEY': 'woot'}}


jsified_python = jsify(pythonified)
print(jsified_python)
# >>> {'abcPep8': 123, 'dictKey': {'pascalCase': 'whatever', 'camelCaseLongKey': 'woot'}}

```