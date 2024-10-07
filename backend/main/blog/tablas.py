get_table = '''<h1>Datos que se obtienen de un get</h1>
<h5>El get te retorna un json,es decir, una lista de objetos cuyos atributos son los siguientes</h5>
<table>
    <thead>
        <tr>
            <th>Parameter ______________________<div></div></th>
            <th>Description <br>_______________________________________________<div></div></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>id</b> <br>(<b>int</b>)</td>
            <td>Será un id único que identificará a esa receta.</td>
        </tr>
        <tr>
            <td><b>nombre</b> <br>(<b>str</b>)</td>
            <td>Nombre único de la receta.</td>
        </tr>
        <tr>
            <td><b>descripcion</b> <br>(<b>str</b>)</td>
            <td>Descripción de la receta.</td>
        </tr>
        <tr>
            <td><b>preparacion</b> <br>(<b>str</b>)</td>
            <td>Preparación de la receta.</td>
        </tr>
        <tr>
            <td><b>imagen</b> <br>(<b>str</b>)</td>
            <td>Retorna un string que es la dirección URL que contiene la imagen, es decir, si accedes a esta URL se carga y renderiza la imagen.</td>
        </tr>
        <tr>
            <td><b>puntuacion</b> <br>(<b>float</b>)</td>
            <td>Puntuación de la receta, va de 0.0 a 5.0.</td>
        </tr>
        <tr>
            <td><b>ingredientes</b> <br>(<b>json</b>)</td>
            <td>Será un json, es decir, una lista de objetos que representan los ingredientes utilizados en la receta. Cada objeto contiene el id, nombre, unidad, precio por unidad y cantidad disponible del ingrediente, extraídos directamente de la base de datos.</td>
        </tr>
        <tr>
            <td><b>cantidades</b> <br>(<b>json</b>)</td>
            <td>Lista de números float que contiene las cantidades (en las unidades respectivas de cada ingrediente) que usa la receta, el orden coincide con la lista de ingredientes.</td>
        </tr>
    </tbody>
</table>
'''
get_example1 = {
        "id": 5,
        "nombre": "Ensalada Premiun",
        "descripcion": "Ensaladita",
        "preparacion": "Echas tomate, lechuga y cebolla",
        "imagen": "/imagenes/imagenes/zu_8.gif",
        "puntuacion": 0.0,
        "cantidades": [
            0.5,
            0.5,
            0.5
        ],
        "ingredientes": [
            {
                "id": 1,
                "nombre": "tomate",
                "unidad": "kg",
                "precio": 1.5,
                "cantidad_disponible": 10.0
            },
            {
                "id": 2,
                "nombre": "lechuga",
                "unidad": "kg",
                "precio": 1.5,
                "cantidad_disponible": 10.0
            },
            {
                "id": 4,
                "nombre": "cebolla",
                "unidad": "kg",
                "precio": 2.0,
                "cantidad_disponible": 10.0
            }
        ]
    }

get_example2 ={
        "id": 6,
        "nombre": "Recetita",
        "descripcion": "epale",
        "preparacion": "epale x2",
        "imagen": "/imagenes/imagenes/zu_5.gif",
        "puntuacion": 0.0,
        "cantidades": [
            0.5
        ],
        "ingredientes": [
            {
                "id": 2,
                "nombre": "lechuga",
                "unidad": "kg",
                "precio": 1.5,
                "cantidad_disponible": 10.0
            }
        ]
    }


get_example = [get_example1,get_example2]

post_table = '''
<h1>Cuerpo de la solicitud de tipo post</h1>
<h5>El cuerpo de la solicitud debe contener los siguientes atributos</h5>
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>nombre <br>(str) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un string.</td>
        </tr>
        <tr>
            <td><b>descripcion <br>(str) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un string.</td>
        </tr>
        <tr>
            <td><b>preparacion <br>(str)<br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un string.</td>
        </tr>
        <tr>
            <td><b>imagen <br>(file) </td>
            <td>Debe ser un archivo de tipo imagen.</td>
        </tr>
        <tr>
            <td><b>puntuacion <br>(float) <mark>REQUIRED</mark></b></td>
            <td>Debe ser un float que esté entre 0.0 y 5.0.</td>
        </tr>
        <tr>
            <td><b>ingredientes <br>(json) <mark>REQUIRED</mark></b></td>
            <td>Debe ser un array de strings, los cuales serán los nombres de los ingredientes que use la receta; estos nombres deben coincidir con los nombres de los ingredientes guardados en la base de datos.</td>
        </tr>
        <tr>
            <td><b>cantidades <br>(json) <mark>REQUIRED</mark></b></td>
            <td>Debe ser un array de floats que representarán las cantidades que usa la receta por cada ingrediente; el orden de este array es el mismo que el de ingredientes.</td>
        </tr>
    </tbody>
</table>
'''

post_example = [{
  "nombre": "Nombre de la receta",
  "descripcion": "Descripción de la receta",
  "preparacion": "Instrucciones detalladas para la preparación de la receta",
  "imagen": "Aqui debe ir una variable que capture el archivo de tipo file", 
  "puntuacion": 4.5,
  "ingredientes": ["tomate","lechuga"],
  "cantidades": [0.5,1.5]
}
]