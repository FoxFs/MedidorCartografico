import tkinter as tk

def calcular_distancia():
    escala = float(entry_escala.get())
    distancia_no_mapa = float(entry_distancia.get())
    distancia_real_cm = escala * distancia_no_mapa
    distancia_real_km = distancia_real_cm / 100000
    label_resultado.config(text=f"Distância real: {distancia_real_km:.2f} km")

#configuração do layout do client
root = tk.Tk()
root.title("Medidor de Escala Cartográfica")

tk.Label(root, text="Escala (ex: para 1:50.000 digite 50000):").pack()
entry_escala = tk.Entry(root)
entry_escala.pack()

tk.Label(root, text="Distância no mapa (cm):").pack()
entry_distancia = tk.Entry(root)
entry_distancia.pack()

tk.Button(root, text="Calcular", command=calcular_distancia).pack()
label_resultado = tk.Label(root, text="Distância real: ")
label_resultado.pack()

root.mainloop()