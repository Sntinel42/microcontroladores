
#include <WiFi.h>
#include <ESPAsyncWebServer.h>  //NECESSARIO INSTALAR MANUALMENTE
#include <AsyncTCP.h>   //NECESSARIO INSTALAR MANUALMENTE

const char *ssid = "<SSID>";
const char *password = "<SENHA>";

AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);

  // Conectar-se à rede Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");

  Serial.println("Endreço IP atribuido: ");
  Serial.println(WiFi.localIP());

  // Definir rotas do servidor web
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/plain", "Hello, ESP32!");
  });

  // Iniciar o servidor web
  server.begin();
}

void loop() {
  // Nada a fazer aqui
}
