$ErrorActionPreference = 'Stop'

$indexNowKey = '1e2cd6976b8c425298b0f3a0d66e3440'
$siteHost = 'yuchen-realty.com'
$urls = @(
  'https://yuchen-realty.com/',
  'https://yuchen-realty.com/install.html'
)

$payload = @{
  host = $siteHost
  key = $indexNowKey
  keyLocation = "https://$siteHost/$indexNowKey.txt"
  urlList = $urls
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Method Post -Uri 'https://api.indexnow.org/indexnow' -ContentType 'application/json; charset=utf-8' -Body $payload | Out-Null
Write-Host 'IndexNow submission accepted for the public website URLs.'
