import yaml

# abrir base de datos (yaml)
f = open('biblio.yaml')

# importarla a un objeto
obras = yaml.load(f)

# generar archivos según el tipo de template
def genera(llave, nombre_archivo, template):
    
    # abrir archivo a escribir
    salida = open(nombre_archivo, 'w')

    # indicar una llave para ordenar
    obras.sort(key = lambda elemento: elemento[llave])

    # abrir template correspondiente
    template = open("templates/" + template + '.tpl', 'r').read()
    inicio, template, final = template.split( '<!--   -->')
    
    print( inicio, file = salida)
    for obra in obras:
        # substituir datos
        print(template.format( obra['Título'], 
                               obra['Autor'], 
                               obra['Año'], 
                               obra['ISBN'], 
                               obra['Idioma'] , 
                               obra['Formato'], 
                               obra['Editorial'], 
                               obra['Fuente'], 
                               obra['Tags'], 
                               obra['Reseña']),
              file = salida)
    print( final, file = salida)
    
genera('Autor', 'autor.html', 'tabla-xhtml')
genera('Autor', 'autor.xml', 'archivo-xml')
genera('Autor', 'tabla.html', 'tabla-unica-xhtml')
