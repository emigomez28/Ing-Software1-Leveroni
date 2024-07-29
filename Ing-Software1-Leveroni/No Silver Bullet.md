
- No van a haber "**balas de plata**" en software, como las hubieron en el hardware (por avances tecnológicos como los transistores), que resuelvan los problemas a nivel general.

- Esto se debe a la separación entre esencia y accidentes del software

- En cuanto a la esencia de este, en su estado más irreducible tiene ciertas propiedades inherentes

- **Complejidad:** es perfectamente variable, arbitraria dependiendo del caso, fundamental para el desarrollo de cada pieza de software. Dificulta encontrar y "atar todos los cabos sueltos", así como el aprendizaje.

- Carece totalmente de linealidad

- **Conformidad:** debe conformarse e integrarse con otros, lo cual no siempre resulta simple

- **Cambiabilidad:** por obvias razones (avances tecnológicos, diferencias con diseños iniciales) el software está en constante cambio

- **Invisibilidad:** no es fácilmente visualizable.

- En cuanto a las dificultades accidentales, estas representan las más grandes que el desarrollo de software alguna vez enfrentó.

- En principio, herramientas como los lenguajes de alto nivel fueron solución a, precisamente, hacer que el desarrollador se encargue de todas las cuestiones de bajo nivel (valga la redundancia)

- Este tipo de lenguajes llevaban el desarrollo de software a un nivel superior de abstracción, donde el programador se separa por completo de las operaciones bitwise, los registros , las condiciones, ramas, canales, discos y demás, eliminando así un nivel completo de complejidad que nunca fue inherente al programa a desarrollar.

- Sin embargo, el querer desarrollar un lenguaje de este tipo termina siendo más un dolor de cabeza para el usuario que un beneficio.

- En cuanto a otras cuestiones/dificultades, como el time-sharing, son abordadas desde otro punto completamente diferente: si bien suponen una mejoría en la productividad de los programadores y en la calidad de los productos, no se compara con la provista por los HLL (lenguajes de alto nivel). Se concentra en preservar la inmediatez, además de que nos permite mantener una descripción general de la complejidad. Aún así, esto tiene un cierto límite de perceptibilidad para el ser humano (aprox 100 ms), a partir del cual no se notan beneficios o mejoras (en cuanto a la inmediatez o ahorro de tiempo, claro está)

- Por último, hablando de los entornos de programación unificados (Unix, Interlisp), podemos notar que si bien estos son de amplio uso, mejoraron la productividad en factores integrales, ya que atacan las dificultades accidentales usando varios programas a la vez.

- Este tipo de avances son los que estimularon el desarrollo de varios "kits de herramientas", ya que cada una podía ser aplicada a cualquier programa usando los formatos estándar.

- Podemos decir, entonces, que son el foco principal de las investigaciones actuales de ingeniería de software.

- **Sistemas expertos:** deriva del “arte de la IA”. Es un programa que contiene un motor generalizado y una base de reglas, diseñado para tomar datos de entrada y asunciones y explorar las consecuencias lógicas a través de las inferencias derivadas de la propia base de reglas, sacando conclusiones y consejos, y ofreciendo una explicación de sus resultados al usuario. 

- **Programación “automática”:** generación de un programa para resolver un problema desde el enunciado de las especificaciones del mismo. Parnas, además de decir que es un eufemismo para programar con un lenguaje de alto nivel, declara que lo que se tiene que dar a conocer no es el problema en sí, sino el método de resolución del mismo.

- **Programación gráfica:** La computación gráfica o representación gráfica de las piezas de software son poco útiles a la hora de, precisamente, visualizar o entender su funcionamiento. Se queja de que los diagramas de flujo son representaciones demasiado burdas, que no permitirían conocer, más que de manera superficial, cómo funciona un software “por debajo”

- Verificación de programas: refiere al testing y debugging, más que nada al esfuerzo que ambas prácticas suponen. Difiere por completo de los programas a prueba de errores, no hay una SB para mejorar la productividad y confiabilidad del producto a desarrollar en la fase de diseño, ni tampoco verificando inicialmente que un diseño es correcto o no, previo a implementar y testear.

- Una verificación perfecta sólo te dice que un programa logró la especificación previamente declarada. Como bien sabemos, dichas especificaciones pueden cambiar durante el desarrollo (según el ciclo de vida del software, es un proceso CÍCLICO). 

- **Estaciones de trabajo:** por más que se mejoren las estaciones de trabajo (o equipos físicos de desarrollo, es decir, las PCs), las mejoras en cuanto al desarrollo de software son prácticamente imperceptibles. No van a dar una mejora mágica. Obviamente que sirve tener una estación más potente, pero tampoco es, valga la redundancia, “mágica”.

- **Ecuación de productividad:**

	Time of task = $\sum_i (Frequency)_i* (Time)_i$  

- **Comprar vs. Construir:** Las piezas de software que se vendían en el momento facilitaban gran parte del trabajo y, como S.E, uno debería aprovechar dichas herramientas a su favor.

- El costo principal del software siempre fue referido al desarrollo y no a la replicación. El hecho de compartir dicho costo disminuye el costo por usuario. Esto es análogo a decir que se incrementa la productividad. (Después empieza a hablar de qué tan aplicables son los paquetes “off-the-shelf” para ciertas tareas, ya que estos son bastante generales. Anteriormente no se usaban tanto por el nivel de especificidad de los problemas a resolver o tareas a llevar a cabo. También menciona la variación enorme en los costos, y que no todos los usuarios podrían comprar los programas de pago “tan mágicos” que se ofrecen en el mercado. Además, nombra que los usuarios de PCs, en su día a día, son mayormente incapaces de siquiera escribir un programa, pero que usan los programas diarios para realizar las tareas diarias que tienen por delante, de manera eficiente.)

- No hay que construir más de lo necesario. El código hay que mantenerlo, debuggearlo y mejorarlo.

- Refinamiento de requerimientos y rápido prototipado: como se describió anteriormente, prácticamente nunca el diseño inicial será el diseño final, con las mismas especificaciones y detalles de principio a fin. Precisamente por ese constante cambio es que lo más difícil de ser un S.E es tener que rectificar posteriormente. Además, como se suelen atender las necesidades puntuales de cada cliente, estos tampoco suelen ser tan específicos en cuanto a los parámetros previamente mencionados.

- **Desarrollo incremental:** (más o menos lo mismo que vengo diciendo en todo el resumen: el software se desarrolla incrementalmente, no necesariamente tiene que tener una versión definitiva inmutable. Es perfectamente capaz de tener add-ons más tarde en el desarrollo)**