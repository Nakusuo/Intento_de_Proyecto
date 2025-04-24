import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from enum import Enum

## 1. Enumeraciones completas con todos los datos requeridos
class TipoDocumento(Enum):
    MEMO = "Memorándum"
    OFICIO = "Oficio"
    INFORME = "Informe"
    SOLICITUD = "Solicitud"
    RECLAMO = "Reclamo"

class EstadoDocumento(Enum):
    RECIBIDO = "Recibido"
    ASIGNADO = "Asignado"
    EN_PROCESO = "En proceso"
    FINALIZADO = "Finalizado"
    ARCHIVADO = "Archivado"

class Actividad(Enum):
    INFORME_TECNICO = "Informe técnico"
    INFORME_SIMPLE = "Informe simple"
    INSPECCION = "Inspección"
    REVISION = "Revisión"
    MANTENIMIENTO = "Mantenimiento"
    TRAMITE_RECURRENTE = "Trámite recurrente"
    ACUSE_DE_RECIBO = "Acuse de recibo"
    APOYO = "Apoyo"

class MedioRecepcion(Enum):
    CORREO = "Correo electrónico"
    MESA_DIGITAL = "Mesa digital"
    FISICO = "Documento físico"
    WHATSAPP = "WhatsApp"

class RolPersonal(Enum):
    JEFATURA = "Jefatura"
    MESA_PARTES = "Mesa de Partes"
    LOC = "LOC"

## 2. Clases del modelo
class Personal:
    def __init__(self, id, nombre_completo, rol):
        self.id = id
        self.nombre_completo = nombre_completo
        self.rol = rol
        self.carga_trabajo = 0
    
    def __str__(self):
        return f"{self.nombre_completo} ({self.rol.value})"

class Documento:
    def __init__(self, id, tipo, numero, remitente, asunto, actividad, medio_recepcion, prioridad):
        self.id = id
        self.tipo = tipo
        self.numero = numero
        self.remitente = remitente
        self.asunto = asunto
        self.actividad = actividad
        self.medio_recepcion = medio_recepcion
        self.prioridad = prioridad
        self.fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.estado = EstadoDocumento.RECIBIDO
        self.responsable = None
        self.respuesta = None
        self.historial = []

