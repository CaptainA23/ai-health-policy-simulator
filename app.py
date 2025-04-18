from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    region = data.get('region')
    policy = data.get('policy')

    # Simulated logic
    response = {
        "mortality_rate": 75,
        "service_coverage": 48
    }

    if policy == "nurse_deployment":
        response["mortality_rate"] -= 15
        response["service_coverage"] += 12
    elif policy == "vaccine_expansion":
        response["mortality_rate"] -= 10
        response["service_coverage"] += 20
    elif policy == "mobile_clinics":
        response["mortality_rate"] -= 8
        response["service_coverage"] += 15

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
