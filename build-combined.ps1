# build-combined.ps1
# Regenerates combined-textbook.md from all numbered section files in content/,
# skipping _index.md and anything outside the chapter-N.N.md naming pattern.
# Run from the repo root (duragauge.github.io).

Get-ChildItem -Path .\content -Recurse -Filter "*.md" |
  Where-Object { $_.Name -match '^\d+\.\d+\.md$' } |
  Sort-Object { [version]$_.BaseName } |
  Get-Content |
  Set-Content combined-textbook.md

Write-Host "combined-textbook.md regenerated."