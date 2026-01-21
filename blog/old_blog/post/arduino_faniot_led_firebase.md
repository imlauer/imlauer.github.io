---
title: "Manejando casa remotamente a través de internet con Arduino FanIOT y firebase"
date: 2024-10-18T07:56:44-03:00
tags: ['esp32']
---
Hace 2 años creé una aplicación en ReactJS con Firebase y leía esos campos de FireBase desde un ESP32 así podía prender y apagar luces remotamente, leer sensores.

#### [Aplicación de ReactJS](/files/reactjs_ESP32logger-main.zip)
```bash
sudo apt remove cmdtest
sudo npm install -g yarn
unzip reactjs_ESP32logger-main.zip
cd reactjs_ESP32logger-main
rm -rf node_modules
rm -rf yarn.lock
yarn add caniuse-lite@1.0.30001632
### Agregá en package.json
"resolutions": {
  "caniuse-lite": "1.0.30001632"
},
### Borrá todos los babels de yarn.lock
The solution was to manually delete all @babel/* entries from yarn.lock and running:

yarn cache clean && yarn install && yarn dedupe

to let Yarn regenerate those with the latest applicable version and hopefully compatible manner. This helped the parsing issue, but a new issue that's mentioned by OP popped up.

yarn install
yarn build
export NODE_OPTIONS=--openssl-legacy-provider
yarn start
```

##### Para arreglar el problema de 404:
https://stackoverflow.com/questions/45412014/how-do-i-set-the-start-url-of-a-manifest-json-to-be-the-root-of-the-site

https://stackoverflow.com/questions/78856773/requires-babel-7-16-0-but-was-loaded-with-7-12-3

### Código que usé en el Arduino o FanIOT.

Para este código usé librerías que ahora las voy a escribir.

Como crear el usuario firebase y obtener la `API_KEY`: https://www.youtube.com/watch?v=cm-Qe2HMJGk

#### Temp Logger
WifiManager -> acceder Wifi usando AP temporal para no hardcodear credenciales.
Abrir servidor web en Arduino (crear)
* Crear página web para loggear y registrar cuentas en el servidor de Arduino usando Firebase.
* Pasar el token de login a Arduino.
* Usar mDNS para no utilizar IP dinámica.
* Guardar en la EEPROM su identificación de FireBase (opcional).
* Usar SNIFFS para servir archivos HTML y un servidor asíncrono para parsear argumento tipo GET y POST.
* Instalar Firebase client esp32.
* Guardar datos de humedad en el respectivo usuario logueado.

##### Bibliotecas usadas:
* WifiManager
* ESPmDNS
* AsyncWebServerESP32
* SNIFFS
* FirebaseESP32
* AsyncTCP
* ArduinoJson
* ds18b20 (dallas temp.)
* OneWire (Max 31850)
* Adafruit ssd1306
* adafruit GFX

Probablemente no necesito usar todas esas librerías pero eso es lo que usé.

**Todo este código lo cargás en el ESP32 o FanIOT y levantará un servidor web en donde tendrás que ingresar el mismo usuario que ingresás en la app de reactjs, y ahí podrás leer los datos, aparte es mejor que cambies la base de datos de firebase por una tuya**

