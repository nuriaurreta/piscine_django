#!/bin/bash #sirve para determinar que el script se ejecutará con bin/bash

if [ "$1" ]; then	# comprueba si existe el argumento
	curl -s "$1" | grep "moved here" | cut -d \" -f 2
fi

# 'curl' realiza una solicitud HTTP al enlace dado por el argumento
# al añadir '-s' omite la información no relevante

# 'grep "moved here" busca la redirección de la url

# cut -d \" -f 2: Toma la salida de grep y la pasa como entrada a cut
# cut se utiliza aquí para cortar o dividir la línea de salida en campos
# delimitados por comillas (-d \")

# -f 2 selecciona el segundo campo, asumiendo que la cadena "moved here" está
# seguida por una URL entre comillas en la línea obtenida por grep