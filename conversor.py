import os
import shutil
from pathlib import Path
from typing import Tuple, Optional

# Dependências opcionais
try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

try:
    import pdfkit
    HAS_PDFKIT = True
except ImportError:
    HAS_PDFKIT = False


class PDFConverter:
    def __init__(self):
        self.wkhtmltopdf_path = self._find_wkhtmltopdf()
        self._check_dependencies()

    def _check_dependencies(self):
        """Verifica e reporta dependências ausentes."""
        if not HAS_PILLOW:
            print("[AVISO] Pillow não instalado - conversão de imagens desativada")
        if not HAS_PDFKIT:
            print("[AVISO] pdfkit não instalado - conversão HTML desativada")
        elif not self.wkhtmltopdf_path:
            print("[AVISO] wkhtmltopdf não encontrado - conversão HTML desativada")

    def _find_wkhtmltopdf(self) -> Optional[str]:
        """Tenta encontrar o wkhtmltopdf no sistema."""
        possible_paths = [
            r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe",
            r"C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe",
            r"C:\wkhtmltopdf\bin\wkhtmltopdf.exe",
            "/usr/local/bin/wkhtmltopdf",
            "/usr/bin/wkhtmltopdf",
        ]
        
        # Verifica caminhos possíveis
        for path in possible_paths:
            if os.path.exists(path):
                return path

        # Tenta encontrar pelo PATH do sistema
        try:
            path = shutil.which("wkhtmltopdf")
            if path:
                return path
        except:
            pass

        return None

    def convert_to_pdf(self, input_path: str, output_path: str) -> Tuple[bool, str]:
        """Converte um arquivo para PDF."""
        if not os.path.exists(input_path):
            return False, "Arquivo de entrada não encontrado"

        ext = Path(input_path).suffix.lower()

        if ext in (".jpg", ".jpeg", ".png", ".bmp") and HAS_PILLOW:
            return self._convert_image_to_pdf(input_path, output_path)

        elif ext in (".html", ".htm"):
            if not HAS_PDFKIT:
                return False, "Conversão de HTML requer pdfkit"
            if not self.wkhtmltopdf_path:
                return False, "wkhtmltopdf não encontrado no sistema"
            return self._convert_html_to_pdf(input_path, output_path)

        return False, f"Formato não suportado: {ext}"

    def _convert_image_to_pdf(self, input_path: str, output_path: str) -> Tuple[bool, str]:
        """Converte imagem para PDF usando Pillow."""
        try:
            img = Image.open(input_path)
            if img.mode == "RGBA":
                img = img.convert("RGB")
            img.save(output_path, "PDF", resolution=100.0)
            return True, ""
        except Exception as e:
            return False, f"Erro ao converter imagem: {str(e)}"

    def _convert_html_to_pdf(self, input_path: str, output_path: str) -> Tuple[bool, str]:
        """Converte HTML para PDF usando pdfkit/wkhtmltopdf."""
        try:
            options = {
                "encoding": "UTF-8",
                "quiet": "",
                "enable-local-file-access": None
            }
            pdfkit.from_file(
                input_path,
                output_path,
                options=options,
                configuration=pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
            )
            return True, ""
        except Exception as e:
            return False, f"Erro ao converter HTML: {str(e)}"