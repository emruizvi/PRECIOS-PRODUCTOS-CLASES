import pandas as pd

productos = {
    "Producto": ["Arroz 2kg", "Aceite 1L", "Leche 1L", "Café 400g"],
    "Precio_anterior": [3.20, 2.75, 1.05, 4.80],
    "Precio_actual": [3.45, 2.69, 1.12, 5.25]
}

df = pd.DataFrame(productos)
df["Variacion_%"] = (
    (df["Precio_actual"] - df["Precio_anterior"]) / df["Precio_anterior"] * 100
).round(2)

df["Alerta"] = df["Variacion_%"].apply(
    lambda x: "SUBIÓ" if x > 5 else ("BAJÓ" if x < 0 else "ESTABLE")
)

print("MONITOR INTELIGENTE DE PRECIOS")
print("=" * 50)
print(df.to_string(index=False))
