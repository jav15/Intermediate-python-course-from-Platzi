def run():
    # my_list = [1, "Hello", True, 4.5]
    # my_dict = {"firstname": "Facundo", "lastname": "Garcia" }

    super_list = [
    {"firstname": "Facundo", "lastname": "Garcia" },
    {"firstname": "Javier", "lastname": "Iglesias" },
    {"firstname": "Enrique", "lastname": "Gamarra" },
    {"firstname": "Pedro", "lastname": "Garcia" },
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floatubg_nums": [1.1, 4.5, 6.43],
    }

    for key in super_dict:
        print (key, ' - ', super_dict[key])

    # for key, value in super_dict.items():
    #     print(key, "-", value)

    # lista = [1, 2.5, 'DevCode', [5,6] ,4]

    for i in super_list:
       print("Nombre:", i["firstname"], i["lastname"])


    # for i in range(11):
    #     print(i)
    # diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
    
    # for key in diccionario:
    #     print (key, ":", diccionario[key])
   

if __name__ == '__main__':
    run()