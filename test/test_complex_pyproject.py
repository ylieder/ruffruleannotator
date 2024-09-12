from ruffruleannotator import annotate

CONFIG = """
[tool.ruff.lint]
select = [
    "F404",
    "F403",
    # Lines are not sorted around comment lines.
    "F402",
    "F401",
    "F406", # already commented lines are not annotated
    # Lines with multiple rule ids are split
    "E112", "E111",
    "E113"]

fixable = [
]
"""

EXPECTED_OUTPUT = """
[tool.ruff.lint]
select = [
    "F403", # undefined-local-with-import-star
    "F404", # late-future-import
    # Lines are not sorted around comment lines.
    "F401", # unused-import
    "F402", # import-shadowed-by-loop-var
    "F406", # already commented lines are not annotated
    # Lines with multiple rule ids are split
    "E111", # indentation-with-invalid-multiple
    "E112", # no-indented-block
    "E113", # unexpected-indentation
]

fixable = []
"""


def test_complex_pyproject():
    result = annotate(CONFIG.strip().splitlines())

    assert result == EXPECTED_OUTPUT.strip().splitlines()
