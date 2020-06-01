from flask import Flask, render_template
import templates
import static.data

app = Flask(__name__)


@app.route('/')
def test():
    return render_template("index.html", title=static.data.my_dict["title"],
                           line=static.data.my_dict["line"],
                           heading=static.data.my_dict["heading"])


app.run(debug=True)
