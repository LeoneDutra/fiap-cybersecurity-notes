# Year 2 · Phase 5 — Análise de Malware (Malware Analysis)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. **Foco defensivo: analisar malware para detectar, classificar e responder. Toda análise ocorre em VM isolada, sem rede com a internet.**

## 🧭 Visão geral

A fase ensina **análise de malware** do ponto de vista do analista/defensor: como pegar um binário suspeito e descobrir **o que ele faz** sem precisar do código‑fonte. Começa montando o **laboratório isolado** (VM no VirtualBox, snapshots, rede fechada) e revisando fundamentos (sistemas de numeração, ASCII, arquitetura x86/registradores). Define os **tipos de malware** e as técnicas que ele usa para resistir à análise (anti‑RE, **polimorfismo**, **metamorfismo**, **ofuscação**, **packing**). Depois percorre as duas abordagens centrais: **análise estática** (básica — hash, imphash, VirusTotal, strings, PEiD, PEStudio; e avançada — disassembly com IDA) e **análise dinâmica/comportamental** (sandbox, Process Hacker, monitoramento de processos, registro e rede com INetSim/RevMon). Fecha estudando **ofuscação** — para reconhecer e desfazer o que o autor do malware faz para esconder assinaturas (código morto, substituição, XOR).

A ideia central: **o objetivo não é "rodar vírus", é extrair IOCs e entender o comportamento** para alimentar detecção (YARA, EDR), resposta a incidentes e threat intelligence. Isolamento e disciplina de laboratório são inegociáveis.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura — CSI Cyber | Roteiro: montar o lab → conceitos → estática → dinâmica → ofuscação. |
| 2 | Introdução à Malware Analysis | Por que usar **máquina virtual** isolada; instalação do **VirtualBox** (Linux/Windows), criação da VM e **snapshots**. Fundamentos: sistemas **decimal/hexadecimal/binário** e conversões, **tabela ASCII** — a base para ler bytes e dumps. |
| 3 | Conceitos de Malware | **Tipos de malware** (vírus, worm, trojan, ransomware, rootkit, spyware, backdoor etc.). Técnicas anti‑análise: **anti engenharia reversa**, **polimorfismo**, **metamorfismo**, **ofuscação e packing**. Engenharia de software × **engenharia reversa**; arquitetura **Intel x86** e **Von Neumann**; **registradores** (EFLAGS, EIP), **opcodes**. |
| 4 | Análise Estática | **Básica**: função **hash** (identificar a amostra), **imphash** (hash das importações), **VirusTotal**, strings, **PEiD** (detectar packer), **PEStudio**. **Avançada**: disassembly e leitura de funções (ex.: com **IDA**) para entender a lógica sem executar. |
| 5 | Análise Dinâmica | **Comportamental**: executar a amostra na VM isolada e observar. **Sandbox** (automatizada, ex.: Any.run/Cuckoo), **Process Hacker** para processos, e monitoramento de **arquivos/registro/rede** (com **INetSim** simulando a internet). Captura de IOCs: domínios, IPs, mutexes, chaves. |
| 6 | Ofuscação de Malware | A perspectiva do autor do malware para escapar de assinaturas de antivírus: **ofuscação baseada em dados** (dobramento constante, substituição com operadores lógicos), **inclusão de código morto**, **ofuscação de fluxo de controle** e o uso de **XOR** para cifrar strings/payloads. Reconhecer esses padrões é como o analista os desfaz. |

## 🔑 Conceitos-chave

