#Proyecto final KC: Aplicación Web de Registro de movimientos de criptomonedas en Flask
Programa realizado en Python con el framework Flask en el que se consultará el valor real en euros de criptomonedas.

#Instalación
- Crea un entorno en VS con el siguiente comando y actívalo
``` py -m env nombre del entorno ```
- Instala Flask con el comando
```pip install flask```
- Ejecuta el siguiente comando y, después, crea un documento .env
```pip install python -dotenv```
- Añade a ese documento ``` FLASK_APP=main.py ``` y ```FLASK_DEBUG=True``` para poder ejecutar el debug de la aplicación con el comando ``` flask run ```
- Una vez realizada la instalación inicial, ejecuta el comando 
```pip freeze > requirements.txt```

- Obten una Apikey en www.coinapi.io
- Usa la plantilla "plantilla config", inserta tu Apikey en el lugar indicado y cambia el nombre a "config.py"

- Para usar la misma base de datos usada en este programa, pega el código de "sentencia_create_criptos.sql" y pégala en tu base de datos.