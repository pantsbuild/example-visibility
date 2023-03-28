def visibility_application(**kwargs):
    """Rules for an application that is not expected to be imported by anything
    else than itself."""
    name = kwargs["name"]
    allowed_dependencies = kwargs.get("allowed_dependencies", [])
    allowed_dependents = kwargs.get("allowed_dependents", [])
    __dependents_rules__(
        (
            {"type": "*"},  # or {"path": "*"}
            f"//src/apps/{name}/*",  # current subtree
            f"//src/apps/{name}/**",  # current subtree, recursively
            *(f"//{path}" for path in allowed_dependents),
            "//tests/**",  # any test can import these sources
            "!*",  # nothing else
        )
    )
    __dependencies_rules__(
        (
            "*",  # applies to everything in this BUILD file
            "/**",  # allow all dependencies in this subtree
            f"//src/apps/utils/*",
            f"//src/shared/*",
            *(f"//{path}" for path in allowed_dependencies),
            "//3rdparty/requirements#click",  # only some 3rd party libraries
            "!*",  # nothing else
        )
    )


def visibility_shared_library(**kwargs):
    """Rules for a shared library which cannot depend on anything else but
    itself and which only certain packages can depend on."""
    name = kwargs["name"]
    allowed_dependencies = kwargs.get("allowed_dependencies", [])
    allowed_dependents = kwargs.get("allowed_dependents", [])
    __dependents_rules__(
        (
            {"type": "*"},  # or {"path": "*"}
            *(f"//{path}" for path in allowed_dependents),
            "//tests/**",  # any test can import these sources
            "!*",  # nothing else
        )
    )
    __dependencies_rules__(
        (
            "*",  # applies to everything in this BUILD file
            "/**",  # allow all dependencies in this subtree
            f"//{name}/*",  # current subtree
            f"//{name}/**",  # current subtree, recursively
            *(f"//{path}" for path in allowed_dependencies),
            "!*",  # nothing else
        )
    )


def visibility_testdata():
    """Rules for a directory containing test data used by tests."""
    __dependents_rules__(
        (
            # anyone may depend on test data if they are in the
            # same subtree
            {"type": "files"},
            "/../**",
            "!*",  # nothing else may depend on files
        )
    )


def visibility_test_suite():
    """Rules for a directory with tests."""
    __dependencies_rules__(
        (
            "*",  # for all files
            "!test_*.py",  # nothing may depend on other tests
            "*",
        ),
        (
            ({"type": "*"},),
            ("*"),
        ),
    )

    __dependents_rules__(
        (
            {"type": "python_tests"},
            "/**",
            # allow dependencies within tests tree (the dependencies
            # rules already ensure that test-to-test dependencies
            # are forbidden, so this is relevant only for conftest.py
            # dependencies and other helpers)
            "!*",  # nothing else may depend on tests
        ),
        (
            {"type": "python_sources"},
            "/**",  # allow dependencies within tests tree
            "!*",  # nothing else may depend on sources
        ),
        (
            # anyone may depend on a conftest.py file that is in the
            # same subtree
            {"path": "./conftest.py"},
            "./**",
            "!*",
        ),
        (
            ({"type": "*"},),
            ("*"),
        ),
    )