## 3. Aplicación principal
class MesaDePartesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Mesa de Partes - Completo")
        self.root.geometry("1000x700")
        
        # Configurar el estilo
        self.configurar_estilos()
        
        # Inicializar datos
        self.inicializar_datos()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def configurar_estilos(self):
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=('Arial', 10))
        style.configure("TButton", font=('Arial', 10), padding=5)
        style.configure("TCombobox", font=('Arial', 10))
        style.configure("Treeview", font=('Arial', 10), rowheight=25)
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
    
    def inicializar_datos(self):
        # Personal exacto como lo solicitaste
        self.personal = [
            Personal("001", "Jefatura", RolPersonal.JEFATURA),
            Personal("002", "Mesa de partes", RolPersonal.MESA_PARTES),
            Personal("003", "Loc De Paz Salazar, Marius", RolPersonal.LOC),
            Personal("004", "Loc Ccorimanya Huachos, Anderson", RolPersonal.LOC),
            Personal("005", "Loc Cisneros Buendias, Edwin", RolPersonal.LOC),
            Personal("006", "Loc Chiclla Melo, Jonathan", RolPersonal.LOC),
            Personal("007", "Loc Huaman Garcia, Gersson", RolPersonal.LOC)
        ]
        
        self.documentos = []
        self.contador_documentos = 1
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestañas
        self.crear_pestana_registro()
        self.crear_pestana_documentos()
        self.crear_pestana_asignacion()
        self.crear_pestana_respuestas()
        self.crear_pestana_busqueda()
    
    def crear_pestana_registro(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Registro")
        
        frame = ttk.LabelFrame(tab, text="Nuevo Documento", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar grid
        for i in range(6):
            frame.columnconfigure(i, weight=1 if i % 2 == 1 else 0)
        
        # Campos del formulario
        ttk.Label(frame, text="Tipo de Documento:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.tipo_doc = ttk.Combobox(frame, values=[t.value for t in TipoDocumento], state="readonly")
        self.tipo_doc.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Número:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.numero_doc = ttk.Entry(frame)
        self.numero_doc.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Remitente:").grid(row=2, column=0, sticky=tk.E, pady=5)
        self.remitente = ttk.Entry(frame)
        self.remitente.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Asunto:").grid(row=3, column=0, sticky=tk.E, pady=5)
        self.asunto = tk.Text(frame, height=4, width=40, font=('Arial', 10))
        self.asunto.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Actividad:").grid(row=0, column=2, sticky=tk.E, pady=5)
        self.actividad = ttk.Combobox(frame, values=[a.value for a in Actividad], state="readonly")
        self.actividad.grid(row=0, column=3, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Medio de Recepción:").grid(row=1, column=2, sticky=tk.E, pady=5)
        self.medio_recepcion = ttk.Combobox(frame, values=[m.value for m in MedioRecepcion], state="readonly")
        self.medio_recepcion.grid(row=1, column=3, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Prioridad:").grid(row=2, column=2, sticky=tk.E, pady=5)
        self.prioridad = ttk.Combobox(frame, values=[1, 2, 3, 4, 5], state="readonly")
        self.prioridad.set(3)
        self.prioridad.grid(row=2, column=3, sticky=tk.EW, padx=5, pady=5)
        
        # Botón Registrar
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=4, column=0, columnspan=4, pady=10)
        ttk.Button(btn_frame, text="Registrar Documento", command=self.registrar_documento).pack(side=tk.RIGHT)
    
    def crear_pestana_documentos(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Documentos")
        
        # Frame principal
        frame = ttk.Frame(tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview (tabla)
        columns = ("id", "tipo", "numero", "remitente", "actividad", "estado", "responsable", "prioridad")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        
        # Configurar columnas
        self.tree.heading("id", text="ID")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("numero", text="Número")
        self.tree.heading("remitente", text="Remitente")
        self.tree.heading("actividad", text="Actividad")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("responsable", text="Responsable")
        self.tree.heading("prioridad", text="Prioridad")
        
        self.tree.column("id", width=80, anchor=tk.CENTER)
        self.tree.column("tipo", width=100, anchor=tk.CENTER)
        self.tree.column("numero", width=100, anchor=tk.CENTER)
        self.tree.column("remitente", width=150)
        self.tree.column("actividad", width=120)
        self.tree.column("estado", width=100, anchor=tk.CENTER)
        self.tree.column("responsable", width=180)
        self.tree.column("prioridad", width=70, anchor=tk.CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Layout
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        # Configurar expansión
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        # Botón Actualizar
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.E)
        ttk.Button(btn_frame, text="Actualizar Lista", command=self.actualizar_listado).pack(side=tk.RIGHT)
    
    def crear_pestana_asignacion(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Asignación")
        
        frame = ttk.LabelFrame(tab, text="Asignar Documento", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Documentos sin asignar
        ttk.Label(frame, text="Documentos sin asignar:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.combo_docs_sin_asignar = ttk.Combobox(frame, state="readonly", width=50)
        self.combo_docs_sin_asignar.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Personal disponible
        ttk.Label(frame, text="Asignar a:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.combo_personal = ttk.Combobox(frame, values=[str(p) for p in self.personal], state="readonly", width=50)
        self.combo_personal.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Botón Asignar
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=2, column=1, sticky=tk.E, pady=10)
        ttk.Button(btn_frame, text="Asignar Documento", command=self.asignar_documento).pack(side=tk.RIGHT)
        
        # Configurar expansión
        frame.columnconfigure(1, weight=1)
        
        # Actualizar combobox
        self.actualizar_combobox_asignacion()
    
    def crear_pestana_respuestas(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Respuestas")
        
        frame = ttk.LabelFrame(tab, text="Registrar Respuesta", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Documentos asignados
        ttk.Label(frame, text="Documentos asignados:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.combo_docs_asignados = ttk.Combobox(frame, state="readonly", width=50)
        self.combo_docs_asignados.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Tipo de respuesta
        ttk.Label(frame, text="Tipo de respuesta:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.tipo_respuesta = ttk.Combobox(frame, values=[t.value for t in TipoDocumento], state="readonly")
        self.tipo_respuesta.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Número de respuesta
        ttk.Label(frame, text="Número de respuesta:").grid(row=2, column=0, sticky=tk.E, pady=5)
        self.numero_respuesta = ttk.Entry(frame)
        self.numero_respuesta.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Contenido de respuesta
        ttk.Label(frame, text="Contenido:").grid(row=3, column=0, sticky=tk.NE, pady=5)
        self.texto_respuesta = tk.Text(frame, height=8, width=60, font=('Arial', 10))
        self.texto_respuesta.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Botón Registrar
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=4, column=1, sticky=tk.E, pady=10)
        ttk.Button(btn_frame, text="Registrar Respuesta", command=self.registrar_respuesta).pack(side=tk.RIGHT)
        
        # Configurar expansión
        frame.columnconfigure(1, weight=1)
        
        # Actualizar combobox
        self.actualizar_combobox_respuestas()
    
    def crear_pestana_busqueda(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Búsqueda")
        
        frame = ttk.LabelFrame(tab, text="Buscar Documentos", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Campos de búsqueda
        ttk.Label(frame, text="Buscar por:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.campo_busqueda = ttk.Combobox(frame, values=["Número", "Remitente", "Asunto", "Responsable"], state="readonly")
        self.campo_busqueda.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame, text="Término:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.termino_busqueda = ttk.Entry(frame)
        self.termino_busqueda.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Botón Buscar
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=2, column=1, sticky=tk.E, pady=5)
        ttk.Button(btn_frame, text="Buscar", command=self.buscar_documentos).pack(side=tk.RIGHT)
        
        # Resultados
        self.tree_busqueda = ttk.Treeview(frame, columns=("id", "tipo", "numero", "remitente", "estado"), show="headings")
        self.tree_busqueda.heading("id", text="ID")
        self.tree_busqueda.heading("tipo", text="Tipo")
        self.tree_busqueda.heading("numero", text="Número")
        self.tree_busqueda.heading("remitente", text="Remitente")
        self.tree_busqueda.heading("estado", text="Estado")
        
        self.tree_busqueda.column("id", width=80, anchor=tk.CENTER)
        self.tree_busqueda.column("tipo", width=100, anchor=tk.CENTER)
        self.tree_busqueda.column("numero", width=100, anchor=tk.CENTER)
        self.tree_busqueda.column("remitente", width=200)
        self.tree_busqueda.column("estado", width=100, anchor=tk.CENTER)
        
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree_busqueda.yview)
        self.tree_busqueda.configure(yscroll=scrollbar.set)
        
        self.tree_busqueda.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, pady=10)
        scrollbar.grid(row=3, column=2, sticky=tk.NS)
        
        # Configurar expansión
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(3, weight=1)
    
    ## Funciones de la lógica de negocio
    def registrar_documento(self):
        try:
            # Validar campos obligatorios
            campos_requeridos = [
                self.tipo_doc.get(),
                self.numero_doc.get(),
                self.remitente.get(),
                self.asunto.get("1.0", tk.END).strip(),
                self.actividad.get(),
                self.medio_recepcion.get()
            ]
            
            if not all(campos_requeridos):
                raise ValueError("Todos los campos marcados con * son obligatorios")
            
            # Obtener valores de los combobox
            tipo = next(t for t in TipoDocumento if t.value == self.tipo_doc.get())
            actividad = next(a for a in Actividad if a.value == self.actividad.get())
            medio = next(m for m in MedioRecepcion if m.value == self.medio_recepcion.get())
            prioridad = int(self.prioridad.get())
            
            # Crear documento
            doc = Documento(
                f"DOC-{self.contador_documentos}",
                tipo,
                self.numero_doc.get(),
                self.remitente.get(),
                self.asunto.get("1.0", tk.END).strip(),
                actividad,
                medio,
                prioridad
            )
            
            self.documentos.append(doc)
            self.contador_documentos += 1
            
            # Limpiar formulario
            self.tipo_doc.set('')
            self.numero_doc.delete(0, tk.END)
            self.remitente.delete(0, tk.END)
            self.asunto.delete("1.0", tk.END)
            self.actividad.set('')
            self.medio_recepcion.set('')
            self.prioridad.set(3)
            
            # Actualizar interfaces
            self.actualizar_listado()
            self.actualizar_combobox_asignacion()
            self.actualizar_combobox_respuestas()
            
            messagebox.showinfo("Éxito", f"Documento registrado con ID: {doc.id}")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def actualizar_listado(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Agregar documentos
        for doc in self.documentos:
            responsable = str(doc.responsable) if doc.responsable else ""
            self.tree.insert("", tk.END, values=(
                doc.id,
                doc.tipo.value,
                doc.numero,
                doc.remitente,
                doc.actividad.value,
                doc.estado.value,
                responsable,
                doc.prioridad
            ))
    
    def actualizar_combobox_asignacion(self):
        docs_sin_asignar = [
            f"{doc.id} - {doc.tipo.value} {doc.numero} ({doc.actividad.value})" 
            for doc in self.documentos 
            if doc.estado == EstadoDocumento.RECIBIDO
        ]
        self.combo_docs_sin_asignar["values"] = docs_sin_asignar
        if docs_sin_asignar:
            self.combo_docs_sin_asignar.current(0)
    
    def actualizar_combobox_respuestas(self):
        docs_asignados = [
            f"{doc.id} - {doc.responsable} ({doc.actividad.value})" 
            for doc in self.documentos 
            if doc.estado == EstadoDocumento.ASIGNADO and doc.responsable
        ]
        self.combo_docs_asignados["values"] = docs_asignados
        if docs_asignados:
            self.combo_docs_asignados.current(0)
    
    def asignar_documento(self):
        try:
            if not self.combo_docs_sin_asignar.get() or not self.combo_personal.get():
                raise ValueError("Debe seleccionar un documento y un responsable")
            
            # Obtener documento seleccionado
            doc_id = self.combo_docs_sin_asignar.get().split(" - ")[0]
            doc = next(d for d in self.documentos if d.id == doc_id)
            
            # Obtener personal seleccionado
            personal_nombre = self.combo_personal.get().split(" (")[0]
            personal = next(p for p in self.personal if p.nombre_completo == personal_nombre)
            
            # Asignar
            doc.responsable = personal
            doc.estado = EstadoDocumento.ASIGNADO
            personal.carga_trabajo += 1
            
            # Actualizar interfaces
            self.actualizar_listado()
            self.actualizar_combobox_asignacion()
            self.actualizar_combobox_respuestas()
            
            messagebox.showinfo("Éxito", f"Documento {doc.id} asignado a {personal.nombre_completo}")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def registrar_respuesta(self):
        try:
            if not all([
                self.combo_docs_asignados.get(),
                self.tipo_respuesta.get(),
                self.numero_respuesta.get(),
                self.texto_respuesta.get("1.0", tk.END).strip()
            ]):
                raise ValueError("Todos los campos son obligatorios")
            
            # Obtener documento seleccionado
            doc_id = self.combo_docs_asignados.get().split(" - ")[0]
            doc = next(d for d in self.documentos if d.id == doc_id)
            
            # Registrar respuesta
            doc.respuesta = {
                "tipo": next(t for t in TipoDocumento if t.value == self.tipo_respuesta.get()),
                "numero": self.numero_respuesta.get(),
                "contenido": self.texto_respuesta.get("1.0", tk.END).strip(),
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            doc.estado = EstadoDocumento.FINALIZADO
            
            # Disminuir carga de trabajo del responsable
            if doc.responsable:
                doc.responsable.carga_trabajo = max(0, doc.responsable.carga_trabajo - 1)
            
            # Limpiar formulario
            self.tipo_respuesta.set('')
            self.numero_respuesta.delete(0, tk.END)
            self.texto_respuesta.delete("1.0", tk.END)
            
            # Actualizar interfaces
            self.actualizar_listado()
            self.actualizar_combobox_respuestas()
            
            messagebox.showinfo("Éxito", f"Respuesta registrada para documento {doc.id}")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def buscar_documentos(self):
        campo = self.campo_busqueda.get()
        termino = self.termino_busqueda.get().lower()
        
        if not campo or not termino:
            messagebox.showwarning("Búsqueda", "Debe especificar un campo y término de búsqueda")
            return
        
        # Limpiar resultados anteriores
        for item in self.tree_busqueda.get_children():
            self.tree_busqueda.delete(item)
        
        # Realizar búsqueda
        resultados = []
        for doc in self.documentos:
            valor = ""
            if campo == "Número":
                valor = doc.numero.lower()
            elif campo == "Remitente":
                valor = doc.remitente.lower()
            elif campo == "Asunto":
                valor = doc.asunto.lower()
            elif campo == "Responsable" and doc.responsable:
                valor = doc.responsable.nombre_completo.lower()
            
            if termino in valor:
                resultados.append(doc)
        
        # Mostrar resultados
        for doc in resultados:
            self.tree_busqueda.insert("", tk.END, values=(
                doc.id,
                doc.tipo.value,
                doc.numero,
                doc.remitente,
                doc.estado.value
            ))
        
        messagebox.showinfo("Búsqueda", f"Se encontraron {len(resultados)} documentos")

if __name__ == "__main__":
    root = tk.Tk()
    app = MesaDePartesApp(root)
    root.mainloop()