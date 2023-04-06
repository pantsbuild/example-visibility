python_sources(
    name="helpers",
)

python_test_utils(
    name="test_utils",
)

python_tests(
    name="tests",
        overrides={
        "test_implementation.py": {
            "dependencies": ["tests/integration/testdata:rectangles"],
        }
    },
)

visibility_test_suite()
