# Importações
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variáveis usadas para o cálculo do consumo dos aparelhos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Primeira página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Terceira página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# O formulário
@app.route('/form')
def form():
    return render_template('form.html')

# Resultados do formulário
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variáveis para a coleta dos dados
    name = request.form['name']
    email = request.form['email']
    adress = request.form['address']
    date = request.form['date']
    
    # Aqui você pode salvar os dados ou enviá-los por email
    return render_template('form_result.html', 
                           # Coloque as variáveis aqui
                           name=name,
                           email=email,
                           address=adress,
                           date=date
                           )

app.run(debug=True)
