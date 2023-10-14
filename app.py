import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=2000
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
     return """
     Suggest a meal and the simple steps to prepare it with five ingredients including one food supplied from the user. 

    Meal: Fried Rice
    Ingredients: Rice, Onion, Celery, Carrot, Egg
    Steps: 1. Cook rice as the bag instructs. Let cool completely.
    2. Clean and chop the vegetables into a small dice.
    3. Fry the vegetables over medium high heat in a wok until translucent. 
    4. Add the rice and egg to the wok, cooking egg completely through. 
    5. Serve and enjoy.

    Meal: Spaghetti and Marinara
    Ingredients: Spaghetti pasta, tomato sauce, eggplant, onions, mozarella cheese
    Steps: 1. Chop eggplant into 1/2" thick rounds, season and bake at 450 in an oven for 30 minutes. 
    2. Cook spaghetti pasta as instructed on box. Boil until al dente then strain.
    3. Chop and saute the onions over medium heat until translucent.
    4. Add tomato sauce to onions and season to taste. 
    5. Combine cooked eggplant, spaghetti pasta, and sauce in a large pot. Cover with mozarella cheese and let melt.
    6. Serve and enjoy.
     
    Meal: 
    Ingredients: {}
    Steps:""".format(
        animal.capitalize()
    )
