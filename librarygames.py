from flask import Flask,render_template,request,redirect
class Game:
        def __init__(self, name, category, console):
                self.name = name
                self.category = category
                self.console = console
                

game1 = Game ('God of War', 'History','Play Station')
game2 = Game ('Counter Strike', 'FPS', 'Computer')
listgames = [game1 , game2]                

'''def __str__(self):
          ret1 = f'{self.name}    -    {self.category}   -    {self.console}'
          return ret1.ljust(32) #OR I can acess those attributes at html code , like 
                                                                   #<td>{{game.name}}</td>...'''


app = Flask(__name__)

'''telling Flask that when someone accesses the *home* URL, the hello()
        function should be called, and what this function returns will be displayed in the browser

        if I type /home after page link, I can acess my website
        '''

@app.route('/')#as argument I can input this '/' to return initial page or load initial page 
def index(): 
        return render_template('lists.html',title ='Games Library', games = listgames)


@app.route('/newgames') 
def new_games():
        return render_template('newgames.html',title = 'New Game')


@app.route('/login')
def login():
        return render_template('login.html', title = 'Login')

#AUTHENTICATION
@app.route('/authenticate', methods = ['POST', ])
def authenticate():
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
                return redirect('/newgames')
        else:
                return redirect('/login')


#CREATING NEW GAMES
@app.route('/cratinnewgames', methods = ['POST', ])
def creatin_new_games():
        
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']
        game = Game(name, category,console)
        listgames.append(game)
        return redirect("/")#returning to initial page







app.run(debug=True)
#app.run(host='0.0.0.0', port=8080) |When I wanna  allow external access to the application I can use the HOST 0.0.0.0
