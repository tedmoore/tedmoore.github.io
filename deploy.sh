cd public
rm -rf *
cd ..
hugo --minify
cd public
git add .
git commit -m "$1"
git push origin main