- **Lab isolado é regra**: VM dedicada, sem pasta compartilhada com rede, **snapshot antes de detonar** e rollback depois. Nunca analisar malware na máquina real nem com acesso à internet.
- **Estática × dinâmica**: a estática examina o arquivo **sem executar** (segura, mas o packing esconde a lógica); a dinâmica **executa e observa** (revela o comportamento real, mas exige isolamento e pode ter evasão de sandbox). As duas se complementam.
- **Estática básica × avançada**: a básica extrai indicadores rápidos (hash, strings, imports, entropia); a avançada desmonta o código (disassembly/decompilação) para entender a lógica.
- **Hash e imphash**: o hash (MD5/SHA‑256) identifica a amostra exata; o **imphash** agrupa amostras que compartilham a mesma tabela de importação — útil para relacionar variantes de uma família.
- **Imports (IAT) como pista**: as APIs que o binário importa (ex.: `CreateRemoteThread`, `InternetOpen`, `CryptEncrypt`) já indicam intenção (injeção, C2, ransomware).
- **Packing e entropia**: malware frequentemente é comprimido/cifrado (UPX e outros). Entropia alta e poucas strings legíveis sugerem packing; é preciso **unpack** antes da estática avançada.
- **Polimorfismo × metamorfismo**: o polimórfico muda sua aparência (cifra o corpo com chave variável) mas mantém a lógica; o metamórfico reescreve o próprio código. Ambos quebram assinaturas simples — por isso a detecção migra para comportamento.
- **Ofuscação**: transformar o código para dificultar a leitura sem mudar o que ele faz (código morto, operadores equivalentes, controle de fluxo embaralhado). O **XOR** é onipresente para esconder strings e payloads — e é reversível.
- **Comportamento é o que importa**: processos criados, injeção, persistência (Run keys, serviços), arquivos escritos, mutex, tráfego de rede e **C2** são os sinais que geram IOCs e regras de detecção.
- **INetSim/rede simulada**: finge ser a internet para o malware "ligar para casa" e revelar domínios/URLs de C2, sem deixar o tráfego sair de verdade.
- **Produto final = detecção**: de uma análise saem IOCs, uma **regra YARA**, um mapeamento no **MITRE ATT&CK** e um relatório — exatamente o que alimenta o SOC e o threat intel.

## 🛠️ Ferramentas e abordagem

**Lab:** VirtualBox + VM Windows (vítima) + VM Linux de análise (REMnux), rede **host‑only** com **INetSim**. **Estática:** PEStudio, PEiD, DIE, strings, capa, YARA, VirusTotal, IDA/Ghidra. **Dinâmica:** Process Hacker, Procmon, Regshot, Wireshark, sandbox (Any.run/Cuckoo).

```text
Fluxo de análise (sempre em VM isolada, com snapshot):
1. Triagem         → hash/imphash, VirusTotal, tipo de arquivo, entropia (packer?)
2. Estática básica → strings, imports (IAT), recursos, capa, YARA
3. Unpack          → se empacotado (UPX -d, dump de memória)
4. Dinâmica        → detonar, Procmon (arquivos/registro), Process Hacker,
                     Regshot (antes/depois), Wireshark + INetSim (C2)
5. Estática avançada → disassembly (IDA/Ghidra) das funções-chave
6. Produto         → IOCs, regra YARA, mapeamento ATT&CK, relatório
```

```bash
# Triagem (em VM, amostra desarmada / sem executar)
sha256sum amostra.bin ; file amostra.bin
strings -n 6 amostra.bin | less
# imphash, entropia e imports: pefile/DIE/PEStudio
capa amostra.bin            # capacidades mapeadas em ATT&CK
yara regras.yar amostra.bin # casar assinaturas

# Unpack comum
upx -d amostra.bin -o amostra_unpacked.bin

# XOR (desofuscar strings) — conceito, feito em ferramenta/decoder do lab
# byte ^ chave repetida = texto original
```

## 🧪 Atividades / CTFs

Não há pasta de CTF; a prática usa **amostras de treino** em VM isolada (nunca malware real sem controle):

- Montar o **lab** (VirtualBox, snapshots, rede host‑only com INetSim) e validar o isolamento.
- Fazer **triagem estática** de uma amostra: hash/imphash, strings, imports, e consultar reputação.
- Identificar **packing** por entropia/PEiD e **desempacotar**.
- **Detonar** numa amostra de treino e capturar o comportamento (Procmon, Process Hacker, Regshot, Wireshark/INetSim), extraindo IOCs.
- **Desofuscar** strings cifradas por XOR e seguir o fluxo de execução no IDA/Ghidra.
- Escrever uma **regra YARA** e mapear as técnicas no **ATT&CK**.

