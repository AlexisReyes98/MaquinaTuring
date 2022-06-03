# MaquinaTuring

UEA: Teoría de Autómatas y Lenguajes.

Proyecto Final.

MAQUINA DE TURING.

Es el modelo matemático de un dispositivo que se compor ta como un autómata finito y
que dispone de una cinta de longitud in finita en la que se pueden leer, escribir o borrar
símbolos. La máquina de Turing es un dispositivo de aceptación que acepta los
idiomas (con junto recursivamente numerable) generados por gramáticas de tipo 0.

Como se menciono es considerada un autómata con la capacidad de reconocer
lenguajes formales de acuerdo a la jerarquía de Chomsky, razón por la cual es muy
superior a otros autómatas como el autómata con pila o el autómata finito.

Definición de la Máquina de Turing.

![image](https://user-images.githubusercontent.com/72325257/171806254-73209513-9c02-408f-97af-4ab89c4f6602.png)

¿Cómo funciona?

La cinta de entrada es leída con un único cabezal. Un registro actual almacena el
estado de la máquina de Turing, en la misma se pueden leer o escribir símbolos en el
al fabeto para la cinta. Los movimientos permitidos en la cinta son; izquierda,
derecha o mantenerse en el sitio. Si la MT alcanza el estado final, se acepta la cadena
de entrada, de lo contrario se rechaza.
