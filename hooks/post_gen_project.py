import os
import shutil
from datetime import date

LICENSE_CHOICE = "{{ cookiecutter.license }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
USE_GITHUB_ACTIONS = "{{ cookiecutter.use_github_actions }}"

if LICENSE_CHOICE == "Proprietary":
    license_text = (
        f"Copyright (c) {date.today().year} {AUTHOR_NAME}\n\n"
        "All rights reserved. This project is not open source.\n"
    )
else:
    with open(os.path.join("licenses", f"{LICENSE_CHOICE}.txt"), encoding="utf-8") as f:
        license_text = f.read()
    license_text = license_text.replace("<year>", str(date.today().year))
    license_text = license_text.replace("<copyright holders>", AUTHOR_NAME)
    license_text = license_text.replace("<owner>", AUTHOR_NAME)
    license_text = license_text.replace("<name of author>", AUTHOR_NAME)

with open("LICENSE", "w", encoding="utf-8") as f:
    f.write(license_text)

shutil.rmtree("licenses")

if USE_GITHUB_ACTIONS == "no":
    workflows_dir = os.path.join(".github", "workflows")
    ci_file = os.path.join(workflows_dir, "ci.yml")
    if os.path.isfile(ci_file):
        os.remove(ci_file)
    for directory in (workflows_dir, ".github"):
        if os.path.isdir(directory) and not os.listdir(directory):
            os.rmdir(directory)

SPDX_LICENSES = {"MIT", "Apache-2.0", "BSD-3-Clause", "GPL-3.0-only"}

pyproject_path = "pyproject.toml"
with open(pyproject_path, encoding="utf-8") as f:
    pyproject = f.read()

if LICENSE_CHOICE in SPDX_LICENSES:
    legacy = 'license = { text = "' + LICENSE_CHOICE + '" }'
    modern = 'license = "' + LICENSE_CHOICE + '"'
    pyproject = pyproject.replace(legacy, modern)

with open(pyproject_path, "w", encoding="utf-8") as f:
    f.write(pyproject)
