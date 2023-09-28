import psutil
import emails
import time
import json
from pathlib import Path

"""
Esse script é escrito utilizando o módulo 'psutil' e baseada nela é criado
alguns gatilhos para que nossa máquina seja monitorada.

"""
destinatarios = ["cruzwilliam14@gmail.com", "willia55@hotmail.com"]
assunto = "Sistema de Monitoramento"

"""

Essa função gatilho espera receber um caminho o arquivo HTML e depois que é passado o caminho,
ela lê o arquivo e em seguida estrutura o e-mail e por fim o envia para todos os interessados.

"""
def gatilho(path):

    try:
        with open(path, "r", encoding="utf-8") as htm:
            doc_htm = htm.read()

        for destino in destinatarios:
            mensagem = emails.gerar_email(dados_remetente["remetente"], destino, assunto, doc_htm)
            emails.enviar_email(mensagem)


    except IOError as erro:
        print("Impossível abrir o arquivo HTML.")
        print(f"Erro: {erro}")


"""

Aqui estou criando um loop infinito para que o monitoramento seja de forma continua
e adicionando um tempo de 300 segundos ou seja 5 minutos entre a execução de cada loop.

"""
while True:

    try:

        with open("config.json") as dados:
            dados_remetente = json.load(dados)

        """

        Esta parte do código faz a verificação da CPU e caso ela esteja trabalhando no limite ou acima do predefinido,
        ele aciona  o gatilho que dispara um email para todos os interessados.

        """
        if psutil.cpu_percent(5) >= 80.00:
            gatilho(Path.cwd()/ "conteudo/templates/cpu.html")


        """

        Esta parte do código faz a verificação da memória RAM e caso ela esteja trabalhando no limite ou acima predefinido,
        ele aciona  o gatilho que dispara um email para todos os interessados.

        """
        if psutil.virtual_memory().percent >= 80.00:
            gatilho(Path.cwd()/ "conteudo/templates/memory.html")



        """

        Esta parte do código faz a verificação de todos os discos de armazenamento, caso algum deles esteja no limite ou acima do predefinido
        ele aciona o gatilho que dispara um email para todos os interessados.

        """
        for disk in psutil.disk_partitions():
            
            uso_disco = psutil.disk_usage(disk.device)
            if uso_disco.percent >= 80.00:
                gatilho(Path.cwd()/ "conteudo/templates/storage.html")


    except json.JSONDecodeError as erro:
        print(f"Erro relacionado ao arquivo JSON.")
        print(f"Erro: {erro}")

    except IOError as erro:
        print(f"Impossível abrir o arquivo JSON.")
        print(f"Erro: {erro}")

    except psutil.Error as erro:
        print("Erro relacionado ao módulo psutil.")
        print(f"Erro: {erro}")

    time.sleep(300)
