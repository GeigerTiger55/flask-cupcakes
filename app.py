"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get('/')
def show_home_page():
    """Shows cupcakes"""
    return render_template("cupcakes.html")

@app.get('/api/cupcakes')
def list_all_cupcakes():
    """Return JSON list of cupcakes 
        - {'cupcakes': [{id, flavor, size, rating, image}, ...]}

    """

    cupcakes = Cupcake.query.order_by('flavor', 'size').all()
    serialized = [c.serialize() for c in cupcakes]
    return jsonify(cupcakes=serialized)


@app.get('/api/cupcakes/<int:c_id>')
def list_single_cupcake(c_id):
    """Return JSON with info about single cupcake
        Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(c_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post('/api/cupcakes')
def create_cupcake():
    """Create cupcake
        - Returns JSON {'cupcake': {id, flavor, size, rating, image}}

    """
    image = request.json["image"] or None

    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=image,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch('/api/cupcakes/<int:c_id>')
def update_cupcake_info(c_id):
    """Update cupcake info
        - Returns JSON {'cupcake': {id, flavor, size, rating, image}}
        with updated info
    """

    cupcake = Cupcake.query.get_or_404(c_id)
    cupcake.flavor = request.json['flavor'] or cupcake.flavor
    cupcake.size = request.json['size'] or cupcake.size
    cupcake.rating = request.json['rating'] or cupcake.rating
    cupcake.image = request.json['image'] or cupcake.image

    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)


@app.delete('/api/cupcakes/<int:c_id>')
def delete_cupcake(c_id):
    """Delete cupcake with c_id
        - Returns JSON {'deleted': cupcake_id}

    """

    cupcake = Cupcake.query.get_or_404(c_id)
    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(deleted=c_id), 200)
