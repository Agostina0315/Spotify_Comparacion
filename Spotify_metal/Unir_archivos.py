import pandas as pd
import glob

archivos = glob.glob("metal_batch*.csv")

if archivos:
    df = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)
    df.to_csv("metal_todo.csv", index=False)
    print("✅ Archivos unidos en metal_todo.csv")
else:
    print("⚠️ No se encontraron archivos metal_batch*.csv en la carpeta.")
