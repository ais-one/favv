#!/bin/bash
echo "Custom App Package Install/Update"
echo ""
read -p "Is your venv activated and framework packages installed? (y/n)" REPLY
echo
if ! [[ $REPLY =~ ^[Yy]$ ]]; then
  echo "Please activate your venv. Press enter to continue exit"
  read # pause exit in windows
  exit
fi

echo
PS3='Please enter your choice: '
options=("Install Current" "Install Latest" "Quit")
select opt in "${options[@]}"
do
  case $opt in
    "Install Current")
      if [ -f requirements.txt.updated ]; then
        # uninstall latest packages
        pip uninstall -r requirements.txt.updated -y
        rm -f requirements.txt.updated
      fi
      # install current packages
      pip install -r requirements.txt
      echo "installed current..."
      ;;
    "Install Latest")
      # uninstall framework
      pip uninstall -r ../../requirements.base.txt -y
      # uninstall current packages
      pip uninstall -r requirements.txt -y
      # install latest packages
      pip install numpy==1.20.1
      # create update file
      pip freeze > requirements.txt.updated
      # install framework
      pip install -r ../../requirements.base.txt
      echo "installed latest... check updated libraries and update requirements file if ok"
      ;;
    "Quit")
        break
        ;;
    *) echo "invalid option $REPLY";;
  esac
done

# echo
echo done... press enter key to exit
read # pause exit in windows
