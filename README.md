# auto_registe_jornada
script para registrar la jornada de forma automatica

```
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
deactivate
```

# Ejemplo de .env
```
#inside file named .env

codigo_centro = "xxxxxxxxxxx"
username = "xxxxxxxxxxxx"
password = "xxxxxxxxxxxxx"

# lunes
inicio_0 = "8:00"
inicioc_0 = "13:30"
finalc_0 = "17:00"
final_0 = "20:30"

# martes
inicio_1 = "11:30"
inicioc_1 = "no"
finalc_1 =  "no"
final_1 = "13:30"

# miercoles
inicio_2 = "10:00"
inicioc_2 = "14:30"
finalc_2 = "15:00"
final_2 = "17:00"

# jueves
inicio_3 = "8:00"
inicioc_3 = "no"
finalc_3 = "no"
final_3 = "13:30"

# viernes
inicio_4 = "8:00"
inicioc_4 = "14:30"
finalc_4 = "17:00"
final_4 = "20:30"
```