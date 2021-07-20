"""Flask app for Cupcakes"""

from flask import Flask, render_template, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import CupcakeForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def load_homepage():
    """Loads index.html"""
    form = CupcakeForm()

    return render_template("index.html", form=form)

@app.route("/cupcakes/<int:cupcake_id>")
def display_cupcake(cupcake_id):
    """Display a cupcake detail"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return render_template("show_cupcake.html", cupcake=cupcake)

@app.route("/api/cupcakes")
def show_cupcakes():
    """"Get data about all cupcakes. Respond with JSON like:
     {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>")
def show_cupcake(cupcake_id):
    """"Get data about a cupcake. Respond with JSON like: 
    {cupcake: {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """"Create a cupcake. Respond with JSON like: 
    {cupcake: {id, flavor, size, rating, image}}"""
    
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None

    new_cupcake = Cupcake(flavor=flavor,
                      size=size,
                      rating=rating,
                      image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake. Respond with JSON of the newly-updated cupcake, like this: 
    {cupcake: {id, flavor, size, rating, image}}"""

    curr_cupcake = Cupcake.query.get_or_404(cupcake_id)

    curr_cupcake.flavor = request.json.get("flavor", curr_cupcake.flavor)
    curr_cupcake.size = request.json.get("size", curr_cupcake.size)
    curr_cupcake.rating = request.json.get("rating", curr_cupcake.rating)

    image = request.json.get("image", None)
    if image is None or image == "":
        curr_cupcake.image = None
    else:
        curr_cupcake.image = image

    # flavor = request.json["flavor"] or curr_cupcake.flavor
    # size = request.json["size"] or curr_cupcake.size
    # rating = request.json["rating"]
    # image = request.json["image"] or None

    # curr_cupcake.flavor = flavor
    # curr_cupcake.size = size
    # curr_cupcake.rating = rating
    # curr_cupcake.image = image

    db.session.commit()

    serialized = curr_cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete cupcake. Respond with JSON like {message: "Deleted"}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted") 





