import tkinter as tk
from tkinter import messagebox
import requests

def api_kontrol():
    """
    Girilen API'yi kontrol eder ve çalışıp çalışmadığını döner.
    """
    api_adresi = entry_api.get()  # Kullanıcıdan API adresini al
    
    if not api_adresi:
        messagebox.showerror("Hata", "Lütfen geçerli bir API adresi girin!")
        return
    
    timeout_suresi = 5  # Zaman aşımı süresi (saniye cinsinden)
    
    try:
        response = requests.get(api_adresi, timeout=timeout_suresi)
        if response.status_code == 200:
            messagebox.showinfo("Başarı", f"API çalışıyor! (Status Code: 200)")
        else:
            messagebox.showerror("Hata", f"API çalışmıyor. (Status Code: {response.status_code})")
    except Exception as e:
        messagebox.showerror("Hata", f"API'ye erişim hatası: {e}")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("API Kontrol Aracı")

# API girişi için bir etiket
label = tk.Label(root, text="Test etmek istediğiniz API adresini girin:")
label.pack(pady=10)

# API adresi girişi için bir giriş kutusu
entry_api = tk.Entry(root, width=50)
entry_api.pack(pady=10)

# API kontrol butonu
button_kontrol = tk.Button(root, text="API'yi Kontrol Et", command=api_kontrol)
button_kontrol.pack(pady=20)

# Pencereyi başlat
root.mainloop()
