import pandas as pd
import matplotlib.pyplot as plt
#para leer el archivo cambiamos de ruta 
datos = pd.read_csv(r"C:\Users\m45am\Desktop\Organizacion-Archivos-Portfolio\Corte_3\Proyecto_3\ventas_tecnologia.csv") 

datos["ingresos"] = datos["cantidad"] * datos["precio_unitario"]

orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
datos["mes"] = pd.Categorical(datos["mes"], categories=orden_meses, ordered=True)
datos = datos.sort_values("mes").reset_index(drop=True)



print("--- ventas por producto ---")
por_producto = datos.groupby("producto")["cantidad"].sum()
por_producto = por_producto.sort_values(ascending=False)
print(por_producto)

print("--- ventas por mes ---")
por_mes = datos.groupby("mes")["cantidad"].sum()
print(por_mes)

print("--- ingresos por producto ---")
ingresos_prod = datos.groupby("producto")["ingresos"].sum()
ingresos_prod = ingresos_prod.sort_values(ascending=False)
for nombre, total in ingresos_prod.items():
    print(f"  {nombre}: ${total:,.0f}")

mas_vendido = por_producto.idxmax()
print(f"\nEl producto mas vendido fue: {mas_vendido} con {por_producto.max()} unidades")



colores = ["steelblue", "seagreen", "goldenrod"]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Ventas semestrales - Tienda de tecnologia", fontsize=14)

por_producto.plot(kind="bar", ax=ax1, color=colores)
ax1.set_title("Ventas por producto")
ax1.set_xlabel("Producto")
ax1.set_ylabel("Unidades vendidas")
ax1.tick_params(axis="x", rotation=0)
ax1.grid(axis="y", linestyle="--", alpha=0.4)


for i, val in enumerate(por_producto.values):
    ax1.text(i, val + 1, str(val), ha="center", fontsize=9)

for i, p in enumerate(["Mouse", "Teclado", "Laptop"]):
    filtro = datos[datos["producto"] == p]
    ventas_mes = filtro.groupby("mes")["cantidad"].sum()
    ax2.plot(ventas_mes.index, ventas_mes.values, marker="o", label=p, color=colores[i])

ax2.set_title("Evolucion mensual")
ax2.set_xlabel("Mes")
ax2.set_ylabel("Unidades")
ax2.tick_params(axis="x", rotation=25)
ax2.legend()
ax2.grid(linestyle="--", alpha=0.4)

por_producto.plot(kind="pie", ax=ax3, autopct="%1.1f%%", colors=colores)
ax3.set_title("Distribucion de ventas")
ax3.set_ylabel("")

plt.tight_layout()
plt.savefig("graficas_ventas.png", dpi=150)
print("\nGraficas guardadas en graficas_ventas.png")
plt.show()


ingresos_mes = datos.groupby("mes")["ingresos"].sum()

print("\--- datos clave del semestre ---")
print(f"Producto que mas dinero genero: {ingresos_prod.idxmax()} (${ingresos_prod.max():,.0f})")
print(f"Producto menos vendido: {por_producto.idxmin()} ({por_producto.min()} unidades)")
print(f"Mes con mas ingresos: {ingresos_mes.idxmax()} (${ingresos_mes.max():,.0f})")
print(f"Producto con mas rotacion: {mas_vendido} ({por_producto.max()} unidades)")

