from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

albums = [
    {"id": 0, "title": "Hybrid Theory", "year": "2000"},
    {"id": 1, "title": "Meteora", "year": "2003"}
]

@app.route('/')
def index():
    return "<h1>Головна сторінка</h1><p>Вітаємо на сайті гурту Linkin Park!</p>"

@app.route('/about')
def about():
    return "<h1>Про проект</h1><p>Цей сайт створено як лабораторну роботу.</p>"

@app.route('/history')
def history():
    return "<h1>Історія гурту</h1><p>Linkin Park — американський рок-гурт, заснований у 1996 році.</p>"

@app.route('/albums')
def show_albums():
    res = "<h1>Альбоми</h1><ul>"
    for album in albums:
        res += f"<li>{album['title']} ({album['year']}) </li>"
    return res

@app.route('/admin/add', methods=['GET', 'POST'])
def add_album():
    if request.method == 'POST':
        new_album = {
            "id": len(albums),
            "title": request.form['title'],
            "year": request.form['year']
        }
        albums.append(new_album)
        return redirect(url_for('show_albums'))
    return '''
        <form method="post">
            Назва: <input type="text" name="title"><br>
            Рік: <input type="text" name="year"><br>
            <input type="submit" value="Додати альбом">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)