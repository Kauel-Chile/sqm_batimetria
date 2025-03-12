# SQM Batimetria

## Descripción

El proyecto `sqm_batimetria` se centra en el modelamiento de las interfaces de las pozas de SQM a partir de las nubes de puntos obtenidas del equipo RIEGL VQ-480G. Este proyecto proporcionar una herramienta que permita la visualización y análisis de las interfaces de las pozas.

## To Do
- [x] Identificar superficies
- [x] Generar modelo continuo
- [x] modeos ocn dos salidas independientes para z y rgb (2 layer)
- [x] sacar datos a partir de los modelos discretos
- [ ] comparacion con los puntos discretos
- [ ] dejar las nubes de putnos en el mismo sistema que sqm

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/sqm_batimetria.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd sqm_batimetria
   ```

3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta el script principal:
   ```bash
   python main.py
   ```

