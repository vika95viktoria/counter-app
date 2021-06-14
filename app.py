from flask import Flask, render_template, request, send_file
from count_server import count_medicine
from werkzeug.exceptions import HTTPException
from file_manager import list_all_files_with_ext, delete_file_from_disk, delete_files
import logging
import os

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(e)
    if isinstance(e, HTTPException):
        return e
    return render_template("500_generic.html", e=e), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def save_file_and_upload_file_to_bucket():
    old_files = list_all_files_with_ext(".xlsx")
    delete_files(old_files)
    if request.method == 'POST':
        f = request.files['file']
        file_name = f.filename
        f.save(file_name)
        logging.info(f"save file {file_name}")
        path = count_medicine(file_name)
        return render_template('index.html', filepath=path)


@app.route('/file/<path:filename>', methods=['GET', 'POST', 'DELETE'])
def download(filename):
    if request.method == 'DELETE':
        delete_file_from_disk(filename)
        return ""
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)