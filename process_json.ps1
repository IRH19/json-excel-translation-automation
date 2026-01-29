# 1. Create an output directory if it doesn't exist
$outputDir = "output_processed"
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
    Write-Host "Created folder: $outputDir" -ForegroundColor Cyan
}

# 2. Get all JSON files in the current folder (excluding other folders)
$jsonFiles = Get-ChildItem -Filter "*.json"

# 3. Loop through each file
foreach ($file in $jsonFiles) {
    $inputPath = $file.FullName
    $outputPath = Join-Path $outputDir $file.Name

    Write-Host "Processing: $($file.Name)..." -NoNewline

    # --- THE JQ COMMAND ---
    # Currently set to '.' which just formats/pretty-prints the JSON.
    # You can change '.' to any jq filter you need.
    Get-Content $inputPath | .\jq.exe '.' | Set-Content $outputPath
    # ----------------------

    Write-Host " Done!" -ForegroundColor Green
}

Write-Host "`nAll files processed! Check the '$outputDir' folder." -ForegroundColor Yellow