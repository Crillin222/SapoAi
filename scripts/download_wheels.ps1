# Navega para a pasta scripts (corrigido com aspas)
cd "E:\Sapo Ai\scripts"

# Cria a pasta wheels se não existir
if (!(Test-Path -Path "wheels")) {
    New-Item -ItemType Directory -Path "wheels"
}

# Baixa todas as dependências do requirements.txt no formato Wheel
Write-Host "[*] Baixando dependências para instalação offline..." -ForegroundColor Cyan
pip download -r requirements.txt -d wheels

Write-Host "`n[+] Download concluído! Todos os arquivos estão em scripts/wheels/" -ForegroundColor Green
Write-Host "[!] Agora, faça o PUSH para o seu GitHub e o PULL no notebook corporativo." -ForegroundColor Yellow
