---
title: "Controlar portón con Firebase"
date: 2025-02-03T16:51:42-03:00
tags: ['porton']
---
Antes de hacer esto grabé un servidor web en el ESP32 para abrir el portón pero funcionaba **MAL** se desconectaba el servidor y cuando andaba tenía mucho lag.

Tenía que conectarme al WiFi y acceder a la URL: http://192.168.0.25/32/on para abrir y cerrar http://192.168.0.25/32/off 

---

MIT APP INVENTOR: https://ai2.appinventor.mit.edu/

Le cambié por 0 y 1:

**Nota**: El programa compartido en esta URL no me funcionó porque usa una librería vieja de Firebase y no me dió el código de la librería vieja tuve que usar otro codigo para el ESP32 pero sí usé la aplicación creada en el MIT APP solo hice unas pequeñas modificaciones como el PIN de salida y el nombre y el ícono de la app y la URL del firebase, etc.

Y en el programa de MIT APP le cambié "ON" y "OFF" por Math - 0 y 1

#### Acá está la aplicación de Android hecha en MIT APP Inventor y el codigo que NO COMPILA para el ESP32 (explicado anteriormente)
http://kio4.com/arduino/117_Wemos_Firebase.htm (https://archive.is/Ytxyu)

http://kio4.com/appinventor/aplicaciones/p117_firebase_pulsador.aia

**Ese código de esp32 no funcionó porque está desactualizado el código de Firebase usa una librería vieja.**

Lo que hice fue usar este código:   
https://github.com/MohammedArmanKhan/Turn-LED-ON-OFF-from-firebase-using-ESP32 (https://archive.is/dMYbr)

En donde contiene la librería vieja usada.

```c
#include <WiFi.h>                                                // esp32 library

#include <IOXhop_FirebaseESP32.h>                                             // firebase library

#define FIREBASE_HOST "tuhost"                         // the project name address from firebase id

#define FIREBASE_AUTH "tuclave"                    // the secret key generated from firebase

#define WIFI_SSID "tured"                                          // input your home or public wifi name

#define WIFI_PASSWORD "tuclave"                                    //password of wifi ssid

String fireStatus = "";                                                     // led status received from firebase

int led = 32;                                                               

void setup() {

  Serial.begin(115200);

  delay(200000);

  pinMode(32, OUTPUT);                

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);                                      //try to connect with wifi

  Serial.print("Connecting to ");

  Serial.print(WIFI_SSID);

  while (WiFi.status() != WL_CONNECTED) {

    Serial.print(".");

    delay(500);

  }

  Serial.println();

  Serial.print("Connected to ");

  Serial.println(WIFI_SSID);

  Serial.print("IP Address is : ");

  Serial.println(WiFi.localIP());                                                      //print local IP address

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);                                       // connect to firebase

  Firebase.setString("/ESP32/LED32", "0");                                          //send initial string of led status

}

void loop() {
  
  fireStatus = Firebase.getString("/ESP32/LED32");                     // get led status input from firebase
  Serial.println(fireStatus);
  if (fireStatus == "1") {                         // compare the input of led status received from firebase

    Serial.println("Led Turned ON");                 

    digitalWrite(32, HIGH);                                                         // make output led ON

  }

  else if (fireStatus == "0") {              // compare the input of led status received from firebase

    Serial.println("Led Turned OFF");

    digitalWrite(32, LOW);                                                         // make output led OFF

  }

  else {

    Serial.println("Wrong Credential! Please send ON/OFF");

  }

}
```

### Si no tenés internet, podés crear un punto acceso con el mismo nombre de tu red y la misma contraseña, y apagar el modem/router así el ESP32 se conecta al punto de acceso WiFi creado por tu celular y podés abrir el portón.


OJO: Cuando usás wifi todo es inestable, lo mejor es usar Ethernet, pero si aún así querés usar wifi podés usar un watchdog timer: https://forum.arduino.cc/t/esp32-periodic-autoreset-possible-solved-1/577976 para que se apague automáticamente luego de un tiempo.

Ethernet: https://forum.arduino.cc/t/exemple-of-a-swtich-on-and-off-a-led-using-ethernet-shield/69032

https://forum.arduino.cc/t/ethernet-shield-and-a-led/207153

Ejemplo uso de Ethernet shield
```bash
#include <SPI.h>
#include <Ethernet.h>

#include <Servo.h>
Servo myservo;  // create servo object to control a servo

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; //physical mac address
byte ip[] = { 192, 168, 1, 102 }; // ip in lan
byte gateway[] = { 192, 168, 1, 1 }; // internet access via router
byte subnet[] = { 255, 255, 255, 0 }; //subnet mask

String readString;

void setup() {
// Open serial communications and wait for port to open:
Serial.begin(9600);

pinMode(13, OUTPUT);

while (!Serial) {
; // wait for serial port to connect. Needed for Leonardo only
}

// start the Ethernet connection and the server:
Ethernet.begin(mac, ip, gateway, gateway, subnet);
}

```
