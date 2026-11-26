# Year 1 · Phase 7 — Segurança de IoT, Firmware e Hardware (IoT, Firmware & Hardware Security)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. Foco conceitual e defensivo.

## 🧭 Visão geral

A fase final do primeiro ano aplica tudo o que veio antes ao mundo físico: a **Internet das Coisas (IoT)** e os dispositivos embarcados. Começa com os fundamentos de IoT (história, arquiteturas em camadas, tecnologias de rádio como RFID/NFC/Bluetooth, protocolos como **MQTT** e **CoAP**), passa por programação embarcada em **C** e **Arduino** (com sensores, protoboard e um gateway MQTT) e por **Python** conversando com o hardware por serial. A segunda metade é **segurança ofensiva/defensiva de IoT**: casos reais (Mirai, Stuxnet, Jeep), a **OWASP IoT Top 10**, **análise de firmware**, **exploração binária em ARM**, **hardware hacking** (UART, JTAG, SPI, I2C) e **Wi‑Fi hacking** (padrões 802.11, WPS, captura de handshake). Fecha com um **projeto social** (ONG Passos Mágicos).

A ideia central: **um dispositivo IoT é um computador completo, muitas vezes mal protegido, numa caixa física que o atacante pode abrir**. Defendê‑lo exige olhar software, firmware, rádio e hardware ao mesmo tempo.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura — Hacking the Planet | Roteiro: IoT, C/Arduino, Python no IoT, segurança IoT, firmware, exploração ARM, hardware e Wi‑Fi. |
| 2 | IoT: definições e aplicabilidade | Linha do tempo da IoT, conceitos e tecnologias, e aplicações (indústria/IIoT, cidades inteligentes, transporte, logística, saúde, casa, energia, agronegócio). |
| 3 | Arquiteturas IoT | Arquitetura em camadas dos dispositivos inteligentes; tecnologias de comunicação **RFID** (tags passivas/semi/ativas), **NFC**, **Bluetooth/BLE**, Zigbee, LoRa; e os protocolos de rede mapeados nas camadas (incluindo **MQTT** e **CoAP**). |
| 4 | Linguagem C | Tipos e variáveis, entrada/saída, estruturas de controle; tipos compostos (vetores, matrizes, strings, **struct**), **ponteiros** e funções (retorno e parâmetros de saída). Base para programar o microcontrolador. |
| 5 | Arduino | Arduino × Raspberry Pi, ambiente **Tinkercad**, circuitos, **protoboard** e sensores. Projetos: controle de luz com potenciômetro, semáforo, alarme com sensor ultrassônico e um **gateway MQTT**. |
| 6 | Desenvolvimento e segurança | Indicadores para escolher plataforma; plataformas corporativas (Dojot, HPE, Siemens MindSphere, **AWS IoT**, Samsung ARTIK). Segurança de aplicações distribuídas, uso de **APIs**, **autenticação em IoT** e estratégias de proteção. |
| 7 | Python aplicado ao IoT | Coleta de dados, comunicação **serial** entre Python e Arduino (nos dois sentidos) e **persistência** dos dados coletados em arquivo/banco. |
| 8 | Introdução à segurança IoT | Por que IoT é alvo. Casos reais: **Thermos‑RAT**, marcapassos vulneráveis, a **botnet Mirai** (câmeras/DVRs com senha padrão), o **Jeep** controlado remotamente e o **Stuxnet** (sabotagem de centrífugas via PLC). |
| 9 | Gadgets IoT | Construção de gadgets de "espião" para estudo: **hardware keylogger**, **BadUSB** (emulação de teclado) e MasterKey. Mostra o risco de dispositivos USB não confiáveis. |
| 10 | Análise de firmware | Metodologia de extração e análise de firmware, guiada pela **OWASP IoT Top 10**: senhas fracas/hardcoded, serviços de rede inseguros, interfaces inseguras, falta de update seguro, componentes desatualizados, pouca privacidade, transferência/armazenamento inseguros, falta de gestão do dispositivo, configurações padrão inseguras e falta de hardening físico. |
| 11 | Exploração binária para embarcados | Diferenças do **ARM** em relação ao x86 (registradores, memória, pilha, sintaxe Assembly). Identificação de **stack‑based buffer overflow** e *crash hunting* em binários embarcados. *(Resumido só em conceitos e defesas.)* |
| 12 | Hardware hacking | Reconhecimento de placas e componentes, equipamento de teste (multímetro, analisador lógico), e as **interfaces de depuração/comunicação**: **UART**, **JTAG/SWD**, **SPI** e **I2C** — por onde se lê firmware e se obtém console. |
| 13 | Wi‑Fi hacking | Famílias wireless (WPAN, WMAN, WWAN, **WLAN**), canais e bandas (2,4/5 GHz), padrões **802.11 a/b/g/n/ac**, modo monitor, captura de **handshake** WPA2, riscos do **WPS** e boas práticas de defesa de Wi‑Fi. |
| 14 | Projeto Formação Social | Case real de projeto social (ONG de educação): laboratório de tecnologia para crianças e adolescentes em vulnerabilidade social (ESG/impacto). |

