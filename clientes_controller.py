import clientes_model

class Cliente:
    def __init__(self, id_cliente, nombre_cliente, apellido_cliente, DNI_cliente, ciudad_cliente):
        self.id_cliente = int(id_cliente)
        self.apellido_cliente = apellido_cliente
        self.nombre_cliente = nombre_cliente
        self.DNI_cliente = DNI_cliente
        self.ciudad_cliente = ciudad_cliente
    
    
    def obtener_cliente_x_Id(self):
        cliente_encontrado = clientes_model.buscar_cliente_x_Id(self.id_cliente)
        if cliente_encontrado:
            cliente_devuelto = Cliente(cliente_encontrado[0], cliente_encontrado[1], 
                                    cliente_encontrado[2], cliente_encontrado[3], 
                                    cliente_encontrado[4])
            return cliente_devuelto 
        else:
            return cliente_encontrado
    
    
    def guardar_cliente(self):
        cliente_nuevo = clientes_model.alta_cliente((self.id_cliente, self.nombre_cliente, 
                                        self.apellido_cliente, self.DNI_cliente, 
                                        self.ciudad_cliente))
        
        cliente_guardado = Cliente(cliente_nuevo[0], cliente_nuevo[1], cliente_nuevo[2], 
                                cliente_nuevo[3], cliente_nuevo[4])
        return cliente_guardado 
    
    def eliminar_cliente(self):
        return clientes_model.baja_cliente(self.id_cliente)
    
    def modificar_cliente(self):
        cliente_modificado = (self.id_cliente, self.nombre_cliente, self.apellido_cliente, self.DNI_cliente, self.ciudad_cliente)
        return clientes_model.modificacion_cliente(cliente_modificado)