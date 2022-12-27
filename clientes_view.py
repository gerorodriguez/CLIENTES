import clientes_controller
import os


def screen_clear():
    # para macOS y  linux (os.name es 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    # para windows platfrom
    else:
        _ = os.system('cls')


    
def menu_principal():
    item = 0
    while item!=99:
        screen_clear()
        print('')
        print('##################')
        print('### CLIENTES ###')
        print('##################')
        print('')
        print('Menú:')
        print('-----------------')
        print('')
        print(' 1 - Buscar CLIENTE por su ID')
        print(' 2 - Alta nuevo cliente')
        print('99 - Finalizar')
        print('')
        item = int(input('Ingrese la opción deseada y presione ENTER para continuar:\n'))
    
        if item == 1:
            id_cliente_a_buscar = ingresar_id_cliente()
            cliente_buscado = buscar_cliente_x_Id(id_cliente_a_buscar)
            if cliente_buscado:
                mostrar_cliente(cliente_buscado)
                menu_baja_modificacion(cliente_buscado)
            else: 
                print('### El Id de Cliente:', 
                                        id_cliente_a_buscar, 'no se ha encontrado ###')
                input('Presione ENTER para continuar.\n') 
            continue
        elif item == 2:
            cliente_nuevo = ingresar_datos_cliente('', 'alta')
            guardar_cliente(cliente_nuevo)
            continue
        elif item != 99: 
            input('La opción ingresada no es válida, presione ENTER para continuar.\n')


def menu_baja_modificacion(cliente_buscado):
    item = 0
    while item!=99:
        print('Menú:')
        print('-----------------')
        print('')
        print(' 1 - Elminar cliente')
        print(' 2 - Modificar cliente')
        print('99 - Volver al menu anterior')
        print('')
        item = int(input('Ingrese la opción deseada y presione ENTER para continuar:\n'))
        if item == 1:
            eliminar_cliente(cliente_buscado)
            input('Presione ENTER para continuar.\n')
            menu_principal()
            break
        elif item == 2:
            cliente_modificado = ingresar_datos_cliente(cliente_buscado, 'modif')
            modificar_cliente(cliente_modificado)
            input('Presione ENTER para continuar.\n')
            menu_principal()
            break
        elif item!=99: 
            print('')
            input('La opción ingresada no es válida, presione ENTER para continuar.\n')

###############################################################################
### FUNCION PARA INGRESO DE DATOS CLIENTE                                    ### 
###############################################################################
def ingresar_datos_cliente(cliente, tipo_ingreso):
    if tipo_ingreso == 'alta':
        titulo = 'Ingrese los datos del nuevo cliente'
    elif tipo_ingreso == 'modif':
        titulo = 'Ingrese los datos a modificar del cliente {} \
            (datos sin cambios presione ENTER)'.format(cliente.id_cliente)
    print('')
    print('########################################################')
    print('### ', titulo)
    print('########################################################')
    print('--------------------------------------------------------')
    val_Apellido = input('Apellido: ')
    print('--------------------------------------------------------')
    val_Nombre = input('Nombre: ')
    print('--------------------------------------------------------')
    val_DNI = input('DNI: ')
    print('--------------------------------------------------------')
    val_Ciudad= input('Ciudad: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    if tipo_ingreso == 'alta':
        cliente_ingresado = clientes_controller.Cliente(1, val_Nombre, val_Apellido, 
                                    val_DNI, val_Ciudad)
    elif tipo_ingreso == 'modif':
        if val_Apellido == '':
            val_Apellido = cliente.apellido_cliente
        if val_Nombre == '':
            val_Nombre = cliente.nombre_cliente
        if val_DNI == '':
            val_DNI = cliente.DNI_cliente
        if val_Ciudad == '':
            val_Ciudad = cliente.ciudad_cliente
        cliente_ingresado = clientes_controller.Cliente(cliente.id_cliente, val_Nombre, 
                    val_Apellido, val_DNI, val_Ciudad)
    return cliente_ingresado    


def ingresar_id_cliente(): 
    screen_clear()
    print('')
    print('########################################################')
    print('### Ingrese Id del cliente a buscar')
    print('########################################################')
    print('--------------------------------------------------------')
    val_Id_Cliente = input('Id Cliente: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return val_Id_Cliente 


###############################################################################
### FUNCION QUE MUESTRA EL CLIENTE RECIBIDO COMO PARAMETRO                    ### 
###############################################################################
def mostrar_cliente(cliente):
    screen_clear()
    print('')
    print('########################################################')
    print('### DATOS CLIENTE ID: {}'.format(cliente.id_cliente))
    print('########################################################')
    print('--------------------------------------------------------')
    print('Apellido: {}'.format(cliente.apellido_cliente))
    print('--------------------------------------------------------')
    print('Nombre: {}'.format(cliente.nombre_cliente))
    print('--------------------------------------------------------')
    print('DNI: {}'.format(cliente.DNI_cliente))
    print('--------------------------------------------------------')
    print('Ciudad: {}'.format(cliente.ciudad_cliente))
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')    

def buscar_cliente_x_Id(id_cliente):
    cliente_a_buscar = clientes_controller.Cliente(id_cliente, '', '', 0, '')
    cliente_buscado = cliente_a_buscar.obtener_cliente_x_Id()
    return cliente_buscado

###############################################################################
### FUNCION OPCION MODIFICAR CLIENTE                                          ### 
###############################################################################
def modificar_cliente(cliente_modificado):
    if cliente_modificado.modificar_cliente():
        print('### El cliente ' + cliente_modificado.apellido_cliente + ', ' + 
            cliente_modificado.nombre_cliente +' (Id de Cliente: '+ 
            str(cliente_modificado.id_cliente) + ') fue modificado exitosamente ###')
    else: 
        print('### Error. El cliente no pudo ser modificado, por favor, intente nuevamente ###')
        
###############################################################################
### FUNCION OPCION ELMINAR CLIENTE                                          ### 
###############################################################################
def eliminar_cliente(cliente_baja):
    if cliente_baja.eliminar_cliente():
        print('#### El cliente ' + cliente_baja.apellido_cliente + ', ' + 
                cliente_baja.nombre_cliente + ' (Id de Cliente: '+ 
                str(cliente_baja.id_cliente) + ') fue eliminado exitosamente ###')
    else: 
        print('### Error. El cliente no pudo ser eliminado, por favor, intente nuevamente ###')

###############################################################################
### FUNCION OPCION ALTA CLIENTE                                               ### 
###############################################################################
def guardar_cliente(cliente_nuevo):
    cliente_guardado = cliente_nuevo.guardar_cliente()
    if cliente_guardado:
        print('### El cliente ' + cliente_guardado.apellido_cliente + ', ' + 
                cliente_guardado.nombre_cliente + ' (Id de Cliente: '+ 
                str(cliente_guardado.id_cliente) + ') fue guardado exitosamente ###')
    else: 
        print('### Error. El cliente no pudo ser guardado, por favor, intente nuevamente ###')


menu_principal()