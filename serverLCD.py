from flask import Flask, request
import time
import json
import RPi.GPIO as GPIO
from RPLCD import CharLCD

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

# Configuração do modo de numeração dos pinos GPIO (use GPIO.BCM ou GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2,
    pin_rs=LCD_RS,
    pin_e=LCD_E,
    pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7],
)

app = Flask(__name__)


@app.route("/receber_post", methods=["POST"])
def receber_post():
    try:
        dados = request.get_json()
        if dados is not None:
            try:
                lcd.clear()

                lcd.write_string(dados.get("name"))
                lcd.cursor_pos = (1, 0)
                lcd.write_string(dados.get("cpf"))

                time.sleep(10)
                lcd.clear()

            except KeyboardInterrupt:
                pass

        else:
            print("Dados não recebidos ou inválidos!")

        return "OK"

    except Exception as e:
        print("Erro ao processar a solicitação:", str(e))
        return "Erro ao processar a solicitação"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
