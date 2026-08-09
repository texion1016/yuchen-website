$ErrorActionPreference = 'Stop'

$token = [Environment]::GetEnvironmentVariable('CLOUDFLARE_API_TOKEN', 'User')
if ([string]::IsNullOrWhiteSpace($token)) {
  throw 'Cloudflare deployment token is missing. Set CLOUDFLARE_API_TOKEN in the Windows user environment first.'
}

$projectRoot = Split-Path $PSScriptRoot -Parent
$nodeBin = 'C:\Users\ROG\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin'
if (-not (Test-Path (Join-Path $nodeBin 'node.exe'))) {
  throw 'The Node.js runtime required for deployment was not found.'
}

$env:PATH = "$nodeBin;$env:PATH"
$env:CLOUDFLARE_API_TOKEN = $token

& (Join-Path $PSScriptRoot 'build-cloudflare-deploy.ps1')
& pnpm dlx wrangler@4.107.0 deploy --config (Join-Path $projectRoot 'wrangler.jsonc')
if ($LASTEXITCODE -ne 0) {
  throw "Cloudflare deployment failed with exit code $LASTEXITCODE."
}

& (Join-Path $PSScriptRoot 'submit-indexnow.ps1')
