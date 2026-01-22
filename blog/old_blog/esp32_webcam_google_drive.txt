---
title: "Subir capturas con una esp32 webcam a google drive"
date: 2023-11-10T04:51:54-03:00
tags: ['esp32','capturas','webcam','google','drive']
---
El ESP32 siempre pierde la conexión con la WiFi y cuando corta la luz tenés que esperar 15 minutos para volver a conectarte agregando un delay al comienzo y a veces la conexión wifi al ser tan pobre tenes que subir foto de menor calidad, entonces tenes 3 opciones:

1. Escribir funciones para detectar si se ha perdido la conexión y volver a reconectarse.
2. Escribir un perro guardían (watchdog): https://github.com/TronixLab/ESP32_Watchdog

3. Reinicialo cada 10 minutos pero para hacer esto tenés que desactivar los sensores
 y escribir manualmente la configuración porque sino siempre van a volver a su valor
 por defecto.

Nos dimos cuenta que tarda para subir la foto 10 minutos aprox. tarda google en aceptar o sea sube fotos 10 minutos atrasados o más.  Estuvimos 30 minutos en frente de la cámara subió solo 1 foto.

Se puede usar un **reloj de vidriera**, en caso de que se pierda la conexión wifi para que se vuelva a tomar.

#### Si la cámara deja de subir imágenes podes ver la lista de ejecuciones desde google script para ver si se sigue conectando pero no puede subir la imagen o es otro problema.



Creo que hay mejores tutoriales que este, por ejemplo enviar las fotos por Telegram, o por correo, o usar firebase. Acá algunos links:

https://randomnerdtutorials.com/page/5/?s=ESP32-CAM
https://randomnerdtutorials.com/esp32-cam-save-picture-firebase-storage/
https://randomnerdtutorials.com/esp32-cam-send-photos-email/
https://randomnerdtutorials.com/telegram-esp32-cam-photo-arduino/
https://randomnerdtutorials.com/esp32-cam-post-image-photo-server/
https://randomnerdtutorials.com/esp32-cam-http-post-php-arduino/
https://randomnerdtutorials.com/esp32-cam-photo-microsd-card-timestamp/
https://randomnerdtutorials.com/esp32-cam-robotics-opencv-autonomous/
https://randomnerdtutorials.com/esp32-cam-display-pictures-firebase-web-app/
https://randomnerdtutorials.com/esp32-cam-connect-external-antenna/
https://randomnerdtutorials.com/send-notifications-esp32/
https://randomnerdtutorials.com/firebase-control-esp32-gpios/


Disabling brownout: https://www.robmiles.com/journal/2020/1/20/disabling-the-esp32-brownout-detector


---

