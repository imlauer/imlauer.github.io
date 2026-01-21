---
title: "ESP32 CAM: Como enviar foto por SMTP, solucionar problema de conexión USB en Windows"
date: 2025-01-02T11:39:01-03:00
tags: ['esp32','smtp','windows']
---
Luego de flashear es recomendable hacer esta prueba: Apagá tu modem/router por unos minutos el esp32 se intentará conectar al wifi pero fallará luego prendelo y el ESP32 se debería reconectar automáticamente, si falla es porque programé algo mal XD, (todavía no hice la prueba).
Quizás la mejora que se le podría hacer al código es contar cuantas veces se intentó conectar al WiFi si es superior a 30 que reinicie el ESP32 con el comando `ESP.restart();` le podes preguntar a ChatGPT seguro te programa algo similar.

Para que este código funcione instalé la biblioteca ESP32 MAIL, lo compilé con ESP32 Wrover Module
https://mobizt.github.io/ESP-Mail-Client/

Para poder flashear tenes que puentear los dos pines (GND y IO0) cuando mirás el monitor serie en modo puente no tiene que aparecer ningún mensaje, si no estás en modo puente y flasheaste algo te mostrará el texto. Si estás en linux yo usé Arduino IDE 1.8 no me gusta el ARDUINO 2 y lo ejecuté como root para poder leer el /dev/ttyUSB0, sino me tiraba permiso denegado.

![https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2024/06/ESP32-CAM-FTDI-programmer.png?w=877&quality=100&strip=all&ssl=1](Pines)

https://randomnerdtutorials.com/program-upload-code-esp32-cam/

#### Como crear una contraseña de aplicación para poder enviar correos desde Gmail (es mejor si usas otro proveedor).
https://support.google.com/mail/answer/185833?hl=en


```bash
#include "esp_camera.h"
#include "SPI.h"
#include "driver/rtc_io.h"
#include "ESP32_MailClient.h"
//#include "ESP_Mail_Client.h"
#include <FS.h>
#include <SPIFFS.h>
#include <WiFi.h>

const char* ssid = "SSID";
const char* password = "wifipassword";

unsigned long previousMillis = 0;
#define INTERVAL 180000 

#define sender_email    "correo@gmail.com"
#define sender_email_password   "clave de aplicación de google que se obtiene habilitando doble factor de autentication"
#define SMTP_Server            "smtp.gmail.com"
#define SMTP_Server_Port        465
#define email_subject          "ESP32-CAM Image Capture"
#define email_recipient        "otrocorreo@gmail.com"

#define CAMERA_MODEL_AI_THINKER

#if defined(CAMERA_MODEL_AI_THINKER)
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
#else
  #error "Camera model not selected"
#endif

SMTPData smtpData;

#define IMAGE_PATH "/image.jpg"

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); //disable brownout detector
  
  Serial.begin(115200);
  Serial.println();
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  
  if (!SPIFFS.begin(true)) {
    Serial.println("An Error has occurred while mounting SPIFFS");
    ESP.restart();
  }
  else {
    delay(500);
    Serial.println("SPIFFS mounted successfully");
  }
  Serial.print("IP Address: http://");
  Serial.println(WiFi.localIP());
   
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
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  
  if(psramFound()){
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }
}

void loop() {
  // Espera 5 minutos para subir la primer foto.
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= INTERVAL) {


    if (WiFi.status() != WL_CONNECTED) {
      Serial.println("WiFi disconnected. Reconnecting...");
      WiFi.disconnect(); // Optional: Disconnect first before reconnecting
      WiFi.reconnect();  // Reconnect to Wi-Fi
      // Wait until the Wi-Fi is reconnected
      while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
      }
      Serial.println("WiFi reconnected");
    }

    captureSave_image();
    sendImage();


    previousMillis = currentMillis;  // Remember the time
  }
}

// Check if photo capture was successful
bool check_photo( fs::FS &fs ) {
  File f_pic = fs.open( IMAGE_PATH );
  unsigned int pic_sz = f_pic.size();
  return ( pic_sz > 100 );
}

// Capture Photo and Save it to SPIFFS
void captureSave_image( void ) {
  camera_fb_t * fb = NULL; 
  bool ok = 0;

  do {
    Serial.println("ESP32-CAM capturing photo...");

    fb = esp_camera_fb_get();
    if (!fb) {
      Serial.println("Failed");
      return;
    }
    Serial.printf("Picture file name: %s\n", IMAGE_PATH);
    File file = SPIFFS.open(IMAGE_PATH, FILE_WRITE);
    if (!file) {
      Serial.println("Failed to open file in writing mode");
    }
    else {
      file.write(fb->buf, fb->len); 
      Serial.print("The picture has been saved in ");
      Serial.print(IMAGE_PATH);
      Serial.print(" - Size: ");
      Serial.print(file.size());
      Serial.println(" bytes");
    }
   
    file.close();
    esp_camera_fb_return(fb);

    ok = check_photo(SPIFFS);
  } while ( !ok );
}

void sendImage( void ) {
  smtpData.setLogin(SMTP_Server, SMTP_Server_Port, sender_email, sender_email_password);
  smtpData.setSender("ESP32-CAM", sender_email);
  smtpData.setPriority("High");
  smtpData.setSubject(email_subject);
  smtpData.setMessage("PFA ESP32-CAM Captured Image.", false);
  smtpData.addRecipient(email_recipient);
  smtpData.addAttachFile(IMAGE_PATH, "image/jpg");
  smtpData.setFileStorageType(MailClientStorageType::SPIFFS);
  smtpData.setSendCallback(sendCallback);
  
  if (!MailClient.sendMail(smtpData))
    Serial.println("Error sending Email, " + MailClient.smtpErrorReason());

  smtpData.empty();
}

void sendCallback(SendStatus msg) {
  Serial.println(msg.info());
}
```
El código es de Sara de RandomNerdTutorials pero en el código original no envía un correo cada 5 minutos sino que sólo lo hace cuando prende. Además agregué una condición para verificar si se perdió la conexión WiFi en loop().    
Otra cosa que me faltó agregar pero que podría servir por si se desconecta de la nada el WiFi: `WiFi.setSleep(false); `

https://forum.arduino.cc/t/esp32-keeps-disconnecting-from-wifi-after-sometime/1261448

Al compilar y subir el programa en Windows Arduino me tiraba un error de `esptool.py` lo solucioné borrando y reinstalando drivers (Administrador de dispositivos y Puertos COM y borrá todos los drivers que están debajo botón derecho propiedades) mostrados acá:

https://forum.arduino.cc/t/a-fatal-esptool-py-error-occurred-cannot-configure-port-something-went-wrong/1225308/7
