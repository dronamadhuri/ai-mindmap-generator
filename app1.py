from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from utils.parser import extract_text
from utils.nlp import process_text
from utils.mindmap import generate_mindmap

app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")
CORS(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return send_from_directory("../frontend/templates", "index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    result = process_text(text)
    graph = generate_mindmap(result["structure"])

    return jsonify({
        "graph": graph,
        "summary": result["summary"]
    })

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)