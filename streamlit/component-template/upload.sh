if [ ! $1 ]; then
  echo "Missing Argument: folder. Press any key to continue..."
  exit
fi

if [ ! $2 ]; then # test or prod
  echo "Missing Argument: environment (test or prod). Press any key to continue..."
  exit
fi

echo "Ensure that your venv is activated"
echo "Ensure that frontend folders are built"
echo "Ensure that version number in setup.py is incremented"
echo "Ensure that _RELEASE flag in __init__.py files are True"
echo "For convenience, you can use .pypirc file in you local machine..."
echo "Clear older version in the python dist"

# navigate to the folder
cd $1

# build the python package
python setup.py sdist bdist_wheel

# upload
if [ "$2" = "test" ]; then
  python -m twine upload --repository testpypi dist/*
else
  python -m twine upload dist/*
fi

echo "Done..."
echo "press enter key to exit"
read # pause exit in windows
