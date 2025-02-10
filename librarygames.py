from flask import Flask,render_template 
class Game:
        def __init__(self, name, category, console):
                self.name = name
                self.category = category
                self.console = console
                pass

        def __str__(self):
          return f'{self.name} - {self.category} - {self.console}' #OR I can acess those attributes at html code , like 
                                                                   #<td>{{game.name}}</td>...


app = Flask(__name__)

'''telling Flask that when someone accesses the *home* URL, the hello()
        function should be called, and what this function returns will be displayed in the browser

        if I type /home after page link, I can acess my website
        '''

@app.route('/home')
def hello(): 
        game1 = Game ('God of War', 'History','Play Station')
        game2 = Game ('Counter Strike', 'FPS', 'Computer')
        games = [game1 , game2]
        return render_template('lists.html',title ='Games Library', list_game = games)

app.run()
#app.run(host='0.0.0.0', port=8080) |When I wanna  allow external access to the application I can use the HOST 0.0.0.0
