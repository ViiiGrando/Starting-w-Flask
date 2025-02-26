from flask import Flask,render_template,request,redirect,session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

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


class User:
        def __init__(self, name,nickname,password):
                self.name = name
                self.nickname = nickname
                self.password = password


user1 = User('Admin', 'admin', 'admin')
user2 = User('Victor', 'viii_grando', '4422')

users = {
        user1.nickname: user1,
        user2.nickname: user2
         } #if I use a list, I need to iterate over all users to find 
                                #the user that I want to authenticate, but with a dictionary 
                                # I can access the user directly by the key, which is the user's nickname 

app = Flask(__name__)
app.secret_key = 'ONE PIECE > NARUTO' #key to encrypt session data

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/libragames'.format(
       SMDB= 'mysql + mysqlconnector',
       user = 'root',
       password = 'admin',
       host = 'localhost',
       database = 'libragames'             

        ) #linking the database to my application

db = SQLAlchemy(app) #linking sqlalchemy in my application

'''telling Flask that when someone accesses the *home* URL, the hello()
        function should be called, and what this function returns will be displayed in the browser

        if I type /home after page link, I can acess my website
        '''

@app.route('/')#as argument I can input this '/' to return initial page or load initial page 
def index(): 
        return render_template('lists.html',title ='Games Library', games = listgames)


@app.route('/newgames') 
def new_games():
        if 'user_logged' not in session or session['user_logged'] == None:
                return redirect(url_for('login', next=url_for('new_games'))) #redirecting the last page that the user was
        return render_template('newgames.html',title = 'New Game')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    next = request.args.get('next') #I can get the next page that the user wants to access
    return render_template('login.html', next=next)#sending our informations of next page to html 
                                                                        #code 
        

@app.route('/logout')
def logout():   
        session['user_logged'] = None #Sesion will be cleared
        flash('Sucessfully logged out')
        return redirect('/logout')



@app.route('/authenticate', methods = ['POST' ]) #AUTHENTICATION
def authenticate():
        if request.form['user'] in users:
                user = users [request.form['user']]
                if request.form['password'] == user.password:
                        session['user_logged'] = user.nickname
                        flash(user.nickname + ' logged successfully')
                        next_page = request.form['next']
                        return redirect(next_page)
        else:
            flash('Invalid user or password')
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