> 💡 Dica de homelab: use o **FLARE VM** + **REMnux** como par de VMs, amostras de treino do **MalwareBazaar** (abuse.ch) e do **PMA labs** (livro *Practical Malware Analysis*), e a sandbox pública **Any.run**/**Hybrid Analysis** para comparar. Sempre snapshot antes e rollback depois.

## ❓ Perguntas de revisão

1. **Por que a análise de malware deve ser feita em VM isolada com snapshot?**
   Para conter a execução (sem contaminar a máquina real nem a rede) e poder reverter ao estado limpo após detonar a amostra. Rede isolada evita que o malware cause dano ou vaze dados de verdade.
2. **Qual a diferença entre análise estática e dinâmica, e por que usar as duas?**
   A estática examina o arquivo sem executar (segura, mas o packing esconde a lógica); a dinâmica executa e observa o comportamento real (precisa de isolamento e pode sofrer evasão). Combinadas, dão o quadro completo.
3. **O que o hash e o imphash dizem sobre uma amostra?**
   O hash identifica o arquivo exato (qualquer mudança gera outro hash). O imphash é o hash da tabela de importações e agrupa amostras com o mesmo conjunto de APIs — útil para relacionar variantes de uma família.
4. **Por que os imports (IAT) são uma pista importante na estática?**
   As APIs importadas revelam intenção: funções de rede sugerem C2, de criptografia sugerem ransomware, de injeção (`CreateRemoteThread`) sugerem evasão. É um indício forte antes mesmo de executar.
5. **O que é packing e como detectá‑lo?**
   É comprimir/cifrar o executável para esconder código e strings. Detecta‑se por entropia alta, poucas strings legíveis e assinaturas de packer (PEiD/DIE). É preciso desempacotar antes da estática avançada.
6. **Qual a diferença entre polimorfismo e metamorfismo?**
   O polimórfico cifra o corpo com chave variável, mudando a aparência mas mantendo a lógica após decifrar; o metamórfico reescreve o próprio código a cada geração. Ambos derrotam assinaturas estáticas simples.
7. **Por que o XOR é tão usado em malware e como o analista lida com ele?**
   Porque é simples, rápido e reversível: cifra strings e payloads para fugir de assinaturas. O analista o reverte aplicando a mesma chave (byte ⊕ chave = original), muitas vezes com um decoder ou script.
8. **O que a análise comportamental procura, e quais ferramentas ajudam?**
   Processos criados, injeção, persistência (Run keys, serviços), arquivos/registro alterados, mutexes e tráfego de rede/C2. Ferramentas: Procmon, Process Hacker, Regshot, Wireshark e INetSim.
9. **Para que serve o INetSim na análise dinâmica?**
   Para simular serviços de internet (DNS, HTTP etc.) em rede isolada, fazendo o malware revelar seus domínios/URLs de C2 sem permitir que o tráfego saia de fato.
10. **Qual é o produto final de uma análise de malware?**
    IOCs (hashes, domínios, IPs, mutexes), uma regra de detecção (YARA), o mapeamento das técnicas no MITRE ATT&CK e um relatório — insumos diretos para o SOC, a resposta a incidentes e o threat intelligence.

## 💼 Conexão com o mercado

- **SOC / DFIR e Threat Intel (analista de malware / reverse engineer)**: é uma especialização valorizada. Extrair IOCs, escrever regras YARA, mapear no ATT&CK e produzir relatórios alimentam detecção e resposta. A análise liga‑se à forense (Fase 2) e à threat intelligence (Fase 1).
- **CompTIA CySA+ / GIAC (GREM)**: tipos de malware, análise estática e dinâmica, sandbox, IOCs e evasão aparecem em *Security Operations*. Esta fase é a base direta do caminho de **reverse engineering** (GREM, PMA).
- **Pós Tech em IA para Segurança**: a detecção de malware é um dos usos mais maduros de ML — classificação por features de PE (imports, entropia, n‑grams de opcode), detecção de variantes e triagem automática de amostras em escala. A ofuscação é exatamente o desafio adversarial que esses modelos enfrentam.

## 📖 Termos da fase

Análise de malware · Laboratório isolado (VM/VirtualBox) · Snapshot · Rede host‑only · Tipos de malware (vírus, worm, trojan, ransomware, rootkit, spyware, backdoor) · Anti engenharia reversa · Polimorfismo · Metamorfismo · Ofuscação · Packing (UPX) · Entropia · Engenharia reversa · Arquitetura x86 / Von Neumann · Registradores (EFLAGS, EIP) · Opcode · Análise estática (básica/avançada) · Hash · Imphash · VirusTotal · Strings · Imports (IAT) · PEiD · PEStudio · DIE · capa · YARA · Disassembly · IDA / Ghidra · Análise dinâmica / comportamental · Sandbox · Process Hacker · Procmon · Regshot · Wireshark · INetSim · REMnux / FLARE VM · IOC · Mutex · Persistência · C2 · XOR · MITRE ATT&CK · Relatório de análise

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
