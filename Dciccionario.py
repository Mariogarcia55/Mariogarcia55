None
#"esta es la parte en la cual el diccionario se almacena"
meme = {'LOL': 'una respuesta a algo gracioso',
    'CRINGE': 'algo raro o embarazoso',
    'ROFL' : 'una respuesta a una broma',
    'SHEESH' : 'ligera desaprobación',
    'CREEPY' : 'aterrador, siniestro',
    'AGGRO' : 'ponerse agresivo/enojado',
     'GOMA': 'estado en que se encuentra una persona depues de tomar mucha cerveza' ,
       'CHULO':'Bonito',
       'CLAVERO':'peleonero o inprudente',
       }
#"la pregunta para saber que palabra buscar"
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme.keys():
    print(meme[palabra])
else:
    print('por favor ingrese la palabra a buscar de manera correcta')
#"la nueva lista "
alumnos ={
    'ALEJANDRO' : 'Educacion fisisca',
    'JOSHUA' : 'Literatura',
    'MARCOS' : 'Matematicas'    
}
nombre_alumno= input("Escribe el nombre del Alumno (¡con mayúsculas!): ")

if nombre_alumno in alumnos.keys():
    print(alumnos[nombre_alumno])
else:
    print('Ingrese el nombre del alumno')
