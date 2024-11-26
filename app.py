from flask import Flask, render_template

app = Flask(__name__)

# Lista de tarefas e suas colunas
tasks = [
    {"name": "Melhorias para a topologia", "url": "https://www.notion.so/Melhorias-para-a-topologia-13bfd21f928280d088c0e74d2924acf7?pvs=21", "status": "To Do"},
    {"name": "Arrumar apresentação gamma.ap", "url": "https://www.notion.so/Arrumar-apresenta-o-gamma-ap-13bfd21f928280679fc4db8c1d315603?pvs=21", "status": "In Progress"},
    {"name": "Etapa 3 (topologia)", "url": "https://www.notion.so/Etapa-3-topologia-136fd21f928280f1a45ee2f374512035?pvs=21", "status": "Done"},
    # Adicione mais tarefas conforme necessário
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
