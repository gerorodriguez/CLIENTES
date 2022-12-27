import mysql.connector
from mysql.connector import Error

def abrir_conexion():
    try:
        conexion=mysql.connector.connect(
                user='root', 
                password='12345', 
                host='localhost', 
                database='clientes', 
                port='3306')
        print("La conexión a la base de datos fue correcta")
        return conexion
    
    except (Exception, Error) as error_capturado: 
        print("Ocurrió el siguiente error en la conexión a la base de datos: ",
                error_capturado) 

def cerrar_conexion(conexion):
    try: 
        conexion.close() 
        print("La conexión a la base de datos cerrada de forma correcta")
    except (Exception, Error) as error_capturado: 
        print("Ocurrió el siguiente error al cerrar la conexión a la base de datos: "
                , error_capturado) 


def buscar_cliente_x_Id(id_buscar):
    try:
        conexion = abrir_conexion() 
        cursor =  conexion.cursor()
        query = 'SELECT ID_CLIENTE, NAME, LAST_NAME, DNI, CITY FROM cliente WHERE ID_CLIENTE = %s'
        cursor.execute(query, (id_buscar,))
        cliente = cursor.fetchone()
        return cliente
    except:
        return False
    finally: 
        cerrar_conexion(conexion)


def alta_cliente(cliente):
    try:
        conexion = abrir_conexion()
        
        cursor =  conexion.cursor()
        
        query = 'INSERT INTO cliente(NAME, LAST_NAME, DNI,\
             CITY) VALUES (%s, %s, %s, %s);'  
             
        cursor.execute(query, cliente[1:])
        conexion.commit()
        
        query = 'SELECT * FROM cliente WHERE ID_CLIENTE = \
                                (SELECT MAX(ID_CLIENTE) FROM cliente)'
        cursor.execute(query) 
        
        cliente = cursor.fetchone()
        
        return cliente
    
    except Error as err:
        print("Se produjo el error", err, "al crear el cliente")
    finally: 
        cerrar_conexion(conexion)
        

def modificacion_cliente(cliente):
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        query = 'UPDATE cliente SET NAME = %s, LAST_NAME = %s, \
            DNI = %s, CITY = %s WHERE ID_CLIENTE = %s;'
        values = (cliente[1], cliente[2], cliente[3], cliente[4], cliente[0])
        cursor.execute(query, values)
        conexion.commit()
        return True
    except: 
        return False
    finally: 
        cerrar_conexion(conexion)

def baja_cliente(id_eliminar):
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        query = 'DELETE FROM cliente WHERE ID_CLIENTE = %s;'
        cursor.execute(query, (id_eliminar,))
        conexion.commit()
        return True
    
    except:
        return False
    finally: 
        cerrar_conexion(conexion)

# alta_cliente((1, "Parker", "Peter", "8798798", "New York"))
print(buscar_cliente_x_Id(2))