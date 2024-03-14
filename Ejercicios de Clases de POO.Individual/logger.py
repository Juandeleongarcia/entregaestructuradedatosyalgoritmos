class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.log_count = 0
        self.file = open(self.filename, "W")
        self.file.write("--Start log--\n")

    def log(self, mensaje):
       self.log_count += 1
       self.file.write(mensaje + "\n")

    def __del__(self):
        self.file.write("--End log: {} log(s)--\n".format(self.log_count))
        self.file.close()

class Test:
    def __init__(self):
        self.logger = Logger("log.txt")

    def llamada(self, mensaje):
        self.logger.log(mensaje)

test = Test()
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))

del test 
