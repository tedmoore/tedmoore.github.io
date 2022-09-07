This repo has the hugo code for building the site. In the `themes` subfolder, there is the theme that i'm using--"ananke"--it is it's own git repo (and there's a forked private github repo for it as well). It is not a submodule though, because I'm `.gitignore`ing the themes folder. The `public` folder (where the static html files go when hugo builds [using `hugo --minify`]) is a git submodule which is the `tedmoore.github.io` github repo that is actually deploying the site using github pages.

### run image optim on all the files
find . -name '*.jpg' -exec /Applications/ImageOptim.app/Contents/MacOS/ImageOptim {} +
find . -name '*.jpeg' -exec /Applications/ImageOptim.app/Contents/MacOS/ImageOptim {} +

### batch run mogrify including sub directories
find . -name '*.png' -exec mogrify -format jpg -quality 60 {} +

### video followed for deploying to github pages
https://www.youtube.com/watch?v=LIFvgrRxdt4