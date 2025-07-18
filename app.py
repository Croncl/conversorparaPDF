from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os
from conversor import PDFConverter

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurações
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'bmp', 'html', 'htm'}

# Garante que a pasta de uploads existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nenhum arquivo enviado')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            output_filename = f"{os.path.splitext(filename)[0]}.pdf"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

            converter = PDFConverter()
            success, message = converter.convert_to_pdf(input_path, output_path)

            if success:
                return redirect(url_for('download', filename=output_filename))
            else:
                flash(f"Erro na conversão: {message}")
                return redirect(request.url)
        else:
            flash('Arquivo com extensão não permitida')
            return redirect(request.url)

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
