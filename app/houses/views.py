from flask import Blueprint, request, render_template, jsonify
from housesGenerator import House
from holdings import Holdings

houses = Blueprint('houses', __name__, url_prefix='/houses')


@houses.route('/')
def index():
    return render_template('houses.html')


@houses.route('/houseGenerator', methods=['GET', 'POST'])
def houseGenerator():
    realm = request.args.get('realm')
    size = request.args.get('size')
    foundation = request.args.get('foundation')
    name = request.args.get('name')
    house = House.startingResources(realm, size, foundation, name)
    from holdings import holdingsData
    generatedHouse = Holdings(holdingsData).generateAllHoldings(house, realm)
    return jsonify(generatedHouse)
