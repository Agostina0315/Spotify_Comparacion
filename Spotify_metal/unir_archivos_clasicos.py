import pandas as pd
import glob

archivos = glob.glob("classical_batch*.csv")

if archivos:
    df = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)
    df.to_csv("classical_todo.csv", index=False)
    print("✅ Archivos unidos en classical_todo.csv")
else:
    print("⚠️ No se encontraron archivos classical_batch*.csv en la carpeta.")
