import sys
import os
import subprocess
from dotenv import load_dotenv

load_dotenv() # Añade esta línea para que lea el archivo .env

# ... resto de tu código ...
# Tu línea actual que lee la llave se queda exactamente igual:
# gemini_key = sys.argv[1] if len(sys.argv) > 1 else os.getenv("GEMINI_API_KEY", "")

def run_step(command: str, description: str):
    print("\n" + "=" * 50)
    print(f"▶ {description}")
    print("=" * 50)
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Error en la etapa: {description}")
        sys.exit(result.returncode)

def main():
    print("🚀 INICIANDO PIPELINE DE REDACCIÓN DE BOLETÍN IA (MODO LOCAL)")

    # Solo necesitamos la llave de Gemini para operar
    gemini_key = sys.argv[1] if len(sys.argv) > 1 else os.getenv("GEMINI_API_KEY", "")

    if not gemini_key:
        print("❌ Error: Falta la credencial GEMINI_API_KEY")
        sys.exit(1)

    # 1. Scraping de URLs
    run_step("python scraper/fetch_sources.py", "FASE 1: Web Scraping de Noticias")

    # 2. Redacción y Formato Visual
    run_step(f"python redactor/generate_draft_gemini.py '{gemini_key}'", "FASE 2A: Redacción B2B con Gemini")
    run_step("python redactor/generate_charts.py", "FASE 2B: Generación Visual de Gráficas de Datos")

    # LA FASE 3 HA SIDO ELIMINADA. EL SCRIPT TERMINA AQUÍ.

    print("\n" + "=" * 50)
    print("🎉 PIPELINE FINALIZADO CON ÉXITO")
    print("✅ El borrador ya está disponible en la carpeta drafts/.")
    print("👉 Ábrelo, cópialo y pégalo en tu chat del 'Sistema Maestro'.")
    print("=" * 50)

if __name__ == "__main__":
    main()
