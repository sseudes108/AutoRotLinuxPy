<div  align="center">
<h1> 1º Projeto Prático - DevOps </h1>
<img src="https://cdn2.gnarususercontent.com.br/1/901407/4f1c6bc4-e335-4aec-b534-8b49ac3df6f2.jpg" alt="Grupo Boticario Logo"  width="50%"/>
<h3>Automação de Rotinas em Ambiente Linux</h3>
</div>

--- 

* **Identificação de Tarefas:** Liste as tarefas que podem ser automatizadas no ambiente Linux.

    Backup de arquivos e diretórios.<br>
    Atualização de selecionados git repos<br>
    Geração de relatórios.<br>
    Auditoria de segurança.<br>

* **Desenvolvimento de Scripts:** Escreva scripts Python para automatizar cada tarefa, utilizando bibliotecas relevantes.

* **Integração com Cron Jobs:** Agende a execução periódica dos scripts usando tarefas cron para automação contínua.

---
<h4>Informações Relevantes</h4>
    Todos os scripts têm seus diretórios configurados para a máquina virtual utilizada durante o desenvolvimento, e precisam ser ajustados para uso em diferentes ambientes.<br>
    Esses scripts dependem da biblioteca "auto_rot_lib.py" para executar funções principais, como a criação de arquivos de log em caso de erro. Todos os caminhos do sistema são definidos em "auto_rot_lib.py" e são chamados conforme necessário pelos scripts de rotina.<br>
    Foi tomada a precaução de evitar comandos diretos e o uso do shell dentro do código Python.<br>

<h6>Sobre os scripts</h6>
    <b>log.py</b>: Cria um log com as ultimas linhas de "/var/log/syslog". Depende que haja uma pasta chamada logs e dentro da mesma um arquivo log.txt com o texto "0". Esse valor é usado para inicar o registro dos logs e manter um registro de quantos foram criados.</br></br>
    <b>uso_memoria.py</b> Lista os 10 processos que estão utilizando o maior valor de memoria e salva a data, o nome do processo e qual o uso de memoria em MB no momento.
---
