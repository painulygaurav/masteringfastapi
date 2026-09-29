# Type hints

A format syntax introduced in Python 3.5 that allows you to explicitly state the expected data types of variables, function arguments, and return values.

Python remains a **dynamically typed language**, meaning the Python runtime doesn't enforce type hints. If a hint specifies a string but you pass an integer, your code will still execute without a native runtime error. Instead, type hints act as specialized metadata meant for developers and external tools.

## Advantages for mondern Python development

- **Catch Bugs Early with Static Analysis**

Use mypy or pyright like a compiler's type-checker.

- **Superior IDE Support (Autocomplete & Intellisense)**

Better autocomplete suggestions, inline warnings if you pass the wrong type to a function.

- **Self-documenting code**

- **Ecosystem Integration**

FastAPI and Pydantic read your function's type hints to automatically handle data validation, query parsing, and interactive documentation generation.
