#import tkinter as tk
#from tkinter import ttk, messagebox
#from datetime import datetime
#from enum import Enum

### 1. Enumeraciones completas con todos los datos requeridos
#class TipoDocumento(Enum):
#    MEMO = "Memorándum"
#    OFICIO = "Oficio"
#    INFORME = "Informe"
#    SOLICITUD = "Solicitud"
#    RECLAMO = "Reclamo"

#class EstadoDocumento(Enum):
#    RECIBIDO = "Recibido"
#    ASIGNADO = "Asignado"
#    EN_PROCESO = "En proceso"
#    FINALIZADO = "Finalizado"
#    ARCHIVADO = "Archivado"

#class Actividad(Enum):
#    INFORME_TECNICO = "Informe técnico"
#    INFORME_SIMPLE = "Informe simple"
#    INSPECCION = "Inspección"
#    REVISION = "Revisión"
#    MANTENIMIENTO = "Mantenimiento"
#    TRAMITE_RECURRENTE = "Trámite recurrente"
#    ACUSE_DE_RECIBO = "Acuse de recibo"
#    APOYO = "Apoyo"

#class MedioRecepcion(Enum):
#    CORREO = "Correo electrónico"
#    MESA_DIGITAL = "Mesa digital"
#    FISICO = "Documento físico"
#    WHATSAPP = "WhatsApp"

#class RolPersonal(Enum):
#    JEFATURA = "Jefatura"
#    MESA_PARTES = "Mesa de Partes"
#    LOC = "LOC"

### 2. Clases del modelo
#class Personal:
#    def __init__(self, id, nombre_completo, rol):
#        self.id = id
#        self.nombre_completo = nombre_completo
#        self.rol = rol
#        self.carga_trabajo = 0
#    
#    def __str__(self):
#        return f"{self.nombre_completo} ({self.rol.value})"

#class Documento:
#    def __init__(self, id, tipo, numero, remitente, asunto, actividad, medio_recepcion, prioridad):
#        self.id = id
#        self.tipo = tipo
#        self.numero = numero
#        self.remitente = remitente
#        self.asunto = asunto
#        self.actividad = actividad
#        self.medio_recepcion = medio_recepcion
#        self.prioridad = prioridad
#        self.fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M")
#        self.estado = EstadoDocumento.RECIBIDO
#        self.responsable = None
#        self.respuesta = None
#        self.historial = []

