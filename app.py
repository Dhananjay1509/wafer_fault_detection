
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os, sys

from src.pipeline.train_pipeline import TraininingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TraininingPipeline()
        train_pipeline.run_pipeline()
        return "Training Completed."
    except Exception as e:
        error_message = str(e)
        lg.error(f"Training error: {error_message}")
        return f"Training Error: {error_message}", 500

@app.route('/predict', methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()
            lg.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                            download_name=prediction_file_detail.prediction_file_name,
                            as_attachment=True)
        else:
            return render_template('upload_file.html')
    except Exception as e:
        error_message = str(e)
        lg.error(f"Prediction error: {error_message}")
        return f"Prediction Error: {error_message}", 500

@app.route("/healthz")
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    try:
        # Only import keep_alive when running in Replit environment
        if os.environ.get('REPL_ID'):
            from keep_alive import keep_alive, ping_self
            from threading import Thread
            
            # Start the keep_alive server
            keep_alive()
            
            # Start the ping thread
            ping_thread = Thread(target=ping_self)
            ping_thread.daemon = True
            ping_thread.start()
        
        # Try different ports if the default is in use
        port = int(os.environ.get("PORT", 5000))
        lg.info(f"Starting server on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        lg.error(f"Failed to start server: {str(e)}")
        raise CustomException(e, sys)




