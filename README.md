# ruffruleannotator

ruffruleannotator is a small tool designed to enhance the readability of Ruff configuration files by annotating all rule IDs with their corresponding titles. This allows users to easily understand the purpose of each ignored/selected rule within their codebase. Additionally, ruffruleannotator can sort the rule IDs within the relevant sections of the TOML file, ensuring a well-organized and readable configuration.

## Example 
Consider the following `pyproject.toml`:
```toml
[project]
name = "packagename"

[tool.ruff.lint]
select = ["D100", "D103", "ERA001", "PLR2004", "F"]

ignore = ["E501", "B"]

[tool.ruff.format]
quote-style = "single"
```
Executing `ruffruleannotator` yield a reformatted config with annotated rule IDs:
```toml
[project]
name = "packagename"

[tool.ruff.lint]
select = [
    "D100", # undocumented-public-module
    "D103", # undocumented-public-function
    "ERA001", # commented-out-code
    "F", # Pyflakes
    "PLR2004", # magic-value-comparison
]

ignore = [
    "B", # flake8-bugbear
    "E501", # line-too-long
]

[tool.ruff.format]
quote-style = "single"
```

## Installation
```shell
pip install ruffruleannotator
```

## Annotate Ruff configurations 
The tool automatically recognizes ruff configs inside `pyproject.toml` and `ruff.toml`. Currently the entries `select`, `ignore`, `fixable` and `unfixable` inside the lint section of the Ruff config are supported for annotating and sorting. All other parts of the file stay unchanged.

Execute tool inside project root directoy:
```shell
ruffruleannotator
```

### Backup
By default a backup of the config file is stored under `~/.ruffruleannotator/backup`. Only the latest version of each project directory is stored. The creation of a config backup can be ignored:
```shell
ruffruleannotator --no-backup
```

### Keep order of entries
By default `ruffruleannotator` sorts the rule IDs within the sections alphabetically. The order of entries can be reserved: 
```shell
ruffruleannotator --no-sort
```

### Automatically confirm changes
By default all expected changes are shown before applied and the user must confirm. The manual confirmation can be skipped:
```shell
ruffruleannotator --yes
```

### Complex formattings
Consider the following config file:
```toml
[tool.ruff.lint]
select = ["F404",
    "F403",
    # A line commented out breaks the sorting. Rule IDs are sorted
    # seperately above and below the comment section.
    "F406", # already commented lines are not annotated
    "F402",
    # Lines with multiple rule ids are split
    "E112", "E111",
    "E113"]
```
After reformatting:
```toml
[tool.ruff.lint]
select = [
    "F403", # undefined-local-with-import-star
    "F404", # late-future-import
    # A line commented out breaks the sorting. Rule IDs are sorted
    # seperately above and below the comment section.
    "F402", # import-shadowed-by-loop-var
    "F406", # already commented lines are not annotated
    # Lines with multiple rule ids are split
    "E111", # indentation-with-invalid-multiple
    "E112", # no-indented-block
    "E113", # unexpected-indentation
]
```

## Contributing

- Create virtual environment
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt
    ```
- Setup pre-commit
    ```shell
    pre-commit install
    ```
- Build package
    ```
    python -m build
    ```
