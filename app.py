from flask import Flask, render_template, request, jsonify, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import json
import os

app = Flask(__name__)

# Load pre-trained model and ingredient labels
model = load_model('model/ingredient_model.h5')
with open('data/ingredient_labels.json', 'r') as f:
    labels = json.load(f)

# Load recipes and nutritional info data (replace with API for larger datasets)
with open('data/recipes.json', 'r') as f:
    recipes = json.load(f)

# Helper function to process uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'})

    # Process the image
    image = Image.open(file)
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    ingredient = labels[np.argmax(prediction)]

    # Get recipes for detected ingredient
    recommended_recipes = [recipe for recipe in recipes if ingredient in recipe['ingredients']]

    return render_template('recipe.html', ingredient=ingredient, recipes=recommended_recipes)

@app.route('/add_to_pantry', methods=['POST'])
def add_to_pantry():
    # Logic for pantry inventory tracking
    ingredient = request.form.get('ingredient')
    # Save ingredient to user pantry (use session or database)
    # Return pantry page with updated items
    return redirect(url_for('pantry'))

@app.route('/generate_shopping_list', methods=['POST'])
def generate_shopping_list():
    # Compare selected recipe ingredients with pantry items and create list of missing ingredients
    # Return shopping list page
    return render_template('shopping_list.html', shopping_list=missing_items)

if __name__ == '__main__':
    app.run(debug=True)
