npm ci --production-only
npm run build

rm -rf ../fastapi/app/static/dist
mv dist ../fastapi/app/static

if [ "$CI" != "true" ]; then
  echo "press enter key to exit"
  read # pause exit in windows
fi
