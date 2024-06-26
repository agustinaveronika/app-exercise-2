from flask import Flask, request, jsonify

app = Flask(__name__)

# To get the Zodiac
def get_zodiac(day, month):
    if (month == "March" and day >= 21) or (month == "April" and day <= 19):
        return "Aries"
    elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
        return "Taurus"
    elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
        return "Gemini"
    elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
        return "Cancer"
    elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
        return "Leo"
    elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
        return "Virgo"
    elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
        return "Libra"
    elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
        return "Scorpio"
    elif (month == "November" and day >= 22) or (month == "December" and day <= 21):
        return "Sagittarius"
    elif (month == "December" and day >= 22) or (month == "January" and day <= 19):
        return "Capricorn"
    elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
        return "Aquarius"
    else:
        (month == "February" and day >= 19) or (month == "March" and day <= 20)
        return "Pisces"

@app.route('/zodiac', methods=['POST'])
def zodiac():
  data = request.get_json()
  name = data["name"]
  month = data["month"]
  day = data["day"]

  # Validate input
  if name.strip() and month and 1 <= day <= 31:
        zodiac = get_zodiac(day, month)
        return jsonify({"zodiac": zodiac}), 200
  else:
        return jsonify({"error": "Invalid input. Please check your data"}), 400

if __name__ == '__main__':
    app.run(debug=True)