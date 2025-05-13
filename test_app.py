from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a test app."

@app.route("/train")
def train_route():
    try:
        # Simplified version for testing
        return "Training would start here. This is a test endpoint."
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/predict', methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            # Simplified version for testing
            return "This would process your uploaded file and return predictions."
        else:
            return "This would show a file upload form. This is a test endpoint."
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route("/healthz")
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
