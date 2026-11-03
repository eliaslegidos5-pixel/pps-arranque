# PPS-E1 · Lectura entrada→sink

| Fichero | Punto de entrada | Sink(s) | Validación (¿cuál? ¿basta?) | Dónde falla según su modelo de ejecución |
|---|---|---|---|---|
| `validar.py` (interpretado) | `sys.argv[1]` (línea 35) | `eval` (línea 30), `os.system` (línea 27) y consulta SQL concatenada (líneas 24-25) | `validar_nombre` solo comprueba que la longitud esté entre 1 y 32. No basta: no restringe caracteres, así que pasan comillas, `;` y paréntesis | Al ser interpretado, el intérprete está disponible en ejecución y `eval`/`os.system` convierten una cadena en código o comandos. Sin frontera entre dato y código, la entrada se ejecuta (se vio con el `SyntaxError` en `eval`) |
| `Validar.java` (bytecode / JVM) | `args[0]` (línea 29) | `st.executeQuery` con SQL concatenado (líneas 21-22); `println` con la entrada (línea 25, inyección en logs) | `validarNombre` comprueba `null` y longitud entre 1 y 32. No basta: no limita caracteres, así que la comilla simple pasa | El bytecode `.class` se puede decompilar (jadx, procyon), por lo que el secreto `apiKey` de la línea 24 queda expuesto. La JVM protege la memoria, pero no evita la inyección SQL |
| `validar.c` (nativo) | `argv[1]` (línea 22) | `strcpy(buffer, nombre)` (línea 17) con `buffer[32]` | Ninguna: ni siquiera se comprueba la longitud | C no tiene seguridad de memoria ni comprobación de límites en ejecución. Un nombre de 32 o más caracteres desborda el buffer de la pila y puede machacar la dirección de retorno |

## ¿Cómo lo corregirías? (una línea por fichero)

- `validar.py`: consulta parametrizada con `?`, quitar `eval`, sustituir `os.system` por `subprocess.run([...])` sin shell y validar con lista blanca (`re.fullmatch(r"[A-Za-z0-9_]{1,32}", nombre)`).
- `Validar.java`: `PreparedStatement` con `setString`, validación con lista blanca (`matches("[A-Za-z0-9_]{1,32}")`) y sacar `apiKey` del código a una variable de entorno.
- `validar.c`: sustituir `strcpy` por `snprintf(buffer, sizeof(buffer), "%s", nombre)` y validar la longitud antes (máximo 31).
