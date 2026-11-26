# Year 1 · Phase 4 — Automação (Shell Script e Python), Risco e Vulnerabilidades (Scripting, Risk & Vulnerability Management)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A quarta fase tem duas metades. A primeira é **programação para segurança**: Shell Script e Bash para automatizar o Linux e depois **Python** do zero (variáveis, decisões, laços, listas, funções e módulos). Em seguida vêm arquivos, **criptografia** (DES/AES, Base64, simulação didática de ransomware) e **sockets** (cliente/servidor TCP e UDP, chat e port scanner). A segunda metade é **gestão**: **gestão de riscos** (COBIT, ISO 27000, ISO 31000), **gestão de vulnerabilidades** (ciclo de vida, métricas NVD/CVSS), **avaliação de vulnerabilidades** com OpenVAS e Nessus no Kali e **monitoramento** de infraestrutura com Zabbix.

A ideia central: **automatizar é o que separa quem opera de quem escala**. Um script em Bash ou Python transforma uma tarefa manual de horas (varrer portas, checar hashes, tratar logs) em segundos. E a gestão de risco e vulnerabilidades dá o critério para decidir **o que corrigir primeiro**.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Roteiro: Shell Script, Python aplicado à segurança, gestão de risco e vulnerabilidades e monitoramento. |
| 2 | Introdução ao Shell Script | Principais shells, permissão de execução, shebang, variáveis e caracteres especiais, aritmética `$(( ))`, parâmetros (`$1`, `$#`, `$@`, `$?`). Estruturas `if`, `for`, `while`, `case`, tratamento de conteúdo (`grep`, `cut`, `tr`, `sed`), expressões regulares e funções com código de retorno e parâmetros. |
| 3 | Mergulhando no Bash | Expansões do Bash (chaves, til, parâmetros, comandos, aritmética, curingas), redirecionamentos e exercícios práticos. |
| 4 | Introdução ao Python | Por que o Python domina em segurança (simples, legível, muitas bibliotecas). Linguagem interpretada, multiparadigma e de alto nível × baixo nível. Instalação e configuração do ambiente. |
| 5 | Variáveis, decisão e laços | Tipos e variáveis, `input`/`print`, `if`/`elif`/`else` (simples, composto, encadeado), operadores lógicos `and`/`or`/`not`, laços `while`/`for`, com exercícios práticos. |
| 6 | Listas, funções e módulos | Listas (criar, acrescentar, remover, buscar e métodos úteis), funções com parâmetros e retorno (sem `input` dentro da função) e criação e importação de **módulos** próprios. |
| 7 | Arquivos e criptografia | Criar, escrever e ler arquivos. Rotina de inventário. Manipulação de strings (slice, `find`, `split`). Conceitos de criptografia simétrica (**DES** × **AES**, com a biblioteca PyCryptodome), **Base64** e uma **simulação didática de ransomware** (cifrar e decifrar arquivos em laboratório). |
| 8 | Python e redes ("Função segura") | Áreas de uso do Python. Biblioteca **socket**: servidor e cliente TCP, chat, comunicação UDP e um **port scanner** simples para identificar portas abertas. |
| 9 | Gestão de riscos | Normas e frameworks: **COBIT**, família **ISO/IEC 27000** e **ISO 31000**. Processo de gestão de risco: contexto → identificação → análise → avaliação → tratamento → aceitação, com comunicação e monitoramento contínuos. Caso prático de uma empresa multiunidade infectada por worm. |
| 10 | Gestão de vulnerabilidades | Quem está vulnerável e por quê (erros de programação, configuração, falta de patch), métricas e severidade do **NVD/CVSS**, tendências de ataque, elementos do programa (escopo, verificação), **ciclo de vida** contínuo e diferença entre avaliação de vulnerabilidades e **pentest**. |
| 11 | Avaliação de vulnerabilidades | Etapas: escopo → avaliar o status → priorizar → corrigir → manter‑se informado → repetir. Frequência de varredura, opções de ferramenta, e instalação e uso do **OpenVAS (GVM)** e do **Nessus Essentials** no **Kali Linux** contra um alvo de laboratório. |
| 12 | Monitoramento com Zabbix (o arquivo tem título de frameworks) | Arquitetura do **Zabbix** (server, banco, frontend web, agentes). Instalação sobre Apache + MySQL + PHP no Debian, agente no Windows (serviço e firewall), cadastro de hosts, alerta de teste e acompanhamento do estado dos servidores. |

## 🔑 Conceitos-chave

