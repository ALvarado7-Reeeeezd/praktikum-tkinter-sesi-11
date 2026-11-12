import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

APP_TITLE = "Pendaftaran Aktivitas Mahasiswa"
BG_COLOR = "#F1F7F2"
GREEN = "#006B3F"
DARK_GREEN = "#004D2C"
WHITE = "#FFFFFF"
TEXT = "#173B2A"
MUTED = "#64796B"

ACTIVITY_OPTIONS = [
    "Programming Club",
    "English Club",
    "Photography Club",
    "Sports Club",
    "Music Club",
    "Arabic Club",
    "Hufadz Club"
]

STUDY_OPTIONS = [
    "Sistem Informasi",
    "Teknik Informatika",
    "Teknologi Informasi"
]

root = tk.Tk()
root.title(APP_TITLE)
root.geometry("950x800")
root.minsize(800, 650)
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", padding=7, font=("Segoe UI", 10))
style.configure("TCombobox", padding=7, font=("Segoe UI", 10))
style.configure("TButton", padding=8, font=("Segoe UI", 10))
style.configure(
    "Green.TButton",
    background=GREEN,
    foreground=WHITE,
    padding=9,
    font=("Segoe UI", 10, "bold")
)
style.map(
    "Green.TButton",
    background=[("active", DARK_GREEN), ("pressed", DARK_GREEN)],
    foreground=[("active", WHITE)]
)
style.configure("TRadiobutton", background=WHITE, font=("Segoe UI", 10))
style.configure("TCheckbutton", background=WHITE, font=("Segoe UI", 10))

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Keluar", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)

header = tk.Frame(root, bg=GREEN, padx=30, pady=22)
header.pack(fill="x")

tk.Label(
    header,
    text="CHECK POTENSI MAHASISWA",
    font=("Segoe UI", 10, "bold"),
    bg=GREEN,
    fg="#D1FAE5"
).pack(anchor="w")

tk.Label(
    header,
    text="Pendaftaran Aktivitas Mahasiswa",
    font=("Segoe UI", 22, "bold"),
    bg=GREEN,
    fg=WHITE
).pack(anchor="w", pady=(8, 4))

tk.Label(
    header,
    text="Daftarkan dirimu dan kembangkan potensimu melalui kegiatan mahasiswa.",
    font=("Segoe UI", 10),
    bg=GREEN,
    fg=WHITE
).pack(anchor="w")

container = tk.Frame(root, bg=BG_COLOR)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, bg=BG_COLOR, highlightthickness=0)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

content = tk.Frame(canvas, bg=BG_COLOR, padx=25, pady=20)
content_window = canvas.create_window((0, 0), window=content, anchor="nw")

def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

def resize_content(event):
    canvas.itemconfigure(content_window, width=event.width)

def mouse_scroll(event):
    canvas.yview_scroll(int(-event.delta / 120), "units")

content.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_content)
canvas.bind_all("<MouseWheel>", mouse_scroll)

tk.Label(
    content,
    text="Formulir Pendaftaran",
    font=("Segoe UI", 17, "bold"),
    bg=BG_COLOR,
    fg=TEXT
).pack(anchor="w")

tk.Label(
    content,
    text="Lengkapi informasi diri dan pilih kegiatan yang ingin kamu ikuti.",
    font=("Segoe UI", 10),
    bg=BG_COLOR,
    fg=MUTED
).pack(anchor="w", pady=(4, 15))

identity_card = tk.Frame(content, bg=WHITE, padx=18, pady=16)
identity_card.pack(fill="x", pady=(0, 14))

tk.Label(
    identity_card,
    text="Informasi Mahasiswa",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=GREEN
).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

tk.Label(
    identity_card,
    text="Nama Lengkap",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT
).grid(row=1, column=0, sticky="w", pady=(0, 5))

tk.Label(
    identity_card,
    text="Program Studi",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT
).grid(row=1, column=1, sticky="w", pady=(0, 5))

name_entry = ttk.Entry(identity_card)
name_entry.grid(row=2, column=0, sticky="ew", padx=(0, 15), pady=(0, 14))

study_combo = ttk.Combobox(
    identity_card,
    values=STUDY_OPTIONS,
    state="readonly"
)
study_combo.grid(row=2, column=1, sticky="ew", pady=(0, 14))
study_combo.set("Pilih Program Studi")

