# Rubikon S.A. - Sistema Empresarial Integrado

Sistema web profesional para gestión técnica, comercial, administrativa y logística de Rubikon S.A.

## Áreas funcionales
- Gestión de personas (clientes, técnicos, empleados, proveedores)
- Autenticación y roles
- Cotizaciones, facturación y productos
- Panel corporativo completo
- Calculadora hidráulica y química integrada
- Reportes PDF y estadísticas visuales
- Sistema modular, seguro y escalable

## Instalación
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate -m "Inicial"
flask db upgrade
flask run