Me compré una cámara ESP32 CAM de MercadoLibre y seguí esta guía para subir las fotos a google drive. [https://web.archive.org/web/20230608061848/https://www.gsampallo.com/2019/10/13/esp32-cam-subir-fotos-a-google-drive/](https://web.archive.org/web/20230608061848/https://www.gsampallo.com/2019/10/13/esp32-cam-subir-fotos-a-google-drive/). Backup: [https://archive.is/ABArm](https://archive.is/ABArm)

Se usa google script. Hice un pequeño cambio en el código agregué sensores para que la cámara tenga una mejor calidad cuando hay mucha luz o poca luz y forcé el http en lugar del https porque no funcionaba con el siguiente parámetro: `client.setInsecure()`;

### Google Script
Accedé a Google Script: [https://script.google.com/](https://script.google.com/)  > New Project
Ahí pegá este código:


```js
function doPost(e) {
  var data = Utilities.base64Decode(e.parameters.data);
  var nombreArchivo = Utilities.formatDate(new Date(), "GMT-3", "yyyyMMdd_HHmmss")+".jpg";
  var blob = Utilities.newBlob(data, e.parameters.mimetype, nombreArchivo );
  
  
   // Save the photo to Google Drive
  var folder, folders = DriveApp.getFoldersByName("ESP32-CAM");
  if (folders.hasNext()) {
    folder = folders.next();
  } else {
    folder = DriveApp.createFolder("ESP32-CAM");
  }
  var file = folder.createFile(blob); 
  return ContentService.createTextOutput('Completo')
}
```

El paso siguiente es guardar el script y publicarlo como aplicación web, esto ultimo lo hacemos desde 
Publicar(Deploy) > Implementar como aplicación web

Debemos elegir que se ejecute como nuestro usuario y que cualquier persona incluso los anónimos tengan acceso a la aplicación; luego confirmamos las opciones que se nos presenta.

En la ultima opción Google nos mostrar una url donde estará publicada nuestra aplicación; debemos copiar esta url, la utilizaremos en el programa del ESP32-CAM.

La url provista tendrá el siguiente formato:

`https://script.google.com/macros/s/XXXXXXXXXXXXXX/exec`
Donde las XXXXXXXXXXXXXX serán reemplazadas por una secuencia alfanumérica que identifica a la aplicación.


##### Para subir el código al ESP32 Arduino

Tenés que puentear GND(ground) con GPIO0 para poder programarlo. Explicado en este video: [https://m.youtube.com/watch?v=oCA7XZl8ztk&feature=youtu.be](https://m.youtube.com/watch?v=oCA7XZl8ztk&feature=youtu.be)

Primero instalá arduino con en distros basadas en debian: `sudo apt install arduino` o en arch: `pacman -S arduino` si no funciona así podés instalar el paquete de la AUR `yay -S arduino-ide-bin` 

Luego  
Archivo > preferencias (ctrl + ,) y agregá esta URL:  

[https://dl.espressif.com/dl/package_esp32_index.json](https://dl.espressif.com/dl/package_esp32_index.json)
dale ok > ok

Ahora andate a   
herramientas > placas > gestor de tarjetas, ahí descargará todos los controladores de las diferentes tarjetas ahí buscá `esp32` e instalá la de espressif systems.

Tenés que usar la configuración de placa:   

tools > board > esp32 > ESP32 Wrover Module  
tools > partition scheme lo ponés a Huge APP  

tools > port /dev/usb


Luego para configurar la velocidad:
Tools > Upload Speed > 115200

Para solucionar el error: `ModuleNotFoundError: No module named 'serial'` ejecutamos `pip install pyserial` o `sudo pacman -S python-pyserial` en arch

Luego ubicate en donde guardaste el sketch y bajá la biblioteca `Base64.c` y `Base64.cpp` con el siguiente comando:
```console
curl -O https://raw.githubusercontent.com/gsampallo/esp32cam-gdrive/master/Base64.cpp
curl -O https://raw.githubusercontent.com/gsampallo/esp32cam-gdrive/master/Base64.h
```

---

Backup de estas bibliotecas por si las dudas las borran: 

Base64.h [https://archive.is/wjM0B](https://archive.is/wjM0B)  
Base64.cpp [https://archive.is/I8sdh](https://archive.is/I8sdh)  

Por si las dudas borran estos archivos el creador era:
```bash
 * Copyright (c) 2013 Adam Rudd.
 * See LICENSE for more information
 * https://github.com/adamvr/arduino-base64

```
___

Para compilar `Ctrl+R`, para compilar y subir el programa `Ctrl+U`

A veces cuando intentás cargar falla la carga un truco que me funcionaba era cambiar la velocidad de serie compilar sin subir y cambiarlo de nuevo a la que estaba antes y ahí sí compilar y subirlo



Así me quedó el código (tenés que descargar las bibliotecas base64.cpp y base64.h y ponerlas en la misma carpeta como se mencionó anteriormente sino no compilará):


```
Este código:

1. No soporta HTTPS y hay que agregar el client.setInsecure(); que no es recomendable por ataques de hombre en el medio aparte en un futuro quedará obsoleto.
2. El WiFi SE VA A DESCONECTAR y hay que programar la reconexión está mal poner el WiFi.begin AFUERA 
 [code]
WiFi.begin(ssid, password);  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
[/code] Eso está mal.
Y dentro del loop tenés que chequear si el WiFi se volvió a desconectar:

Debería ser :

[code]
void connectWiFi()
{
  int status = WL_IDLE_STATUS;
  
  while (status != WL_CONNECTED)
  {
    status = WiFi.begin(ssid, password);
    Serial.println("Connecting to WiFi...");
    Serial.print(".");
    delay(300);
  }

  Serial.print(" IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
}
void check_WiFi()
{
  if ( (WiFi.status() != WL_CONNECTED) )
  {
    Serial.println(F("\nWiFi lost. Call connectMultiWiFi in loop"));
    connectWiFi();
  }
}
[/code]

El WiFi.begin tiene que estar dentro del loop while.

Y dentro de loop() hay que llamar a check_WiFi()

Algo así: https://forum.arduino.cc/t/arduino-wifi-rev2-reconnecting-to-wifi-after-disconnected/1022789/5
```

```c
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "Base64.h"

#include "esp_camera.h"


const char* ssid     = "tu_red";   //your network SSID
const char* password = "tu_clave";   //your network password
const char* myDomain = "script.google.com";
String myScript = "/macros/s/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/exec";    //Replace with your own url


String myFilename = "filename=ESP32-CAM.jpg";
String mimeType = "&mimetype=image/jpeg";
String myImage = "&data=";

int waitingTime = 360000; //Wait 6 minutes to google response.

#define CAMERA_MODEL_AI_THINKER // Has PSRAM

#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

void setup()
{
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);

  Serial.begin(115200);
  delay(900000);

  WiFi.mode(WIFI_STA);

  Serial.println("");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("STAIP address: ");
  Serial.println(WiFi.localIP());

  Serial.println("");

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  //config.xclk_freq_hz = 20000000;
  config.xclk_freq_hz = 5000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_VGA;  // UXGA|SXGA|XGA|SVGA|VGA|CIF|QVGA|HQVGA|QQVGA
  config.jpeg_quality = 10;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    delay(1000);
    ESP.restart();
  }

  // Estos son los sensores que agregué
  sensor_t * s = esp_camera_sensor_get();
  s->set_brightness(s, 0);     // -2 to 2
  s->set_contrast(s, 0);       // -2 to 2
  s->set_saturation(s, 0);     // -2 to 2
  s->set_special_effect(s, 0); // 0 to 6 (0 - No Effect, 1 - Negative, 2 - Grayscale, 3 - Red Tint, 4 - Green Tint, 5 - Blue Tint, 6 - Sepia)
  s->set_whitebal(s, 1);       // 0 = disable , 1 = enable
  s->set_awb_gain(s, 1);       // 0 = disable , 1 = enable
  s->set_wb_mode(s, 0);        // 0 to 4 - if awb_gain enabled (0 - Auto, 1 - Sunny, 2 - Cloudy, 3 - Office, 4 - Home)
  s->set_exposure_ctrl(s, 1);  // 0 = disable , 1 = enable
  s->set_aec2(s, 1);           // 0 = disable , 1 = enable
  s->set_ae_level(s, 0);       // -2 to 2
  s->set_aec_value(s, 300);    // 0 to 1200
  s->set_gain_ctrl(s, 1);      // 0 = disable , 1 = enable
  s->set_agc_gain(s, 0);       // 0 to 30
  //s->set_gainceiling(s, (gainceiling_t)0);  // 0 to 6
  s->set_gainceiling(s, (gainceiling_t)2);  // 0 to 6
  s->set_bpc(s, 1);            // 0 = disable , 1 = enable
  s->set_wpc(s, 1);            // 0 = disable , 1 = enable
  s->set_raw_gma(s, 1);        // 0 = disable , 1 = enable
  s->set_lenc(s, 1);           // 0 = disable , 1 = enable
  s->set_hmirror(s, 0);        // 0 = disable , 1 = enable
  s->set_vflip(s, 0);          // 0 = disable , 1 = enable
  s->set_dcw(s, 1);            // 0 = disable , 1 = enable
  s->set_colorbar(s, 0);       // 0 = disable , 1 = enable
}

boolean enviar = true;

void loop() {
  //if(enviar) {
    saveCapturedImage();
    enviar = false;
    delay(300000);
  //}
}

void saveCapturedImage() {
  Serial.println("Connect to " + String(myDomain));
  WiFiClientSecure client;
  client.setInsecure();

  if (client.connect(myDomain, 443)) {
    Serial.println("Connection successful");

    camera_fb_t * fb = NULL;
    fb = esp_camera_fb_get();
    if(!fb) {
      Serial.println("Camera capture failed");
      delay(1000);
      ESP.restart();
      return;
    }

    char *input = (char *)fb->buf;
    char output[base64_enc_len(3)];
    String imageFile = "";
    for (int i=0;i<fb->len;i++) {
      base64_encode(output, (input++), 3);
      if (i%3==0) imageFile += urlencode(String(output));
    }
    String Data = myFilename+mimeType+myImage;

    esp_camera_fb_return(fb);

    Serial.println("Send a captured image to Google Drive.");

    client.println("POST " + myScript + " HTTP/1.1");
    client.println("Host: " + String(myDomain));
    client.println("Content-Length: " + String(Data.length()+imageFile.length()));
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println();

    client.print(Data);
    int Index;
    for (Index = 0; Index < imageFile.length(); Index = Index+1000) {
      client.print(imageFile.substring(Index, Index+1000));
    }

    Serial.println("Waiting for response.");
    long int StartTime=millis();
    while (!client.available()) {
      Serial.print(".");
      delay(100);
      if ((StartTime+waitingTime) < millis()) {
        Serial.println();
        Serial.println("No response.");
        //If you have no response, maybe need a greater value of waitingTime
        break;
      }
    }
    Serial.println();
    while (client.available()) {
      Serial.print(char(client.read()));
    }
  } else {
    Serial.println("Connected to " + String(myDomain) + " failed.");
  }
  client.stop();
}

//https://github.com/zenmanenergy/ESP8266-Arduino-Examples/
String urlencode(String str)
{
    String encodedString="";
    char c;
    char code0;
    char code1;
    char code2;
    for (int i =0; i < str.length(); i++){
      c=str.charAt(i);
      if (c == ' '){
        encodedString+= '+';
      } else if (isalnum(c)){
        encodedString+=c;
      } else{
        code1=(c & 0xf)+'0';
        if ((c & 0xf) >9){
            code1=(c & 0xf) - 10 + 'A';
        }
        c=(c>>4)&0xf;
        code0=c+'0';
        if (c > 9){
            code0=c - 10 + 'A';
        }
        code2='\0';
        encodedString+='%';
        encodedString+=code0;
        encodedString+=code1;
        //encodedString+=code2;
      }
      yield();
    }
    return encodedString;
}
```

Para grabar el programa en la ESP32 usé el programa Arduino y para configurar el arduino seguí este video: [https://m.youtube.com/watch?v=oCA7XZl8ztk&feature=youtu.be](https://youtube.com/watch?v=gN8MamCE4qE) a veces me puteaba diciendo que compiló mal le cambiaba la velocidad de la comunicación serial y volvía a poner la que estaba y funcionaba

[https://youtube.com/watch?v=XqT1rLHl3DE](https://youtube.com/watch?v=XqT1rLHl3DE)


---

#### Si querés simplemente tener un servidor sin subir las fotos a ningún lado hace lo siguiente

Para crear un servidor web de transmisión de video con una placa ESP32-CAM, puedes seguir estos pasos:  
1. Conectá tu placa ESP32-CAM a tu computadora usando un cable USB y abre el IDE de Arduino (sudo apt install -y arduino).  
2. herramientas > placas > gestor de tarjetas > buscá esp32 > y lo instalamos. También instalá la biblioteca ESP32-CAM en el IDE de Arduino. 
3. Abra el código de ejemplo "CameraWebServer" de la biblioteca ESP32-CAM (Archivo - Ejemplos - ESP32 - Cámara - CameraWebServer).  
4. Configura los ajustes de tu red WiFi en el código editando las siguientes líneas:  

Sacá el comentario de la línea `#define CAMERA MODEL AI THINKER` y sacá el define que no está comentado: `WROVER` algo así

```c
const char* ssid = "tu_SSID";  
const char* contraseña = "tu_CONTRASEÑA";  
```

5. Seleccioná el puerto de conexión (Tools > port)
6. Una vez cargado el código en el ESP32, abrí el Monitor Serial en el IDE de Arduino para ver la dirección IP asignada a su placa ESP32-CAM por su red WiFi o podés verla haciendo un escaneo con nmap.   
  
Podés personalizar el servidor web de transmisión de video modificando el código y agregando funciones adicionales, como detección de movimiento o control remoto del módulo de la cámara.  
  
### A veces no funciona porque no está bien conectada la camara.

Para conectarlo: https://imlauer.blogspot.com/2025/01/esp32.html
