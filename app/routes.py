from flask import Blueprint, jsonify, request
from .weather import get_weather
from .recommend import recommend_clothing

bp = Blueprint("main", __name__)

@bp.route("/recommend")
def recommend():
    city = request.args.get("city", "Munich")

    weather = get_weather(city)
    outfit = recommend_clothing(weather)

    return jsonify({
        "city": city,
        "weather": weather,
        "recommendation": outfit
    })

@bp.route("/")
def home():
    return "hello world"