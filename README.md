<!-- markdownlint-disable -->
# capacitacion-pytest

## Realizar contribuciones

1. Hacer git clone del repositorio:

```bash
git clone https://github.com/santiagomgdev/capacitacion-pytest.git
```

2. Realizar modificaciones en rama development

```bash
git branch -a # Verificar que existe rama development
git checkout development

# Trabajar rama local para subirla a remota
git checkout -b development

# Realizar cambios
git add .
git commit -m "mensaje commit" 
git push origin development
```

3. Subir cambios a development

```bash
git push -u origin development
```

## Sesión 1

- Subir ejercicio en directorio de acuerdo a asignación -> test/Sesion 1/

```txt
/1 - Duber
/2 - Carolina
/3 - Christian
/4 - Edward
/5 - Rafa
/6 - Andrés
```

## Sesión 2

- Subir ejercicio en directorio -> test/Sesion 2/test/test_funcionalidad.py

## Sesión 4

## Instalación

1. Crear un entorno virtual:
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

2. Instalar dependencias:
    pip install -r requirements.txt

## Ejecución de pruebas

1. Ejecutar todas las pruebas de integración:
    pytest src/tests/test_integration.py -v

2. Ejecutar una clase de prueba específica:
    pytest src/tests/test_integration.py::TestUserCRUDIntegration -v

3. Ejecutar con cobertura:
    pip install pytest-cov
    pytest src/tests/test_integration.py --cov=. --cov-report=html

4. Ejecutar pruebas con salida detallada:
    pytest src/tests/test_integration.py -v -s

## Referencias

- <https://www.youtube.com/watch?v=EgpLj86ZHFQ>
- <https://www.browserstack.com/guide/playwright-vs-selenium>
- <https://stackoverflow.com/questions/652292/what-is-unit-testing-and-how-do-you-do-it>
- <https://stackoverflow.com/questions/652292/what-is-unit-testing-and-how-do-you-do-it>
- <https://docs.pytest.org/en/stable/explanation/anatomy.html>
