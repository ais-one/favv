## [If Necessary] Upgrade pip - windows

if need to upgrade pip

```
c:\users\<user>\test\favv\fastapi\dev\scripts\python.exe -m pip install --upgrade pip
```

## Usage Commands

Reference: https://pip.pypa.io/en/stable/cli/

Some commonly used commands...

```bash
# install
pip install <package>
pip install -r requirements-base.txt

# check for outdated
pip list --outdated
pip list --uptodate

# upgrading - will not work because versions are always fixed
pip install -r requirements-base.txt --upgrade
pip install --upgrade PACKAGE_NAME
pip install --upgrade

# uninstall
pip uninstall <package>
pip uninstall -r requirements.txt -y

# check, freeze
pip check
pip freeze --exclude numpy > requirements-base .txt
pip freeze > requirements.txt
```



## PIP review

Not used

```
# for updating packages
pip install pip-review
pip-review

# allow human intervention for updates
pip-review --interactive

# update all
pip-review --auto
```
