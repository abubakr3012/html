import customtkinter as ctk
import tkintermapview
from tkinter import messagebox

ctk.set_appearance_mode("dark")  # 🌙 Тёмный режим
ctk.set_default_color_theme("blue")

class FastMapApp:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Abubakr")
        self.root.geometry("1000x700")

        # ===== Верхняя панель =====
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=10)

        self.lat_entry = ctk.CTkEntry(self.frame, placeholder_text="Latitude")
        self.lat_entry.grid(row=0, column=0, padx=5)

        self.lon_entry = ctk.CTkEntry(self.frame, placeholder_text="Longitude")
        self.lon_entry.grid(row=0, column=1, padx=5)

        self.go_button = ctk.CTkButton(self.frame, text="Go", command=self.go_to_location)
        self.go_button.grid(row=0, column=2, padx=5)

        # ===== Карта =====
        self.map_widget = tkintermapview.TkinterMapView(
            self.root,
            width=1000,
            height=600,
            corner_radius=0
        )
        self.map_widget.pack(fill="both", expand=True)

        self.map_widget.set_position(40, 60)
        self.map_widget.set_zoom(5)

        self.root.mainloop()

    def go_to_location(self):
        try:
            lat = float(self.lat_entry.get())
            lon = float(self.lon_entry.get())

            self.map_widget.set_position(lat, lon)
            self.map_widget.set_zoom(12)

            self.map_widget.set_marker(lat, lon, text="Location")

        except:
            messagebox.showerror("Error", "Invalid coordinates!")

if __name__ == "__main__":
    FastMapApp()