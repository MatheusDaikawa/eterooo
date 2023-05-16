from bottle import route, run, template
from variavel.exercicio_um import metros_para_cm
from variavel.exercicio_um import salario_hora


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)




@route('/ex1/<m:float>')
def ex1_route(m):
    cm = metros_para_cm(m)
    cm = f'{cm:.2f}'
    return template('<h1>{{r}} cm</h1>', r = cm)

@route('/ex2/<m:float>')
def ex2_route(m):
    cm = metros_para_cm(m)
    cm = f'{cm:.2f}'
    return template('<h1>{{r}} cm</h1>', r = cm)


run(host='localhost', port=8081)