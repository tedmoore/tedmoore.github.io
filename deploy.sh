cd public
rm -rf *
cd ..
export GITHUB_TOKEN="$(< ../tedsgithubtoken.txt)"
cd python
python3 render-appearances-spreadsheet.py
python3 get-repos.py
cd ..
hugo --minify
cp CNAME public
cd public
git add .
git commit -m "$1"
git push -f origin main