### 3. Aplicación principal
#class MesaDePartesApp:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("Sistema de Mesa de Partes - Completo")
#        self.root.geometry("1000x700")
#        
#        self.configurar_estilos()
#        self.inicializar_datos()
#        self.crear_interfaz()
#    
#    def configurar_estilos(self):
#        style = ttk.Style()
#        style.configure("TFrame", background="#f0f0f0")
#        style.configure("TLabel", background="#f0f0f0", font=('Arial', 10))
#        style.configure("TButton", font=('Arial', 10), padding=5)
#        style.configure("TCombobox", font=('Arial', 10))
#        style.configure("Treeview", font=('Arial', 10), rowheight=25)
#        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
#    
#    def inicializar_datos(self):
#        self.personal = [
#            Personal("001", "Jefatura", RolPersonal.JEFATURA),
#            Personal("002", "Mesa de partes", RolPersonal.MESA_PARTES),
#            Personal("003", "Loc De Paz Salazar, Marius", RolPersonal.LOC),
#            Personal("004", "Loc Ccorimanya Huachos, Anderson", RolPersonal.LOC),
#            Personal("005", "Loc Cisneros Buendias, Edwin", RolPersonal.LOC),
#            Personal("006", "Loc Chiclla Melo, Jonathan", RolPersonal.LOC),
#            Personal("007", "Loc Huaman Garcia, Gersson", RolPersonal.LOC)
#        ]
#        
#        self.documentos = []
#        self.contador_documentos = 1
#    
#    def crear_interfaz(self):
#        self.notebook = ttk.Notebook(self.root)
#        self.notebook.pack(fill=tk.BOTH, expand=True)
#        
#        self.crear_pestana_registro()
#        self.crear_pestana_documentos()
#        self.crear_pestana_asignacion()
#        self.crear_pestana_respuestas()
#        self.crear_pestana_busqueda()
#    
#    def crear_pestana_registro(self):
#        tab = ttk.Frame(self.notebook)
#        self.notebook.add(tab, text="Registro")
#        
#        frame = ttk.LabelFrame(tab, text="Nuevo Documento", padding=15)
#        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#        
#        for i in range(6):
#            frame.columnconfigure(i, weight=1 if i % 2 == 1 else 0)
#        
#        ttk.Label(frame, text="Tipo de Documento:").grid(row=0, column=0, sticky=tk.E, pady=5)
#        self.tipo_doc = ttk.Combobox(frame, values=[t.value for t in TipoDocumento], state="readonly")
#        self.tipo_doc.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Número:").grid(row=1, column=0, sticky=tk.E, pady=5)
#        self.numero_doc = ttk.Entry(frame)
#        self.numero_doc.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Remitente:").grid(row=2, column=0, sticky=tk.E, pady=5)
#        self.remitente = ttk.Entry(frame)
#        self.remitente.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Asunto:").grid(row=3, column=0, sticky=tk.E, pady=5)
#        self.asunto = tk.Text(frame, height=4, width=40, font=('Arial', 10))
#        self.asunto.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Actividad:").grid(row=0, column=2, sticky=tk.E, pady=5)
#        self.actividad = ttk.Combobox(frame, values=[a.value for a in Actividad], state="readonly")
#        self.actividad.grid(row=0, column=3, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Medio de Recepción:").grid(row=1, column=2, sticky=tk.E, pady=5)
#        self.medio_recepcion = ttk.Combobox(frame, values=[m.value for m in MedioRecepcion], state="readonly")
#        self.medio_recepcion.grid(row=1, column=3, sticky=tk.EW, padx=5, pady=5)
#        
#        ttk.Label(frame, text="Prioridad:").grid(row=2, column=2, sticky=tk.E, pady=5)
#        self.prioridad = ttk.Combobox(frame, values=[1, 2, 3, 4, 5], state="readonly")
#        self.prioridad.set(3)
#        self.prioridad.grid(row=2, column=3, sticky=tk.EW, padx=5, pady=5)
#        
#        btn_frame = ttk.Frame(frame)
#        btn_frame.grid(row=4, column=0, columnspan=4, pady=10)
#        ttk.Button(btn_frame, text="Registrar Documento", command=self.registrar_documento).pack(side=tk.RIGHT)
#    
#    def crear_pestana_documentos(self):
#        tab = ttk.Frame(self.notebook)
#        self.notebook.add(tab, text="Documentos")
#        
#        frame = ttk.Frame(tab)
#        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#        
#        columns = ("id", "tipo", "numero", "remitente", "actividad", "estado", "responsable", "prioridad")
#        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
#        
#        self.tree.heading("id", text="ID")
#        self.tree.heading("tipo", text="Tipo")
#        self.tree.heading("numero", text="Número")
#        self.tree.heading("remitente", text="Remitente")
#        self.tree.heading("actividad", text="Actividad")
#        self.tree.heading("estado", text="Estado")
#        self.tree.heading("responsable", text="Responsable")
#        self.tree.heading("prioridad", text="Prioridad")
#        
#        self.tree.column("id", width=80, anchor=tk.CENTER)
#        self.tree.column("tipo", width=100, anchor=tk.CENTER)
#        self.tree.column("numero", width=100, anchor=tk.CENTER)
#        self.tree.column("remitente", width=150)
#        self.tree.column("actividad", width=120)
#        self.tree.column("estado", width=100, anchor=tk.CENTER)
#        self.tree.column("responsable", width=180)
#        self.tree.column("prioridad", width=70, anchor=tk.CENTER)
#        
#        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
#        self.tree.configure(yscroll=scrollbar.set)
#        
#        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
#        scrollbar.grid(row=0, column=1, sticky=tk.NS)
#        
#        frame.columnconfigure(0, weight=1)
#        frame.rowconfigure(0, weight=1)
#        
#        btn_frame = ttk.Frame(frame)
#        btn_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.E)
#        ttk.Button(btn_frame, text="Actualizar Lista", command=self.actualizar_listado).pack(side=tk.RIGHT)
