from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route("/api/v1/healthz")
def health():
   return jsonify({
      "status": "up"
   })

@app.route("/api/v1/details")
def details():
   return jsonify({
      "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "hostname": socket.gethostname(),
      "message": "You are a conqueror of worlds! 3>"
   })

app.run(host="0.0.0.0")