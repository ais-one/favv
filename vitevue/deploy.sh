if [ ! $1 ]; then # environment eg. uat
  echo "Missing 1st argument, project environment. Press any key to continue..."
  read
  exit
fi

if [ ! $2 ]; then # app name
  echo "Missing 2nd argument, application name. Press any key to continue..."
  read
  exit
fi

cp src/web/$2/deploy/apploader.js .
cp src/web/$2/deploy/.env.$1 .

echo "build and deploy"
npm ci # cannot use --production-only as vite dependency is needed
npx vite build --mode $1

rm -rf ../fastapi/app/static/dist
mv dist ../fastapi/app/static

if [ "$CI" != "true" ]; then
  echo "press enter key to exit"
  read # pause exit in windows
fi
