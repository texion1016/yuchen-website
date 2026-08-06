$ErrorActionPreference = 'Stop'

$token = [Environment]::GetEnvironmentVariable('CLOUDFLARE_API_TOKEN', 'User')
if ([string]::IsNullOrWhiteSpace($token)) {
  throw '找不到 Cloudflare 部署 Token。请先在此电脑的 Windows 使用者环境变量设定 CLOUDFLARE_API_TOKEN。'
}

$projectRoot = Split-Path $PSScriptRoot -Parent
$nodeBin = 'C:\Users\ROG\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin'
if (-not (Test-Path (Join-Path $nodeBin 'node.exe'))) {
  throw '找不到部署所需的 Node.js 执行环境。'
}

$env:PATH = "$nodeBin;$env:PATH"
$env:CLOUDFLARE_API_TOKEN = $token

& (Join-Path $PSScriptRoot 'build-cloudflare-deploy.ps1')
& pnpm dlx wrangler@4.107.0 deploy --config (Join-Path $projectRoot 'wrangler.jsonc')
if ($LASTEXITCODE -ne 0) {
  throw "Cloudflare 部署失败（退出码 $LASTEXITCODE）。"
}
