from ruffruleannotator import annotate

RUFF_SIMPLE_CONFIG_PYPROJECT = """
[other.tool]
key = "value"

[other.tool.lint]
key = []

[tool.ruff.lint]
# 1. Enable flake8-bugbear (`B`) rules, in addition to the defaults.
select = ["E4", "E7", "E9", "F", "B"]

# 2. Avoid enforcing line-length violations (`E501`)
ignore = ["E501"]

# 3. Avoid trying to fix flake8-bugbear (`B`) violations.
unfixable = ["B"]

# 4. Ignore `E402` (import violations) in all `__init__.py` files, and in selected subdirectories.
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["E402"]
"**/{tests,docs,tools}/*" = ["E402"]

[tool.ruff.format]
# 5. Use single quotes in `ruff format`.
quote-style = "single"
"""

RUFF_SIMPLE_CONFIG_PYPROJECT_EXPECTED = """
[other.tool]
key = "value"

[other.tool.lint]
key = []

[tool.ruff.lint]
# 1. Enable flake8-bugbear (`B`) rules, in addition to the defaults.
select = [
    "B", # flake8-bugbear
    "E4", # Subset of pycodestyle errors
    "E7", # Subset of pycodestyle errors
    "E9", # Subset of pycodestyle errors
    "F", # Pyflakes
]

# 2. Avoid enforcing line-length violations (`E501`)
ignore = [
    "E501", # line-too-long
]

# 3. Avoid trying to fix flake8-bugbear (`B`) violations.
unfixable = [
    "B", # flake8-bugbear
]

# 4. Ignore `E402` (import violations) in all `__init__.py` files, and in selected subdirectories.
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["E402"]
"**/{tests,docs,tools}/*" = ["E402"]

[tool.ruff.format]
# 5. Use single quotes in `ruff format`.
quote-style = "single"
"""


def test_ruff_default_pyproject():
    config = RUFF_SIMPLE_CONFIG_PYPROJECT.strip().splitlines()
    result = annotate(config)
    expected_result = RUFF_SIMPLE_CONFIG_PYPROJECT_EXPECTED.strip().splitlines()

    assert len(result) == len(expected_result)
    assert all(result[i] == expected_result[i] for i in range(len(result)))
