import pandas as pd
import glob

archivos = glob.glob("pop_batch*.csv")

if archivos:
    df = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)
    df.to_csv("pop_todo.csv", index=False)
    print("✅ Archivos unidos en pop_todo.csv")
else:
    print("⚠️ No se encontraron archivos pop_batch*.csv en la carpeta.")