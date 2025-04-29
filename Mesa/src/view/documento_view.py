import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

class DocumentoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.window = tk.Frame(self.root, bg="#d1e0e0")
        self.window.pack(fill="both", expand=True)

        # Crear el widget Notebook para las pestañas
        self.tab_control = ttk.Notebook(self.window)
        self.tab_control.pack(fill="both", expand=True)

        # Crear las pestañas
        self.crear_tab_menu()

    def _limpiar_ventana(self):
        # Limpiar contenido dentro de la ventana
        for widget in self.window.winfo_children():
            widget.destroy()

    def crear_tab_menu(self):
        # Pestaña de "Documentos"
        documentos_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(documentos_tab, text="Documentos")

        # Agregar el contenido de la pestaña "Documentos"
        self.ver_documentos(documentos_tab)

        # Pestaña de "Crear Documento"
        crear_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(crear_tab, text="Crear Documento")

        # Agregar el contenido de la pestaña "Crear Documento"
        self.crear_documento(crear_tab)

        # Pestaña de "Personal"
        personal_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(personal_tab, text="Personal y Tareas")

        # Agregar el contenido de la pestaña "Personal"
        self.ver_personal(personal_tab)

    def ver_documentos(self, parent_frame):
        # Título
        tk.Label(parent_frame, text="Documentos Registrados", font=("Arial", 14), bg="#d1e0e0").pack(pady=20)

        # Lista de documentos (suponemos que la base de datos devuelve una lista de diccionarios o tuplas)
        documentos = self.controller.obtener_documentos()

        # Crear un Treeview para mostrar los documentos
        tree = ttk.Treeview(parent_frame, columns=("ID", "Tipo", "Contenido", "Fecha", "Estado"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Tipo", text="Tipo de Documento")
        tree.heading("Contenido", text="Contenido")
        tree.heading("Fecha", text="Fecha de Recepción")
        tree.heading("Estado", text="Estado")

        # Insertar documentos en el Treeview
        for doc in documentos:
            tree.insert("", "end", values=(doc["id_documento"], doc["tipo_documento"], doc["contenido"], doc["fecha_recepcion"], doc["estado"]))

        tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Botón para volver
        tk.Button(parent_frame, text="Volver", command=lambda: self.tab_control.select(0), width=20, height=2, bg="#FFB6C1").pack(pady=10)

    def ver_personal(self, parent_frame):
        # Título
        tk.Label(parent_frame, text="Personal y Tareas Asignadas", font=("Arial", 14), bg="#d1e0e0").pack(pady=20)

        # Lista de personal (suponemos que la base de datos devuelve una lista de diccionarios o tuplas)
        personal = self.controller.obtener_personal_con_tareas()

        # Crear un Treeview para mostrar el personal y sus tareas
        tree = ttk.Treeview(parent_frame, columns=("Nombre", "Área", "Documentos Pendientes", "Documentos Realizados"), show="headings")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Área", text="Área")
        tree.heading("Documentos Pendientes", text="Pendientes")
        tree.heading("Documentos Realizados", text="Realizados")

        # Insertar personal y tareas en el Treeview
        for persona in personal:
            tree.insert("", "end", values=(persona["nombre"], persona["area"], persona["documentos_pendientes"], persona["documentos_realizados"]))

        tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Botón para volver
        tk.Button(parent_frame, text="Volver", command=lambda: self.tab_control.select(0), width=20, height=2, bg="#FFB6C1").pack(pady=10)

    def crear_documento(self, parent_frame):
        # Título
        tk.Label(parent_frame, text="Nuevo Documento", font=("Arial", 14), bg="#d1e0e0").pack(pady=10)

        frame = tk.Frame(parent_frame, bg="#d1e0e0")
        frame.pack(padx=20, pady=10)

        # Tipo de Documento (ComboBox)
        tk.Label(frame, text="Tipo de documento:", bg="#d1e0e0").grid(row=0, column=0, sticky='e', pady=5)
        tipos = self.controller.obtener_tipos_documento()  # Obtenemos los tipos de documento
        tipo_var = tk.StringVar()
        tipo_combo = ttk.Combobox(frame, textvariable=tipo_var, values=tipos, state='readonly')
        tipo_combo.grid(row=0, column=1, pady=5)

        # Número HT
        tk.Label(frame, text="Número HT (si tiene):", bg="#d1e0e0").grid(row=1, column=0, sticky='e', pady=5)
        ht_entry = tk.Entry(frame)
        ht_entry.grid(row=1, column=1, pady=5)

        # Fecha de Recepción
        tk.Label(frame, text="Fecha de recepción:", bg="#d1e0e0").grid(row=2, column=0, sticky='e', pady=5)
        fecha_entry = DateEntry(frame, date_pattern='yyyy-mm-dd')  # Utilizamos DateEntry para la fecha
        fecha_entry.grid(row=2, column=1, pady=5)

        # Contenido del Documento (textarea)
        tk.Label(frame, text="Contenido (resumen):", bg="#d1e0e0").grid(row=3, column=0, sticky='ne', pady=5)
        contenido_text = tk.Text(frame, height=6, width=40)  # Usamos un Text para el contenido
        contenido_text.grid(row=3, column=1, pady=5)

        # Personal que atenderá
        tk.Label(frame, text="Asignar a:", bg="#d1e0e0").grid(row=4, column=0, sticky='e', pady=5)
        personal_lista = self.controller.obtener_lista_personal()  # Obtenemos la lista de personal
        personal_var = tk.StringVar()
        personal_combo = ttk.Combobox(frame, textvariable=personal_var, values=personal_lista, state='readonly')
        personal_combo.grid(row=4, column=1, pady=5)

        # Botón para guardar
        def crear():
            tipo = tipo_combo.get()
            contenido = contenido_text.get("1.0", tk.END).strip()
            fecha = fecha_entry.get()
            ht = ht_entry.get().strip()
            personal = personal_combo.get()

            if not tipo or not contenido or not fecha or not personal:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return

            try:
                documento = self.controller.crear_documento(tipo, contenido, fecha, ht, personal)
                messagebox.showinfo("Información", f"Documento creado con ID: {documento.id_documento}")
                self.tab_control.select(0)  # Volver a la pestaña de menú

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(parent_frame, text="Crear Documento", command=crear, width=20, height=2, bg="#A5C8D8").pack(pady=15)
        tk.Button(parent_frame, text="Volver", command=lambda: self.tab_control.select(0), width=20, height=2, bg="#FFB6C1").pack()

def mostrar_pendientes_personal(self, nombre):
    pendientes = self.controller.obtener_pendientes_por_personal(nombre)

    if not pendientes:
        messagebox.showinfo("Pendientes", "Este personal no tiene documentos pendientes.")
        return

    # Ventana de detalle
    detalle = tk.Toplevel(self.root)
    detalle.title(f"Pendientes de {nombre}")

    tree = ttk.Treeview(detalle, columns=("ID", "Tipo", "Contenido", "Fecha"), show="headings")
    tree.pack(fill="both", expand=True)

    tree.heading("ID", text="ID")
    tree.heading("Tipo", text="Tipo de Documento")
    tree.heading("Contenido", text="Contenido")
    tree.heading("Fecha", text="Fecha de Recepción")

    for doc in pendientes:
        tree.insert("", "end", values=doc)
