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

$publicFiles = @('index.html', 'install.html', 'manifest.json', 'sw.js', 'yc-console-8k3n7q.html', 'regional-portal.html', 'sourcing-portal.html', 'admin-manifest.json', 'developer-partnership.html', 'broker-partnership.html', 'robots.txt', 'sitemap.xml', '1e2cd6976b8c425298b0f3a0d66e3440.txt')
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
Write-Host 'Included: public site, secured administrator console, assets, photo'
