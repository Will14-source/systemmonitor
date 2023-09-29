
# System Monitor

Este projeto é um monitor de sistema operacional que utiliza python e html para verificar o uso de recursos da máquina, como CPU, memória e disco. Caso o uso de algum desses recursos esteja acima de um limite pré-definido, o programa envia um email para o usuário informando sobre a situação. O email é enviado usando a biblioteca smtplib do python, que permite o envio de mensagens através do gmail. Este arquivo readme contém as instruções para instalar e executar o projeto, bem como as dependências necessárias.


## Instalação

Instalando o projeto no Unix/Linux e Windows.

Instale o Python 3.10 ou superior -
[Download](https://www.python.org/)

Obtenha o repositório do projeto em:

```bash  
$ git clone https://github.com/William-Cruz14/systemmonitor.git
```
Após executar o comando acima é preciso alterar o arquivo **config.json** com o e-mail que será o remetente, senha de apps Google pois foi testado utilizando Gmail, na variável **destinatarios** no arquivo **main_script.py** coloque todos os e-mails de destinatários.

No Unix/Linux:
```bash
python3 -m pip install -r requirements.txt
```
No Windows:
```bash
python -m pip install -r requirements.txt
```

## Unix/Linux

1 - Crie um arquivo **.service** como este:
```bash
[Init]
Description = My Script Python
After = network.target

[Service]
Type = simple
ExecStart = /usr/bin/python3 /home/{user}/systemmonitor
WorkingDirectory = /home/{user}/systemmonitor

[Install]
WantedBy = multi-user.target
Alias = scriptpython.service

```
2 - Em seguida mova o arquivo para:

```bash
mv myscript.service /etc/systemd/system
```
3 - Execute esses comandos:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
sudo systemctl start myscript.service
```
4 - Por fim para ver se funcionou execute:
```bash
sudo systemctl status myscript.service
```

## Windows

No windows altere a extensão do arquivo **main_script.py** para **main_script.pyw**

1 - Feito a alteração acima, pressione a tecla **WIN** + **R** e digite:
```bash
shell:startup
```
2 - Dentro da pasta crie um atalho para o arquivo **main_script.pyw**

3 - Reinicie a máquina para ativar o script.
## Demonstração

Se algum desses recursos ultrapassar um limite pré-definido, o script enviará um email de alerta com um gif correspondente ao recurso afetado. Por exemplo, se a CPU estiver sobrecarregada, o email terá um gif de um processador pegando fogo.

![gif](https://i.ibb.co/3013J4Z/CPU.gif)
## Autores

- [@William-Cruz14](https://github.com/William-Cruz14)


## 🚀 Sobre mim
Eu sou uma pessoa desenvolvedora back-end estou sempre buscando novos conhecimentos e desafios na área de tecnologia. Sou apaixonado pelo que faço e gosto de criar soluções inovadoras e eficientes para os problemas que enfrento.

