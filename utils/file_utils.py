import os
from pathlib import Path

def create_output_folder(base_path: str, folder_name: str = "PDF_Converted") -> str:
    """Cria uma pasta para os arquivos convertidos."""
    output_path = os.path.join(base_path, folder_name)
    os.makedirs(output_path, exist_ok=True)
    return output_path

def get_valid_files(folder_path: str, skip_extensions: list = [".pdf"]) -> list:
    """Lista arquivos válidos para conversão."""
    valid_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if Path(file).suffix.lower() not in skip_extensions:
                valid_files.append(os.path.join(root, file))
    return valid_files