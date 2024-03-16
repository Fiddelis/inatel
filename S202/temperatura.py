from pymongo import MongoClient
from datetime import datetime
from threading import Thread
from time import sleep
import random

"""
{
    _id,                    (Gerado automaticamente)
    nomeSensor,             (Ex.: Sensor 1, Temp 2)
    unidadeMedida,          (Padrão: C°)
    sensorAlarmado,         (Temperatura > 38 ? true : false)
    valorSensor[
        {
        valorSensor         (30 < Temperatura < 40)
        hora                (Horario atual da maquina)
        }
    ]
}
"""

formato_horario = "%Y-%m-%d %H:%M:%S"

client = MongoClient("mongodb://localhost:27017")

db = client["bancoiot"]
sensores = db.sensores


def inserir_temperatura_db(sensor):
    resultado = sensores.insert_one({
        'nomeSensor': sensor,
        'valorSensor':[],
        'unidadeMedida':'C°',
        'sensorAlarmado':False
    })

    if resultado.acknowledged:
        print("Documento Adicionado!")


def atualizar_temperatura_db(sensor, temperatura):
    horario_atual = datetime.now().strftime(formato_horario)
    if(temperatura > 38):
        return True
    else:
        sensor_alarmado = False
        resultado = sensores.update_one({'nomeSensor': sensor}, {'$push':{'valorSensor':{'temperatura':temperatura,
                                                                                         'valorSensor':horario_atual}}})

    if resultado.acknowledged:
        print(f"Sucesso: {sensor}: {temperatura} C°, Alarmado:{sensor_alarmado}")
    else:
        ("Erro ao inserir")

    return sensor_alarmado


def gerar_leitura_aleatoria(sensor, intervalo):
    while True:
        temperatura = random.randrange(30, 40)
        
        if(temperatura > 38):
            print(f"Atenção! Temperatura muito alta! Verificar {sensor}")
            break
        else:
            atualizar_temperatura_db(sensor, temperatura)
            sleep(intervalo)


inserir_temperatura_db("Sensor 1")
inserir_temperatura_db("Sensor 2")
inserir_temperatura_db("Sensor 3")
Thread(target=gerar_leitura_aleatoria, args=("Sensor 1", 5)).start()
Thread(target=gerar_leitura_aleatoria, args=("Sensor 2", 5)).start()
Thread(target=gerar_leitura_aleatoria, args=("Sensor 3", 5)).start()


