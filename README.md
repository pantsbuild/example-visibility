# Visibility rules

This is a toy repository containing a few [visibility rules](https://github.com/pantsbuild/pants/blob/main/docs/markdown/Using%20Pants/validating-dependencies.md) 
that should help you to get started writing own rules. 
You can amend the `pants-plugins/macros.py` rules or modify the Python source code and see what kind of 
violations your changes trigger. For instance, adding

```python
from src.apps.geometry.implementation import calculate_rectangle_area
```

to `src/apps/algebra/main.py` would trigger the following violation:

```
DependencyRuleActionDeniedError: src/apps/algebra/main.py has 1 dependency violation:

  * src/apps/algebra/BUILD[!*] -> src/apps/geometry/BUILD[!*] : DENY
    python_sources src/apps/algebra/main.py -> python_sources src/apps/geometry/implementation.py
```

because an application is not allowed to import from another application.

There's a branch named `dependency-violations` containing multiple violations that you can check out to learn more.

Run `pants lint ::` to validate dependencies.

## Rules

### Sources

1. Application `src/apps/algebra` cannot import from application `src/apps/geometry` and vice versa; they can depend 
on `src/apps/utils/`, `src/shared/` and certain 3rd party requirements (only `click`). 
2. `src/apps/utils` can only be imported from the `src/apps` and cannot depend on `src/shared`.
3. `src/shared` cannot depend on anything other than the code within the `src/shared`.

### Tests

1. Tests in a test suite cannot depend on non-code resources from another test suite (e.g. `tests/unit` cannot depend on
files from `tests/integration`).
2. Tests in a test suite cannot depend on code in test modules from another test suite (e.g. 
`tests/unit/test_implementation.py` cannot depend on code from `tests/integration/test_implementation.py`).
3. Helpers modules in a test suite can only depend on source code in the same suite and cannot depend on sources
from another test suite (e.g. `tests/integration/helpers.py` cannot depend on `tests/unit/helpers.py`).
4. Tests in a test suite can depend on `conftest.py` files in the test suite and up in the directory hierarchy (e.g. 
`tests/unit/test_implementation.py` can depend on `tests/unit/conftest.py` and `tests/conftest.py`, but it cannot
depend on `tests/integration/conftest.py`).