## 🔑 Conceitos-chave

- **Camadas da IoT**: percepção (sensores/atuadores) → rede (rádio e protocolos) → middleware/plataforma → aplicação. Cada camada tem seus riscos e seus controles.
- **Protocolos leves**: **MQTT** (publish/subscribe via broker) e **CoAP** (REST sobre UDP) foram feitos para dispositivos com pouca CPU/energia — e muitas vezes vêm **sem TLS nem autenticação** por padrão.
- **Rádio é superfície de ataque**: RFID, NFC, Bluetooth, Zigbee e Wi‑Fi podem ser espionados ou falsificados. Alcance curto não é segurança.
- **Firmware é o sistema do dispositivo**: extrair e analisar o firmware (binwalk e similares) revela senhas hardcoded, chaves, serviços e binários vulneráveis. É a base da avaliação de segurança de IoT.
- **OWASP IoT Top 10**: a lista de referência dos riscos mais comuns. Os campeões são **senhas padrão/hardcoded**, **serviços de rede inseguros** e **falta de atualização segura**.
- **Mirai e a senha padrão**: a maior botnet de IoT se espalhou só testando usuários/senhas de fábrica em Telnet. A lição: trocar credenciais padrão e fechar serviços de gestão.
- **ARM × x86**: embarcados usam ARM. Os conceitos de pilha e overflow são os mesmos da Fase 5, mas a sintaxe Assembly e os registradores mudam. As mesmas mitigações (NX, canary, atualização) valem.
- **Interfaces de hardware**: **UART** costuma dar um console serial direto; **JTAG/SWD** permitem depurar e ler memória; **SPI/I2C** acessam chips de flash e sensores. Fisicamente acessíveis, são o caminho de quem abre a caixa.
- **BadUSB**: um dispositivo USB pode se passar por teclado e digitar comandos sozinho. Por isso não se conecta USB desconhecido — e por isso existem políticas de bloqueio de dispositivos.
- **Defesa em profundidade para IoT**: segmentar os dispositivos em VLAN própria, exigir TLS e autenticação, assinar e validar atualizações (secure boot), desativar serviços e portas de debug em produção, e manter inventário e patch.
- **Segurança física**: se o atacante tem o dispositivo na mão, pode soldar, ler a flash e extrair segredos. Hardening físico (desabilitar JTAG, criptografar a flash) faz parte do modelo de ameaça.

## 🛠️ Ferramentas e comandos

**Ambiente:** Arduino/Tinkercad, Python (pyserial), Kali Linux, VM **IoTGoat** (firmware vulnerável de propósito, para estudo em rede isolada). Hardware: multímetro, analisador lógico, adaptador USB‑UART.

```c
// Arduino (C) — leitura de sensor e publicação
int valor = analogRead(A0);
Serial.println(valor);        // envia pela serial ao gateway/host
```

```python
# Python conversando com o Arduino por serial
import serial
ard = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
linha = ard.readline().decode().strip()      # recebe do IoT
ard.write(b'1')                                # envia para o IoT

# MQTT (publish/subscribe)
import paho.mqtt.client as mqtt
c = mqtt.Client(); c.connect("broker.local", 1883)
c.publish("casa/sala/temp", "23.5")
```

```bash
# Análise de firmware (defensiva, em imagens próprias/autorizadas)
binwalk firmware.bin                 # identificar seções e sistemas de arquivos
binwalk -e firmware.bin              # extrair
strings squashfs-root/etc/shadow     # procurar senhas hardcoded (estudo)
grep -rniE "password|api[_-]?key|token" squashfs-root/

# Inspeção de binário ARM
file ./bin; readelf -h ./bin; objdump -d -M arm ./bin | less; checksec --file=./bin

# Wi-Fi (só na própria rede / lab autorizado)
iw dev; airmon-ng start wlan0; airodump-ng wlan0mon
# captura de handshake WPA2 para auditoria da própria senha
```

## 🧪 Atividades / CTFs

A pasta `CTF/Fase7` contém a VM **IoTGoat** (imagens `.img`, `.vmdk`, `.vdi`) — um firmware OpenWrt deliberadamente vulnerável, feito para treino sobre a OWASP IoT Top 10. Registro só o **tema**; não executei a VM nem reproduzo soluções.

Labs dos materiais (em ambiente isolado, com hardware/arquivos próprios):

- Montar circuitos no **Tinkercad** e programar o Arduino em C (potenciômetro, semáforo, alarme ultrassônico).
- Construir um **gateway MQTT** e fazer Python e Arduino trocarem dados por serial, persistindo o resultado.
- **Extrair e analisar firmware** com binwalk, procurando senhas e serviços inseguros (OWASP IoT Top 10).
- Reconhecer **UART/JTAG/SPI/I2C** numa placa e explicar o que cada interface expõe.
- Auditar a **própria rede Wi‑Fi**: modo monitor, canais, captura do handshake e teste da robustez da senha.

> 💡 Dica de homelab: pratique na **IoTGoat** e na **Damn Vulnerable IoT Device (DVID)**, use o **FACT** ou o **EMBA** para análise automatizada de firmware, e o simulador do Tinkercad para eletrônica sem comprar peças. Para Wi‑Fi, audite apenas redes suas.

