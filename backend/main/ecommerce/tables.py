get_table_ingrediente = '''
<h1>Datos que se obtienen de un get</h1>
<h5>El get te retorna un json,es decir, una lista de objetos cuyos atributos son los siguientes</h5>
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>id <br>(int)</td>
            <td>Recibirá el id único del ingrediente.</td>
        </tr>
        <tr>
            <td><b>nombre <br>(str)</b></td>
            <td>Recibirá el nombre único del ingrediente.</td>
        </tr>
        <tr>
            <td><b>unidad <br>(str)</td>
            <td>Recibirá la unidad del ingrediente (ejemplo: "kg", "litros").</td>
        </tr>
        <tr>
            <td><b>cantidad_disponible</b></td>
            <td>Recibirá la cantidad disponible de ese ingrediente.</td>
        </tr>
        <tr>
            <td><b>precio <br>(float)</b></td>
            <td>Recibirá el precio por unidad del ingrediente.</td>
        </tr>
        <tr>
            <td><b>unidades_vendidas <br>(float)</b></td>
            <td>Recibirá las unidades vendidas de ese ingrediente.</td>
        </tr>
    </tbody>
</table>
'''

get_example_ingrediente = [
  {
    "id": 1,
    "nombre": "tomate",
    "unidad": "kg",
    "cantidad_disponible": 10,
    "precio": 1.5,
    "unidades_vendidas": 0
  },
  {
    "id": 2,
    "nombre": "lechuga",
    "unidad": "kg",
    "cantidad_disponible": 10,
    "precio": 1.5,
    "unidades_vendidas": 0
  },
  {
    "id": 4,
    "nombre": "cebolla",
    "unidad": "kg",
    "cantidad_disponible": 10,
    "precio": 2,
    "unidades_vendidas": 0
  }
]

post_table_ingrediente = '''<h1>Cuerpo de la solicitud de tipo post</h1>
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
            <td>Debe ser el nombre único del ingrediente.</td>
        </tr>
        <tr>
            <td><b>unidad <br>(str) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser la unidad del ingrediente.</td>
        </tr>
        <tr>
            <td><b>cantidad_disponible <br>(float) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser la cantidad disponible de ese ingrediente.</td>
        </tr>
        <tr>
            <td><b>precio <br>(float) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser el precio por unidad del ingrediente.</td>
        </tr>
        <tr>
            <td><b>unidades_vendidas <br>(float) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser las unidades vendidas de ese ingrediente.</td>
        </tr>
    </tbody>
</table>
'''

post_example_ingrediente = {
        "nombre": "tomate",
        "unidad": "kg",
        "precio": 1.5,
        "cantidad_disponible": 10.0,
        'unidades_vendidas ': 0.0,
      }

get_table_factura = '''<h1>Datos que se obtienen de un get</h1>
<h5>El get te retorna un json, es decir, una lista de objetos cuyos atributos son los siguientes</h5>
<table>
    <thead>
        <tr>
            <th>Parameter ______________________<div></div></th>
            <th>Description <br>_______________________________________________<div></div></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>id <br>(int)</b></td>
            <td>Será un id único que identificará a esa factura.</td>
        </tr>
        <tr>
            <td><b>codigo <br>(str)</b></td>
            <td>Será el código único de la factura.</td>
        </tr>
        <tr>
            <td><b>nombreCliente <br>(str)</b></td>
            <td>Será el nombre del usuario que hizo la compra.</td>
        </tr>
        <tr>
            <td><b>formaPago <br>(str)</b></td>
            <td>Será la forma de pago utilizada.</td>
        </tr>
        <tr>
            <td><b>cedula <br>(int)</b></td>
            <td>Será la cédula del usuario.</td>
        </tr>
        <tr>
            <td><b>ingredientes <br>(json)</b></td>
            <td>Será un json, es decir, una lista de objetos que representan los ingredientes utilizados en la receta. Cada objeto contiene el id, nombre, unidad, precio por unidad y cantidad disponible del ingrediente, extraídos directamente de la base de datos.</td>
        </tr>
        <tr>
            <td><b>total <br>(float)</b></td>
            <td>Será el total que debe pagar el usuario por la compra.</td>
        </tr>
        <tr>
            <td><b>cantidades <br>(json)</b></td>
            <td>Será un json que representa una lista de números float. Esta lista contiene las cantidades (en las unidades respectivas de cada ingrediente) que usa la receta para cada ingrediente, con un orden que coincide con la lista de ingredientes en el json.</td>
        </tr>
        <tr>
            <td><b>fecha <br>(str)</b></td>
            <td>Será un string con la fecha en que se hizo la compra, en formato año-mes-día.</td>
        </tr>
        <tr>
            <td><b>hora <br>(str)</b></td>
            <td>Será un string con la hora en que se realizó la compra.</td>
        </tr>
    </tbody>
</table>
'''

get_example_factura = [{
        "id": 1,
        "codigo": "0000001",
        "nombreCliente": "Alvarez",
        "formaPago": "Efectivo",
        "cedula": 27314851,
        "ingredientes": [
            {
                "id": 2,
                "nombre": "lechuga",
                "unidad": "kg",
                "precio": 1.5
            }
        ],
        "total": 10.0,
        "cantidades": [
            2
        ],
        "fecha": "2024-10-06",
        "hora": "21:54:56.346678"
    }]

post_table_factura = '''<h1>Cuerpo de la solicitud de tipo post</h1>
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
            <td><b>nombreCliente <br>(str) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un string que será el nombre del usuario que realizó la compra.</td>
        </tr>
        <tr>
            <td><b>formaPago <br>(str) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un string que será la forma de pago del usuario.</td>
        </tr>
        <tr>
            <td><b>cedula <br>(int) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un int que será la cédula del usuario.</td>
        </tr>
        <tr>
            <td><b>total <br>(float) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un float que será el total que pagará el usuario.</td>
        </tr>
        <tr>
            <td><b>ingredientes <br>(json) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un array de strings, los cuales serán los nombres de los ingredientes que usa la receta; estos nombres deben coincidir con los nombres de los ingredientes guardados en la base de datos.</td>
        </tr>
        <tr>
            <td><b>cantidades <br>(json) <br><mark>REQUIRED</mark></b></td>
            <td>Debe ser un array de floats que representarán las cantidades que usa la receta por cada ingrediente; el orden de este array es el mismo que el de ingredientes.</td>
        </tr>
    </tbody>
</table>
'''

post_example_factura = [{
    "cedula": 22406784,
    "total": 22.5,
    "ingredientes": ["lechuga", "Tomate"],
    "cantidades": [0.5,2],
    "nombreCliente": "Alejandro Alvarez",
    "formaPago": "credito debito"
}]