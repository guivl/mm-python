import random


INPUT = "data/output-00000-of-00001"

def isHealthy(sensorId):
    """
    Função para validar se a quantidade de passos está dentro de uma faixa saudável
    :param sensorId: String
    :return: Bool
    """
    steps = sns[sensorId]
    if steps > 4961:
        return True
    else:
        return False

if __name__ == '__main__':
    # Abrindo o arquivo que possue exemplos de ID de sensores #
    with open(INPUT, 'rb') as ifp:
        # Pulando a primeira linha pois é o cabeçalho
        header = ifp.readline()

        # Instanciando duas listas que vão receber os dados dos sensores e uma simulação de quantidade de passos #
        sensors = list()
        steps = list()

        # Para cada linha do nosso dataset vamos decodificar em utf-8, limpar a linha, atribuir o sensor_id para a
        # lista sensors, criar um número randomico de quantidade de passos e atribuir para a lista steps #
        for line in ifp:
            event_data = line.decode('utf8').replace('\n', '').replace('(', '').replace(')', '').replace(' ', '')\
                .replace("'", "")
            sensor_id = event_data.split(',')[0]
            # O if ignora valores nulos #
            if sensor_id == '':
                pass
            else:
                sensors.append(sensor_id)
            steps.append(random.sample(range(200,8000), 1)[0])

    # Agora vamos concatenar as duas listas em um dicionário de dados, assim temos #
    sns = dict(zip(sensors, steps))
    for sId in sns.keys():
        if isHealthy(sId):
            print('Parabéns você completou sua meta de passos!')