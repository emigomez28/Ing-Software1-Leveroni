
- Se da cuando un objeto contiene como colaborador interno otra instancia de la misma clase, que a su vez contiene otra instancia de la misma clase, generando así una estructura de árbol 
  -> EJ: Ejercicio del Portfolio

- Componer objetos en estructuras de tipo árbol para representar jerarquías. Permite que los clientes traten de manera uniforme a los objetos y composiciones.

- El código que usa estas clases debe tratar de forma distinta al objeto primitivo y al contenedor, para ello, se emplea una estrategia recursiva para que el cliente pueda tratarlos de forma identica, asi este no tiene que realizar esa distinción.