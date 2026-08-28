from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def start():
    answer = ""
    if request.method == "POST":
        grade = request.form.get("txtGrade", "").strip()

        try:
            grade_value = int(grade)
            if grade_value >= 70:
                answer = "Aprobado"
            else:
                answer = "Aprendizaje inicial"
        except ValueError:
            error = "Ingresa una nota numérica válida."

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
