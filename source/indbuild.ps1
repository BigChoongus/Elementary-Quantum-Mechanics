# Build Index html

 pandoc --mathjax -s "index.md" `
    --include-in-header "mathjax-config.html" `
    --include-before-body "preamble.tex" `
    -c "style.css" `
    -o "../docs/index.html"