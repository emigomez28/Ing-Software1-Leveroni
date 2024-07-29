- Cuando se quieren comparar 2 objetos complejos, la forma de comparar objetos trivialmente es usando los operadores lógicos. 

- Otra forma es utilizando un objeto nuevo `Comparador` que reciba 2 instancias de un objeto completo y las compare. Este separará a los objetos en partes mas pequeñas y sencillas de comparar hasta saber si son iguales o no.

- El problema con esto es que cuanto más complejo sea el objeto a comparar, mas dificil será su comparación y separación. Por otro lado, este nuevo objeto debe saber como "separar" y realizar comparaciones sencillas.

- No es mantenible, ya que cada vez que se modifique el objeto habrá que modificar el comparador, por otro lado, tener este objeto obliga a exponer la implementación.

- Para resolver esto, hago que el mismo objeto reciba otra instancia del mismo y recursivamente resuelva si son iguales o no -> Object Recursion Pattern



