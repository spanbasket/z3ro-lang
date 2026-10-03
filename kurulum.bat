@echo off
chcp 65001 > nul
echo [z3r Kurulumu Başlatılıyor...]

:: 1. AppData içinde z3r klasörü oluşturalım
if not exist "%LocalAppData%\z3r" mkdir "%LocalAppData%\z3r"

:: 2. z3r.exe dosyasını dist klasöründen AppData\z3r klasörüne kopyalayalım
copy /Y "dist\z3r.exe" "%LocalAppData%\z3r\z3r.exe"

:: 3. Windows klasörüne atılacak köprü .bat dosyasını oluşturalım
echo @echo off > "%Temp%\z3r.bat"
echo "%LocalAppData%\z3r\z3r.exe" %%* >> "%Temp%\z3r.bat"

:: 4. Yönetici izniyle z3r.bat dosyasını C:\Windows klasörüne taşıyalım
echo [Bilgi] z3r küresel komut haline getiriliyor (Yönetici izni gerekebilir)...
move /Y "%Temp%\z3r.bat" "C:\Windows\z3r.bat"

echo ==================================================
echo   TEBRİKLER! z3r BAŞARIYLA KURULDU! 
echo ==================================================
pause