- **Script = automação reprodutível**: shebang (`#!/bin/bash`), permissão `+x`, parâmetros e códigos de saída (`$?`, onde 0 significa sucesso) permitem encadear tarefas e tratar erros.
- **Expressões regulares (regex)**: a linguagem de padrões que alimenta `grep`, `sed` e o módulo `re` do Python. É essencial para extrair IPs, e‑mails e hashes de logs.
- **Python para segurança**: interpretado, legível e com bibliotecas para tudo (socket, hashlib, requests, scapy, PyCryptodome). É a linguagem padrão de PoCs, automação de SOC e ML.
- **Funções e módulos**: código reutilizável e testável. Separar entrada/saída da lógica facilita reaproveitar o código.
- **Criptografia simétrica**: a mesma chave cifra e decifra. O **DES** (56 bits) é obsoleto; o **AES** (128/192/256 bits) é o padrão atual. **Base64 é codificação, não criptografia.**
- **Ransomware na prática**: o atacante cifra arquivos com uma chave simétrica e cobra pela chave. Simular isso em laboratório ajuda a entender por que **backups offline** e a **detecção precoce** são decisivos.
- **Sockets**: abstração de comunicação de rede (IP + porta + protocolo). O TCP é orientado a conexão (handshake); o UDP não tem conexão. Um port scan TCP connect tenta abrir conexões e registra quais portas respondem.
- **Risco = probabilidade × impacto** (sobre um ativo, explorando uma vulnerabilidade, por uma ameaça). As opções de **tratamento** são mitigar, transferir, evitar ou aceitar.
- **Gestão × avaliação de vulnerabilidades × pentest**: a gestão é o programa contínuo; a avaliação é a varredura que lista falhas; o pentest explora as falhas para provar o impacto.
- **Priorização**: não dá para corrigir tudo de uma vez. A ordem vem do CVSS combinado com a exposição (internet × interna), a criticidade do ativo e a existência de exploit público.
- **Monitoramento de disponibilidade**: o Zabbix coleta métricas (CPU, disco, serviços) e dispara alertas. É o "D" da tríade CID na prática.

## 🛠️ Ferramentas e comandos

**Ambiente:** Linux (Bash), Python 3 + IDE, Kali Linux, OpenVAS/GVM, Nessus Essentials, Zabbix (server no Debian, agente no Windows).

```bash
# Shell Script
#!/bin/bash
echo "Script: $0 | args: $# | todos: $@"
for host in $(cat hosts.txt); do ping -c1 -W1 "$host" &>/dev/null && echo "$host UP"; done
case "$1" in start) echo inicia;; stop) echo para;; *) echo "uso: $0 start|stop";; esac
total=$(( $(wc -l < log.txt) * 2 )); grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log | sort -u
chmod +x script.sh && ./script.sh start; echo $?
```

```python
# Python
with open("inventario.txt", "a") as f: f.write("srv01;10.0.0.5\n")
linhas = open("inventario.txt").read().splitlines(); host, ip = linhas[0].split(";")

import hashlib; hashlib.sha256(b"senha").hexdigest()
import base64; base64.b64encode(b"texto"); base64.b64decode("dGV4dG8=")

from Crypto.Cipher import AES                    # PyCryptodome
cipher = AES.new(chave_16_bytes, AES.MODE_EAX); ct, tag = cipher.encrypt_and_digest(dados)

import socket                                    # port scan TCP connect (só em lab autorizado)
for porta in [21, 22, 80, 443]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.5)
    print(porta, "aberta" if s.connect_ex(("192.168.56.10", porta)) == 0 else "fechada"); s.close()
```

```bash
# Avaliação de vulnerabilidades / monitoramento
sudo gvm-setup && sudo gvm-start          # OpenVAS (GVM) no Kali → https://127.0.0.1:9392
sudo systemctl start nessusd              # Nessus Essentials → https://localhost:8834
sudo systemctl enable --now zabbix-server zabbix-agent apache2
```

## 🧪 Atividades / CTFs

A pasta `CTF` desta fase guarda os scripts e arquivos que usei nos desafios. Resumo só **os temas**, sem soluções:

- **Hashes e wordlists**: gerar hashes e compará‑los a uma lista de palavras (o conceito de ataque de dicionário contra hashes sem salt).
- **Ransomware didático**: decifrar um arquivo cifrado em laboratório (uma imagem) sabendo o algoritmo e a chave, o que reforça os conceitos de criptografia simétrica.
- **Processamento de arquivos**: contar linhas, tratar listas de nomes e ler arquivos no formato `passwd`.
- **Análise de dados em CSV grande**: filtrar e agregar um dataset público de casos por condado (US counties) com Python.
- **Depuração**: corrigir scripts com erro.

Labs dos materiais: scripts Bash com parâmetros, laços e funções; exercícios de Python; inventário em arquivo; cifrar e decifrar com DES/AES; chat por socket e port scanner; varredura com OpenVAS e Nessus contra uma VM alvo; e monitoramento com Zabbix e alerta de teste.

