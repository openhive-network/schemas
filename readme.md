## Introduction

Schemas package is a tool for validating the structure of JSON data. This package is a set of library-based
[jsonschema](https://json-schema.org/) wrappers, allowing you to easily and quickly write schemas that can be used for
 validation, e.g. API response.

## Installation
<details>
<summary>Install with PyCharm</summary>

- With opened project, select tab "Python Packages" at the bottom of window, click "Add Package" and then "From Disk".

![Installation instructions](./documentation/pycharm_install_0.png)

- Select 'Schemas' directory, mark "Install as editable" option and click OK.

![Installation instructions](./documentation/pycharm_install_1.png)

</details>

<details>
<summary>Install in virtual environment manually</summary>

```bash
cd ~/virtual_environments               # Select location for virtual environment
python3 -m venv venv                    # Create virtual environment in current directory
source venv/bin/activate                # Activate it
pip install -e ~/hive/tests/schemas     # Install Schemas
```
</details>

<details>
<summary>Install in your operating system scope (not recommended)</summary>
Enter following command in terminal:

```bash
pip3 install -e ~/hive/tests/schemas
```
</details>
