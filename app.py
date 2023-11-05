import math
import tkinter as tk

def vent_de_travers(vitesse_vent, angle):
    angle_en_radians = math.radians(angle)
    vent_travers = vitesse_vent * math.sin(angle_en_radians)
    return vent_travers

def calculate_vent_de_travers():
    vitesse_vent = float(vent_entry.get())
    numero_piste = int(piste_entry.get())
    direction_vent = int(direction_entry.get())

    cap = cap_from_piste(numero_piste)
    angle_vent = (direction_vent - cap) % 360

    resultat = vent_de_travers(vitesse_vent, angle_vent)
    result_label.config(text=f"Le vent de travers est de {resultat:.2f} kt.")

def cap_from_piste(piste):
    caps_pistes = {
        1: 0, 2: 45, 3: 90, 4: 135,
        5: 180, 6: 225, 7: 270, 8: 315,
        9: 0, 10: 45, 11: 90, 12: 135,
        13: 180, 14: 225, 15: 270, 16: 315,
        17: 0, 18: 45, 19: 90, 20: 135,
        21: 180, 22: 225, 23: 270, 24: 315
    }

    return caps_pistes.get(piste, 0)

root = tk.Tk()
root.title("Calcul du vent de travers")

vent_label = tk.Label(root, text="Vitesse du vent (kt) : ")
vent_label.pack()
vent_entry = tk.Entry(root)
vent_entry.pack()

piste_label = tk.Label(root, text="Numéro de piste : ")
piste_label.pack()
piste_entry = tk.Entry(root)
piste_entry.pack()

direction_label = tk.Label(root, text="Direction du vent (degrés) : ")
direction_label.pack()
direction_entry = tk.Entry(root)
direction_entry.pack()

calculate_button = tk.Button(root, text="Calculer", command=calculate_vent_de_travers)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()