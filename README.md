Este proyecto es una calculadora sencilla de Índice de Masa Corporal (IMC) desarrollada en Python.
------------------------------------------------------------------------------------------------
Funcionalidades🔗

Solicita al usuario su peso (en kilogramos) y su altura (en metros).

Calcula el IMC utilizando la fórmula: IMC = peso / (altura^2).

Clasifica el resultado según las categorías de la OMS:

Bajo peso: IMC menor a 18.5.

Peso normal: IMC entre 18.5 y 24.9.

Sobrepeso: IMC entre 25 y 29.9.

Obesidad: IMC mayor o igual a 30.

Maneja errores como:

Datos no numéricos.

Peso o altura inválidos.
------------------------------------------------------------------------------------------------
Requisitos⬇️

Python 3.6 o superior.
------------------------------------------------------------------------------------------------
Cómo ejecutar el proyecto⬇️

Clona este repositorio o descarga los archivos del proyecto.

Abre una terminal y navega hasta la carpeta donde se encuentra el archivo calculadora_imc.py.

Ejecuta el siguiente comando:

python calculadora_imc.py

Sigue las instrucciones en la terminal para ingresar tu peso y altura.
------------------------------------------------------------------------------------------------
Ejemplo de uso

Entrada válida⬇️

Ingresa tu peso en kilogramos: 70
Ingresa tu altura en metros (ejemplo: 1.80): 1.80
Tu IMC es: 21.60
Clasificación: Peso normal
------------------------------------------------------------------------------------------------
Entrada inválida⬇️

Peso inválido

Ingresa tu peso en kilogramos: -5
Ingresa tu altura en metros (ejemplo: 1.80): 1.80
El peso debe ser mayor a 0.
------------------------------------------------------------------------------------------------
Altura inválida⬇️

Ingresa tu peso en kilogramos: 70
Ingresa tu altura en metros (ejemplo: 1.80): 180
La altura debe estar en metros (ejemplo: 1.80).
------------------------------------------------------------------------------------------------
Entrada no numérica⬇️

Ingresa tu peso en kilogramos: abc
Por favor, ingresa valores numéricos válidos.
------------------------------------------------------------------------------------------------
Estructura del proyecto

calculadora_imc/➡️

 calculadora_imc.py ➡️ # Archivo principal del proyecto
 README.md ➡️          # Documentación del proyecto
-----------------------------------------------------------------------------------------------
Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.

Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para más información.
