import requests
import random
import datetime

get_response = requests.get(url='http://www.tianos.com/site/register')
correos = [
    "@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com",
    "@yahoo.es", "@usmp.pe", "@upc.pe", "@catolica.pe", "@ulm.pe",
    "@cesarvallejo.pe", "@ucv.pe", "@upn.pe", "@esan.pe", "@icpna.pe"
]

nombres = [
    "jose", "carlitos", "luiggi", "daniel", "bernal",
    "ludovick", "lamas_matos", "erica_cueva", "carlos",
    "cythia", "fiorette", "shirley", "juanjo", "johon",
    "walter", "walle", "wolverine", "stron", "ironman",
    "hombreg", "siriusBlack", "mafalda", "jaimito"
]

c = 11
while c <= 1111:
    now = datetime.datetime.now()
    fecha = now.strftime("%y-%m-%d %H:%M:%S")
    rC = random.randint(0, len(correos) - 1)
    rN = random.randint(0, len(nombres) - 1)
    name = nombres[rN]
    email = nombres[rN] + str(c) + correos[rC]
    post_data = {
        'User[name_user]': '{}'.format(name),
        'User[email_user]': '{}'.format(email),
        'User[pass_user]': '123456',
        'User[terms]': '0',
        'User[terms]': '1'
    }
    post_response = requests.post(url="http://www.tianos.com/site/register", data=post_data)
    print(post_response, fecha, name, email)
    c += 1
