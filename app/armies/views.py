from flask import Blueprint, render_template


armies = Blueprint('armies', __name__, url_prefix='/armies')


@armies.route('/')
def index():
	return render_template('armies.html')