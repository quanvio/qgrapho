# QGrapho one-click installer (Windows PowerShell)
# Usage: irm .../install.ps1 | iex  OR  .\scripts\install.ps1

$ErrorActionPreference = "Stop"

$QgraphoHome = if ($env:QGRAPHO_HOME) { $env:QGRAPHO_HOME } else { Join-Path $env:USERPROFILE ".qgrapho" }
$FromSource  = $args -contains "--from-source"
$RepoRoot    = Split-Path $PSScriptRoot -Parent

function Write-Step($msg) { Write-Host "==> $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host " ok  $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host " !!  $msg" -ForegroundColor Yellow }

Write-Step "Installing QGrapho to $QgraphoHome"
New-Item -ItemType Directory -Force -Path $QgraphoHome, (Join-Path $QgraphoHome "data\graphs"), (Join-Path $QgraphoHome "config") | Out-Null

$env:QGRAPHO_HOME = $QgraphoHome
$env:QGRAPHO_SRC  = $RepoRoot

if (Test-Path (Join-Path $RepoRoot "config\qgrapho.example.toml")) {
    Copy-Item (Join-Path $RepoRoot "config\qgrapho.example.toml") (Join-Path $QgraphoHome "config\qgrapho.example.toml") -Force
    $dest = Join-Path $QgraphoHome "config.toml"
    if (-not (Test-Path $dest)) {
        Copy-Item (Join-Path $RepoRoot "config\qgrapho.example.toml") $dest -Force
    }
}

$python = $null
foreach ($cmd in @("python", "python3", "py")) {
    if (Get-Command $cmd -ErrorAction SilentlyContinue) {
        $python = $cmd
        break
    }
}

if ($python) {
    Write-Step "Installing QGrapho CLI via pip"
    & $python -m pip install --upgrade pip 2>$null
    & $python -m pip install -e $RepoRoot
    if ($LASTEXITCODE -eq 0) { Write-Ok "qgrapho CLI installed" }
    else { Write-Warn "pip install failed — ensure Python 3.11+" }
} else {
    Write-Warn "Python not found — install Python 3.11+ from python.org"
}

if ($FromSource) {
    Write-Ok "Source: $RepoRoot"
}

Write-Ok "QGrapho installed"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. qgrapho --version"
Write-Host "  2. qgrapho init"
Write-Host "  3. qgrapho doctor"
Write-Host "  4. qgrapho start"
Write-Host ""
Write-Host "Development: see ROADMAP.md"
