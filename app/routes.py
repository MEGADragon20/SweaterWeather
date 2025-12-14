from flask import Blueprint, jsonify, request, render_template
from .weather import get_weather
from .recommend import recommend_clothing

bp = Blueprint("main", __name__)

@bp.route("/recommend")
def recommend():
    city = request.args.get("city", "Munich")
    print("reached ", city)

    weather = get_weather(city)
    outfit = recommend_clothing(weather)

    print("reached nearly the end")
    return render_template(
        "recommend.html",
        city = city,
        weather = weather,
        outfit = outfit
    )

@bp.route("/")
def home():
    return render_template("index.html")