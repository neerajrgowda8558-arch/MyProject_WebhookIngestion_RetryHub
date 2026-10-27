# Lab 5: Static Code Analysis — Issue Table

| No. | Tool | Issue | Type | Fix Applied |
|---|---|---|---|---|
| 1 | Pylint | Mutable default argument | Code quality / bug prevention | Changed the default argument to `None` and handled initialization safely. |
| 2 | Pylint / Bandit | Use of `eval()` | Security | Replaced dynamic expression evaluation with validated numeric discount calculation. |
| 3 | Bandit | Weak MD5 hash | Security | Replaced MD5 with SHA-256. |
| 4 | Bandit | Insecure pseudo-random PIN generation | Security | Used the `secrets` module for PIN generation. |
| 5 | Bandit | Shell execution using `os.system()` | Security | Removed shell execution and used a direct confirmation message. |
| 6 | Pylint / Flake8 | Bare exception handler | Code quality | Replaced broad exception handling with explicit checks. |
| 7 | Pylint / Flake8 | Unused imports and variables | Code quality | Removed unused imports and variables. |
| 8 | Pylint / Flake8 | Naming and formatting violations | Style | Applied snake_case names, docstrings, proper line lengths, and consistent formatting. |

## Verification

- Initial Pylint score: 4.81/10
- Final Pylint score: 10.00/10
- Final Bandit result: No issues identified
- Final Flake8 result: No violations reported

## Reflection

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations. Pylint helped improve code quality, Bandit identified security risks, and Flake8 checked Python formatting conventions. Fixing these issues improved the readability, maintainability, and security of the restaurant order system.