- Source Article 
    - https://hynek.me/articles/testing-packaging/
- Testing and Packaging 
- src
- it looks better to have docs, src, and tests directories in your project root – in that order! 
- you move your packages into a src directory and tell your packaging build backend about it. 
- Ex. If you use pyproject.toml:

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]

- coverage run --parallel -m pytest tests   (measure coverage against entire package with no src)
- Ex. there is a solution in coverage which is the [paths] configuration section. It allows you to tell coverage which paths it should consider equivalent:

[run]
branch = True
source = attr

[paths]
source =
   src
   .tox/py*/**/site-packages