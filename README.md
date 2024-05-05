# cocke younger kasami algorithm
Solucion a la tarea 2 de Lenguajes Formales y Compiladores<br>
Por: Felipe Ochoa y Jacobo Giraldo<br>
Implementar el algoritmo de Cocke-Kasami-Younger (Lecture 27) de Kozen.<br>
version: Python 3.11.9<br>
IDE: Pycharm 2023.3.2<br>
Explicacion de funcion: <br>
Vamos a considerar un ejemplo simple para ilustrar cómo funciona el algoritmo CKY.  Supongamos que tenemos la siguiente gramática libre de contexto (GLC): <br>
S -> AB | SS <br>
A -> a <br>
B -> b <br>
Y queremos analizar la cadena aabb.  <br>
1. Inicializamos la tabla DP. Para una cadena de longitud 4, tendremos una tabla de 4x4.  <br>
2. Rellenamos la diagonal de la tabla DP. Para cada carácter en la cadena, añadimos los símbolos no terminales que pueden generarlo. En este caso, 'a' puede ser generado por 'A' y 'b' puede ser generado por 'B'. Por lo tanto, añadimos 'A' a dp[0][1] y dp[1][2], y 'B' a dp[2][3] y dp[3][4].  <br>
3. Rellenamos el resto de la tabla DP. Para cada celda (i, j), consideramos todas las posibles divisiones de la subcadena desde i hasta j en dos partes. Si la primera parte puede ser generada por algún símbolo no terminal 'X' y la segunda parte puede ser generada por algún símbolo no terminal 'Y', y si hay una regla de producción 'Z -> XY', entonces añadimos 'Z' a dp[i][j]. <br>
Por ejemplo, considera la celda dp[0][2]. La subcadena desde 0 hasta 2 es 'aa', que puede ser generada por 'AA'. Como tenemos la regla de producción 'S -> AA', añadimos 'S' a dp[0][2].  <br>
4. Continuamos este proceso hasta que la tabla DP esté completamente llena. Al final, si el símbolo inicial de la gramática (en este caso, 'S') está en dp[0][n], entonces la cadena puede ser generada por la gramática.  
Aquí está cómo se ve la tabla DP después de cada paso: <br>
Paso 1: <br>
[{}, {}, {}, {}, {}] <br>
[{}, {}, {}, {}, {}] <br>
[{}, {}, {}, {}, {}] <br>
[{}, {}, {}, {}, {}] <br>

Paso 2: <br>
[{A}, {}, {}, {}, {}] <br>
[{}, {A}, {}, {}, {}] <br>
[{}, {}, {B}, {}, {}] <br>
[{}, {}, {}, {B}, {}] <br>

Paso 3: <br>
[{A}, {S}, {}, {}, {}] <br>
[{}, {A}, {S}, {}, {}] <br>
[{}, {}, {B}, {S}, {}] <br>
[{}, {}, {}, {B}, {}] <br>

Paso 4: <br>
[{A}, {S}, {S}, {}, {}] <br>
[{}, {A}, {S}, {S}, {}] <br>
[{}, {}, {B}, {S}, {S}] <br>
[{}, {}, {}, {B}, {}] <br>

Paso Final: <br>
[{A}, {S}, {S}, {S}, {S}] <br>
[{}, {A}, {S}, {S}, {S}] <br>
[{}, {}, {B}, {S}, {S}] <br>
[{}, {}, {}, {B}, {}] <br> 

Sustentación Jacobo Giraldo : <br> 
https://eafit-my.sharepoint.com/:v:/g/personal/jgiraldoz_eafit_edu_co/EZxNn1ugAohDlkulnsM6tTEBbEMFQGkzArox78siBdE0XA?e=LlFmGO&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D <br>
Sustentacion Felipe Ochoa: <br>
https://youtu.be/x-X5mZXJgzw
