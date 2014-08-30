from flask import Flask
from frontend.views import frontend
from npc.views import npc
from houses.views import houses
from armies.views import armies

app = Flask(__name__)
app.register_blueprint(frontend)
app.register_blueprint(npc)
app.register_blueprint(houses)
app.register_blueprint(armies)