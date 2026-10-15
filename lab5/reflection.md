# Reflection

The attached handout ends at the deliverables section and does not include its four reflection prompts. These four responses address the static-analysis learning outcomes described in the handout.

1. **What did static analysis contribute?** It surfaced security risks and maintainability problems before execution, including shell invocation, unsafe SQL construction, and unused code. Running the tools gave specific findings to verify and fix.

2. **Which issue mattered most, and why?** The shell invocation with `shell=True` was the most concerning because it executes through a command interpreter. Removing the subprocess also made the backup notice simpler and portable.

3. **How did the tools differ?** Pylint highlighted Python quality and naming issues, Flake8 focused on formatting and PEP 8 conventions, and Bandit identified security-sensitive patterns. Their findings overlap, but each brings a different lens.

4. **What are the limits of static analysis?** A clean report cannot prove that behavior is correct or that every security problem is absent. The code still needs human review and runtime checks, especially for edge cases such as unknown artifact IDs and unusual input.
