class MyClass:
    def get_self_instance(self):
        return self
    
    def get_length(self, iterable):
        return len(iterable)

objeto = MyClass()

obtener_instancia_self = objeto.get_self_instance

print(obtener_instancia_self())

instancia_1 = MyClass()
instancia_2 = MyClass()
print(instancia_1 is instancia_2)

obtener_longitud = objeto.get_length

print(obtener_longitud(()))

print(MyClass().get_length((objeto,)))

print(MyClass.get_length(objeto, (objeto, obtener_longitud)))

print(objeto.get_length((obtener_instancia_self(), 1, 'z')))
