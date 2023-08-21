@echo off

for %%f in (*.py) do (
    echo Ejecutando el script %%f
    python "%%f"
    echo Script %%f finalizado.
    echo.
)

pause
