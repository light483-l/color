from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/table/<gender>/<int:age>')
def table_param(gender, age):
    wall_color = '#FFC0CB' if gender.lower() == 'female' else '#87CEEB'

    marsian_img = 'child_marsian.png' if age < 21 else 'adult_marsian.png'

    return render_template('table.html',
                           wall_color=wall_color,
                           marsian_img=marsian_img,
                           gender=gender,
                           age=age)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
