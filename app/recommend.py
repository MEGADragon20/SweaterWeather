def recommend_clothing(weather):
    temp = weather["temp"]
    rain = weather["rain"]

    if temp < 5:
        base = "winter jacket"
    elif temp < 15:
        base = "light jacket"
    elif temp < 25:
        base = "sweater"
    else:
        base = "t-shirt"

    if rain > 0:
        return f"{base} and a raincoat"
    return base
