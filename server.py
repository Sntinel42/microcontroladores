#! /bin/bash/

from flask import Flask, request
import subprocess, time, json

app = Flask(__name__)


@app.route("/receber_post", methods=["POST"])
def receber_post():
    try:
        dados = request.get_json()
        if dados is not None:
            print("Nome:  ", dados.get("name"))
            print("CPF: ", dados.get("cpf"))
        else:
            print("Dados não recebidos ou inválidos!")

        subprocess.run("echo 0 | sudo tee /sys/class/leds/ACT/brightness", shell=True)
        time.sleep(5)

        subprocess.run("echo 1 | sudo tee /sys/class/leds/ACT/brightness", shell=True)
        time.sleep(10)

        subprocess.run("echo mmc0 | sudo tee /sys/class/leds/ACT/trigger", shell=True)

        return "OK"

    except Exception as e:
        print("Erro ao processar a solicitação:", str(e))
        return "Erro ao processar a solicitação"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")





# Para testar o codigo utilize o cURL abaixo
# curl -X POST -H "Content-Type: application/json" -d '{"name": "SeuNome", "cpf": "SeuCPF"}' http://localhost:5000/receber_post