tk.Label(
    identity_card,
    text="Jenis Kelamin",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT
).grid(row=3, column=0, sticky="w", pady=(0, 6))

gender_var = tk.StringVar(value="")
gender_frame = tk.Frame(identity_card, bg=WHITE)
gender_frame.grid(row=4, column=0, sticky="w")

ttk.Radiobutton(
    gender_frame,
    text="Laki-laki",
    variable=gender_var,
    value="Laki-laki"
).pack(side="left", padx=(0, 18))

ttk.Radiobutton(
    gender_frame,
    text="Perempuan",
    variable=gender_var,
    value="Perempuan"
).pack(side="left")

identity_card.columnconfigure(0, weight=1)
identity_card.columnconfigure(1, weight=1)

activity_card = tk.Frame(content, bg=WHITE, padx=18, pady=16)
activity_card.pack(fill="x", pady=(0, 14))

tk.Label(
    activity_card,
    text="Pilihan Kegiatan Mahasiswa",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=GREEN
).pack(anchor="w", pady=(0, 10))

activity_content = tk.Frame(activity_card, bg=WHITE)
activity_content.pack(fill="x")

checkbox_frame = tk.Frame(activity_content, bg=WHITE)
checkbox_frame.pack(side="left", fill="both", expand=True)

tk.Label(
    checkbox_frame,
    text="Pilih kegiatan:",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT
).pack(anchor="w", pady=(0, 6))

activity_vars = {}
syncing = False

def sync_listbox_from_checkbuttons():
    global syncing
    syncing = True
    activity_listbox.selection_clear(0, tk.END)
    for index, activity in enumerate(ACTIVITY_OPTIONS):
        if activity_vars[activity].get():
            activity_listbox.selection_set(index)
    syncing = False

for activity in ACTIVITY_OPTIONS:
    var = tk.BooleanVar(value=False)
    activity_vars[activity] = var
    ttk.Checkbutton(
        checkbox_frame,
        text=activity,
        variable=var,
        command=sync_listbox_from_checkbuttons
    ).pack(anchor="w", pady=2)

listbox_frame = tk.Frame(activity_content, bg=WHITE)
listbox_frame.pack(side="left", fill="both", expand=True, padx=(20, 0))

tk.Label(
    listbox_frame,
    text="Daftar kegiatan tersedia:",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT
).pack(anchor="w", pady=(0, 6))

listbox_container = tk.Frame(listbox_frame, bg=WHITE)
listbox_container.pack(fill="both", expand=True)

activity_listbox = tk.Listbox(
    listbox_container,
    height=7,
    selectmode=tk.MULTIPLE,
    font=("Segoe UI", 10),
    exportselection=False
)
activity_listbox.pack(side="left", fill="both", expand=True)

listbox_scrollbar = ttk.Scrollbar(
    listbox_container,
    orient="vertical",
    command=activity_listbox.yview
)
listbox_scrollbar.pack(side="right", fill="y")
activity_listbox.configure(yscrollcommand=listbox_scrollbar.set)

for activity in ACTIVITY_OPTIONS:
    activity_listbox.insert(tk.END, activity)

def sync_checkbuttons_from_listbox(event=None):
    global syncing
    if syncing:
        return
    syncing = True
    selected = activity_listbox.curselection()
    for index, activity in enumerate(ACTIVITY_OPTIONS):
        activity_vars[activity].set(index in selected)
    syncing = False

activity_listbox.bind("<<ListboxSelect>>", sync_checkbuttons_from_listbox)

reason_card = tk.Frame(content, bg=WHITE, padx=18, pady=16)
reason_card.pack(fill="x", pady=(0, 14))

tk.Label(
    reason_card,
    text="Alasan Mengikuti Kegiatan",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=GREEN
).pack(anchor="w", pady=(0, 8))

reason_text = tk.Text(
    reason_card,
    height=4,
    font=("Segoe UI", 10),
    wrap="word",
    padx=8,
    pady=7
)
reason_text.pack(fill="x")

tk.Label(
    reason_card,
    text="Ceritakan alasan dan tujuan kamu mengikuti kegiatan tersebut.",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg=MUTED
).pack(anchor="w", pady=(5, 0))

