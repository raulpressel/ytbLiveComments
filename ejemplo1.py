import pytchat
import os
import json

'''Scypt que sirve para sacar comentarios de videos online'''

videoID ="r8CBlLQfwEA"

chat = pytchat.create(video_id=videoID)



def salvar(Archivo, Valor):
    if os.path.exists(Archivo):
        with open(Archivo) as f:
            data = json.load(f)
    else:
        data = []
    data.append(Valor)

    with open(Archivo, 'w') as f:
        json.dump(data,f,indent=4)
    
while chat.is_alive():
    
    for c in chat.get().sync_items():
        print("aca estoy")
        chatData = {
            "Tiempo": c.datetime,
            "Tipo": c.type,
            "Nombre": c.author.name,
            "CanalID": c.author.channelId,
            "Mensaje": c.message
        }
        
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
        salvar('catec.json', chatData)

