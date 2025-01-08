from flask import Flask, render_template, jsonify # type: ignore
import time
import threading

app = Flask(__name__)

class Cronometro: 
    def __init__(self):
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            time.sleep(1)
            self.incremento()

    def stop(self):
        self.running = False

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def get_time(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

cronometro = Cronometro()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    threading.Thread(target=cronometro.start).start()
    return jsonify(success=True)

@app.route('/stop')
def stop():
    cronometro.stop()
    return jsonify(success=True)

@app.route('/time')
def time_():
    return jsonify(time=cronometro.get_time())

if __name__ == '__main__':
    app.run(debug=True)
