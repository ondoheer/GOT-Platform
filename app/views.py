from app import app

from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask.ext.stormpath import (
    StormpathManager,
    StormpathError,
    User,
    login_user,
    user,
    login_required,
    logout_user
)
from NPCgenerator import generateNPC
from housesGenerator import House
from holdings import Holdings



@app.route('/')
def index():
	
    return render_template('index.html')

# Ruta fisica del generadorNPC


@app.route('/npc')
def npc():
    return render_template('npc.html')

# funcion de la aplicacion que corre el generador


@app.route('/NPCgenerator', methods=['GET'])
def NPCgenerator():
    genderReceived = request.args['gender']
    if genderReceived == 'male':
        gender = 'male'
    elif genderReceived == 'female':
        gender = 'female'
    age = request.args['age']
    generatedNPC = generateNPC.generateNPC(gender, age)
    return jsonify(generatedNPC)


# funcion que genera las casas
@app.route('/houses')
def houses():
    return render_template('houses.html')


@app.route('/houseGenerator', methods=['GET', 'POST'])
def houseGenerator():
    realm = request.args.get('realm')
    size = request.args.get('size')
    foundation = request.args.get('foundation')
    name = request.args.get('name')
    house = House.startingResources(realm, size, foundation, name)
    from holdings import holdingsData
    generatedHouse = Holdings(holdingsData).generateAllHoldings(house, realm)
    return jsonify(generatedHouse)


# funcion que calculara precios de items
@app.route('/store')
def store():
    return 'Pagina en construccion'


# funcion que calculara precios de items
@app.route('/character')
def other():
    return 'Aqui ira la hoja de personaje'
