import os
import io
import pytest
from unittest.mock import patch
from pathlib import Path
from pdf_converter import PDFConverter  # ajuste para o caminho real do seu módulo

@pytest.fixture
def converter():
    return PDFConverter()

def test_convert_image_to_pdf_mocked(converter, tmp_path):
    # Criar um arquivo fictício com extensão de imagem
    fake_img = tmp_path / "fake_image.png"
    fake_img.write_bytes(b"fake image content")

    # Mockar o método real que converte imagem para pdf
    with patch.object(PDFConverter, "_convert_image_to_pdf", return_value=(True, "")) as mock_method:
        success, msg = converter.convert_to_pdf(str(fake_img), str(tmp_path / "saida.pdf"))
        mock_method.assert_called_once()
        assert success
        assert msg == ""

def test_convert_html_to_pdf_mocked(converter, tmp_path):
    fake_html = tmp_path / "fake.html"
    fake_html.write_text("<html><body>Test</body></html>")

    with patch.object(PDFConverter, "_convert_html_to_pdf", return_value=(True, "")) as mock_method:
        # Forçar o wkhtmltopdf_path para simular que está disponível
        converter.wkhtmltopdf_path = "/usr/bin/wkhtmltopdf"
        success, msg = converter.convert_to_pdf(str(fake_html), str(tmp_path / "saida.pdf"))
        mock_method.assert_called_once()
        assert success
        assert msg == ""

def test_convert_unsupported_file(converter, tmp_path):
    fake_txt = tmp_path / "file.txt"
    fake_txt.write_text("test")

    success, msg = converter.convert_to_pdf(str(fake_txt), str(tmp_path / "saida.pdf"))
    assert not success
    assert "Formato não suportado" in msg

def test_file_not_found(converter):
    success, msg = converter.convert_to_pdf("arquivo_que_nao_existe.xyz", "saida.pdf")
    assert not success
    assert "Arquivo de entrada não encontrado" in msg
