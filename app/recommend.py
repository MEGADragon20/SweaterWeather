def recommend_clothing(weather):
    temp = weather["temp"]
    rain = weather["rain"]
    wind = weather["wind"]

    if temp < 5:
        base = "Winter jacket"
    elif temp < 15:
        base = "Light jacket"
    elif temp < 25:
        base = "Sweater"
    else:
        base = "T-shirt"

    if rain > 50 and wind < 8:
        return f"{base} and an umbrella."
    elif rain > 0:
        return f"{base} and a raincoat."
    
    return f"{base}."
