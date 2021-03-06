#!/bin/bash
echo "Custom App Package Install/Update"
read -p "Is your venv activated? (y/n)" REPLY
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
      if [ -f requirements.base.txt.updated ]; then
        # uninstall latest packages
        pip uninstall -r requirements.base.txt.updated -y
        rm -f requirements.base.txt.updated
      fi
      # install current packages
      pip install -r requirements.base.txt
      echo "installed current..."
      ;;
    "Install Latest")
      # uninstall
      pip uninstall -r app/custom_app/requirements.txt -y
      pip uninstall -r requirements.base.txt -y
      # reinistall and get new versions
      # aiofiles - for serving static files in fastapi
      pip install aiofiles fastapi uvicorn[standard] python-multipart SQLAlchemy passlib[bcrypt] python-jose[cryptography] boto3 pymongo redis huey
      pip freeze > requirements.base.txt.updated
      pip install -r app/custom_app/requirements.txt
      echo
      echo "installed latest... check updated libraries and update requirements file if ok"
      ;;
    "Quit")
      break
      ;;
    *) echo "invalid option $REPLY";;
  esac
done

# echo check the dependencies
# check_result=`pip check`
# if [[ $check_result =~ 'No broken requirements found.' ]]; then
#   echo "pip check pass"
#   pip freeze > requirements.base.txt.updated
# else
#   echo "pip check failed"
#   echo $check_result
# fi

echo
echo done... press enter key to exit
read # pause exit in windows
