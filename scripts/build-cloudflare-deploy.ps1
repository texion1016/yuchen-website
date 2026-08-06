$ErrorActionPreference = 'Stop'

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$publishDir = Join-Path $projectRoot 'cloudflare-deploy'
$expectedPublishDir = [System.IO.Path]::GetFullPath((Join-Path $projectRoot 'cloudflare-deploy'))

if ($publishDir -ne $expectedPublishDir) {
  throw "Refusing to modify an unexpected publish directory: $publishDir"
}

if (Test-Path -LiteralPath $publishDir) {
  Remove-Item -LiteralPath $publishDir -Recurse -Force
}

New-Item -ItemType Directory -Path $publishDir | Out-Null

$publicFiles = @('index.html', 'install.html', 'manifest.json')
foreach ($file in $publicFiles) {
  $source = Join-Path $projectRoot $file
  if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
    throw "Required public file is missing: $file"
  }
  Copy-Item -LiteralPath $source -Destination $publishDir
}

foreach ($directory in @('assets', 'photo')) {
  $source = Join-Path $projectRoot $directory
  if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "Required public directory is missing: $directory"
  }
  Copy-Item -LiteralPath $source -Destination $publishDir -Recurse
}

Write-Host "Cloudflare upload folder ready: $publishDir"
Write-Host 'Included: index.html, install.html, manifest.json, assets, photo'
