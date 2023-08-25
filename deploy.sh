cd public
rm -rf *
cd ..
cd python
python3 render-appearances-spreadsheet.py
cd ..
git add .
git commit -m "$1"
git push origin main
hugo --minify
cp CNAME public
cd public
git add .
git commit -m "$1"
git push -f origin main