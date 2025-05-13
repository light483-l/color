from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/table_param/<gender>/<int:age>')
def table_param(gender, age):
    # Определяем цвет стен
    wall_color = '#FFC0CB' if gender.lower() == 'female' else '#87CEEB'

    # Определяем изображение марсианина
    marsian_img = 'child_marsian.png' if age < 21 else 'adult_marsian.png'

    return render_template('table_param.html',
                           wall_color=wall_color,
                           marsian_img=marsian_img,
                           gender=gender,
                           age=age)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)