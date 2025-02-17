from flask import Flask,render_template,request,redirect,session, flash
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
app.secret_key = 'ONE PIECE > NARUTO' #key to encrypt session data

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


@app.route('/authenticate', methods = ['POST', ]) #AUTHENTICATION
def authenticate():
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
                session['user_logged'] =request.form['user'] #which information I wanna store in session
                
                flash(session['user_logged'] + 'logged successfully')
                ''' FLASH is a function 
                that shows a  fast message into users screen
                simmilar to print, but pertences to Flask
                BUT TO MAKE THE  MESSAGE APPEARS I NEED A FLASH MESSAGE BLOCK, WHICH NEEDS TO BE PLACED IN  HTML CODE
                
                If I don't store the information in the session when the user has logged, the success message will still be displayed, 
                but you won't have access to the user's name in other parts of the application, 
                which can be a problem I you want to personalize the user's experience or check whether the user is logged in.'''
                return redirect('/newgames')
        else:
                flash('Invalid user or password, try again')
                return redirect('/login')


@app.route('/cratinnewgames', methods = ['POST', ])#CREATING NEW GAMES
def creatin_new_games():
        
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']
        game = Game(name, category,console)
        listgames.append(game)
        return redirect("/")#returning to initial page







app.run(debug=True)
'''app.run(host='0.0.0.0', port=8080) |When I wanna  allow external access to the
 application I can use the HOST 0.0.0.0'''