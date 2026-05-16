import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route("/config")
def config():
    """
    Azure App Service reads these from environment variables.
    Those env vars are Key Vault references, so Azure automatically
    resolves them to the actual Function URLs from Key Vault.
    """
    return jsonify({
        "saveLogUrl":      os.environ.get("SAVE_LOG_URL", ""),
        "getSummaryUrl":   os.environ.get("GET_SUMMARY_URL", ""),
        "timerSummaryUrl": os.environ.get("TIMER_SUMMARY_URL", "")
    })


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
