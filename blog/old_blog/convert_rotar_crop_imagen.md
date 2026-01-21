---
title: "Covert: Rotar, cortar y achicar y agregar fondo a una imagen usando el comando convert de ImageMagick."
date: 2025-07-12T09:24:31-03:00
tags: ['tools']
---
Para rotar una imagen 90 grados con el comando convert de ImageMagick:  
  
* 90° a favor del reloj (clockwise):  
    
```bash  
convert imagen.jpg -rotate 90 salida.jpg  
```  
    
* 90° en contra del reloj (counterclockwise):  
    
```bash  
convert imagen.jpg -rotate -90 salida.jpg  
```  
    
**Achicar imagen a `200x200`**:     
```  
convert -resize x200 input.png output.png  
```  

# Agregar fondo a una imagen

### Add a solid background (e.g. white) to a transparent image:

```bash
convert input.png -background white -alpha remove -alpha off output.png
```

### Place on a colored background canvas:

```bash
convert input.png -background "#ffcc00" -gravity center -extent 800x800 output.png
```

👉 This puts your image in the middle of an 800×800 yellow canvas.

### Merge with another background image:

```bash
convert background.jpg input.png -gravity center -composite output.png
```

#### Cortar imagen
```bash
# Si cambias el 400 corta mas la imagen.
convert Screenshot_20250911-184255.png -crop 0x100%+0+400 geohot.jpg
# Si cambias el porcentaje cambia la posicion de la imagen
convert Screenshot_20250911-184255.png -crop 0x50%+0+500 geohot.jpg && fim geohot.jpg
```

