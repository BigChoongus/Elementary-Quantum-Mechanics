for ($i=1; $i -le 9; $i++) {
    $prev = $i - 1
    $next = $i + 1

    # Generate navigation links dynamically
    if ($prev -ge 1) {
        $prev_link = "<a href='$prev.html'>&larr; Previous Chapter</a>"
    } else {
        $prev_link = ""
    }
    
    if ($next -le 9) {
        $next_link = "<a href='$next.html'>Next Chapter &rarr;</a>"
    } else {
        $next_link = ""
    }

    # Replace placeholders in footer.html and save a temp version
    (Get-Content "footer.html") -replace "{{prev_link}}", $prev_link -replace "{{next_link}}", $next_link | Set-Content "footer-temp.html"

    Write-Output "Converting $i.tex to docs/$i.html..."
    
    # Correctly use double dashes for Pandoc inside PowerShell
    & pandoc --mathjax -s "$i.tex" `
        --include-in-header "mathjax-config.html" `
        --include-before-body "preamble.tex" `
        --include-after-body "footer-temp.html" `
        -c "style.css" `
        -o "../docs/$i.html"
}

# Cleanup temp footer file
Remove-Item "footer-temp.html"


