# Infocasas Property Info

Este proyecto permite obtener información sobre una propiedad en Infocasas utilizando su ID.

## Requisitos

- Python 3.9 o superior
- Poetry

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/dianjmv/infocasas-property.git
```
2. Ingresa al directorio del proyecto:
```bash
cd infocasas-property
```
3. Instala las dependencias del proyecto utilizando Poetry:
```bash
poetry install
```
## Ejecución
Para ejecutar el script main.py utilizando Poetry, sigue estos pasos:

1. Abre una terminal en el directorio del proyecto.

2. Ejecuta el siguiente comando, reemplazando `<property_id>` con el ID de la propiedad::
```bash
poetry run python main.py <property_id>
```

## Uso
Después de ejecutar el script con el ID de la propiedad como argumento, se mostrará información sobre la propiedad en Infocasas, incluyendo el título, el precio y un enlace para obtener más información.