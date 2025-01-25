from flask import Flask, request, jsonify

app = Flask(__name__)

def classify_water_quality(pH, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    # Define thresholds for water quality classification

    if (pH < 6.5 or pH > 8.5):
        return "Unsafe to Drink"
    if hardness > 250:
        return "Unsafe to Drink"
    if solids > 500:
        return "Unsafe to Drink"
    if chloramines > 4:
        return "Unsafe to Drink"
    if sulfate > 250:
        return "Unsafe to Drink"
    if conductivity > 1000:
        return "Unsafe to Drink"
    if organic_carbon > 2:
        return "Unsafe to Drink"
    if trihalomethanes > 80:
        return "Unsafe to Drink"
    if turbidity > 5:
        return "Unsafe to Drink"
    
    # Additional categories based on use cases
    if pH >= 6.5 and pH <= 8.5 and solids <= 500:
        return "Not Suitable for Drinking, but Fine for Other Uses"
    
    return "Safe to Drink"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        pH = float(request.form['ph'])
        hardness = float(request.form['hardness'])
        solids = float(request.form['solids'])
        chloramines = float(request.form['chloramines'])
        sulfate = float(request.form['sulfate'])
        conductivity = float(request.form['conductivity'])
        organic_carbon = float(request.form['organic_carbon'])
        trihalomethanes = float(request.form['trihalomethanes'])
        turbidity = float(request.form['turbidity'])

        # Get water quality prediction
        prediction = classify_water_quality(pH, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
        
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
