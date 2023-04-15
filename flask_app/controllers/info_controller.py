from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.info_model import Info

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def post():
    print(request.form)
    if not Info.validate_info(request.form):
        return redirect('/')
    data =  {
        'name': request.form['name'],
        'dojo_location': request.form['dojo_location'],
        'fav_language': request.form['fav_language'],
        'comment': request.form['comment'] 
        }
    Info.save(data)
    return redirect('/result')

@app.route('/result')
def result():
    all_infos = Info.get_all()
    return render_template("result.html", all_infos = all_infos)