> 💡 Dica de homelab: transforme o port scanner num script com `argparse`, `concurrent.futures` e saída em JSON. Depois compare o resultado com `nmap -sT`. Exporte o relatório do OpenVAS e monte uma planilha de priorização (CVSS + exposição + criticidade do ativo).

## ❓ Perguntas de revisão

1. **O que significam `$#`, `$@` e `$?` num script Bash?**
   `$#` é o número de argumentos, `$@` é a lista de todos os argumentos e `$?` é o código de saída do último comando (0 = sucesso).
2. **Por que Base64 não é criptografia?**
   Porque não usa chave: é só uma representação reversível de bytes em texto. Qualquer pessoa decodifica. Serve para transporte (e‑mail, JSON), não para sigilo.
3. **DES ou AES? Por quê?**
   AES. O DES usa uma chave efetiva de 56 bits e é quebrável por força bruta; o AES usa chaves de 128, 192 ou 256 bits e é o padrão atual (FIPS 197).
4. **Qual a diferença entre TCP e UDP do ponto de vista de um socket?**
   O TCP (`SOCK_STREAM`) é orientado a conexão: tem handshake, garante entrega e ordem. O UDP (`SOCK_DGRAM`) não tem conexão nem garantia de entrega, e por isso é mais leve (usado em DNS, streaming e VoIP).
5. **Como um port scanner TCP connect decide que uma porta está aberta?**
   Ele tenta completar o three‑way handshake com `connect`/`connect_ex`. Se a conexão é aceita (retorno 0), a porta está aberta. Recusa (RST) ou timeout indicam porta fechada ou filtrada.
6. **Quais são as etapas do processo de gestão de riscos da ISO 31000/27005?**
   Contexto → identificação → análise → avaliação → tratamento → aceitação, com comunicação/consulta e monitoramento/análise crítica acontecendo durante todo o processo.
7. **Quais são as quatro formas de tratar um risco?**
   Mitigar ou reduzir (aplicar controles), transferir ou compartilhar (seguro, terceirização), evitar (deixar de fazer a atividade) e aceitar (assumir formalmente o risco residual).
8. **Qual a diferença entre avaliação de vulnerabilidades e teste de penetração?**
   A avaliação identifica e lista vulnerabilidades, geralmente de forma automatizada e ampla. O pentest explora ativamente as falhas, de forma manual e direcionada, para provar o impacto real.
9. **Além da nota CVSS, o que considerar para priorizar uma correção?**
   A exposição do ativo (internet × rede interna), a criticidade do ativo para o negócio, a existência de exploit público ou de exploração ativa (ex.: catálogo KEV) e a existência de controles compensatórios.
10. **Para que serve o Zabbix numa operação de segurança?**
    Para monitorar a disponibilidade e o desempenho de servidores, redes e serviços, com alertas. Ele detecta quedas, discos cheios ou serviços parados antes que virem incidente e gera histórico para análise.

## 💼 Conexão com o mercado

- **SOC (analista N1/N2)**: scripts em Bash e Python automatizam enriquecimento de IOCs, consultas a APIs (VirusTotal, AbuseIPDB), parsing de logs e respostas de SOAR. A gestão de vulnerabilidades (relatórios de Nessus/OpenVAS/Qualys) e o monitoramento (Zabbix, Grafana) são rotinas de quem trabalha em operações de segurança.
- **CompTIA Security+ (SY0‑701)**: gestão de riscos (identificação, análise, tratamento, apetite e tolerância), frameworks (ISO 27001/27002/31000, COBIT), varredura de vulnerabilidades × pentest, CVSS/CVE, priorização, criptografia simétrica (AES × DES), hashing e conceitos de ransomware caem em *Security Program Management*, *Security Operations* e *General Security Concepts*.
- **Pós Tech em IA para Segurança**: Python é a linguagem de ML (pandas, scikit‑learn, PyTorch). O exercício de tratar um CSV de milhões de linhas é a mesma habilidade de preparar datasets de logs. A gestão de risco dá a base para avaliar riscos de modelos de IA (ex.: NIST AI RMF).

## 📖 Termos da fase

Shell Script · Shebang · Variáveis e parâmetros posicionais · Código de saída (exit code) · Estruturas de controle (if/for/while/case) · Expressões regulares (regex) · Função · Python · Linguagem interpretada · Lista · Módulo · Manipulação de arquivos · Slice / split · Criptografia simétrica · DES · AES · Base64 · Ransomware · Hash · Ataque de dicionário · Socket · TCP × UDP · Port scanner · Risco · Ameaça · Vulnerabilidade · Ativo · Tratamento de risco · Risco residual · COBIT · ISO/IEC 27001 · ISO 31000 · Gestão de vulnerabilidades · NVD · Avaliação de vulnerabilidades · Pentest · OpenVAS/GVM · Nessus · Kali Linux · Zabbix · Monitoramento

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
