from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Función para procesar preguntas de matemática básica
def process_math_question(question):
    try:
        # Evalúa la expresión matemática (¡cuidado con la seguridad!)
        result = eval(question)
        return f"El resultado es: {result}"
    except:
        return "Lo siento, no pude entender la pregunta. Asegúrate de que sea una operación matemática válida."

# Ruta principal para la interfaz del chatbot
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar las preguntas del chatbot
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    response = process_math_question(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
