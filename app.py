"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.get('/api/cupcakes')
def list_all_cupcakes():
    """Return JSON list of cupcakes 
        - [{id, flavor, size...}, ...]
    
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:c_id>')
def list_single_cupcake(c_id):
    """Return JSON with info about single cupcake
    
    """

    cupcake = Cupcake.query.get_or_404(c_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """Create cupcake
        - Returns JSON {'cupcake': {id, flavor, size...}}
    
    """
    image = request.json["image"]
    image = str(image) if image else None

    new_cupcake = Cupcake(
        flavor = request.json["flavor"],
        size = request.json["size"],
        rating = request.json["rating"],
        image = image,
    )
    
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)