- Muchos métodos no solo tienen el mismo nombre, sino que también hacen lo mismo -> Polimorfismo. EJ: **atacar** en Combatientes Fantasticos

- Para que 2 métodos sean polimórficos. no solo deben tener el mismo nombre, sino la misma cantidad de parámetros, los mismos "efectos colaterales" y el mismo tipo de retorno. EJ: **add:** en una Collection

- 2 métodos que son polimórficos deben aparecer en el mimo protocolo

- La descripción de un método documenta 2 cosas, el propósito y los detalles de implementación.

- Para que 2 métodos sean polimórficos, deben tener el mismo propósito. No deberían tener los mismos detalles de implementación.

- Para que 2 clases sean polimórficas, deben tener la misma "interfaz central" de mensajes polimórficos. 

-  Un colaborador puede intercambiar las clases sí y solo sí usa los mensajes dentro de la "interfaz central".

- Para que una jerarquía sea polimórfica, todas sus clases deben compartir la misma "interfaz central" polimórfica. 

- La jerarquia polimórfica y su interfaz central es definida por una clase abstracta -> Template Class

- Una jerarquía polimórfica encapsula código que es altamente reutilizable, flexible y extensible -> Buen uso de POO

- No sobre documentar 