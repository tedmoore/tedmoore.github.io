cd public
rm -rf *
cd ..
python3 python/render-appearances-spreadsheet.py
hugo --minify
cp CNAME public
cd public
git add .
git commit -m "$1"
git push origin main