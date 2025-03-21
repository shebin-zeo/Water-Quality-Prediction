# Water Quality Prediction

This project uses machine learning to predict the quality of water based on several chemical and physical properties. The model helps to determine if water is safe for drinking, unsafe for drinking, or not suitable for drinking but fine for other uses. 

## Features
- Predict water quality based on inputs like pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.
- Results display whether the water is "Safe to Drink", "Unsafe to Drink", or "Not Suitable for Drinking, but Fine for Other Uses".
- Frontend interface built using HTML, Bootstrap, and JavaScript.
- Backend built using Flask and scikit-learn to load the pre-trained water quality model (`water_quality_model.pkl`).

## Requirements

### Backend
- Python 3.x
- Flask
- scikit-learn
- pickle

### Frontend
- HTML
- Bootstrap
- JavaScript (jQuery)

## Setup

### 1. Clone the repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/shebin-zeo/water-quality-prediction.git
