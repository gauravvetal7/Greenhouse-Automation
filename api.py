from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# ----------------------------
# Create data folder if missing
# ----------------------------
os.makedirs("data", exist_ok=True)

DATA_FILE = "data/sensor_data.json"

# ----------------------------
# Create default JSON file
# ----------------------------
if not os.path.exists(DATA_FILE):
    default_data = {
        "temperature": 0,
        "humidity": 0,
        "soil": 0,
        "light": 0
    }

    with open(DATA_FILE, "w") as f:
        json.dump(default_data, f, indent=4)


# ----------------------------
# Home Page
# ----------------------------
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>🌿 Smart Greenhouse API</h2>
    <h3>Server is Running Successfully!</h3>
    <p>Use <b>POST /update</b> to send sensor data.</p>
    """


# ----------------------------
# Receive Sensor Data
# ----------------------------
@app.route("/update", methods=["POST"])
def update():

    try:

        sensor_data = request.get_json(force=True)

        if sensor_data is None:
            return jsonify({
                "status": "error",
                "message": "No JSON received"
            }), 400

        print("\n========== DATA RECEIVED ==========")
        print(sensor_data)
        print("===================================\n")

        with open(DATA_FILE, "w") as f:
            json.dump(sensor_data, f, indent=4)

        return jsonify({
            "status": "success",
            "message": "Sensor data updated"
        }), 200

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


# ----------------------------
# View Latest Sensor Data
# ----------------------------
@app.route("/sensor", methods=["GET"])
def sensor():

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return jsonify(data)


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":

    print("====================================")
    print(" Smart Greenhouse Flask API Started ")
    print("====================================")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

    @app.route("/control", methods=["POST"])
    def control():

        control_data = request.get_json()

        with open("data/device_control.json", "w") as file:
            json.dump(control_data, file, indent=4)

        return jsonify({
            "status": "success"
    })