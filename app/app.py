from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def cuenta():
    return render_template("cuenta.html")

@app.route("/gracias")
def gracias():
    datos = {
        "nombre": request.args.get("nombre", "").strip(),
        "juegos": request.args.get("juegos", "").strip(),
        "interes": request.args.get("interes", "").strip(),
        "deporte": request.args.get("deporte", "").strip(),
        "series": request.args.get("series", "").strip(),
    }
    return render_template("gracias.html", **datos)

if __name__ == "__main__":
    app.run(debug=True)
