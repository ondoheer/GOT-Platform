from flask import Blueprint, request, render_template, jsonify
from NPCgenerator import generateNPC

npc = Blueprint('npc', __name__, url_prefix='/npc')


@npc.route('/')
def index():
    return render_template('npc.html')


@npc.route('/NPCgenerator', methods=['GET'])
def NPCgenerator():
    genderReceived = request.args['gender']
    if genderReceived == 'male':
        gender = 'male'
    elif genderReceived == 'female':
        gender = 'female'
    age = request.args['age']
    generatedNPC = generateNPC.generateNPC(gender, age)
    return jsonify(generatedNPC)
