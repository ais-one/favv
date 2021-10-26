#!/bin/bash
# $0. The name of script itself.
# $$ Process id of current shell.
# $* Values of all the arguments. ...
# $# Total number of arguments passed to script.
# $@ Values of all the arguments.
# $? Exit status id of last command.

echo "CI? [$CI]"

if [ ! $1 ]; then # test or production
  echo "Missing environment. Press any key to continue..."
  if [ "$CI" != "true" ]; then
    read
  fi
  exit
fi

# if [ "$1" = "development" ]; then
#   echo "Cannot deploy using development environment. Press any key to continue..."
#   if [ "$CI" != "true" ]; then
#     read
#   fi
#   exit
# fi

echo "Ensure that version number in setup.py is incremented"
echo "Ensure that _RELEASE flag in __init__.py files are True"
echo "For convenience, you can use .pypirc file in you local machine..."

pwd=`pwd`
echo $pwd

# build the frontend
cd streamlit_sidemenu/frontend
npm install
npm run build
cd $pwd

# build the python package
python setup.py sdist bdist_wheel

# upload
if [ "$1" = "test" ]; then
  python -m twine upload --repository testpypi dist/*
else
  python -m twine upload dist/*
fi

echo "Done..."

if [ "$CI" != "true" ]; then
  echo "press enter key to exit"
  read # pause exit in windows
fi
