<#
=================================================================================
SCRIPT: build-combined.ps1
DESCRIPTION: 
  Combines all individual chapter section Markdown files into a single file 
  (`combined-textbook.md`) for easy proofreading, printing, or full-book LLM-analysis.

HOW TO RUN THIS SCRIPT:

  Option 1: From VS Code (Recommended)
    1. Open the built-in terminal (Ctrl + ` or View -> Terminal).
    2. Make sure the dropdown at the top right of the terminal is set to "PowerShell".
    3. Run:
          .\build-combined.ps1
    4. If there is a "script execution is disabled" error, run the following to bypass:
          powershell -ExecutionPolicy Bypass -File .\build-combined.ps1

  Option 2: From Windows PowerShell (Standalone App)
    1. Open Windows PowerShell.
    2. Navigate (cd) to the project root directory:
          cd C:\path\to\duragauge.github.io
    3. Run:
          .\build-combined.ps1

  Option 3: From Windows Command Prompt (cmd.exe)
    Call PowerShell directly:
          powershell -ExecutionPolicy Bypass -File .\build-combined.ps1

WHAT THIS SCRIPT DOES:
  1. Creates/clears `combined-textbook.md` in the root folder.
  2. Adds a date/time stamp to the very top of the file as an HTML comment.
  3. Scans the `content/` folder for files named `X.Y.md` (e.g., `1.1.md`, `2.3.md`).
  4. Automatically SKIPS:
     - All practice files (e.g., `1.1-practice.md` - excluded by regex).
     - Section index files (e.g., `_index.md`).
  5. Sorts the files numerically/version-wise (so 1.10 comes after 1.9, not before).
  6. Appends all content into `combined-textbook.md`.
=================================================================================
#>

# 1. Create the timestamp string
$timestamp = "<!-- Generated on: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -->`n`n"

# 2. Write the024-01-01 / timestamp to the file first (overwriting previous contents)
Set-Content -Path .\combined-textbook.md -Value $timestamp -Encoding UTF8

# 3. Find, sort, and append all matching chapter files
Get-ChildItem -Path .\content -Recurse -Filter "*.md" |
  Where-Object { $_.Name -match '^\d+\.\d+\.md$' } |
  Sort-Object { [version]$_.BaseName } |
  Get-Content |
  Add-Content .\combined-textbook.md -Encoding UTF8

Write-Host "Success! 'combined-textbook.md' has been regenerated with a new timestamp." -ForegroundColor Green