from PyQt5 import QtWidgets, uic, QtGui, QtCore
from WIDGET import logIMG
import time
c = [True, 0]
btc2 = [True, True, True]
class SolucionEscritorio:
    
    def __init__(self):
        
        #Cargado Principal de FRM
        self.app = QtWidgets.QApplication([])
        self.menu = uic.loadUi("FRM_S/FRM_MEN_PRINCIPAL.ui")
        self.log = uic.loadUi("FRM_S/FRM_LOGIN.ui")
        self.reg = uic.loadUi("FRM_S/FRM_REG_USER.ui")
        self.rprod = uic.loadUi("FRM_S/FRM_REG_PROD.ui")
        
        #Asignacion de los titulos de las ventanas de los FRM
        self.log.setWindowTitle("Acceso Login")
        self.menu.setWindowTitle("Menu Principal")
        self.reg.setWindowTitle("Registro de Usuario")
        self.rprod.setWindowTitle("Registro de Productos")
        
        #Interfaz de Splash
        ImgPix2 = QtGui.QPixmap("IMG/METROSPLASH.png")
        self.splash = QtWidgets.QSplashScreen(ImgPix2, QtCore.Qt.WindowStaysOnTopHint)
        self.splash.setMask(ImgPix2.mask())
        self.splash.show()

        #Tres segundos de Splash
        for i in range(1, 11):
            time.sleep(0.3)
        
        #Termino de Splash e inicio del Menu
        self.splash.finish(self.menu)
        
        #Funcion de los botones FRM Login
        self.log.login.clicked.connect(self.botonlog)
        self.log.cerrar.clicked.connect(self.cierrelog)
        
        #Funcion de los botones FRM Menu Principal
        self.menu.bt_inicio_sesion.clicked.connect(self.conexionLog)
        self.menu.bt_registrate.clicked.connect(self.conexionReg)
        self.menu.bt_ingreso_ventas.clicked.connect(self.si_ventas)
        self.menu.bt_ingreso_compras.clicked.connect(self.si_compras)
        self.menu.bt_ingreso_almacen.clicked.connect(self.si_almacen)
        #self.menu.bt_accion1.clicked.connect(self.accionar1)
        self.menu.bt_accion2.clicked.connect(self.accionar2)
        #self.menu.bt_accion3.clicked.connect(self.accionar3)
        
        #Funcion de los botones FRM Registro de Usuario
        self.reg.bt_cancelar.clicked.connect(self.cierreReg)
        
        #Funcion de los botones FRM Registro de Productos
        self.rprod.bt_cancelar_prod.clicked.connect(self.cierreRegProd)
        
        #AGREGRADO DE DATOS EN COMBO-BOX
        #PARA MENU
        self.menu.cb_estado.addItem("Disponible","4")
        self.menu.cb_estado.addItem("Ausente","3")
        self.menu.cb_estado.addItem("Ocupado","2")
        self.menu.cb_estado.addItem("Descanso","1")
        self.menu.cb_estado.addItem("Inactivo","0")
        self.menu.cb_estado.setCurrentIndex(self.menu.cb_estado.findData("0"))
        
        #PARA REG USER
        self.reg.cb_tipoDNI_personal.addItem("Seleccione","0")
        self.reg.cb_tipoDNI_personal.addItem("DNI","1")
        self.reg.cb_tipoDNI_personal.addItem("CE","2")
        self.reg.cb_tipoDNI_personal.addItem("Pasaporte","3")
        
        self.reg.cb_permisos_reg.addItem("Usuario Estandar","0")
        self.reg.cb_permisos_reg.addItem("Usuario Privilegiado","1")
        self.reg.cb_permisos_reg.addItem("Admin","2")

        self.reg.cb_rol_reg.addItem("Seleccione","0")
        self.reg.cb_rol_reg.addItem("Vendedor","1")
        self.reg.cb_rol_reg.addItem("Auxiliar de Almacén","2")
        self.reg.cb_rol_reg.addItem("Auxiliar de Compras","3")
        self.reg.cb_rol_reg.addItem("Asistente de Ventas","4")
        self.reg.cb_rol_reg.addItem("Jefe de Ventas","5")
        self.reg.cb_rol_reg.addItem("Jefe de Almacen","6")
        self.reg.cb_rol_reg.addItem("Jefe de Compras","7")
        self.reg.cb_rol_reg.addItem("Administrador General","8")
        self.reg.cb_rol_reg.addItem("Administrador del Sistema","9")
        self.reg.cb_rol_reg.addItem("Analista del Sistema","10")
        self.reg.cb_rol_reg.addItem("Gerente","11")
        
        #PARA REG PRODUCTO
        self.rprod.cb_medida_prod.addItem("Seleccione","0")
        self.rprod.cb_medida_prod.addItem("Unidad","1")
        self.rprod.cb_medida_prod.addItem("Kg","2")
        
        self.rprod.cb_cat_prod.addItem("Seleccione","0")
        self.rprod.cb_cat_prod.addItem("Alimentos","1")
        self.rprod.cb_cat_prod.addItem("Tecnologia","2")
        self.rprod.cb_cat_prod.addItem("Ropa","3")
        self.rprod.cb_cat_prod.addItem("Electrodomesticos","4")
        self.rprod.cb_cat_prod.addItem("Higiene","5")
        self.rprod.cb_cat_prod.addItem("Deportes","6")
        
        self.rprod.cb_state_prod.addItem("Seleccione","0")
        self.rprod.cb_state_prod.addItem("Disponible","0")
        self.rprod.cb_state_prod.addItem("No Disponible","0")
        self.rprod.cb_state_prod.addItem("No comercial","0")
        
        #Ocultado de Botones Iniciales
        self.menu.bt_accion1.hide()
        self.menu.bt_accion2.hide()
        self.menu.bt_accion3.hide()
        
        #Ejecucion de Menu Principal
        self.menu.show()
        self.app.exec()
        
        
    #BOTONES LOGIN
    def botonlog(self):
        user = self.log.username.text()
        pazz = self.log.password.text()
        if len(user) == 0 or len(pazz) == 0:
            self.log.warning.setText("¡Los campos no deben estar vacios!")
        else:
            self.log.warning.setText("¡Sesion Iniciada!")
            
    def cierrelog(self):
        #Se limpia los datos antes de cerrar
        self.log.warning.setText("")
        self.log.username.setText("")
        self.log.password.setText("")
        #Se cierra FRM Login y se abre FRM Menu Principal
        self.log.close()
        self.menu.show()
    
    
    #BOTONES MENU PRINCIPAL   
    def conexionLog(self):
        self.menu.close()
        self.log.show()
    
    def conexionReg(self):
        self.menu.close()
        self.reg.show()
        
    def si_ventas(self):#0
        if c[0] == True:
            self.menu.bt_accion1.show()
            self.menu.bt_accion2.show()
            self.menu.bt_accion3.show()
            c[0] = False
            c[1] = 0

        else:
            c[1] = 0
            self.menu.bt_accion1.setText("Registro\nde\nClientes")
            self.menu.bt_accion2.setText("Registro\nde\nProductos")
            self.menu.bt_accion3.show()
                
    def si_compras(self):#1
        if c[0] == True:
            self.menu.bt_accion1.setText("Registro\nde\nProveedores")
            self.menu.bt_accion2.setText("Generar\nPedido\nde Compra")
            self.menu.bt_accion1.show()
            self.menu.bt_accion2.show()
            c[0] = False
            c[1] = 1
            
        else:
            c[1] = 1
            self.menu.bt_accion1.setText("Registro\nde\nProveedores")
            self.menu.bt_accion2.setText("Generar\nPedido\nde Compra")
            self.menu.bt_accion3.hide()
        
    def si_almacen(self):#2
        if c[0] == True:
            self.menu.bt_accion1.setText("Registro\nde Guias\nde Entrada")
            self.menu.bt_accion2.setText("Registro\nde Guias\nde Salida")
            self.menu.bt_accion1.show()
            self.menu.bt_accion2.show()
            c[0] = False
            c[1] = 2
            
        else:
            c[1] = 2
            self.menu.bt_accion1.setText("Registro\nde Guias\nde Entrada")
            self.menu.bt_accion2.setText("Registro\nde Guias\nde Salida")
            self.menu.bt_accion3.hide()
            
    #def accionar1(self):
        
    def accionar2(self):
        if c[1] == 0:
            self.menu.close()
            self.rprod.show()
        else:
            if c[1] == 1:
                self.menu.close()
                self.log.show()#SOLO ES DE PRUEBA
            #else:
                #if c[1] == 2:
        
    #def accionar3(self):
            
            
    #BOTONES REGISTRO DE USUARIO
    def cierreReg(self):
        self.reg.close()
        self.menu.show()
        
    
    #BOTONES REGISTRO DE PRODUCTOS
    def cierreRegProd(self):
        self.rprod.close()
        self.menu.show()