from flask import Flask, render_template, request, send_file
import os
from convert import convert_webp

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "hasil"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    files = request.files.getlist("images")
    output_format = request.form.get("format")

    converted_files = []

    for file in files:

        if file.filename == "":
            continue

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        output_filename = os.path.splitext(file.filename)[0] + "." + output_format
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        convert_webp(input_path, output_path, output_format)

        converted_files.append(output_path)

    if converted_files:
        return send_file(converted_files[0], as_attachment=True)

    return "Tidak ada file yang diproses"


if __name__ == "__main__":
    app.run(debug=True)