## ❓ Perguntas de revisão

1. **Por que o MQTT e o CoAP são comuns em IoT, e qual o risco de segurança associado?**
   São leves e eficientes para dispositivos com pouca CPU e energia (MQTT é publish/subscribe por broker; CoAP é REST sobre UDP). O risco é que frequentemente são implantados sem TLS nem autenticação, deixando dados e comandos expostos.
2. **O que a botnet Mirai explorou, e qual a lição?**
   Testou credenciais de fábrica (usuário/senha padrão) em serviços como Telnet de câmeras e DVRs. A lição: trocar senhas padrão, desativar serviços de gestão expostos e segmentar os dispositivos.
3. **Cite três itens da OWASP IoT Top 10.**
   Senhas fracas/hardcoded, serviços de rede inseguros e falta de mecanismo de atualização seguro (também: interfaces inseguras, componentes desatualizados, configurações padrão inseguras etc.).
4. **O que é análise de firmware e por que é central na segurança de IoT?**
   É extrair e examinar o software que roda no dispositivo (sistema de arquivos, binários, configs). Revela senhas e chaves hardcoded, serviços ativos e componentes vulneráveis — exatamente o que um atacante procuraria.
5. **Para que servem UART, JTAG, SPI e I2C num hardware?**
   UART costuma dar um console serial; JTAG/SWD permitem depurar e ler memória; SPI e I2C comunicam com chips (flash, sensores). São pontos físicos por onde se lê firmware e se obtém acesso.
6. **Qual a diferença entre explorar um binário ARM e um x86?**
   Os conceitos (pilha, overflow, controle de fluxo) são os mesmos, mas ARM tem outra sintaxe de Assembly, outro conjunto e uso de registradores e convenções próprias. As mitigações (NX, canary, atualização) continuam valendo.
7. **O que é um ataque BadUSB?**
   Um dispositivo USB que se apresenta como teclado (HID) e "digita" comandos automaticamente ao ser conectado. Por isso não se deve conectar USB desconhecido e convém aplicar políticas de controle de dispositivos.
8. **Por que a segurança física importa em IoT?**
   Porque o dispositivo fica acessível ao atacante, que pode abrir a caixa, soldar nas interfaces de debug e ler a flash para extrair segredos. Hardening físico (desabilitar JTAG, cifrar a flash, secure boot) entra no modelo de ameaça.
9. **Quais boas práticas defendem uma implantação de IoT?**
   Segmentar em VLAN própria, trocar credenciais padrão, exigir TLS e autenticação, assinar e validar atualizações, desativar serviços e portas de debug em produção, e manter inventário e patch.
10. **O que o caso Stuxnet mostra sobre segurança de sistemas embarcados/OT?**
    Que malware pode atravessar o mundo digital e causar dano físico (sabotou centrífugas via PLC), mesmo em redes isoladas (air‑gapped), reforçando a importância de segurança em OT/ICS e do controle de mídias removíveis.

## 💼 Conexão com o mercado

- **SOC / Blue team e OT**: dispositivos IoT/OT são cada vez mais parte do inventário a monitorar. Reconhecer tráfego MQTT/CoAP, detectar dispositivos com credenciais padrão e isolar redes de IoT é tarefa real. Casos como Mirai e Stuxnet moldaram as práticas de segmentação e monitoramento de OT/ICS.
- **CompTIA Security+ (SY0‑701)**: IoT, embedded, ICS/SCADA, RTOS, considerações de segurança física, protocolos inseguros e segmentação de rede aparecem em *Security Architecture*; a análise de firmware e os riscos de supply chain tocam *Threats, Vulnerabilities & Mitigations*.
- **Pós Tech em IA para Segurança**: a IoT gera telemetria em massa (sensores, logs de dispositivos) — matéria‑prima para modelos de detecção de anomalia em borda (edge/TinyML) e para IDS específicos de OT. Entender os protocolos e os riscos dessa fase é pré‑requisito para aplicar IA à segurança de dispositivos.

## 📖 Termos da fase

Internet das Coisas (IoT) · IIoT · Dispositivo embarcado · Microcontrolador · Arquitetura em camadas da IoT · RFID · NFC · Bluetooth / BLE · Zigbee · LoRa · MQTT · CoAP · Broker · Linguagem C · Ponteiro · struct · Arduino · Raspberry Pi · Tinkercad · Protoboard · Sensor / atuador · Comunicação serial (UART) · Gateway IoT · AWS IoT · API · Autenticação em IoT · Mirai · Stuxnet · BadUSB · Hardware keylogger · Firmware · Análise de firmware · binwalk · OWASP IoT Top 10 · Senha hardcoded · Secure boot · Exploração binária ARM · Stack-based buffer overflow · JTAG / SWD · SPI · I2C · Analisador lógico · Wi‑Fi (WLAN) · 802.11 a/b/g/n/ac · WPS · Handshake WPA2 · Modo monitor · OT / ICS / SCADA / PLC

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
