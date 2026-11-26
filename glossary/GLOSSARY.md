# 📖 Glossary (PT ↔ EN)

> Generated from `glossary.csv` by `scripts/build_glossary.py`. Edit the CSV, not this file.

**447 terms**

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x) · [Z](#z) · [Á](#á)

## A

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Active Directory (AD)** | Active Directory | Sistemas | Serviço de diretório da Microsoft que centraliza identidades, computadores, grupos e políticas de uma rede. | Y1P3 |
| **ADB (ADB)** | Android Debug Bridge | IoT e Hardware | Ferramenta de linha de comando para comunicar com dispositivos/emuladores Android. | Y2P4 |
| **AGDLP (AGDLP)** | Accounts, Global, Domain Local, Permissions | GRC | Boa prática de aninhamento de grupos: conta → grupo global → grupo de domínio local → permissão (AGUDLP com universal). | Y1P3 |
| **Aleatorização do espaço de endereços (ASLR)** | Address Space Layout Randomization | Sistemas | Mitigação que aleatoriza os endereços de carga de módulos, pilha e heap a cada execução. | Y1P5 |
| **Ameaça** | Threat | GRC | Agente ou evento com potencial de causar dano a um ativo. | Y1P4 |
| **Analisador lógico** | Logic analyzer | IoT e Hardware | Equipamento que captura e decodifica sinais digitais de barramentos como UART, SPI e I2C. | Y1P7 |
| **Android Runtime (ART)** | Android Runtime | IoT e Hardware | Ambiente de execução dos apps Android, que roda o bytecode (DEX). | Y2P4 |
| **AndroidManifest** | AndroidManifest.xml | IoT e Hardware | Arquivo que declara componentes, permissões e configurações de um app Android. | Y2P4 |
| **Anonimato** | Anonymity | Threat Intel | Ocultar quem é o autor de uma ação (diferente de privacidade, que oculta o conteúdo). | Y2P1 |
| **Análise de firmware** | Firmware analysis | Forense | Extrair e examinar o firmware em busca de segredos, serviços e vulnerabilidades. | Y1P7 |
| **Análise de fluxo (NetFlow)** | Flow analysis | Redes | Analisar metadados de conexões (IPs, portas, bytes) em vez de cada pacote, para escala. | Y1P6 |
| **Análise estática e dinâmica** | Static and dynamic analysis | Forense | Examinar o código sem executar (estática) e observar o app em execução (dinâmica). | Y2P4 |
| **Análise in-vivo** | Live analysis (in-vivo) | Forense | Coleta de evidências com o sistema ligado, capturando dados voláteis. | Y2P2 |
| **Análise post-mortem** | Post-mortem analysis | Forense | Análise de uma imagem de disco com o sistema desligado, após o incidente. | Y2P2 |
| **APKTool** | APKTool | Forense | Ferramenta que desmonta e remonta recursos e código smali de um APK. | Y2P4 |
| **Arduino** | Arduino | IoT e Hardware | Plataforma aberta de prototipagem eletrônica com microcontrolador e IDE em C. | Y1P7 |
| **Arquitetura ARM (ARM)** | ARM architecture | Sistemas | Arquitetura RISC de baixo consumo, dominante em celulares e dispositivos embarcados. | Y1P5 |
| **Arquitetura do Android** | Android platform architecture | IoT e Hardware | Camadas do Android: kernel Linux, HAL, ART, bibliotecas nativas, framework Java e system apps. | Y2P4 |
| **Arquitetura x86 (x86)** | x86 architecture | Sistemas | Família de arquiteturas de processador CISC da Intel/AMD, dominante em PCs e servidores. | Y1P5 |
| **AS-REP roasting** | AS-REP roasting | Ameaças e Ataques | Abuso de contas sem pré-autenticação Kerberos para obter dados e quebrar a senha offline. | Y2P3 |
| **Assembly (ASM)** | Assembly language | Desenvolvimento | Linguagem de baixo nível que mapeia quase diretamente as instruções da CPU. | Y1P5 |
| **Assinatura de APK** | APK signing | IoT e Hardware | Processo que assina o aplicativo (esquemas v1/v2/v3) para garantir integridade e origem. | Y2P4 |
| **Assinatura digital** | Digital signature | Criptografia | Hash de uma mensagem cifrado com a chave privada do autor; garante autenticidade e não repúdio. | Y1P6 |
| **Assinatura SMB/LDAP** | SMB/LDAP signing | Sistemas | Controle que assina mensagens para impedir adulteração e ataques de relay. | Y2P3 |
| **Ataque de dicionário** | Dictionary attack | Ameaças e Ataques | Tentar senhas de uma lista de palavras (wordlist) contra um login ou contra hashes. | Y1P4 |
| **Ataque Fraggle** | Fraggle attack | Ameaças e Ataques | Variante do Smurf que usa pacotes UDP em vez de ICMP para amplificação por broadcast. | Y1P6 |
| **Ataque Smurf** | Smurf attack | Ameaças e Ataques | DoS de amplificação que envia ICMP a um endereço de broadcast forjando o IP da vítima. | Y1P6 |
| **Ativo** | Asset | GRC | Qualquer coisa de valor para a organização que precisa de proteção. | Y1P4 |
| **auditd** | Linux Audit daemon | Forense | Serviço que registra eventos de segurança no nível do kernel conforme regras definidas. | Y1P2 |
| **Autenticação Kerberos** | Kerberos authentication | Criptografia | Protocolo de autenticação do AD baseado em tickets (TGT e TGS) emitidos pelo KDC. | Y2P3 |
| **Autenticação simultânea de iguais (SAE)** | Simultaneous Authentication of Equals | Criptografia | Troca de chaves do WPA3-Personal que substitui o PSK e resiste a ataques de dicionário offline. | Y1P1 |
| **Autenticação, autorização e auditoria (AAA)** | Authentication, Authorization and Accounting | GRC | Framework que controla quem acessa (autenticação), o que pode fazer (autorização) e registra o que fez (accounting). | Y1P1 |
| **Autoconfiguração sem estado (SLAAC)** | Stateless Address Autoconfiguration | Redes | Mecanismo IPv6 em que o host gera o próprio endereço a partir do prefixo anunciado pelo roteador. | Y1P1 |
| **Autopsy** | Autopsy / The Sleuth Kit | Forense | Plataforma forense para analisar imagens de disco: timeline, carving e sistema de arquivos. | Y2P2 |
| **Avaliação de vulnerabilidades** | Vulnerability assessment | GRC | Varredura (geralmente automatizada) que identifica e lista vulnerabilidades em um escopo. | Y1P4 |
| **awk** | awk | Sistemas | Linguagem de processamento de texto orientada a colunas/campos. | Y1P2 |

## B

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **BadUSB** | BadUSB | Ameaças e Ataques | Dispositivo USB que se passa por teclado (HID) e injeta comandos automaticamente. | Y1P7 |
| **Base nacional de vulnerabilidades (NVD)** | National Vulnerability Database | GRC | Base do NIST que enriquece os CVEs com CVSS, CPE e referências. | Y1P4 |
| **Base64** | Base64 | Criptografia | Codificação (não criptografia) que representa dados binários em texto ASCII. | Y1P2 |
| **Biblioteca de vínculo dinâmico (DLL)** | Dynamic-Link Library | Sistemas | Biblioteca compartilhada do Windows carregada por vários programas em tempo de execução. | Y1P5 |
| **Bind shell** | Bind shell | Ameaças e Ataques | Shell em que a máquina alvo abre uma porta e espera o atacante se conectar. | Y2P3 |
| **binwalk** | binwalk | Forense | Ferramenta que identifica e extrai sistemas de arquivos e dados embutidos num firmware. | Y1P7 |
| **Binário** | Binary / executable | Sistemas | Arquivo com código de máquina e dados prontos para o SO carregar e executar. | Y1P5 |
| **Bit menos significativo (LSB)** | Least Significant Bit | Criptografia | Método de esteganografia que altera o bit menos significativo de cada byte para embutir dados. | Y1P6 |
| **Blind SQL Injection** | Blind SQL Injection | Ameaças e Ataques | SQLi em que o resultado não aparece; infere-se pela resposta (booleano) ou tempo. | Y2P4 |
| **BloodHound** | BloodHound | Ameaças e Ataques | Ferramenta que mapeia caminhos de ataque no AD em um grafo (quem chega a Domain Admin). | Y2P3 |
| **Bloqueio de herança** | Block inheritance | Sistemas | Configuração na OU que impede herdar GPOs de níveis superiores. | Y1P3 |
| **Bluetooth Low Energy (BLE)** | Bluetooth Low Energy | IoT e Hardware | Variante de Bluetooth de baixo consumo usada em wearables e sensores IoT. | Y1P7 |
| **Broker MQTT** | MQTT broker | IoT e Hardware | Servidor central que recebe publicações e as distribui aos assinantes dos tópicos. | Y1P7 |
| **Buffer overflow (BOF)** | Buffer overflow | Ameaças e Ataques | Escrever mais dados do que o buffer comporta, sobrescrevendo memória adjacente. | Y1P5 |
| **Burp Suite** | Burp Suite | Ameaças e Ataques | Plataforma de teste de segurança web com proxy, repeater, intruder e scanner. | Y2P4 |

## C

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Cadeia de custódia** | Chain of custody | Forense | Registro documentado de quem coletou, manuseou e guardou cada evidência, quando e como. | Y2P2 |
| **Censys** | Censys | Threat Intel | Motor de busca de hosts, certificados e serviços expostos, similar ao Shodan. | Y2P1 |
| **Certificate Transparency (CT)** | Certificate Transparency | Redes | Logs públicos de certificados TLS emitidos, úteis para descobrir subdomínios. | Y2P1 |
| **Chamada de sistema (syscall)** | System call | Sistemas | Interface pela qual um programa pede um serviço ao kernel. | Y1P5 |
| **Ciclo de instrução** | Instruction cycle (fetch-decode-execute) | Sistemas | Sequência que a CPU repete: buscar a instrução, decodificá-la e executá-la. | Y1P5 |
| **Ciclo de resposta a incidentes (PICERL)** | Incident response lifecycle | Resposta a Incidentes | Fases da resposta: Preparação, Identificação, Contenção, Erradicação, Recuperação e Lições Aprendidas. | Y2P2 |
| **Ciclo de vida do OSINT** | OSINT lifecycle | Threat Intel | Etapas: requisitos (PIR), coleta, processamento, análise, produção, disseminação e feedback. | Y2P1 |
| **Cifra de César** | Caesar cipher | Criptografia | Cifra de substituição que desloca cada letra um número fixo de posições. | Y1P6 |
| **Cifra de Vigenère** | Vigenère cipher | Criptografia | Cifra de substituição polialfabética que usa uma palavra-chave para variar o deslocamento. | Y1P6 |
| **CIS Benchmark (CIS)** | CIS Benchmark | GRC | Guias de configuração segura publicados pelo Center for Internet Security. | Y1P2 |
| **CoAP (CoAP)** | Constrained Application Protocol | IoT e Hardware | Protocolo REST leve sobre UDP para dispositivos com poucos recursos. | Y1P7 |
| **COBIT (COBIT)** | Control Objectives for Information and Related Technologies | GRC | Framework da ISACA para governança e gestão de TI. | Y1P4 |
| **Componente Android** | Android component | Desenvolvimento | Blocos de um app: Activity, Service, Content Provider e Broadcast Receiver. | Y2P4 |
| **Componente exportado** | Exported component | Ameaças e Ataques | Componente acessível por outros apps; se exposto sem proteção, vira vetor de ataque. | Y2P4 |
| **Comunicação serial (UART)** | Serial communication (UART) | IoT e Hardware | Troca de dados bit a bit por uma interface serial; UART dá console a muitos dispositivos. | Y1P7 |
| **Condição de corrida (TOCTOU)** | Race condition | Ameaças e Ataques | Falha causada pela ordem/temporização de acessos concorrentes a um recurso compartilhado. | Y1P5 |
| **Console de gerenciamento de política de grupo (GPMC)** | Group Policy Management Console | Sistemas | Ferramenta para criar, vincular e analisar GPOs. | Y1P3 |
| **Contenção** | Containment | Resposta a Incidentes | Ação de impedir a propagação do incidente, isolando sistemas afetados. | Y2P2 |
| **Contrainteligência** | Counterintelligence | Threat Intel | Medidas para detectar e frustrar a coleta de inteligência do adversário sobre você. | Y2P1 |
| **Controlador de domínio (DC)** | Domain Controller | Sistemas | Servidor que guarda uma cópia do banco do AD, autentica usuários e replica alterações com outros DCs. | Y1P3 |
| **Controlador lógico programável (PLC)** | Programmable Logic Controller | IoT e Hardware | Computador industrial robusto que controla máquinas e processos em tempo real. | Y1P7 |
| **Convenção de chamada** | Calling convention | Desenvolvimento | Regras de como argumentos são passados e quem limpa a pilha (cdecl, stdcall, fastcall). | Y1P5 |
| **Cookie SameSite** | SameSite cookie attribute | Desenvolvimento | Atributo que limita o envio de cookies em requisições de outros sites, mitigando CSRF. | Y2P4 |
| **Correlação de eventos** | Event correlation | Resposta a Incidentes | Relacionar logs de fontes diferentes no tempo para reconstruir um ataque. | Y2P2 |
| **Corrupção de memória** | Memory corruption | Ameaças e Ataques | Classe de bugs em que o programa lê/escreve fora dos limites previstos. | Y1P5 |
| **Credential dumping** | Credential dumping | Ameaças e Ataques | Extrair hashes, senhas ou tickets da memória (LSASS) ou do disco. | Y2P3 |
| **Credential Guard** | Windows Credential Guard | Sistemas | Recurso do Windows que isola credenciais em ambiente virtualizado, dificultando o dumping. | Y2P3 |
| **Criptografia assimétrica** | Asymmetric cryptography | Criptografia | Esquema com par de chaves: a pública cifra/verifica e a privada decifra/assina. | Y1P6 |
| **Criptografia simétrica** | Symmetric encryption | Criptografia | Esquema em que a mesma chave cifra e decifra os dados. | Y1P4 |
| **cron** | cron | Sistemas | Serviço de agendamento de tarefas recorrentes, configurado no crontab. | Y1P2 |
| **Cross-Site Request Forgery (CSRF)** | Cross-Site Request Forgery | Ameaças e Ataques | Fazer o navegador autenticado da vítima executar uma ação indesejada. | Y2P4 |
| **Cross-Site Scripting (XSS)** | Cross-Site Scripting | Ameaças e Ataques | Injetar script que executa no navegador de outra vítima. | Y2P4 |
| **CTI estratégica** | Strategic threat intelligence | Threat Intel | Inteligência de alto nível sobre tendências e risco, voltada a executivos e decisões de longo prazo. | Y2P1 |
| **CTI operacional** | Operational threat intelligence | Threat Intel | Inteligência sobre campanhas e intenções de um ator específico, para resposta e caça. | Y2P1 |
| **CTI tática** | Tactical threat intelligence | Threat Intel | Inteligência sobre TTPs e comportamento dos adversários, voltada aos times de defesa. | Y2P1 |
| **CTI técnica** | Technical threat intelligence | Threat Intel | Indicadores técnicos específicos (IoCs) para alimentar ferramentas de detecção. | Y2P1 |
| **Cyber Kill Chain** | Cyber Kill Chain | Threat Intel | Modelo da Lockheed Martin com 7 fases de um ataque, do reconhecimento às ações no objetivo. | Y2P1 |
| **Código de saída** | Exit code / return code | Desenvolvimento | Número que um comando devolve ao terminar; 0 indica sucesso e outro valor indica erro. | Y1P4 |

## D

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Dado, informação e inteligência** | Data, information, intelligence | Threat Intel | Hierarquia: dado é o fato bruto, informação é o dado com contexto, inteligência é a análise que apoia decisão. | Y2P1 |
| **Daemon** | Daemon | Sistemas | Processo que roda em segundo plano prestando um serviço. | Y1P2 |
| **Dark web** | Dark web | Ameaças e Ataques | Parte da deep web acessível só por redes de anonimato como o Tor, usada para o bem e para o mal. | Y1P6 |
| **Debugger** | Debugger | Desenvolvimento | Ferramenta que executa um programa passo a passo, inspecionando registradores e memória. | Y1P5 |
| **Deception** | Deception | Threat Intel | Uso de iscas e informações falsas (honeypots, honeytokens) para enganar e detectar o atacante. | Y2P1 |
| **Defesa em profundidade** | Defense in depth | GRC | Empilhar várias camadas de controle para que a falha de uma não comprometa o todo. | Y1P6 |
| **Delegação de controle** | Delegation of control | GRC | Concessão de tarefas administrativas específicas sobre uma OU sem dar privilégio total. | Y1P3 |
| **DHCP Snooping** | DHCP Snooping | Redes | Recurso do switch que só aceita respostas DHCP de portas confiáveis e monta uma tabela de vínculos IP-MAC-porta. | Y1P1 |
| **Diamond Model** | Diamond Model | Threat Intel | Modelo que correlaciona adversário, capacidade, infraestrutura e vítima numa intrusão. | Y2P1 |
| **Diffie-Hellman (DH)** | Diffie-Hellman key exchange | Criptografia | Protocolo que permite a duas partes combinarem uma chave secreta por um canal público. | Y1P6 |
| **Directory traversal** | Directory traversal | Ameaças e Ataques | Usar sequências como ../ para acessar arquivos fora do diretório previsto. | Y2P4 |
| **Dispositivo embarcado** | Embedded device | IoT e Hardware | Computador de propósito específico, com recursos limitados, dentro de um produto. | Y1P7 |
| **Distribuição Linux** | Linux distribution (distro) | Sistemas | Pacote completo formado pelo kernel Linux, ferramentas GNU, gerenciador de pacotes e configurações. | Y1P2 |
| **Domínio** | Domain | Sistemas | Unidade administrativa e de replicação do AD, identificada por um nome DNS. | Y1P3 |
| **DORA (DORA)** | Discover, Offer, Request, Acknowledge | Redes | As quatro mensagens da concessão DHCP. | Y1P3 |
| **Double free** | Double free | Ameaças e Ataques | Liberar duas vezes a mesma região de memória, corrompendo as estruturas do alocador. | Y1P5 |
| **Due diligence** | Due diligence | GRC | Investigação cuidadosa para verificar a legitimidade de uma pessoa, empresa ou informação. | Y2P1 |

## E

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **EFLAGS** | EFLAGS register | Sistemas | Registrador de status cujos bits (flags) refletem o resultado das operações (zero, carry, sinal etc.). | Y1P5 |
| **Encaminhador DNS** | DNS forwarder | Redes | DNS para onde o servidor envia as consultas que não consegue resolver localmente. | Y1P3 |
| **Encapsulamento** | Encapsulation | Redes | Cada camada acrescenta seu cabeçalho aos dados da camada de cima antes de enviar; o destino faz o processo inverso. | Y1P1 |
| **Endereço de retorno** | Return address | Sistemas | Endereço empilhado por uma chamada de função para onde a execução volta ao terminar. | Y1P5 |
| **Endereço IPv4 (IPv4)** | IPv4 address | Redes | Endereço lógico de 32 bits escrito em 4 octetos decimais. | Y1P1 |
| **Endereço IPv6 (IPv6)** | IPv6 address | Redes | Endereço de 128 bits em hexadecimal, em 8 grupos separados por dois-pontos. | Y1P1 |
| **Endereço MAC (MAC)** | MAC address | Redes | Endereço físico de 48 bits da interface de rede, usado na camada 2. | Y1P1 |
| **Endereço virtual (VA)** | Virtual Address | Sistemas | Endereço usado pelo processo, traduzido para físico pela MMU; RVA é relativo à base do módulo. | Y1P5 |
| **Endereços privados** | Private addressing (RFC 1918) | Redes | Faixas IPv4 reservadas para uso interno, não roteáveis na Internet: 10/8, 172.16/12, 192.168/16. | Y1P1 |
| **Endurecimento** | Hardening | GRC | Conjunto de configurações que reduzem a superfície de ataque de um sistema. | Y1P2 |
| **Engenharia reversa** | Reverse engineering | Ameaças e Ataques | Analisar um binário sem o código-fonte para entender seu funcionamento. | Y1P5 |
| **Engenharia social** | Social engineering | Ameaças e Ataques | Manipulação psicológica de pessoas para obter informações ou acesso. | Y2P1 |
| **Enumeração de AD** | Active Directory enumeration | Ameaças e Ataques | Mapeamento de usuários, grupos, computadores, GPOs e relações de confiança do domínio. | Y2P3 |
| **Envenenamento de ARP** | ARP spoofing / ARP poisoning | Ameaças e Ataques | Envio de respostas ARP falsas para associar o MAC do atacante ao IP de outro host (ex.: gateway), permitindo MitM. | Y1P1 |
| **Envenenamento de cache ARP** | ARP cache poisoning | Ameaças e Ataques | Enviar respostas ARP falsas para redirecionar o tráfego ao atacante (MitM ou DoS). | Y1P6 |
| **Envenenamento de LLMNR/NBT-NS** | LLMNR/NBT-NS poisoning | Ameaças e Ataques | Abuso de protocolos legados de resolução de nomes na LAN para capturar hashes de autenticação. | Y2P3 |
| **Erradicação** | Eradication | Resposta a Incidentes | Remoção da causa do incidente (malware, conta comprometida, vulnerabilidade). | Y2P2 |
| **Escalada de privilégio (PrivEsc)** | Privilege escalation | Ameaças e Ataques | Quando um atacante sai de um acesso limitado para um nível mais alto (ex.: root). | Y1P2 |
| **Escalonamento** | Scheduling | Sistemas | Decisão do SO sobre qual processo ou thread usa a CPU e por quanto tempo. | Y1P3 |
| **Esteganografia** | Steganography | Criptografia | Técnica de ocultar a existência de uma mensagem dentro de outro arquivo (imagem, áudio). | Y1P6 |
| **Esteganálise** | Steganalysis | Forense | Conjunto de técnicas para detectar a presença de dados ocultos por esteganografia. | Y1P6 |
| **Estrutura** | Struct | Desenvolvimento | Tipo composto de C que agrupa variáveis de tipos diferentes. | Y1P7 |
| **Evidência volátil** | Volatile evidence | Forense | Dado que se perde ao desligar o sistema (memória, processos, conexões, cache). | Y2P2 |
| **Executable and Linkable Format (ELF)** | Executable and Linkable Format | Sistemas | Formato de binário do Linux/Unix, com cabeçalho, program headers e section headers. | Y1P5 |
| **Expressão regular (regex)** | Regular expression | Desenvolvimento | Linguagem de padrões para buscar e extrair texto. | Y1P4 |

## F

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **F3EAD (F3EAD)** | Find, Fix, Finish, Exploit, Analyze, Disseminate | Threat Intel | Ciclo que integra operações e inteligência, da identificação do alvo à disseminação do aprendizado. | Y2P1 |
| **Failover DHCP** | DHCP failover | Redes | Dois servidores DHCP compartilham escopos para manter a entrega de IPs se um falhar. | Y1P3 |
| **Feed de ameaças** | Threat feed | Threat Intel | Fluxo contínuo de IoCs e informações de ameaças consumido por ferramentas de segurança. | Y2P1 |
| **FFUF (FFUF)** | Fuzz Faster U Fool | Ameaças e Ataques | Fuzzer web rápido para descobrir caminhos e parâmetros. | Y2P4 |
| **Filtro WMI (WMI)** | WMI filter | Sistemas | Consulta WMI que limita a aplicação de uma GPO a máquinas que atendam a um critério. | Y1P3 |
| **Fingerprint de tecnologia** | Technology fingerprinting | Ameaças e Ataques | Identificar as tecnologias e versões de um site ou serviço. | Y2P3 |
| **Fingerprinting** | Device/browser fingerprinting | Ameaças e Ataques | Identificar um usuário por características do dispositivo e navegador, mesmo sem cookies. | Y2P1 |
| **Firewall com estado** | Stateful firewall | Redes | Firewall que acompanha o estado das conexões e libera automaticamente o tráfego de retorno. | Y1P1 |
| **Firewall de aplicação web (WAF)** | Web Application Firewall | Desenvolvimento | Filtra requisições HTTP/HTTPS para proteger aplicações web (SQLi, XSS etc.). | Y1P1 |
| **Firewall de próxima geração (NGFW)** | Next-Generation Firewall | Redes | Firewall que soma inspeção de aplicação (camada 7), IPS integrado e controle por usuário/aplicação. | Y1P1 |
| **firewalld** | firewalld | Redes | Firewall dinâmico baseado em zonas, gerenciado pelo firewall-cmd, com regras runtime e permanentes. | Y1P2 |
| **Firmware** | Firmware | IoT e Hardware | Software de baixo nível gravado no dispositivo que controla o hardware. | Y1P7 |
| **Floresta** | Forest | Sistemas | Conjunto de uma ou mais árvores que compartilham schema e relações de confiança; é a fronteira de segurança do AD. | Y1P3 |
| **Fluxos padrão** | Standard streams (stdin/stdout/stderr) | Sistemas | Canais de entrada (fd 0), saída (fd 1) e erro (fd 2) de um processo. | Y1P2 |
| **Forense de e-mail** | Email forensics | Forense | Análise de cabeçalhos, metadados e conteúdo de e-mails para rastrear origem e autenticidade. | Y2P2 |
| **Forense de navegador** | Browser forensics | Forense | Análise de histórico, cache, cookies e downloads do navegador. | Y2P2 |
| **Forense de rede** | Network forensics | Forense | Captura e análise de tráfego de rede para investigar incidentes. | Y2P2 |
| **Fork bomb** | Fork bomb | Ameaças e Ataques | Ataque de negação de serviço que cria processos sem parar até esgotar os recursos do sistema. | Y1P5 |
| **Força bruta** | Brute force | Ameaças e Ataques | Tentativas repetidas de adivinhar senhas até acertar. | Y1P2 |
| **fstab** | File systems table | Sistemas | Arquivo /etc/fstab que lista o que é montado automaticamente no boot e com quais opções. | Y1P2 |
| **FTK Imager** | FTK Imager | Forense | Ferramenta para criar imagens forenses e visualizar evidências, calculando hashes. | Y2P2 |
| **Função** | Function | Desenvolvimento | Bloco de código nomeado e reutilizável que recebe parâmetros e pode retornar um valor. | Y1P4 |
| **Função de derivação de chave (KDF)** | Key Derivation Function | Criptografia | Função lenta e com salt para transformar senhas em chaves, resistente a força bruta. | Y1P6 |
| **Funções inseguras de C** | Unsafe C functions | Desenvolvimento | Funções que não checam limites e causam overflow: gets, strcpy, sprintf, scanf. | Y1P5 |
| **Fuzzing** | Fuzzing | Ameaças e Ataques | Enviar entradas malformadas ou aleatórias em massa para encontrar falhas e crashes. | Y1P5 |

## G

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Gateway IoT** | IoT gateway | IoT e Hardware | Dispositivo que agrega sensores e faz a ponte entre a rede local de IoT e a internet/nuvem. | Y1P7 |
| **Gerenciador de pacotes** | Package manager | Sistemas | Ferramenta que instala, atualiza e remove software resolvendo dependências. | Y1P2 |
| **Gerenciador de volumes lógicos (LVM)** | Logical Volume Manager | Sistemas | Camada que agrupa discos (PV) em pools (VG) e cria volumes lógicos (LV) redimensionáveis. | Y1P2 |
| **Gerenciamento de eventos e informações de segurança (SIEM)** | Security Information and Event Management | Resposta a Incidentes | Plataforma que centraliza, correlaciona e alerta sobre logs de várias fontes. | Y2P2 |
| **Gestão de patches** | Patch management | GRC | Processo de testar, aprovar e aplicar atualizações de segurança. | Y1P3 |
| **Gestão de vulnerabilidades** | Vulnerability management | GRC | Programa contínuo para identificar, classificar, priorizar, corrigir e verificar vulnerabilidades. | Y1P4 |
| **Globbing** | Globbing / pattern matching | Sistemas | Uso de curingas (*, ?, [ ]) pelo shell para casar nomes de arquivos. | Y1P2 |
| **gMSA (gMSA)** | Group Managed Service Account | Sistemas | Conta de serviço com senha longa gerida e rotacionada automaticamente pelo AD. | Y2P3 |
| **GNU Privacy Guard (GPG)** | GNU Privacy Guard | Criptografia | Implementação livre do OpenPGP para cifrar, decifrar e assinar com chaves assimétricas. | Y1P6 |
| **GNU/Linux** | GNU/Linux | Sistemas | Nome que reconhece que o sistema combina o kernel Linux com as ferramentas do projeto GNU. | Y1P2 |
| **gobuster** | gobuster | Ameaças e Ataques | Ferramenta de brute force de diretórios, arquivos e subdomínios. | Y2P4 |
| **Golden Ticket** | Golden Ticket | Ameaças e Ataques | Ticket Kerberos (TGT) forjado com o hash da conta krbtgt, dando acesso quase irrestrito. | Y2P3 |
| **Google dorks** | Google dorks | Threat Intel | Operadores de busca avançada para encontrar informações e exposições específicas. | Y2P1 |
| **GPO forçada** | Enforced GPO | Sistemas | Link de GPO que prevalece sobre conflitos e ignora o bloqueio de herança. | Y1P3 |
| **grep** | Global regular expression print | Sistemas | Busca linhas que casam com um padrão (texto ou regex). | Y1P2 |
| **Grupo de segurança** | Security group | Sistemas | Grupo do AD usado para conceder permissões; escopos: global, domínio local e universal. | Y1P3 |
| **Guymager** | Guymager | Forense | Ferramenta Linux de aquisição de imagens forenses (dd/E01) com verificação de hash. | Y2P2 |
| **Gêmeo maligno** | Evil twin | Ameaças e Ataques | Ponto de acesso falso com o mesmo SSID de uma rede legítima para atrair vítimas. | Y1P1 |

## H

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Hacktivismo** | Hacktivism | Ameaças e Ataques | Ataques motivados por causas políticas ou sociais, normalmente defacement ou DoS. | Y1P1 |
| **Handshake WPA2** | WPA2 handshake | Redes | Troca de mensagens no início da conexão Wi-Fi, capturável para auditar a força da senha. | Y1P7 |
| **Hash** | Hash function | Criptografia | Função unidirecional que mapeia qualquer entrada em um resumo de tamanho fixo. | Y1P6 |
| **Hash criptográfico** | Cryptographic hash | Criptografia | Função que gera um resumo de tamanho fixo e irreversível; qualquer mudança no dado muda o hash. | Y1P4 |
| **hashcat** | hashcat | Ameaças e Ataques | Ferramenta de quebra de hashes acelerada por GPU, com muitos modos de algoritmo. | Y1P6 |
| **Heap** | Heap | Sistemas | Região de memória para alocação dinâmica em tempo de execução. | Y1P5 |
| **Hexadecimal (hex)** | Hexadecimal | Sistemas | Base numérica 16; cada dígito representa 4 bits, usado para endereços e opcodes. | Y1P5 |
| **Hierarquia padrão de sistema de arquivos (FHS)** | Filesystem Hierarchy Standard | Sistemas | Padrão que define a função de cada diretório no Linux. | Y1P2 |
| **Homem no meio (MitM)** | Man-in-the-Middle | Ameaças e Ataques | Atacante se posiciona entre duas partes para interceptar ou alterar a comunicação. | Y1P1 |
| **Honeypot** | Honeypot | Threat Intel | Sistema isca, sem valor real, criado para atrair atacantes e estudar suas técnicas. | Y2P1 |

## I

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **I2C (I2C)** | Inter-Integrated Circuit | IoT e Hardware | Barramento serial de dois fios para conectar sensores e periféricos ao microcontrolador. | Y1P7 |
| **ICMP redirect** | ICMP redirect attack | Ameaças e Ataques | Uso de mensagens ICMP redirect forjadas para alterar a rota de um host e desviar o tráfego. | Y1P6 |
| **Imagem forense** | Forensic image | Forense | Cópia bit a bit de uma mídia, com hash de integridade, usada para análise. | Y2P2 |
| **Incidente de segurança** | Security incident | Resposta a Incidentes | Evento que compromete (ou ameaça) a confidencialidade, integridade ou disponibilidade de ativos. | Y2P2 |
| **Inclusão de arquivo local/remoto (LFI/RFI)** | Local/Remote File Inclusion | Ameaças e Ataques | Incluir e executar arquivos locais (LFI) ou remotos (RFI) por entrada não validada. | Y2P4 |
| **Indicador de ataque (IoA)** | Indicator of Attack | Threat Intel | Sinal de comportamento ou intenção de ataque em andamento, antes do dano concluído. | Y2P1 |
| **Indicador de comprometimento (IoC)** | Indicator of Compromise | Threat Intel | Evidência técnica de que um sistema já foi comprometido (hash, IP, domínio, chave de registro). | Y2P1 |
| **Infraestrutura de chaves públicas (PKI)** | Public Key Infrastructure | Criptografia | Conjunto de autoridades, certificados e políticas que gerencia chaves públicas e identidades. | Y1P6 |
| **Injeção** | Injection | Ameaças e Ataques | Envio de entrada maliciosa que a aplicação interpreta como comando ou consulta. | Y1P2 |
| **Injeção de comando** | Command injection | Ameaças e Ataques | Executar comandos do SO por meio de entrada não tratada passada a um shell. | Y2P4 |
| **Injeção de SQL (SQLi)** | SQL Injection | Ameaças e Ataques | Injetar SQL por entrada não tratada para ler ou alterar o banco. | Y2P4 |
| **Inspeção dinâmica de ARP (DAI)** | Dynamic ARP Inspection | Redes | Valida mensagens ARP contra a tabela do DHCP Snooping e descarta as falsificadas. | Y1P1 |
| **Inspeção profunda de pacotes (DPI)** | Deep Packet Inspection | Redes | Análise do payload dos pacotes (camada 7), não só dos cabeçalhos, para identificar aplicações e assinaturas. | Y1P6 |
| **Inteligência de ameaças cibernéticas (CTI)** | Cyber Threat Intelligence | Threat Intel | Coleta, análise e produção de conhecimento sobre adversários e ameaças para apoiar decisões de segurança. | Y2P1 |
| **Inteligência de fontes abertas (OSINT)** | Open Source Intelligence | Threat Intel | Coleta e análise de informações disponíveis publicamente para produzir inteligência. | Y2P1 |
| **Inteligência geoespacial (GEOINT)** | Geospatial Intelligence | Threat Intel | Geolocalização e análise de alvos a partir de imagens, metadados e referências visuais. | Y2P1 |
| **Intent** | Intent | Desenvolvimento | Objeto de mensagem que aciona componentes ou comunica entre apps no Android. | Y2P4 |
| **Interface binária de aplicação (ABI)** | Application Binary Interface | Sistemas | Contrato de baixo nível (tamanhos, chamadas, registradores) que permite binários interoperarem. | Y1P5 |
| **Internet das Coisas (IoT)** | Internet of Things | IoT e Hardware | Rede de objetos físicos com sensores e conectividade que coletam e trocam dados. | Y1P7 |
| **IoT Industrial (IIoT)** | Industrial IoT | IoT e Hardware | Uso de IoT em indústria e infraestrutura crítica, ligado a OT/ICS. | Y1P7 |
| **IPsec (IPsec)** | Internet Protocol Security | Criptografia | Conjunto de protocolos (IKE, ESP, AH) que cifra e autentica pacotes IP; modos transporte e túnel. | Y1P1 |
| **ISO 31000** | ISO 31000 | GRC | Norma com princípios e diretrizes genéricas para gestão de riscos. | Y1P4 |
| **ISO/IEC 27001** | ISO/IEC 27001 | GRC | Norma internacional que define os requisitos de um Sistema de Gestão de Segurança da Informação (SGSI); a 27002 traz os controles. | Y1P4 |

## J

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **JADX** | JADX | Forense | Decompilador que converte um APK/DEX de volta para código Java legível. | Y2P4 |
| **John the Ripper (John)** | John the Ripper | Ameaças e Ataques | Ferramenta de quebra de senhas por dicionário, força bruta e regras. | Y1P6 |
| **journalctl** | journalctl | Forense | Ferramenta para consultar o journal do systemd (logs binários estruturados). | Y1P2 |
| **JTAG (JTAG)** | Joint Test Action Group | IoT e Hardware | Interface de depuração de hardware que permite controlar a CPU e ler memória. | Y1P7 |

## K

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Kali Linux** | Kali Linux | Ameaças e Ataques | Distribuição Debian voltada a testes de segurança, com centenas de ferramentas pré-instaladas. | Y1P4 |
| **Kerberoasting** | Kerberoasting | Ameaças e Ataques | Pedir tickets de serviço (SPN) e quebrar offline a senha da conta de serviço. | Y2P3 |
| **Kerberos** | Kerberos | Criptografia | Protocolo de autenticação baseado em tickets usado pelo AD. | Y1P3 |
| **Kernel** | Kernel | Sistemas | Núcleo do sistema operacional: gerencia CPU, memória, dispositivos e processos, fazendo a ponte entre hardware e software. | Y1P2 |
| **krbtgt (krbtgt)** | krbtgt account | Sistemas | Conta do AD cuja chave assina todos os tickets Kerberos; seu comprometimento permite o Golden Ticket. | Y2P3 |

## L

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **LAMP (LAMP)** | Linux, Apache, MySQL, PHP | Desenvolvimento | Stack clássica de servidor web: Linux + Apache + MySQL/MariaDB + PHP. | Y1P2 |
| **LAPS (LAPS)** | Local Administrator Password Solution | Sistemas | Solução que define senha única e rotacionada para o administrador local de cada máquina. | Y2P3 |
| **LDAP (LDAP)** | Lightweight Directory Access Protocol | Redes | Protocolo de consulta e manipulação de diretórios como o Active Directory. | Y2P3 |
| **Linguagem C (C)** | C language | Desenvolvimento | Linguagem compilada de baixo nível, base de sistemas operacionais e firmware. | Y1P7 |
| **Linguagem interpretada** | Interpreted language | Desenvolvimento | Linguagem executada por um interpretador linha a linha, sem compilar para binário antes. | Y1P4 |
| **Link analysis** | Link analysis | Threat Intel | Técnica de visualizar e analisar relações entre entidades para revelar padrões. | Y2P1 |
| **Lista** | List | Desenvolvimento | Estrutura de dados ordenada e mutável do Python. | Y1P4 |
| **Lista de controle de acesso (ACL)** | Access Control List | Redes | Lista ordenada de regras permit/deny aplicada a uma interface para filtrar tráfego; termina com um deny implícito. | Y1P1 |
| **Lista de controle de acesso discricionária (DACL)** | Discretionary Access Control List | Sistemas | Define quais princípios têm quais permissões sobre um objeto do AD. | Y2P3 |
| **Little-endian** | Little-endian | Sistemas | Ordem de bytes em que o byte menos significativo é armazenado primeiro; padrão no x86. | Y1P5 |
| **Lições aprendidas** | Lessons learned | Resposta a Incidentes | Revisão pós-incidente para melhorar processos e evitar recorrência. | Y2P2 |
| **Log de evento do Windows (EVTX)** | Windows Event Log | Forense | Registros de eventos do sistema (.evtx): logons, serviços, erros e segurança. | Y2P2 |
| **LSASS (LSASS)** | Local Security Authority Subsystem Service | Sistemas | Processo do Windows que guarda credenciais em memória; alvo de credential dumping. | Y2P3 |
| **LSDOU (LSDOU)** | Local, Site, Domain, OU | Sistemas | Ordem de processamento das GPOs; a mais próxima do objeto vence em conflito. | Y1P3 |

## M

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Maltego** | Maltego | Threat Intel | Ferramenta de análise de links e OSINT que monta grafos de relações entre entidades. | Y2P1 |
| **Malware sem arquivo** | Fileless malware | Ameaças e Ataques | Código malicioso que vive na memória sem gravar arquivo no disco, dificultando a detecção. | Y2P2 |
| **MD5 (MD5)** | Message Digest 5 | Criptografia | Função de hash de 128 bits, hoje insegura por sofrer colisões. | Y1P6 |
| **Memória virtual** | Virtual memory | Sistemas | Abstração que dá a cada processo um espaço de endereçamento próprio, mapeado em páginas na memória física ou em disco. | Y1P3 |
| **Metasploit** | Metasploit Framework | Ameaças e Ataques | Framework de exploração com módulos, payloads e pós-exploração. | Y2P3 |
| **Metasploitable2** | Metasploitable2 | Ameaças e Ataques | Máquina virtual Linux propositalmente vulnerável, usada para treino de pentest em laboratório. | Y1P6 |
| **Metodologia OSCAR (OSCAR)** | OSCAR methodology | Forense | Método de forense de rede: Obtain, Strategize, Collect, Analyze, Report. | Y2P2 |
| **Microcontrolador (MCU)** | Microcontroller | IoT e Hardware | Chip que integra CPU, memória e periféricos para controlar um dispositivo. | Y1P7 |
| **Mimikatz** | Mimikatz | Ameaças e Ataques | Ferramenta que extrai credenciais e manipula tickets Kerberos no Windows. | Y2P3 |
| **Mirai** | Mirai botnet | Ameaças e Ataques | Botnet de IoT que infectou dispositivos usando credenciais de fábrica e lançou grandes DDoS. | Y1P7 |
| **MISP (MISP)** | Malware Information Sharing Platform | Threat Intel | Plataforma aberta para armazenar, correlacionar e compartilhar IoCs e informações de ameaças entre organizações. | Y2P1 |
| **MITRE ATT&CK (ATT&CK)** | MITRE ATT&CK | Threat Intel | Base de conhecimento de táticas e técnicas reais de adversários, usada como linguagem comum de detecção. | Y2P1 |
| **Modelo OSI (OSI)** | OSI reference model | Redes | Modelo de referência da ISO com 7 camadas (física, enlace, rede, transporte, sessão, apresentação, aplicação). | Y1P1 |
| **Modo monitor** | Monitor mode | Redes | Modo da placa Wi-Fi que captura todo o tráfego do ar, não só o endereçado a ela. | Y1P7 |
| **Monitoramento** | Monitoring | Resposta a Incidentes | Coleta contínua de métricas e eventos para detectar falhas ou anomalias. | Y1P4 |
| **Movimento lateral** | Lateral movement | Ameaças e Ataques | Reusar credenciais para pular de uma máquina a outra dentro da rede. | Y2P3 |
| **MQTT (MQTT)** | Message Queuing Telemetry Transport | IoT e Hardware | Protocolo leve de mensagens publish/subscribe via broker, popular em IoT. | Y1P7 |
| **Máscara curinga** | Wildcard mask | Redes | Máscara usada em ACLs e no OSPF em que 0 = bit deve coincidir e 1 = bit ignorado (o inverso da máscara de sub-rede). | Y1P1 |
| **Máscara de tamanho variável (VLSM)** | Variable Length Subnet Mask | Redes | Divisão de um bloco em sub-redes de tamanhos diferentes conforme a necessidade de cada uma. | Y1P1 |
| **Módulo** | Module | Desenvolvimento | Arquivo .py com funções e variáveis que pode ser importado por outros programas. | Y1P4 |
| **Módulos de autenticação plugáveis (PAM)** | Pluggable Authentication Modules | Sistemas | Framework modular de autenticação do Linux (complexidade de senha, bloqueio após falhas etc.). | Y1P2 |

## N

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Negação de serviço (DoS / DDoS)** | Denial of Service | Ameaças e Ataques | Ataque que esgota recursos de um serviço ou rede para torná-lo indisponível; DDoS usa muitas origens ao mesmo tempo. | Y1P1 |
| **Nessus** | Nessus | GRC | Scanner de vulnerabilidades comercial da Tenable; a versão Essentials é gratuita e limitada. | Y1P4 |
| **NetExec** | NetExec (nxc) | Ameaças e Ataques | Ferramenta de pós-exploração e enumeração de redes Windows/AD (sucessora do CrackMapExec). | Y2P3 |
| **NetworkMiner** | NetworkMiner | Forense | Ferramenta que extrai arquivos, credenciais e sessões de um PCAP de forma passiva. | Y2P2 |
| **NFC (NFC)** | Near Field Communication | IoT e Hardware | Comunicação de rádio de curtíssimo alcance, derivada do RFID. | Y1P7 |
| **NIST SP 800-61** | NIST SP 800-61 | Resposta a Incidentes | Guia do NIST para tratamento de incidentes de segurança computacional. | Y2P2 |
| **Nome principal de serviço (SPN)** | Service Principal Name | Sistemas | Identificador de um serviço no Kerberos, associado a uma conta; alvo do Kerberoasting. | Y2P3 |
| **NTLM (NTLM)** | NT LAN Manager | Criptografia | Esquema de hash/autenticação de senhas do Windows, alvo de ataques como pass-the-hash. | Y1P6 |
| **NTLM relay** | NTLM relay | Ameaças e Ataques | Retransmitir uma autenticação NTLM capturada para outro serviço, assumindo a identidade da vítima. | Y2P3 |
| **Nuclei** | Nuclei | Ameaças e Ataques | Scanner rápido baseado em templates YAML para detectar vulnerabilidades conhecidas. | Y2P4 |
| **Não repúdio** | Non-repudiation | GRC | Garantia de que o autor de uma ação não consegue negar depois que a realizou. | Y1P1 |
| **Nível funcional** | Functional level | Sistemas | Define os recursos disponíveis num domínio ou floresta conforme a versão mínima dos DCs. | Y2P3 |

## O

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Objeto de política de grupo (GPO)** | Group Policy Object | Sistemas | Conjunto de configurações aplicadas a usuários e computadores do domínio via AD. | Y1P3 |
| **OpenVAS (OpenVAS / GVM)** | Open Vulnerability Assessment Scanner | GRC | Scanner de vulnerabilidades open source do Greenbone Vulnerability Management. | Y1P4 |
| **OpenVPN** | OpenVPN | Redes | VPN de código aberto baseada em SSL/TLS, flexível e muito usada em acesso remoto. | Y1P1 |
| **Ordem da volatilidade** | Order of volatility | Forense | Prioridade de coleta: do dado mais volátil (RAM) ao mais estável (disco/backup). | Y2P2 |
| **OWASP IoT Top 10** | OWASP IoT Top 10 | GRC | Lista de referência dos dez riscos de segurança mais comuns em dispositivos IoT. | Y1P7 |
| **OWASP Top 10** | OWASP Top 10 | Desenvolvimento | Lista de consenso das dez vulnerabilidades mais críticas em aplicações web. | Y2P4 |

## P

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Padrão avançado de criptografia (AES)** | Advanced Encryption Standard | Criptografia | Cifra de bloco simétrica padrão (FIPS 197) com chaves de 128, 192 ou 256 bits. | Y1P4 |
| **Padrão de criptografia de dados (DES)** | Data Encryption Standard | Criptografia | Cifra de bloco simétrica antiga com chave efetiva de 56 bits; hoje é considerada insegura. | Y1P4 |
| **Paginação** | Paging | Sistemas | Divisão da memória em páginas de tamanho fixo mapeadas pela tabela de páginas. | Y1P3 |
| **PAP / CHAP / MS-CHAPv2 (PAP / CHAP)** | Password / Challenge-Handshake Authentication Protocol | Redes | Protocolos de autenticação de acesso remoto: PAP envia senha em texto claro; CHAP e MS-CHAPv2 usam desafio-resposta. | Y1P3 |
| **Parâmetros posicionais** | Positional parameters | Desenvolvimento | Argumentos passados ao script, acessados como $1, $2…, $# (quantidade) e $@ (todos). | Y1P4 |
| **Pass-the-hash (PtH)** | Pass-the-hash | Ameaças e Ataques | Autenticar usando o hash NTLM da senha, sem conhecer a senha em claro. | Y2P3 |
| **Password spray** | Password spraying | Ameaças e Ataques | Testar uma senha comum contra muitas contas para evitar bloqueio por tentativas. | Y2P3 |
| **Payload** | Payload | Ameaças e Ataques | Código entregue após a exploração; staged (em partes) ou stageless (inteiro). | Y2P3 |
| **Permissões Android** | Android permissions | IoT e Hardware | Mecanismo que exige autorização para um app acessar recursos sensíveis (câmera, contatos). | Y2P4 |
| **Permissões de arquivo** | File permissions (rwx) | Sistemas | Controle de leitura, escrita e execução para dono, grupo e outros, em notação simbólica ou octal. | Y1P2 |
| **Persistência de domínio** | Domain persistence | Ameaças e Ataques | Manter acesso ao domínio mesmo após a resposta inicial, forjando credenciais ou tickets. | Y2P3 |
| **Perícia digital** | Digital forensics | Forense | Coleta, preservação e análise de evidências digitais de forma cientificamente defensável. | Y2P2 |
| **Perícia forense de memória** | Memory forensics | Forense | Análise de um dump da memória RAM para encontrar processos, injeções e malware. | Y2P2 |
| **Pilha** | Stack | Sistemas | Região de memória LIFO para variáveis locais e endereços de retorno; cresce para endereços menores. | Y1P5 |
| **Pilha dupla** | Dual-stack | Redes | Método de transição em que equipamentos rodam IPv4 e IPv6 ao mesmo tempo. | Y1P1 |
| **Pilha TCP/IP (TCP/IP)** | TCP/IP stack | Redes | Arquitetura de protocolos usada na Internet, com 4 camadas: acesso à rede, internet, transporte e aplicação. | Y1P1 |
| **Pipe** | Pipe | Sistemas | Operador | que envia a saída de um comando como entrada do próximo. | Y1P2 |
| **Pipelining** | Pipelining | Sistemas | Técnica que sobrepõe etapas de várias instruções para aumentar a vazão da CPU. | Y1P5 |
| **Pivotagem** | Pivoting (OSINT) | Threat Intel | Usar um dado encontrado para descobrir outros relacionados, expandindo a investigação. | Y2P1 |
| **Playbook** | Playbook | Resposta a Incidentes | Procedimento padronizado passo a passo para responder a um tipo de incidente. | Y2P2 |
| **Política de segurança de conteúdo (CSP)** | Content Security Policy | Desenvolvimento | Cabeçalho que restringe de onde o navegador pode carregar scripts e recursos. | Y2P4 |
| **Ponteiro** | Pointer | Desenvolvimento | Variável que armazena o endereço de memória de outro dado. | Y1P7 |
| **Ponteiro de instrução (EIP / RIP)** | Instruction pointer | Sistemas | Registrador que contém o endereço da próxima instrução a ser executada; controlá-lo é controlar o fluxo. | Y1P5 |
| **Ponto de acesso não autorizado (Rogue AP)** | Rogue access point | Ameaças e Ataques | AP instalado na rede sem autorização, abrindo uma porta de entrada. | Y1P1 |
| **Port mirroring (SPAN)** | Port mirroring (SPAN) | Redes | Recurso do switch que copia o tráfego de uma porta para outra, onde fica o analisador. | Y1P6 |
| **Port scanner** | Port scanner | Ameaças e Ataques | Ferramenta que testa portas de um host para descobrir quais serviços estão abertos. | Y1P4 |
| **Portable Executable (PE)** | Portable Executable | Sistemas | Formato de executável do Windows (EXE, DLL, SYS), com cabeçalhos, seções e tabelas de importação. | Y1P5 |
| **Prevenção de execução de dados (DEP / NX)** | Data Execution Prevention | Sistemas | Mitigação que marca regiões de dados (como a pilha) como não executáveis. | Y1P5 |
| **Primeiro o caminho mais curto (OSPF)** | Open Shortest Path First | Redes | IGP de estado de enlace (link-state) que usa o algoritmo de Dijkstra e organiza a rede em áreas (área 0 = backbone). | Y1P1 |
| **Princípio do menor privilégio (PoLP)** | Principle of least privilege | GRC | Dar a cada usuário ou processo apenas as permissões estritamente necessárias. | Y1P2 |
| **Processamento de loopback** | Loopback processing | Sistemas | Modo de GPO que aplica configurações de usuário conforme o computador onde ele faz logon. | Y1P3 |
| **Processo (PID)** | Process (PID) | Sistemas | Programa em execução, identificado por um número (PID). | Y1P2 |
| **Protoboard** | Breadboard | IoT e Hardware | Placa de contatos para montar circuitos sem solda. | Y1P7 |
| **Protocolo de autenticação extensível (EAP)** | Extensible Authentication Protocol | Criptografia | Framework de autenticação que suporta certificados, tokens e PEAP; base do 802.1X. | Y1P3 |
| **Protocolo de borda (BGP)** | Border Gateway Protocol | Redes | Protocolo de vetor de caminho usado entre sistemas autônomos; é o roteamento da Internet. | Y1P1 |
| **Protocolo de configuração dinâmica de hosts (DHCP)** | Dynamic Host Configuration Protocol | Redes | Serviço que entrega IP, máscara, gateway e DNS automaticamente aos clientes. | Y1P3 |
| **Protocolo de controle de transmissão (TCP)** | Transmission Control Protocol | Redes | Protocolo de transporte orientado a conexão, com three-way handshake, confirmação e ordenação. | Y1P4 |
| **Protocolo de datagrama de usuário (UDP)** | User Datagram Protocol | Redes | Protocolo de transporte sem conexão e sem garantia de entrega; leve e rápido. | Y1P4 |
| **Protocolo de transferência de arquivos (FTP)** | File Transfer Protocol | Redes | Protocolo de transferência de arquivos (TCP 21) sem criptografia; FTPS adiciona TLS. | Y1P2 |
| **Protocolo de transferência de hipertexto (HTTP)** | Hypertext Transfer Protocol | Redes | Protocolo de aplicação da Web, baseado em requisição/resposta (métodos GET, POST etc.). | Y1P1 |
| **Protocolo Spanning Tree (STP)** | Spanning Tree Protocol | Redes | Protocolo que bloqueia caminhos redundantes entre switches para evitar loops de camada 2. | Y1P1 |
| **Proxy** | Proxy | Redes | Intermediário que repassa requisições, mudando o IP visto pelo destino. | Y2P1 |
| **Proxy de interceptação** | Intercepting proxy | Ameaças e Ataques | Ferramenta entre o navegador e o servidor para ler e modificar requisições web. | Y2P4 |
| **PTES (PTES)** | Penetration Testing Execution Standard | Ameaças e Ataques | Metodologia padrão de pentest em fases, do pré-engajamento ao relatório. | Y2P4 |
| **Python** | Python | Desenvolvimento | Linguagem interpretada, de alto nível e multiparadigma, muito usada em automação de segurança e ciência de dados. | Y1P4 |

## Q

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Quebra de controle de acesso** | Broken Access Control | Ameaças e Ataques | Falha que permite acessar recursos ou ações além do autorizado. | Y2P4 |

## R

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **RADIUS (RADIUS)** | Remote Authentication Dial-In User Service | Redes | Protocolo AAA (UDP 1812/1813) que combina autenticação e autorização e cifra só a senha; ideal para acesso à rede. | Y1P1 |
| **Rainbow table** | Rainbow table | Ameaças e Ataques | Tabela pré-computada de hashes para reverter senhas rapidamente; o salt a inutiliza. | Y1P6 |
| **Ransomware** | Ransomware | Ameaças e Ataques | Malware que cifra os dados (ou o disco inteiro) e exige resgate para liberar. | Y1P1 |
| **Recon-ng** | Recon-ng | Threat Intel | Framework de reconhecimento em Python, com módulos no estilo Metasploit. | Y2P1 |
| **Reconhecimento (Recon)** | Reconnaissance | Ameaças e Ataques | Fase de coleta de informações sobre o alvo; passivo (sem tocar o alvo) ou ativo (interagindo). | Y2P3 |
| **Rede de longa distância (WAN)** | Wide Area Network | Redes | Rede que interliga LANs em grandes áreas geográficas. | Y1P1 |
| **Rede local (LAN)** | Local Area Network | Redes | Rede que cobre uma área pequena (casa, andar, empresa) e termina no roteador/gateway. | Y1P1 |
| **Rede local sem fio (WLAN)** | Wireless LAN | Redes | Rede sem fio local baseada nos padrões IEEE 802.11 (Wi-Fi). | Y1P7 |
| **Rede local virtual (VLAN)** | Virtual LAN | Redes | Segmentação lógica de um switch em domínios de broadcast separados. | Y1P1 |
| **Rede privada virtual (VPN)** | Virtual Private Network | Redes | Túnel cifrado sobre uma rede pública que liga usuários ou sites como se estivessem na mesma rede. | Y1P1 |
| **Redirecionamento** | Redirection | Sistemas | Envio de entradas ou saídas para arquivos (>, >>, <, 2>&1). | Y1P2 |
| **Registrador** | Register | Sistemas | Pequena área de armazenamento dentro da CPU, extremamente rápida, usada no processamento. | Y1P5 |
| **Registradores de uso geral (GPR)** | General-purpose registers | Sistemas | Registradores x86 usados em cálculos e manipulação de dados: EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP. | Y1P5 |
| **Registro do Windows** | Windows Registry | Forense | Banco hierárquico de configuração do Windows, rico em artefatos forenses. | Y2P2 |
| **Registros DNS (RR)** | DNS resource records | Redes | Entradas de uma zona: SOA, NS, A, AAAA, CNAME, MX, PTR, SRV etc. | Y1P3 |
| **Relatório forense** | Forensic report | Forense | Documento claro e reprodutível com método, achados e conclusões da perícia. | Y2P2 |
| **Requisitos prioritários de inteligência (PIR)** | Priority Intelligence Requirements | Threat Intel | Perguntas-chave que direcionam a coleta e a análise de inteligência. | Y2P1 |
| **Retorno do investimento em segurança (ROSI)** | Return on Security Investment | GRC | Métrica que estima o retorno financeiro de um investimento em segurança (perda evitada × custo). | Y1P6 |
| **Reverse shell** | Reverse shell | Ameaças e Ataques | Shell em que a máquina alvo se conecta de volta ao atacante, contornando firewalls de entrada. | Y2P3 |
| **RFID (RFID)** | Radio-Frequency Identification | IoT e Hardware | Identificação por radiofrequência usando etiquetas (passivas, semipassivas ou ativas) e leitores. | Y1P7 |
| **Risco** | Risk | GRC | Possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto a um ativo; costuma ser estimado como probabilidade × impacto. | Y1P4 |
| **Risco residual** | Residual risk | GRC | Risco que sobra depois de aplicados os controles. | Y1P4 |
| **Roteamento dinâmico** | Dynamic routing | Redes | Roteadores trocam informações por protocolos e montam as rotas automaticamente. | Y1P1 |
| **Roteamento e acesso remoto (RRAS)** | Routing and Remote Access Service | Redes | Função do Windows Server que provê VPN, NAT e roteamento. | Y1P3 |
| **Roteamento estático** | Static routing | Redes | Rotas configuradas manualmente pelo administrador. | Y1P1 |
| **Roteamento sem classes (CIDR)** | Classless Inter-Domain Routing | Redes | Notação e técnica que define a máscara pelo número de bits de rede (/n), sem depender das classes. | Y1P1 |
| **RSA (RSA)** | Rivest-Shamir-Adleman | Criptografia | Algoritmo assimétrico para cifra e assinatura digital, baseado na dificuldade de fatorar números grandes. | Y1P6 |
| **rsync** | rsync | Sistemas | Ferramenta de cópia e sincronização incremental, local ou remota (via SSH). | Y1P2 |
| **rsyslog** | rsyslog | Forense | Serviço que recebe e grava logs em arquivos de texto ou os encaminha para servidores remotos/SIEM. | Y1P2 |
| **Rubeus** | Rubeus | Ameaças e Ataques | Ferramenta para abuso de Kerberos (roasting, tickets) no Windows. | Y2P3 |

## S

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Sandbox de aplicativo** | Application sandbox | IoT e Hardware | Isolamento de cada app Android com UID próprio, limitando seu acesso. | Y2P4 |
| **SEAndroid (SEAndroid)** | Security-Enhanced Android | IoT e Hardware | Implementação de SELinux no Android que aplica MAC para reforçar o isolamento. | Y2P4 |
| **Searchsploit** | Searchsploit | Ameaças e Ataques | Busca offline no banco de exploits do Exploit-DB. | Y2P4 |
| **Secure boot** | Secure boot | IoT e Hardware | Mecanismo que só permite executar firmware assinado e confiável no boot. | Y1P7 |
| **sed** | Stream editor | Sistemas | Editor de fluxo para substituir, apagar ou extrair texto por padrão. | Y1P2 |
| **Segregação de funções (SoD)** | Separation of duties | GRC | Dividir uma tarefa crítica entre pessoas diferentes para evitar fraude e erro. | Y1P6 |
| **Segurança de porta** | Port Security | Redes | Limita quais e quantos MACs podem usar uma porta do switch e define a ação em caso de violação. | Y1P1 |
| **Segurança mobile** | Mobile security | IoT e Hardware | Proteção de dispositivos e aplicativos móveis (Android/iOS) e seus dados. | Y2P4 |
| **Segurança operacional (OpSec)** | Operational Security | Threat Intel | Práticas para proteger a própria operação de investigação, evitando expor identidade e intenções. | Y2P1 |
| **Segurança por obscuridade** | Security by obscurity | GRC | Depender do segredo sobre o funcionamento do sistema como proteção; fraco se usado sozinho. | Y1P6 |
| **Senha hardcoded** | Hardcoded password | Ameaças e Ataques | Credencial fixa embutida no firmware ou código, impossível de o usuário trocar. | Y1P7 |
| **Server Message Block (SMB)** | Server Message Block | Redes | Protocolo de compartilhamento de arquivos e impressoras (comum no Windows; Samba no Linux). | Y1P2 |
| **Server-Side Request Forgery (SSRF)** | Server-Side Request Forgery | Ameaças e Ataques | Forçar o servidor a fazer requisições a destinos escolhidos pelo atacante. | Y2P4 |
| **Servidor de políticas de rede (NPS)** | Network Policy Server | Redes | Implementação de RADIUS da Microsoft para autenticar e autorizar VPN, Wi-Fi e 802.1X. | Y1P3 |
| **Servidor web** | Web server | Desenvolvimento | Software que atende requisições HTTP/HTTPS e entrega páginas ou APIs. | Y1P2 |
| **Serviços de Domínio do Active Directory (AD DS)** | Active Directory Domain Services | Sistemas | Função do Windows Server que transforma o servidor em controlador de domínio. | Y1P3 |
| **Serviços de informações da Internet (IIS)** | Internet Information Services | Desenvolvimento | Servidor web da Microsoft. | Y1P3 |
| **SFTP / SCP (SFTP / SCP)** | SSH File Transfer Protocol / Secure Copy | Redes | Transferência de arquivos cifrada que usa o canal SSH. | Y1P2 |
| **Shebang** | Shebang | Desenvolvimento | Primeira linha de um script (#!) que indica qual interpretador deve executá-lo. | Y1P4 |
| **Shell** | Shell | Sistemas | Interpretador de comandos entre o usuário e o kernel; o Bash é o mais comum no Linux. | Y1P2 |
| **Shell Script** | Shell script | Desenvolvimento | Arquivo de comandos de shell executado em sequência para automatizar tarefas. | Y1P4 |
| **Shell seguro (SSH)** | Secure Shell | Redes | Protocolo de acesso remoto cifrado (TCP 22), com autenticação por senha ou chave. | Y1P2 |
| **Shellcode** | Shellcode | Ameaças e Ataques | Pequeno trecho de código de máquina usado como payload em exploração de memória. | Y1P5 |
| **Shodan** | Shodan | Threat Intel | Motor de busca de dispositivos e serviços expostos na internet. | Y2P1 |
| **Silver Ticket** | Silver Ticket | Ameaças e Ataques | Ticket de serviço (TGS) forjado para um serviço específico, mais furtivo que o Golden. | Y2P3 |
| **Sistema autônomo (AS)** | Autonomous System | Redes | Conjunto de redes sob uma única política de roteamento, identificado por um número (ASN). | Y1P1 |
| **Sistema de arquivos** | Filesystem | Sistemas | Estrutura que organiza como os dados são gravados no disco. | Y1P2 |
| **Sistema de arquivos de rede (NFS)** | Network File System | Redes | Protocolo para compartilhar diretórios pela rede, montados como se fossem locais. | Y1P2 |
| **Sistema de controle industrial (ICS)** | Industrial Control System | IoT e Hardware | Conjunto de sistemas (SCADA, PLC) que automatiza processos industriais. | Y1P7 |
| **Sistema de detecção de intrusão (IDS)** | Intrusion Detection System | Resposta a Incidentes | Monitora o tráfego ou o host e gera alertas sobre atividade suspeita, sem bloquear (passivo). | Y1P1 |
| **Sistema de nomes de domínio (DNS)** | Domain Name System | Redes | Serviço que traduz nomes em endereços IP de forma hierárquica e distribuída. | Y1P1 |
| **Sistema de pontuação de vulnerabilidades (CVSS)** | Common Vulnerability Scoring System | GRC | Padrão do FIRST que dá uma nota de 0 a 10 à gravidade de uma vulnerabilidade. | Y1P2 |
| **Sistema de prevenção de intrusão (IPS)** | Intrusion Prevention System | Resposta a Incidentes | Fica em linha (inline) e bloqueia em tempo real o tráfego identificado como malicioso. | Y1P1 |
| **Sistema operacional (SO / OS)** | Operating system | Sistemas | Software que gerencia o hardware e oferece abstrações (processos, arquivos, memória) aos programas. | Y1P3 |
| **Sniffing** | Sniffing | Ameaças e Ataques | Captura passiva do tráfego de rede para ler dados, especialmente os em texto claro. | Y1P6 |
| **Snort** | Snort | Redes | IDS/IPS open source baseado em assinaturas, muito usado em detecção de intrusão. | Y2P2 |
| **Sock puppet** | Sock puppet | Threat Intel | Persona falsa, isolada e consistente, usada para investigar sem expor a identidade real. | Y2P1 |
| **Socket** | Socket | Redes | Ponto final de comunicação em rede (IP + porta + protocolo) usado pelos programas para trocar dados. | Y1P4 |
| **SPI (SPI)** | Serial Peripheral Interface | IoT e Hardware | Barramento serial síncrono para comunicação com chips, como memórias flash. | Y1P7 |
| **SpiderFoot** | SpiderFoot | Threat Intel | Ferramenta automatizada de OSINT que coleta dados de centenas de fontes. | Y2P1 |
| **Splunk** | Splunk | Resposta a Incidentes | SIEM e plataforma de análise de logs que usa a linguagem de busca SPL. | Y2P2 |
| **sqlmap** | sqlmap | Ameaças e Ataques | Ferramenta que automatiza a detecção e exploração de SQL Injection. | Y2P4 |
| **ss** | Socket statistics | Redes | Lista sockets e portas em escuta ou conexões ativas, junto com o processo dono. | Y1P2 |
| **Stack canary** | Stack canary | Sistemas | Valor secreto colocado antes do endereço de retorno; se for alterado, o programa aborta. | Y1P5 |
| **Steghide** | Steghide | Criptografia | Ferramenta de esteganografia que embute e extrai dados cifrados em imagens e áudio. | Y1P6 |
| **STIX/TAXII (STIX/TAXII)** | Structured Threat Information eXpression / Trusted Automated eXchange | Threat Intel | Padrões para descrever (STIX) e transportar (TAXII) inteligência de ameaças de forma estruturada. | Y2P1 |
| **Stuxnet** | Stuxnet | Ameaças e Ataques | Malware que sabotou centrífugas industriais via PLC, mostrando dano físico por código. | Y1P7 |
| **sudo** | Superuser do | Sistemas | Executa um comando com privilégios de outro usuário (normalmente root), com registro em log. | Y1P2 |
| **SUID (SUID)** | Set User ID | Sistemas | Bit especial que faz um executável rodar com o privilégio do dono do arquivo; alvo comum de escalada de privilégio. | Y1P2 |
| **Superusuário** | Superuser (root) | Sistemas | Conta com privilégio total no sistema (UID 0); deve ser usada só quando necessário. | Y1P2 |
| **Swapping** | Swapping | Sistemas | Mover páginas ou processos entre a RAM e o disco para liberar memória. | Y1P5 |
| **SYN flood** | SYN flood | Ameaças e Ataques | DoS que envia muitos SYN sem completar o handshake, esgotando as conexões meio-abertas. | Y1P6 |
| **sysctl** | sysctl | Sistemas | Comando para ler e ajustar parâmetros do kernel em tempo de execução. | Y1P2 |
| **systemd** | systemd | Sistemas | Sistema de inicialização e gerenciador de serviços (units), dependências e logs do Linux moderno. | Y1P2 |

## T

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Tabela de endereços de importação (IAT)** | Import Address Table | Sistemas | Tabela do PE com os endereços das funções de API importadas de outras DLLs. | Y1P5 |
| **Tabela de endereços MAC (CAM)** | MAC address table (CAM table) | Redes | Tabela do switch que associa endereços MAC às portas para encaminhar quadros. | Y1P1 |
| **TACACS+ (TACACS+)** | Terminal Access Controller Access-Control System Plus | Redes | Protocolo AAA (TCP/49) que cifra o pacote inteiro e separa as três funções; ideal para administrar equipamentos. | Y1P1 |
| **tcpdump** | tcpdump | Redes | Capturador de pacotes em linha de comando; grava PCAPs para análise. | Y1P2 |
| **Tecnologia operacional (OT)** | Operational Technology | IoT e Hardware | Hardware e software que monitoram e controlam processos físicos industriais. | Y1P7 |
| **Telnet** | Telnet | Redes | Protocolo antigo de acesso remoto (TCP 23) que trafega tudo em texto claro. | Y1P2 |
| **Teste de intrusão (Pentest)** | Penetration test | Ameaças e Ataques | Ataque simulado e autorizado que explora vulnerabilidades para provar o impacto. | Y1P4 |
| **Texto claro** | Cleartext | Ameaças e Ataques | Dados transmitidos sem criptografia, legíveis por quem capturar o tráfego. | Y1P2 |
| **theHarvester** | theHarvester | Threat Intel | Ferramenta que coleta e-mails, nomes, subdomínios e hosts de fontes públicas. | Y2P1 |
| **Thread** | Thread | Sistemas | Linha de execução dentro de um processo; threads compartilham a memória do processo. | Y1P3 |
| **Three-way handshake** | Three-way handshake | Redes | Estabelecimento de conexão TCP: SYN → SYN-ACK → ACK. | Y1P4 |
| **Tier Model** | Administrative Tier Model | GRC | Modelo que separa contas administrativas por nível (DC, servidores, estações) para conter comprometimento. | Y2P3 |
| **Timeline forense** | Forensic timeline | Forense | Reconstrução cronológica dos eventos a partir de múltiplos artefatos. | Y2P2 |
| **Tinkercad** | Tinkercad | IoT e Hardware | Simulador online de circuitos e Arduino, usado para prototipar sem hardware físico. | Y1P7 |
| **Tomada de conta (ATO)** | Account takeover | Ameaças e Ataques | Uso de credenciais legítimas roubadas para controlar a conta de uma vítima. | Y1P1 |
| **Tor (Tor)** | The Onion Router | Redes | Rede de anonimato que roteia o tráfego por vários nós cifrados; dá acesso à dark web. | Y1P6 |
| **Tradução de endereços de rede (NAT)** | Network Address Translation | Redes | Troca de endereços IP (geralmente privado→público) na borda da rede. | Y1P1 |
| **Tratamento de risco** | Risk treatment | GRC | Decisão sobre um risco: mitigar, transferir, evitar ou aceitar. | Y1P4 |
| **Tronco 802.1Q** | 802.1Q trunk | Redes | Link que transporta várias VLANs entre switches, marcando os quadros com a tag da VLAN. | Y1P1 |
| **Tríade CID (CID / CIA)** | CIA triad | GRC | Os três pilares da segurança da informação: confidencialidade, integridade e disponibilidade. | Y1P1 |
| **tshark** | tshark | Forense | Versão em linha de comando do Wireshark, útil para automação e extração de campos. | Y1P6 |
| **Táticas, técnicas e procedimentos (TTP)** | Tactics, Techniques and Procedures | Threat Intel | O comportamento do adversário: o porquê (tática), o como (técnica) e o passo a passo (procedimento). | Y2P1 |

## U

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Unidade organizacional (OU)** | Organizational Unit | Sistemas | Contêiner do AD que organiza objetos e recebe GPOs e delegação de controle. | Y1P3 |
| **Use-after-free (UAF)** | Use-after-free | Ameaças e Ataques | Usar um ponteiro depois que a memória que ele referenciava foi liberada. | Y1P5 |

## V

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Varredura de portas** | Port scan | Ameaças e Ataques | Sondagem de hosts para descobrir quais estão ativos e quais serviços/portas estão abertos; costuma ser o primeiro passo de um ataque. | Y1P1 |
| **Vetor de ataque** | Attack vector | Ameaças e Ataques | Caminho ou meio usado pelo atacante para chegar ao alvo. | Y1P1 |
| **vim** | Vi IMproved | Sistemas | Editor de texto do terminal com modos normal, inserção e comando. | Y1P2 |
| **Volatility** | Volatility Framework | Forense | Framework open source de análise forense de memória RAM. | Y2P2 |
| **Vulnerabilidade** | Vulnerability | GRC | Fraqueza em sistema, processo ou pessoa que pode ser explorada por uma ameaça. | Y1P4 |
| **Vulnerabilidades e exposições comuns (CVE)** | Common Vulnerabilities and Exposures | GRC | Catálogo público de vulnerabilidades conhecidas, mantido pelo MITRE, com um ID único para cada uma. | Y1P2 |

## W

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Web fuzzing** | Web fuzzing | Ameaças e Ataques | Enviar muitas entradas automatizadas a parâmetros web para encontrar falhas. | Y2P4 |
| **WHOIS** | WHOIS | Redes | Serviço que consulta dados de registro de um domínio ou bloco de IP. | Y2P1 |
| **Windows Server** | Windows Server | Sistemas | Linha de sistemas operacionais da Microsoft para servidores, com funções como AD, DNS, DHCP, IIS e Hyper-V. | Y1P3 |
| **Windows Server Update Services (WSUS)** | Windows Server Update Services | Sistemas | Serviço que centraliza aprovação e distribuição de atualizações Microsoft na rede. | Y1P3 |
| **Wine (Wine)** | Wine Is Not an Emulator | Sistemas | Camada de compatibilidade que roda executáveis Windows no Linux sem emular o SO. | Y1P5 |
| **WinRM (WinRM)** | Windows Remote Management | Sistemas | Serviço de administração remota do Windows, usado também para movimento lateral. | Y2P3 |
| **Wireshark** | Wireshark | Forense | Analisador de protocolos de rede com interface gráfica, para capturar e dissecar pacotes. | Y1P6 |
| **Wordlist** | Wordlist | Ameaças e Ataques | Lista de senhas ou palavras usadas em ataques de força bruta ou dicionário. | Y1P4 |
| **WPA2 (WPA2)** | Wi-Fi Protected Access 2 | Criptografia | Padrão de segurança Wi-Fi com AES-CCMP; modos Personal (PSK) e Enterprise (802.1X/RADIUS). | Y1P1 |
| **WPA3 (WPA3)** | Wi-Fi Protected Access 3 | Criptografia | Sucessor do WPA2 com SAE, forward secrecy e opção de 192 bits no modo Enterprise. | Y1P1 |
| **WPS (WPS)** | Wi-Fi Protected Setup | Ameaças e Ataques | Recurso de configuração fácil de Wi-Fi com PIN, vulnerável a força bruta. | Y1P7 |
| **WPScan** | WPScan | Ameaças e Ataques | Scanner de vulnerabilidades específico para WordPress. | Y2P4 |
| **Write blocker** | Write blocker | Forense | Dispositivo/software que impede qualquer escrita na mídia original durante a coleta. | Y2P2 |

## X

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **XML External Entity (XXE)** | XML External Entity | Ameaças e Ataques | Abuso de entidades externas em XML para ler arquivos ou fazer SSRF. | Y2P4 |

## Z

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Zabbix** | Zabbix | Sistemas | Plataforma open source de monitoramento de redes, servidores e aplicações, com agentes e alertas. | Y1P4 |
| **Zona de pesquisa inversa** | Reverse lookup zone | Redes | Zona que resolve IP → nome usando registros PTR. | Y1P3 |
| **Zona DNS** | DNS zone | Redes | Parte do namespace DNS sob responsabilidade de um servidor; pode ser primária ou secundária (cópia). | Y1P3 |

## Á

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Árvore de domínios** | Domain tree | Sistemas | Conjunto de domínios do AD com namespace DNS contíguo. | Y1P3 |
