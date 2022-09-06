### run image optim on all the files
find . -name '*.jpg' -exec /Applications/ImageOptim.app/Contents/MacOS/ImageOptim {} +
find . -name '*.jpeg' -exec /Applications/ImageOptim.app/Contents/MacOS/ImageOptim {} +

### batch run mogrify including sub directories
find . -name '*.png' -exec mogrify -format jpg -quality 60 {} +