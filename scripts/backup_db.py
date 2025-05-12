import shutil
import os
from datetime import datetime

ORIGEN = "rubikonsa.db"
DESTINO = f"respaldo/db_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"

os.makedirs("respaldo", exist_ok=True)

if os.path.exists(ORIGEN):
    shutil.copy2(ORIGEN, DESTINO)
    print(f"✅ Respaldo generado: {DESTINO}")
else:
    print("❌ Base de datos no encontrada.")
