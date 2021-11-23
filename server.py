from flask import Flask

app = Flask(__name__)


@app.route("/")
def game_start():
    return '<h1 style="text-align: center">Guess a number between 0 and 9!</h1>' \
           '<img src="https://i.pinimg.com/originals/8b/37/4e/8b374e2a29c9a5c9ee4b9383bf4906b3.jpg"' \
           'width=700>'


@app.route("/<int:number>")
def check_guess(number):
    secret_number = 3
    if number < 0 or number > 9:
        return '<h1 style="text-align: center">Your number was not between 0 and 9...</h1>' \
               '<img src="https://previews.123rf.com/images/alvincadiz/alvincadiz1604/alvincadiz160400358/56426319-vector-illustration-of-smiley-emoticon-sad-face.jpg"' \
               'width=700>'
    if number == secret_number:
        return '<h1 style="color: green">Wowww! you guessed correctly. Amazing!!!!</h1>' \
               '<img src="https://media3.giphy.com/media/l7fdqmHQ1jCg2HzQlx/200w.webp?cid=ecf05e47ratj2u8xltlmp7i1k6vetjn2z20gsng5od6s6xir&rid=200w.webp&ct=g"' \
               'width=700>'
    elif number > secret_number:
        return '<h1 style="color: red">Your number is TOO high. Try a little lower?</h1>' \
               '<img src="https://media3.giphy.com/media/MZMGlrOKUjEwGCkNER/200w.webp?cid=ecf05e479pc0txhcwd5uovffytfrvtd6ak1ohqjlcnqr1mnx&rid=200w.webp&ct=g"' \
               'width=700>'
    elif number < secret_number:
        return '<h1 style="color: red">Your number is too low. Try being less LOW?</h1>' \
               '<img src="https://media2.giphy.com/media/lReVblhSRtxXtfK81w/200w.webp?cid=ecf05e47t12ng6f3qcrruqm5zpc35p40eznoti3hi4qifl1z&rid=200w.webp&ct=g"' \
               'width=700>'
    else:
        return '<h1 style="color: red">This text should never appear (function check_guess())</h1>'


if __name__ == "__main__":
    app.run(debug=True)
