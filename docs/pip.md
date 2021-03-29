## [If Necessary] Upgrade pip - windows

if need to upgrade pip

```
c:\users\<user>\test\fastapi-eg\dev\scripts\python.exe -m pip install --upgrade pip
```

## Usage Commands

```bash
pip install <package>
pip freeze > requirements.txt

# for updating packages
pip install pip-review
pip-review

# allow human intervention for updates
pip-review --interactive

# update all
pip-review --auto

pip list --outdated
pip list --uptodate

pip install --upgrade PACKAGE_NAME

# uninstall

pip uninstall <package>
pip freeze > requirements.txt
```
