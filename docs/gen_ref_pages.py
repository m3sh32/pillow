"""
Generate the code reference pages.
Source:  https://mkdocstrings.github.io/recipes/

mkdocs runs this script on each build
"""

from pathlib import Path

import mkdocs_gen_files


service_lib = sorted(Path("service/lib").rglob("*.py"))
service_src = sorted(Path("service/src").rglob("*.py"))
client_src = sorted(Path("client/src").rglob("*.py"))
paths = service_lib + service_src + client_src

nav = mkdocs_gen_files.nav.Nav()

for path in paths:
    module_path = path.with_suffix("")  #
    doc_path = path.with_suffix(".md")  #
    full_doc_path = Path("reference", doc_path)  #

    parts = list(module_path.parts)

    if parts[-1] == "__init__":  #
        parts = parts[:-1]
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()  # type:ignore

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:  #
        identifier = ".".join(parts)  #
        print("::: " + identifier, file=fd)  #

    mkdocs_gen_files.set_edit_path(full_doc_path, path)  #

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:  #
    nav_file.writelines(nav.build_literate_nav())
