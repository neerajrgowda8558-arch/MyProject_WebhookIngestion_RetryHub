# Lab 5 - Static Code Analysis
Restaurant Order System: Pylint, Bandit, and Flake8 reports and fixes.

## Reflection

**1. What is static code analysis?**  
Static code analysis checks source code without running the program to identify potential bugs, security vulnerabilities, and coding-style problems.

**2. What did Pylint, Bandit, and Flake8 identify?**  
Pylint identified code-quality issues, Bandit identified security risks, and Flake8 identified formatting and style violations.

**3. What changes were made to improve the program?**  
I removed unsafe `eval()` and shell execution, replaced MD5 with SHA-256, used secure PIN generation, fixed exception handling, and improved naming and formatting.

**4. What were the final results?**  
Pylint improved from 4.81/10 to 10.00/10. Bandit reported no issues, and Flake8 reported no violations.

**5. What did I learn?**  
I learned that static analysis helps make Python programs safer, cleaner, easier to maintain, and less likely to contain common coding mistakes.
