## Instalar ffmpeg

### Linux (debian o ubuntu)

Actualizar repositorios
- `sudo apt update`

Instalar ffmpeg  
- `sudo apt install ffmpeg`

Verificar version

- `ffmpeg -version`

### Windows

- Descargar .zip de la siguiente url `https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z`
- Descomprimir contenido de carpeta
- Cambiar nombre a carpeta por ffmpeg
- Mover carpeta a disco C:
- Agregar path a windows apuntando a la siguiente direccion `C:\Ffmpeg\bin`


## Instalar pydub
- `pip install pydub`

## Convertir audio

- Ejecutar main.py pasando los parametros del archivo a convertir por ejemplo:
`python main.py audio.wav audio.mp3`
  
## Version sin python

- Se puede ejecutar la conversion sin necesidad de python siguiendo el siguiente ejemplo:
`ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3`