button_frame = tk.Frame(content, bg=BG_COLOR)
button_frame.pack(fill="x", pady=(0, 14))

summary_card = tk.Frame(content, bg=WHITE, padx=18, pady=16)
summary_card.pack(fill="x", pady=(0, 20))

tk.Label(
    summary_card,
    text="Ringkasan Pendaftaran",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=GREEN
).pack(anchor="w", pady=(0, 8))

summary_text = tk.Text(
    summary_card,
    height=10,
    font=("Consolas", 10),
    wrap="word",
    padx=9,
    pady=8,
    state="disabled"
)
summary_text.pack(fill="x")

def display_summary(data):
    summary_text.config(state="normal")
    summary_text.delete("1.0", tk.END)
    summary_text.insert(tk.END, data)
    summary_text.config(state="disabled")

def submit_registration():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning(
            "Peringatan",
            "Nama lengkap wajib diisi!",
            parent=root
        )
        name_entry.focus_set()
        return

    study = study_combo.get()
    if study == "Pilih Program Studi":
        study = "Belum dipilih"

    gender = gender_var.get()
    if not gender:
        gender = "Belum dipilih"

    selected_activities = [
        activity for activity in ACTIVITY_OPTIONS
        if activity_vars[activity].get()
    ]

    if selected_activities:
        activity_result = "\n".join(
            f"- {activity}" for activity in selected_activities
        )
    else:
        activity_result = "- Belum memilih kegiatan"

    reason = reason_text.get("1.0", tk.END).strip()
    if not reason:
        reason = "Tidak ada alasan yang dituliskan."

    registration_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    summary = (
        "DATA PENDAFTARAN MAHASISWA\n"
        "----------------------------------------\n"
        f"Nama Lengkap  : {name}\n"
        f"Program Studi : {study}\n"
        f"Jenis Kelamin : {gender}\n\n"
        "Kegiatan yang Dipilih:\n"
        f"{activity_result}\n\n"
        "Alasan Pendaftaran:\n"
        f"{reason}\n\n"
        f"Waktu Pendaftaran: {registration_time}\n"
        "\nPendaftaran berhasil."
    )

    display_summary(summary)
    messagebox.showinfo(
        "Pendaftaran Berhasil",
        f"Terima kasih, {name}!\n\nData pendaftaran berhasil ditampilkan.",
        parent=root
    )

def reset_form():
    confirmation = messagebox.askyesno(
        "Konfirmasi Reset",
        "Apakah kamu yakin ingin mengosongkan formulir?",
        parent=root
    )
    if not confirmation:
        return

    name_entry.delete(0, tk.END)
    study_combo.set("Pilih Program Studi")
    gender_var.set("")

    for var in activity_vars.values():
        var.set(False)

    activity_listbox.selection_clear(0, tk.END)
    reason_text.delete("1.0", tk.END)
    display_summary("Belum ada data pendaftaran.")
    name_entry.focus_set()

ttk.Button(
    button_frame,
    text="Submit Pendaftaran",
    style="Green.TButton",
    command=submit_registration
).pack(side="left", padx=(0, 8))

ttk.Button(
    button_frame,
    text="Reset Formulir",
    command=reset_form
).pack(side="left")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Tentang Aplikasi")
    about_window.geometry("350x230")
    about_window.resizable(False, False)
    about_window.configure(bg=WHITE)
    about_window.transient(root)
    about_window.grab_set()

    tk.Label(
        about_window,
        text="CHECK POTENSI MAHASISWA",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=GREEN
    ).pack(pady=(25, 10))

    tk.Label(
        about_window,
        text="Pendaftaran Aktivitas Mahasiswa",
        font=("Segoe UI", 14, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(pady=5)

    tk.Label(
        about_window,
        text="Aplikasi pendaftaran kegiatan mahasiswa.\nDibuat menggunakan Python dan Tkinter.",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=MUTED,
        justify="center"
    ).pack(pady=12)

    ttk.Button(
        about_window,
        text="Tutup",
        command=about_window.destroy
    ).pack(pady=5)

help_menu.add_command(label="Tentang Aplikasi", command=show_about)

root.bind("<Return>", lambda event: submit_registration())

display_summary("Belum ada data pendaftaran.\nSilakan lengkapi formulir, kemudian tekan Submit.")
name_entry.focus_set()


root.mainloop()