```c
#include <WiFiManager.h> // https://github.com/tzapu/WiFiManager
//
// A simple server implementation showing how to:
//  * serve static messages
//  * read GET and POST parameters
//  * handle missing pages / 404s
//

#include <Arduino.h>
#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Firebase_ESP_Client.h>
#include "time.h"
#include <FastLED.h>//https://github.com/FastLED/FastLED


#define LED_PIN  27
#define NUM_LEDS 4
#define BRIGHTNESS 75
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB//RGB
CRGB leds[NUM_LEDS];


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

#define Pagina_Login R"====(<meta content="width=device-width,initial-scale=1"name=viewport><style>body{font-family:Arial,Helvetica,sans-serif}form{border:3px solid #f1f1f1}input[type=password],input[type=text]{width:100%;padding:12px 20px;margin:8px 0;display:inline-block;border:1px solid #ccc;box-sizing:border-box}button{background-color:#04AA6D;color:#fff;padding:14px 20px;margin:8px 0;border:none;cursor:pointer;width:100%}button:hover{opacity:.8}.cancelbtn{width:auto;padding:10px 18px;background-color:#f44336}.imgcontainer{text-align:center;margin:24px 0 12px 0}img.avatar{width:40%;border-radius:50%}.container{padding:16px}span.psw{float:right;padding-top:16px}@media screen and (max-width:300px){span.psw{display:block;float:none}.cancelbtn{width:100%}}</style><h2>Login Form</h2><form action=/_login><div class=container><label for=uname><b>Username</b></label><input name=uname placeholder="Enter Username"required><label for=psw><b>Password</b></label><input name=psw placeholder="Enter Password"required type=password> <button type=submit>Login</button><label><input name=remember type=checkbox checked> Remember me</label></div><div class=container style=background-color:#f1f1f1><button type=button class=cancelbtn>Cancel</button> <span class=psw>Forgot <a href=#>password?</a></span></div></form>)===="
const char *Pagina = R"====(<title>Panel</title><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><style>body{font-family:monospace}.cards{margin:auto;max-width:800px;display:flex;flex-wrap:wrap;align-items:center}.card{flex:1 0 200px;text-align:center}.card .text{padding:0 20px 20px}.title{text-align:center}.hide{display:none}.green{background:green}.red{background:red}@-webkit-keyframes spin{0%{-webkit-transform:rotate(0)}100%{-webkit-transform:rotate(360deg)}}@keyframes spin{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}.alert{padding:20px;background-color:#f44336;color:#fff;opacity:1;transition:opacity .6s;margin-bottom:15px}.alert.success{background-color:#04aa6d}.alert.info{background-color:#2196f3}.alert.warning{background-color:#ff9800}.closebtn{margin-left:15px;color:#fff;font-weight:700;float:right;font-size:22px;line-height:20px;cursor:pointer;transition:.3s}.center{text-align:center;max-width:900px}.closebtn:hover{color:#000}</style><div id=loading style=height:100%;width:99%;position:absolute;background-color:#fff;text-align:center><h3 class=loader>Cargando...</h3></div><div id=alerts style=position:fixed;text-align:center></div><h3 class=title>Panel</h3><hr><span class=center><p><b>Guardando cada 3 minutos valores de los sensores en el usuario: </b><span id=user></span><p>Reloj Arduino (<a href=https://www.worlddata.info/timezones/gmt-greenwich-mean-time.php>GMT</a>): <span id=localtime></span><p id=refreshing></span><main class="cards hide" id=inicio><article class=card><div class=text><h5>Sensor Temperatura</h5><span id=celsius></span><br><span id=fahrenheit></span></div></article><article class=card><div class=text><h5>Sensor LDR</h5>Intensidad de Luz: <span id=ldr></span></div></article><article class=card><div class=text><h5>Sensor TILT</h5><span id=tilt></span></div></article><article class=card><div class=text><h5>Buzzer</h5><button class=green onclick=enviar_sonido()>Enviar Sonido</button></div></article><article class=card><div class=text><h5>LED 1</h5><button class=green onclick="accion_led(1,'encender')">Encender</button>
<button class=red onclick="accion_led(1,'apagar')" value=Apagar>Apagar</button></div></article><article class=card><div class=text><h5>LED 2</h5><button class=green onclick="accion_led(2,'encender')">Encender</button>
<button class=red onclick="accion_led(2,'apagar')" value=Apagar>Apagar</button></div></article><article class=card><div class=text><h5>LED 3</h5><button class=green onclick="accion_led(3,'encender')">Encender</button>
<button class=red onclick="accion_led(3,'apagar')" value=Apagar>Apagar</button></div></article><article class=card><div class=text><h5>LEDs Inteligentes WS2812b</h5><button class=green onclick="accion_led(4,'encender')">Encender</button>
<button class=red onclick="accion_led(4,'apagar')">Apagar</button></div></article><article class=card><div class=text><h5>OLED 128X32</h5><form onsubmit=send_oled_message(event)>Ingresa el Mensaje: <input name=oled id=oled>
<input class="button green" type=submit value=Enviar></form></div></article></main><script>getdata();function countdown(remaining){if(remaining<=0){getdata();remaining=5;}
document.getElementById('refreshing').innerText='Auto refresco en... '+remaining;setTimeout(function(){countdown(remaining-1);},1000);}
countdown(5)
function close_alert(element){document.getElementById('alerts').innerHTML=''}
async function accion_led(led,accion){async function enviar_peticion(){var response;if(accion=="encender"){document.getElementById('alerts').innerHTML+="<div class=\"alert info\"> <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Info!</strong> Encendiendo el led: "+led+"</div>"
response=await fetch(`/api/led/encender?led=${led}`);}else if(accion=="apagar"){document.getElementById('alerts').innerHTML+="<div class=\"alert info\"> <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Info!</strong> Apagando el led: "+led+"</div>"
response=await fetch(`/api/led/apagar?led=${led}`);}
var data=await response.json();console.log('printing data server')
console.log(data);return data;}
enviar_peticion().then(function(data){document.getElementById('alerts').innerHTML+="<div class=\"alert success\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Exito!</strong> La petición se envió correctamente.  </div>"}).catch(function(reason){document.getElementById('alerts').innerHTML+="<div class=\"alert error\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Error!</strong> "+reason+"  </div>";})}
async function send_oled_message(e){e.preventDefault();currentvalue=document.getElementById('oled').value;if(currentvalue==''){document.getElementById('alerts').innerHTML+="<div class=\"alert error\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Error!</strong> El mensaje no puede estar vacio.  </div>";return;}
document.getElementById('alerts').innerHTML+="<div class=\"alert info\"> <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Info!</strong> Enviando texto "+currentvalue+" al display</div>"
fetch(`/api/display?message=${currentvalue}`).then(response=>response.json()).then(function(data){document.getElementById('alerts').innerHTML+="<div class=\"alert success\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Exito!</strong> La petición se envió correctamente.  </div>"}).catch(function(reason){document.getElementById('alerts').innerHTML+="<div class=\"alert error\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Error!</strong> "+reason+"  </div>";})}
function enviar_sonido(){document.getElementById('alerts').innerHTML+="<div class=\"alert info\"> <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Info!</strong> Enviando sonido al Buzzer</div>"
fetch('/buzzer').then(response=>response.json()).then(function(data){document.getElementById('alerts').innerHTML+="<div class=\"alert success\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Exito!</strong> La petición se envió correctamente.  </div>"}).catch(function(reason){document.getElementById('alerts').innerHTML+="<div class=\"alert error\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Error!</strong> "+reason+"  </div>";})}
async function getdata(){getdata_sensors().then(function(data){document.getElementById('celsius').innerText=data["temp_celsius"]+'° Celsius';document.getElementById('fahrenheit').innerText=data['temp_fahrenheit']+'° Fahrenheit';document.getElementById('ldr').innerText=data['ldr'];document.getElementById('tilt').innerText=data['tilt'];document.getElementById('user').innerText=data['user'];document.getElementById('localtime').innerText=data['localtime'];document.getElementById('loading').style="display:none;"
document.getElementById('inicio').classList.remove('hide');}).catch(function(reason){document.getElementById('alerts').innerHTML+="<div class=\"alert error\" > <span class=\"closebtn\" onclick=\"close_alert()\">&times;</span>  <strong>Error!</strong> "+reason+"  </div>";})}
async function getdata_sensors(){let response=await fetch('/api/sensors');var data=await response.json();console.log('printing data server')
console.log(data);return data;}</script>)====";


// Provide the token generation process info.
#include <addons/TokenHelper.h>

// Provide the RTDB payload printing info and other helper functions.
#include <addons/RTDBHelper.h>

#define API_KEY "AIzaSyAXZzTwC_Nqh-ZCepllSi8XKTnOcd6UtY4"

/* 3. If work with RTDB, define the RTDB URL */

//#define DATABASE_URL "http://35.201.97.85/" 
#define DATABASE_URL "http://esp32-bd971-default-rtdb.firebaseio.com/" 

// GPIO where the DS18B20 is connected to
const int oneWireBus = 19;     

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);


bool logged = false;




FirebaseJson json;
FirebaseJsonArray WS2812b_;
FirebaseJsonData result;

/* 4. Define the Firebase Data object */
FirebaseData fbdo;

/* 5. Define the FirebaseAuth data for authentication data */
FirebaseAuth auth;

/* 6. Define the FirebaseConfig data for config data */
FirebaseConfig config;


void signIn(String email, String password)
{
    /* Assign the user sign in credentials */
    auth.user.email = email;
    auth.user.password = password;

    /* Initialize the library with the Firebase authen and config */
    logged = true;
    Firebase.begin(&config, &auth);
}





int one_light_pin= 32;
int two_light_pin = 33;
int three_light_pin = 25;

// Variable to save USER UID
String uid;

// Database main path (to be updated in setup with the user UID)
String databasePath;
String databasePath_write;
// Database child nodes
const char *tempPath_c = "/temperature_c";
const char *tempPath_f = "/temperature_f";
const char *ldrPath = "/ldr";
const char *timePath = "/timestamp";
const char *tiltPath = "/tilt";
const char *gmtTimePath = "/gmtTime";

// Parent Node (to be updated in every loop)
//char parentPath[100];

#define BUZZER_PIN  14 // ESP32 pin GIOP18 connected to piezo buzzer

int timestamp;

const char* ntpServer = "pool.ntp.org";

float temperature;


// Timer variables (send new readings every three minutes)
unsigned long sendDataPrevMillis = 0;
unsigned long timerDelay = 1800000;
// 180000

//unsigned long timerDelay = 3600;

int sensorPinTILT = 26;
int sensorPinLDR = 39; // select the input pin for LDR 
int sensorValue = 0; // variable to store the value coming from the sensor

// Function that gets current epoch time
unsigned long getTime() {
  time_t now;
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    //Serial.println("Failed to obtain time");
    return(0);
  }
  time(&now);
  return now;
}

char timeStringBuff[50];
char *printLocalTime()
{
  time_t rawtime;
  struct tm timeinfo;

  if(!getLocalTime(&timeinfo))
  {
    Serial.println("Failed to obtain time");
    sprintf(timeStringBuff,"Error al obtener fecha");
    return timeStringBuff; 
  }
  //char timeStringBuff[50]; //50 chars should be enough
  //strftime(timeStringBuff, sizeof(timeStringBuff), "%A, %B %d %Y %H:%M:%S", &timeinfo);
  strftime(timeStringBuff, 50, "%A, %B %d %Y %H:%M:%S", &timeinfo);
  //print like "const char*"
  Serial.println(timeStringBuff);

  //Optional: Construct String object 
  return timeStringBuff;
}




bool signupOK = false;



AsyncWebServer server(1234);


void notFound(AsyncWebServerRequest *request) {
    request->send(404, "text/plain", "Not found");
}



// ...

void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(one_light_pin, red_light_value);
  analogWrite(two_light_pin, green_light_value);
  analogWrite(three_light_pin, blue_light_value);
}

void setup() {
    // put your setup code here, to run once:
    Serial.begin(115200);
    configTime(-1*3600*3, 0, ntpServer);
    WiFi.mode(WIFI_STA); // explicitly set mode, esp defaults to STA+AP
    // it is a good practice to make sure your code sets wifi mode how you want it.

    FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
    FastLED.setBrightness(BRIGHTNESS);



    if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
      Serial.println(F("SSD1306 allocation failed"));
      for(;;);
    }

        
    display.clearDisplay();
  
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    // Display static text
    display.println("Ingrese con su cuenta de Firebase.");
    display.display(); 
    display.startscrollleft(0x00, 0x0F);

    pinMode(one_light_pin, OUTPUT);
    pinMode(two_light_pin, OUTPUT);
    pinMode(three_light_pin, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);



    
    pinMode(sensorPinTILT, INPUT);
    digitalWrite(sensorPinTILT, HIGH);
 
    
    //WiFiManager, Local intialization. Once its business is done, there is no need to keep it around
    WiFiManager wm;

    // settings - wipe stored credentials for testing
    // these are stored by the esp library

    
    //wm.resetSettings();

    // Automatically connect using saved credentials,
    // if connection fails, it starts an access point with the specified name ( "AutoConnectAP"),
    // if empty will auto generate SSID, if password is blank it will be anonymous AP (wm.autoConnect())
    // then goes into a blocking loop awaiting configuration and will return success result

    bool res;
    // res = wm.autoConnect(); // auto generated AP name from chipid
    // res = wm.autoConnect("AutoConnectAP"); // anonymous ap
    res = wm.autoConnect("AutoConnectAP","password"); // password protected ap

    if(!res) {
        Serial.println("Failed to connect");
        //return;
        ESP.restart();
    } 
    else {
        //if you get here you have connected to the WiFi    
        Serial.println("connected...yeey :)");

 
            
        Serial.print("Connected with IP: ");
        Serial.println(WiFi.localIP());
        Serial.println();

        Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);
        

        /* Assign the API key (required) */
        config.api_key = API_KEY;

        /* Assign the RTDB URL */
        config.database_url = DATABASE_URL;

        Firebase.reconnectWiFi(true);
        fbdo.setResponseSize(2048);


        // If the signupError.message showed "ADMIN_ONLY_OPERATION", you need to enable Anonymous provider in project's Authentication.

        /* Assign the callback function for the long running token generation task */
        config.token_status_callback = tokenStatusCallback; // see addons/TokenHelper.h

        /** The id token (C++ string) will be available from config.signer.tokens.id_token
         * if the sig-up was successful.
         *
         * Now you can initialize the library using the internal created credentials.
         *
         * If the sign-up was failed, the following function will initialize because
         * the internal authentication credentials are not created.
         */
        //config.max_token_generation_retry = 5;
        //Firebase.begin(&config, &auth);


      

        display.clearDisplay();
      
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        // Display static text
        display.println(WiFi.localIP().toString());
        display.startscrollleft(0x00, 0x0F);



        /*server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
            sensors.requestTemperatures(); 
            request->send(200, "text/html", "<meta name=\"viewport\" content=\"width=device-width, height=device-height, initial-scale=1\"><h2>HOLA USUARIO "+String(uid)+"</h2><h3>SENSOR LDR: " + String(analogRead(sensorPinLDR)) + "<BR> TEMPERATURA EN CELSIUS: "+String(sensors.getTempCByIndex(0))+"<BR>Temp en Fahrenheit: "+String(sensors.getTempFByIndex(0))+"<BR>  TILT: "+ String(digitalRead(sensorPinTILT)) +"</h3>");
        });*/
        server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
            request->send(200, "text/html", Pagina);
        });
        
        server.on("/buzzer", HTTP_GET, [](AsyncWebServerRequest *request){
            AsyncResponseStream *response = request->beginResponseStream("application/json");
            DynamicJsonDocument json(1024);
            
            json["status"] = "ok";
        
            digitalWrite(BUZZER_PIN, HIGH);
            delay(2000);
            digitalWrite(BUZZER_PIN, LOW);
            serializeJson(json, *response);
            request->send(response);
        });
        server.on("/login", HTTP_GET, [](AsyncWebServerRequest *request){
            request->send(200, "text/html", Pagina_Login);
        });


        server.on("/_login", HTTP_GET, [] (AsyncWebServerRequest *request) {

          AsyncResponseStream *response = request->beginResponseStream("application/json");
          DynamicJsonDocument json(1024);
          
          String usuario; String clave; bool error = false;
          if (request->hasParam("uname") && request->hasParam("psw")) {
              usuario = request->getParam("uname")->value(); 
              clave = request->getParam("psw")->value(); 

              signIn(usuario, clave);
              display.clearDisplay();
              display.setTextSize(1);
              display.setTextColor(WHITE);
              display.setCursor(0, 0);
              // Display static text
              display.println("OK.");
              display.display(); 

              json["status"] = "ok";
              serializeJson(json, *response);
              request->send(response);
          } else {
              error = true;
              json["status"] = "error";
              serializeJson(json, *response);
              request->send(response);
          }

        });

        

        server.on("/api/led/apagar", HTTP_GET, [] (AsyncWebServerRequest *request) {

          AsyncResponseStream *response = request->beginResponseStream("application/json");
          DynamicJsonDocument json(1024);
          
          String led; bool error = false;
          if (request->hasParam("led")) {
              led = request->getParam("led")->value(); 
              if (led.compareTo("1") == 0) analogWrite(one_light_pin, 0);
              else if (led.compareTo("2") == 0) analogWrite(two_light_pin, 0);
              else if (led.compareTo("3") == 0) analogWrite(three_light_pin, 0);
              //else if (led.compareTo("4") == 0) {FastLED.clear();FastLED.show();}
          } else {
              error = true;
          }
          
          if (error) json["status"] = "ok";
          else{json["status"] = "error";json["message"] = "El parametro led no puede ser nulo.";}
          
          serializeJson(json, *response);
          request->send(response);
        });

        server.on("/api/led/encender", HTTP_GET, [] (AsyncWebServerRequest *request) {

          AsyncResponseStream *response = request->beginResponseStream("application/json");
          DynamicJsonDocument json(1024);
          
          String led; bool error = false;
          if (request->hasParam("led")) {
              led = request->getParam("led")->value(); 
              Serial.println("el doctor muerte a la yuta uno por uno");
              Serial.println(led);
              if (led.compareTo("1") == 0) analogWrite(one_light_pin, 255);
              if (led.compareTo("2") == 0) analogWrite(two_light_pin, 255);
              if (led.compareTo("3") == 0)analogWrite(three_light_pin, 255);

                            
          } else {
              error = true;
          }
          
          if (error) json["status"] = "ok";
          else{json["status"] = "error";json["message"] = "Falta el parametro led.";}
          
          serializeJson(json, *response);
          request->send(response);
        });


        server.on("/api/display", HTTP_GET, [] (AsyncWebServerRequest *request) {

          AsyncResponseStream *response = request->beginResponseStream("application/json");
          DynamicJsonDocument json(1024);
          
          bool error = false; String text;
          if (request->hasParam("message")) {
              text = request->getParam("message")->value(); 
              display.clearDisplay();
              display.setTextSize(1);
              display.setTextColor(WHITE);
              display.setCursor(0, 0);
              // Display static text
              display.println(text);
              display.display(); 
              display.startscrollleft(0x00, 0x0F);
          } else {
              error = true;
          }
          
          if (error) json["status"] = "ok";
          else{json["status"] = "error";json["message"] = "Falta el parametro message.";}
          
          serializeJson(json, *response);
          request->send(response);
        });



        

        // Send a GET request to <IP>/get?message=<message>
        server.on("/api/sensors", HTTP_GET, [] (AsyncWebServerRequest *request) {
          AsyncResponseStream *response = request->beginResponseStream("application/json");
          DynamicJsonDocument json(1024);
          
          //json["localtime"] = String(printLocalTime());
          json["localtime"] = printLocalTime();
          json["temp_celsius"] = sensors.getTempCByIndex(0);
          json["temp_fahrenheit"] = sensors.getTempFByIndex(0);
          json["tilt"] = digitalRead(sensorPinTILT);
          json["ldr"] = analogRead(sensorPinLDR);
          json["user"] = uid;
          serializeJson(json, *response);
          request->send(response);
        });



        server.onNotFound(notFound);
        DefaultHeaders::Instance().addHeader("Access-Control-Allow-Origin", "*");
        server.begin();
        sensors.begin();

        // Getting the user UID might take a few seconds
        Serial.println("Getting User UID");
        while ((auth.token.uid) == "") {
          Serial.print('.');
          delay(1000);
        }


        // Print user UID
        uid = auth.token.uid.c_str();
        //sprintf(uid, "%s", auth.token.uid);
        Serial.print("User UID: ");
        Serial.println(uid);
      
        // Update database path
        databasePath = "/UsersData/" + uid + "/readings";
        //sprintf(databasePath, "/UsersData/%s/readings", uid);
        databasePath_write = "/UsersData/" + uid + "/writtings/tempLogger";
        //sprintf(databasePath_write, "/UsersData/%s/writtings/tempLogger", uid);
    }

}
//         String path = auth.token.uid.c_str(); //<- user uid

void loop() {
  
  // Send new readings to database
  if (Firebase.ready() && logged && (millis() - sendDataPrevMillis > timerDelay || sendDataPrevMillis == 0)){

    sendDataPrevMillis = millis();

    //Get current timestamp
    //timestamp = getTime();

    time_t now;
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo)) {
      //Serial.println("Failed to obtain time");
      timestamp = 0;
    }
    time(&now);
    timestamp = now;



    
    //timestamp = 1234;
    Serial.print ("time: ");
    Serial.println (timestamp);

    //String parentPath;
    //parentPath = databasePath.c_str() + "/" + String(timestamp);
    char parentPath[100];
    sprintf(parentPath,"%s/%d",databasePath.c_str(),timestamp); 

    sensors.requestTemperatures(); 
    float celsius = sensors.getTempCByIndex(0);
    float fahrenheit = sensors.getTempFByIndex(0);
    while (celsius == -127.00 || fahrenheit == -196.60){
        sensors.requestTemperatures(); 
        celsius = sensors.getTempCByIndex(0);
        fahrenheit = sensors.getTempFByIndex(0);
        delay(5000);
    }
    


    json.set(tempPath_c, String(celsius));
    json.set(tempPath_f, String(fahrenheit));
    json.set(ldrPath, String(analogRead(sensorPinLDR)));
    json.set(tiltPath, String(digitalRead(sensorPinTILT)));
    json.set(timePath, timestamp);
    json.set(gmtTimePath, printLocalTime());
    Serial.printf("Set json... %s\n", Firebase.RTDB.setJSON(&fbdo, parentPath, &json) ? "ok" : fbdo.errorReason().c_str());

    Serial.printf("Getting json...\n");

    char aux[100];

    int led_rojo,led_amarillo,led_verde,_buzzer;
    char _oled[200];

    sprintf(aux,"%s/led_rojo",databasePath_write.c_str()); 
    Serial.println(aux);
    Firebase.RTDB.getInt(&fbdo, aux, &led_rojo);
    
    sprintf(aux,"%s/led_amarillo",databasePath_write.c_str()); 
    Serial.println(aux);
    Firebase.RTDB.getInt(&fbdo, aux, &led_amarillo);
    
    sprintf(aux,"%s/led_verde",databasePath_write.c_str()); 
    Serial.println(aux);
    //Serial.println('led verde:');
    Serial.println(led_verde);
    Firebase.RTDB.getInt(&fbdo, aux, &led_verde);
    
    sprintf(aux,"%s/buzzer",databasePath_write.c_str()); 
    Serial.println(aux);
    Firebase.RTDB.getInt(&fbdo, aux, &_buzzer);
    

    int on_off;
    for (int i=1; i<5; i++){
        sprintf(aux,"%s/WS2812b%d",databasePath_write.c_str(),i);
        //Serial.println('working?');
        Serial.println(aux);
        Firebase.RTDB.getArray(&fbdo, aux, &WS2812b_);
        WS2812b_.get(result,0);
        String colorString = result.to<String>();
        Serial.println(colorString);
        long color_hex = strtol(colorString.c_str(), NULL, 16);
        leds[i-1] = color_hex;
        WS2812b_.get(result,1);
        on_off = result.to<int>();
        //Serial.println('reckful');
        Serial.println(on_off);
        if(on_off) FastLED.show();
        else{ leds[i-1] = strtol("0x000000", NULL,16) ;FastLED.show(); }
    }


    sprintf(aux,"%s/oled",databasePath_write.c_str()); 
    Firebase.RTDB.getString(&fbdo, aux, _oled);


    /*if (_led1 == 1) analogWrite(one_light_pin, 255);
    if (_led2 == 1) analogWrite(two_light_pin, 255);
    if (_led3 == 1) analogWrite(three_light_pin, 255);
    if (_led1 == 0) analogWrite(one_light_pin, 0);
    if (_led2 == 0) analogWrite(two_light_pin, 0);
    if (_led3 == 0) analogWrite(three_light_pin, 0);*/

    if (_buzzer){
        sprintf(aux,"%s/buzzer",databasePath_write.c_str()); 
        Firebase.RTDB.set(&fbdo, aux, false);
        digitalWrite(BUZZER_PIN, HIGH);
        delay(2000);
        digitalWrite(BUZZER_PIN, LOW);
    }

    if (!led_rojo) analogWrite(one_light_pin, 0);
    if (!led_amarillo) analogWrite(two_light_pin, 0);
    if (!led_verde) analogWrite(three_light_pin, 0);
    
    if (led_rojo) analogWrite(one_light_pin, 255);
    if (led_amarillo) analogWrite(two_light_pin, 255);
    if (led_verde) analogWrite(three_light_pin, 255);


    
    Serial.println("Contenido de _oled: ");
    Serial.println(_oled);
    if(strcmp(_oled,"") != 0){
      display.clearDisplay();
      display.setTextSize(1);
      display.setTextColor(WHITE);
      display.setCursor(0, 0);
      // Display static text
      display.println(_oled);
      display.display(); 
      display.startscrollleft(0x00, 0x0F);
    }
  }
}
```



Más información: 

https://redirect.invidious.io/search?q=firebase+esp32

