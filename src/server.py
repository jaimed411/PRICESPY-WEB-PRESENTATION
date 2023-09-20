try:
    from flask import Flask, send_from_directory
except ImportError:
    print("You don't have Flask installed, run `$ pip3 install flask` and try again")
    exit(1)

import os, subprocess

# Define el directorio base para archivos estáticos
static_file_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Deshabilita la caché

# Función para servir el archivo index.html
@app.route('/', methods=['GET'])
def serve_index():
    index_path = os.path.join(static_file_dir, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(static_file_dir, 'index.html')
    else:
        return "<h1 align='center'>404</h1><h2 align='center'>Archivo index.html no encontrado</h2>"

# Función para servir otros archivos
@app.route('/<path:path>', methods=['GET'])
def serve_other_files(path):
    file_path = os.path.join(static_file_dir, path)
    if os.path.exists(file_path):
        return send_from_directory(static_file_dir, path)
    else:
        return "<h1 align='center'>404</h1><h2 align='center'>Archivo no encontrado</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, extra_files=['./'])
