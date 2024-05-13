from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from recipe_parser import parse
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class foods(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    cook_time_min = db.Column(db.Integer, nullable = False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/result', methods=['GET'])
def result():
    food = request.args.get('food')
    if food:
        result = parse(food)
        if not result:
            return 'There is nothing we can do'
        else:
            image_url = result['image']
            title = result['label']
            ingredients = result['ingredients']
            health = result['healthLabels'][0:10]
            return render_template('food.html', image = image_url, full_title = title, ingredients = ingredients, health=health)
    return render_template('food.html')

@app.route('/recomendation/<string:label>')
def recomend(label):
    result = parse(label)
    if not result:
        return 'There is nothing we can do'
    else:
        image_url = result['image']
        title = result['label']
        ingredients = result['ingredients']
        health = result['healthLabels'][0:10]
    return render_template('food.html', image = image_url, full_title = title, ingredients = ingredients, health=health )

if __name__ == '__main__':
    app.run(debug=True)
