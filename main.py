import customtkinter as ctk
import sqlite3
import os
import sys
import winreg
from tkinter import messagebox
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DB_NAME = "metas_semanais.db"


# =========================
# BANCO DE DADOS
# =========================
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meta TEXT,
    categoria TEXT,
    prioridade TEXT,
    status TEXT,
    prazo TEXT,
    observacoes TEXT
)
""")

conn.commit()


# =========================
# INICIAR COM WINDOWS
# =========================
def toggle_startup(enable):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "PlanilhaMetas"
    exe_path = os.path.abspath(sys.argv[0])

    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_ALL_ACCESS)

    try:
        if enable:
            winreg.SetValueEx(reg, app_name, 0, winreg.REG_SZ, exe_path)
        else:
            winreg.DeleteValue(reg, app_name)
    except:
        pass


# =========================
# APP
# =========================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Planilha de Metas Semanais")
        self.geometry("1100x650")

        self.create_widgets()
        self.load_data()

    # =====================
    # INTERFACE
    # =====================
    def create_widgets(self):

        # -------- Frame superior
        top = ctk.CTkFrame(self)
        top.pack(fill="x", padx=10, pady=10)

        self.meta_entry = ctk.CTkEntry(top, placeholder_text="Meta / Atividade", width=200)
        self.meta_entry.grid(row=0, column=0, padx=5)

        self.categoria = ctk.CTkOptionMenu(top, values=[
            "Estudos", "Saúde", "Projetos", "Lazer", "Trabalho", "Manutenção"
        ])
        self.categoria.grid(row=0, column=1, padx=5)

        self.prioridade = ctk.CTkOptionMenu(top, values=[
            "Alta", "Média", "Baixa"
        ])
        self.prioridade.grid(row=0, column=2, padx=5)

        self.status = ctk.CTkOptionMenu(top, values=[
            "Não iniciado", "Em andamento", "Concluído"
        ])
        self.status.grid(row=0, column=3, padx=5)

        self.prazo = ctk.CTkOptionMenu(top, values=[
            "Segunda", "Terça", "Quarta", "Quinta",
            "Sexta", "Sábado", "Domingo"
        ])
        self.prazo.grid(row=0, column=4, padx=5)

        self.obs_entry = ctk.CTkEntry(top, placeholder_text="Observações", width=200)
        self.obs_entry.grid(row=0, column=5, padx=5)

        add_btn = ctk.CTkButton(top, text="Adicionar Meta", command=self.add_meta)
        add_btn.grid(row=0, column=6, padx=10)

        # =========================================================
        # TABELA PROFISSIONAL
        # =========================================================
        table_frame = ctk.CTkFrame(self, corner_radius=12)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
            background="#1e1e1e",
            foreground="#ffffff",
            rowheight=34,
            fieldbackground="#1e1e1e",
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure("Treeview.Heading",
            background="#2b2b2b",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat"
        )

        style.map("Treeview.Heading",
            background=[("active", "#3a3a3a")]
        )

        style.map("Treeview",
            background=[("selected", "#144870")],
            foreground=[("selected", "white")]
        )

        columns = ("Meta", "Categoria", "Prioridade", "Status", "Prazo", "Observações")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.tree.column("Meta", anchor="w", width=260)
        self.tree.column("Categoria", anchor="center", width=120)
        self.tree.column("Prioridade", anchor="center", width=110)
        self.tree.column("Status", anchor="center", width=140)
        self.tree.column("Prazo", anchor="center", width=110)
        self.tree.column("Observações", anchor="w", width=300)

        for col in columns:
            self.tree.heading(col, text=col)

        scrollbar = ctk.CTkScrollbar(table_frame, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Zebra rows
        self.tree.tag_configure("oddrow", background="#252526")
        self.tree.tag_configure("evenrow", background="#1e1e1e")

        # -------- Frame inferior
        bottom = ctk.CTkFrame(self)
        bottom.pack(fill="x", padx=10, pady=5)

        del_btn = ctk.CTkButton(bottom, text="Excluir Selecionada", command=self.delete_meta)
        del_btn.pack(side="left", padx=5)

        edit_btn = ctk.CTkButton(bottom, text="Marcar como Concluído", command=self.mark_done)
        edit_btn.pack(side="left", padx=5)

        self.startup_var = ctk.BooleanVar()
        startup_check = ctk.CTkCheckBox(
            bottom,
            text="Iniciar com o Windows",
            variable=self.startup_var,
            command=lambda: toggle_startup(self.startup_var.get())
        )
        startup_check.pack(side="right", padx=10)

    # =====================
    # FUNÇÕES
    # =====================
    def add_meta(self):

        meta = self.meta_entry.get().strip()
        if not meta:
            messagebox.showwarning("Aviso", "Digite uma meta.")
            return

        categoria = self.categoria.get()
        prioridade = self.prioridade.get()
        status = self.status.get()
        prazo = self.prazo.get()
        obs = self.obs_entry.get()

        cursor.execute("SELECT COUNT(*) FROM metas WHERE prioridade='Alta'")
        high_count = cursor.fetchone()[0]

        if prioridade == "Alta" and high_count >= 3:
            if not messagebox.askyesno(
                "Regra dos 3",
                "Você já possui 3 metas de prioridade alta.\nDeseja adicionar mesmo assim?"
            ):
                return

        cursor.execute("""
            INSERT INTO metas(meta, categoria, prioridade, status, prazo, observacoes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (meta, categoria, prioridade, status, prazo, obs))

        conn.commit()
        self.load_data()

        self.meta_entry.delete(0, "end")
        self.obs_entry.delete(0, "end")

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        cursor.execute("SELECT id, meta, categoria, prioridade, status, prazo, observacoes FROM metas")

        for index, row in enumerate(cursor.fetchall()):

            status_tag = row[4]
            zebra = "evenrow" if index % 2 == 0 else "oddrow"

            self.tree.insert(
                "",
                "end",
                iid=row[0],
                values=row[1:],
                tags=(status_tag, zebra)
            )

        self.tree.tag_configure("Concluído", background="#1f6e43")
        self.tree.tag_configure("Em andamento", background="#5a4a00")
        self.tree.tag_configure("Não iniciado", background="#3a3a3a")

    def delete_meta(self):

        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            cursor.execute("DELETE FROM metas WHERE id=?", (item,))
        conn.commit()

        self.load_data()

    def mark_done(self):

        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            cursor.execute(
                "UPDATE metas SET status='Concluído' WHERE id=?",
                (item,)
            )

        conn.commit()
        self.load_data()


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = App()
    app.mainloop()