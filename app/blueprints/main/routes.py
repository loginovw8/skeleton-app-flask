from flask import render_template
from app.blueprints.main import bp


@bp.route('/')
def main():
    return render_template('index.html.jinja')
