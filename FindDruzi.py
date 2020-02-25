from flask import Flask, render_template, request
import build_friends_map
import twitter

url = 'https://api.twitter.com/1.1/friends/list.json'
app = Flask('__FindDruzi__')


@app.route('/')
def search():
    return render_template('search.html')


@app.route('/map', methods=['GET', 'POST'])
def map():
    user = ''
    if request.method == 'POST':
        user = request.form['user']
    return build_friends_map.build_map(twitter.get_friends_locations(url, user))


if __name__ == '__main__':
    app.run(debug=True)



