# 📖 Glossary (PT ↔ EN)

> Generated from `glossary.csv` by `scripts/build_glossary.py`. Edit the CSV, not this file.

**185 terms**

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z) · [Á](#á)

## A

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Active Directory (AD)** | Active Directory | Sistemas | Serviço de diretório da Microsoft que centraliza identidades, computadores, grupos e políticas de uma rede. | Y1P3 |
| **AGDLP (AGDLP)** | Accounts, Global, Domain Local, Permissions | GRC | Boa prática de aninhamento de grupos: conta → grupo global → grupo de domínio local → permissão (AGUDLP com universal). | Y1P3 |
| **Ameaça** | Threat | GRC | Agente ou evento com potencial de causar dano a um ativo. | Y1P4 |
| **Ataque de dicionário** | Dictionary attack | Ameaças e Ataques | Tentar senhas de uma lista de palavras (wordlist) contra um login ou contra hashes. | Y1P4 |
| **Ativo** | Asset | GRC | Qualquer coisa de valor para a organização que precisa de proteção. | Y1P4 |
| **auditd** | Linux Audit daemon | Forense | Serviço que registra eventos de segurança no nível do kernel conforme regras definidas. | Y1P2 |
| **Autenticação simultânea de iguais (SAE)** | Simultaneous Authentication of Equals | Criptografia | Troca de chaves do WPA3-Personal que substitui o PSK e resiste a ataques de dicionário offline. | Y1P1 |
| **Autenticação, autorização e auditoria (AAA)** | Authentication, Authorization and Accounting | GRC | Framework que controla quem acessa (autenticação), o que pode fazer (autorização) e registra o que fez (accounting). | Y1P1 |
| **Autoconfiguração sem estado (SLAAC)** | Stateless Address Autoconfiguration | Redes | Mecanismo IPv6 em que o host gera o próprio endereço a partir do prefixo anunciado pelo roteador. | Y1P1 |
| **Avaliação de vulnerabilidades** | Vulnerability assessment | GRC | Varredura (geralmente automatizada) que identifica e lista vulnerabilidades em um escopo. | Y1P4 |
| **awk** | awk | Sistemas | Linguagem de processamento de texto orientada a colunas/campos. | Y1P2 |

## B

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Base nacional de vulnerabilidades (NVD)** | National Vulnerability Database | GRC | Base do NIST que enriquece os CVEs com CVSS, CPE e referências. | Y1P4 |
| **Base64** | Base64 | Criptografia | Codificação (não criptografia) que representa dados binários em texto ASCII. | Y1P2 |
| **Bloqueio de herança** | Block inheritance | Sistemas | Configuração na OU que impede herdar GPOs de níveis superiores. | Y1P3 |

## C

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **CIS Benchmark (CIS)** | CIS Benchmark | GRC | Guias de configuração segura publicados pelo Center for Internet Security. | Y1P2 |
| **COBIT (COBIT)** | Control Objectives for Information and Related Technologies | GRC | Framework da ISACA para governança e gestão de TI. | Y1P4 |
| **Console de gerenciamento de política de grupo (GPMC)** | Group Policy Management Console | Sistemas | Ferramenta para criar, vincular e analisar GPOs. | Y1P3 |
| **Controlador de domínio (DC)** | Domain Controller | Sistemas | Servidor que guarda uma cópia do banco do AD, autentica usuários e replica alterações com outros DCs. | Y1P3 |
| **Criptografia simétrica** | Symmetric encryption | Criptografia | Esquema em que a mesma chave cifra e decifra os dados. | Y1P4 |
| **cron** | cron | Sistemas | Serviço de agendamento de tarefas recorrentes, configurado no crontab. | Y1P2 |
| **Código de saída** | Exit code / return code | Desenvolvimento | Número que um comando devolve ao terminar; 0 indica sucesso e outro valor indica erro. | Y1P4 |

## D

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Daemon** | Daemon | Sistemas | Processo que roda em segundo plano prestando um serviço. | Y1P2 |
| **Delegação de controle** | Delegation of control | GRC | Concessão de tarefas administrativas específicas sobre uma OU sem dar privilégio total. | Y1P3 |
| **DHCP Snooping** | DHCP Snooping | Redes | Recurso do switch que só aceita respostas DHCP de portas confiáveis e monta uma tabela de vínculos IP-MAC-porta. | Y1P1 |
| **Distribuição Linux** | Linux distribution (distro) | Sistemas | Pacote completo formado pelo kernel Linux, ferramentas GNU, gerenciador de pacotes e configurações. | Y1P2 |
| **Domínio** | Domain | Sistemas | Unidade administrativa e de replicação do AD, identificada por um nome DNS. | Y1P3 |
| **DORA (DORA)** | Discover, Offer, Request, Acknowledge | Redes | As quatro mensagens da concessão DHCP. | Y1P3 |

## E

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Encaminhador DNS** | DNS forwarder | Redes | DNS para onde o servidor envia as consultas que não consegue resolver localmente. | Y1P3 |
| **Encapsulamento** | Encapsulation | Redes | Cada camada acrescenta seu cabeçalho aos dados da camada de cima antes de enviar; o destino faz o processo inverso. | Y1P1 |
| **Endereço IPv4 (IPv4)** | IPv4 address | Redes | Endereço lógico de 32 bits escrito em 4 octetos decimais. | Y1P1 |
| **Endereço IPv6 (IPv6)** | IPv6 address | Redes | Endereço de 128 bits em hexadecimal, em 8 grupos separados por dois-pontos. | Y1P1 |
| **Endereço MAC (MAC)** | MAC address | Redes | Endereço físico de 48 bits da interface de rede, usado na camada 2. | Y1P1 |
| **Endereços privados** | Private addressing (RFC 1918) | Redes | Faixas IPv4 reservadas para uso interno, não roteáveis na Internet: 10/8, 172.16/12, 192.168/16. | Y1P1 |
| **Endurecimento** | Hardening | GRC | Conjunto de configurações que reduzem a superfície de ataque de um sistema. | Y1P2 |
| **Envenenamento de ARP** | ARP spoofing / ARP poisoning | Ameaças e Ataques | Envio de respostas ARP falsas para associar o MAC do atacante ao IP de outro host (ex.: gateway), permitindo MitM. | Y1P1 |
| **Escalada de privilégio (PrivEsc)** | Privilege escalation | Ameaças e Ataques | Quando um atacante sai de um acesso limitado para um nível mais alto (ex.: root). | Y1P2 |
| **Escalonamento** | Scheduling | Sistemas | Decisão do SO sobre qual processo ou thread usa a CPU e por quanto tempo. | Y1P3 |
| **Expressão regular (regex)** | Regular expression | Desenvolvimento | Linguagem de padrões para buscar e extrair texto. | Y1P4 |

## F

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Failover DHCP** | DHCP failover | Redes | Dois servidores DHCP compartilham escopos para manter a entrega de IPs se um falhar. | Y1P3 |
| **Filtro WMI (WMI)** | WMI filter | Sistemas | Consulta WMI que limita a aplicação de uma GPO a máquinas que atendam a um critério. | Y1P3 |
| **Firewall com estado** | Stateful firewall | Redes | Firewall que acompanha o estado das conexões e libera automaticamente o tráfego de retorno. | Y1P1 |
| **Firewall de aplicação web (WAF)** | Web Application Firewall | Desenvolvimento | Filtra requisições HTTP/HTTPS para proteger aplicações web (SQLi, XSS etc.). | Y1P1 |
| **Firewall de próxima geração (NGFW)** | Next-Generation Firewall | Redes | Firewall que soma inspeção de aplicação (camada 7), IPS integrado e controle por usuário/aplicação. | Y1P1 |
| **firewalld** | firewalld | Redes | Firewall dinâmico baseado em zonas, gerenciado pelo firewall-cmd, com regras runtime e permanentes. | Y1P2 |
| **Floresta** | Forest | Sistemas | Conjunto de uma ou mais árvores que compartilham schema e relações de confiança; é a fronteira de segurança do AD. | Y1P3 |
| **Fluxos padrão** | Standard streams (stdin/stdout/stderr) | Sistemas | Canais de entrada (fd 0), saída (fd 1) e erro (fd 2) de um processo. | Y1P2 |
| **Força bruta** | Brute force | Ameaças e Ataques | Tentativas repetidas de adivinhar senhas até acertar. | Y1P2 |
| **fstab** | File systems table | Sistemas | Arquivo /etc/fstab que lista o que é montado automaticamente no boot e com quais opções. | Y1P2 |
| **Função** | Function | Desenvolvimento | Bloco de código nomeado e reutilizável que recebe parâmetros e pode retornar um valor. | Y1P4 |

## G

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Gerenciador de pacotes** | Package manager | Sistemas | Ferramenta que instala, atualiza e remove software resolvendo dependências. | Y1P2 |
| **Gerenciador de volumes lógicos (LVM)** | Logical Volume Manager | Sistemas | Camada que agrupa discos (PV) em pools (VG) e cria volumes lógicos (LV) redimensionáveis. | Y1P2 |
| **Gestão de patches** | Patch management | GRC | Processo de testar, aprovar e aplicar atualizações de segurança. | Y1P3 |
| **Gestão de vulnerabilidades** | Vulnerability management | GRC | Programa contínuo para identificar, classificar, priorizar, corrigir e verificar vulnerabilidades. | Y1P4 |
| **Globbing** | Globbing / pattern matching | Sistemas | Uso de curingas (*, ?, [ ]) pelo shell para casar nomes de arquivos. | Y1P2 |
| **GNU/Linux** | GNU/Linux | Sistemas | Nome que reconhece que o sistema combina o kernel Linux com as ferramentas do projeto GNU. | Y1P2 |
| **GPO forçada** | Enforced GPO | Sistemas | Link de GPO que prevalece sobre conflitos e ignora o bloqueio de herança. | Y1P3 |
| **grep** | Global regular expression print | Sistemas | Busca linhas que casam com um padrão (texto ou regex). | Y1P2 |
| **Grupo de segurança** | Security group | Sistemas | Grupo do AD usado para conceder permissões; escopos: global, domínio local e universal. | Y1P3 |
| **Gêmeo maligno** | Evil twin | Ameaças e Ataques | Ponto de acesso falso com o mesmo SSID de uma rede legítima para atrair vítimas. | Y1P1 |

## H

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Hacktivismo** | Hacktivism | Ameaças e Ataques | Ataques motivados por causas políticas ou sociais, normalmente defacement ou DoS. | Y1P1 |
| **Hash criptográfico** | Cryptographic hash | Criptografia | Função que gera um resumo de tamanho fixo e irreversível; qualquer mudança no dado muda o hash. | Y1P4 |
| **Hierarquia padrão de sistema de arquivos (FHS)** | Filesystem Hierarchy Standard | Sistemas | Padrão que define a função de cada diretório no Linux. | Y1P2 |
| **Homem no meio (MitM)** | Man-in-the-Middle | Ameaças e Ataques | Atacante se posiciona entre duas partes para interceptar ou alterar a comunicação. | Y1P1 |

## I

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Injeção** | Injection | Ameaças e Ataques | Envio de entrada maliciosa que a aplicação interpreta como comando ou consulta. | Y1P2 |
| **Inspeção dinâmica de ARP (DAI)** | Dynamic ARP Inspection | Redes | Valida mensagens ARP contra a tabela do DHCP Snooping e descarta as falsificadas. | Y1P1 |
| **IPsec (IPsec)** | Internet Protocol Security | Criptografia | Conjunto de protocolos (IKE, ESP, AH) que cifra e autentica pacotes IP; modos transporte e túnel. | Y1P1 |
| **ISO 31000** | ISO 31000 | GRC | Norma com princípios e diretrizes genéricas para gestão de riscos. | Y1P4 |
| **ISO/IEC 27001** | ISO/IEC 27001 | GRC | Norma internacional que define os requisitos de um Sistema de Gestão de Segurança da Informação (SGSI); a 27002 traz os controles. | Y1P4 |

## J

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **journalctl** | journalctl | Forense | Ferramenta para consultar o journal do systemd (logs binários estruturados). | Y1P2 |

## K

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Kali Linux** | Kali Linux | Ameaças e Ataques | Distribuição Debian voltada a testes de segurança, com centenas de ferramentas pré-instaladas. | Y1P4 |
| **Kerberos** | Kerberos | Criptografia | Protocolo de autenticação baseado em tickets usado pelo AD. | Y1P3 |
| **Kernel** | Kernel | Sistemas | Núcleo do sistema operacional: gerencia CPU, memória, dispositivos e processos, fazendo a ponte entre hardware e software. | Y1P2 |

## L

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **LAMP (LAMP)** | Linux, Apache, MySQL, PHP | Desenvolvimento | Stack clássica de servidor web: Linux + Apache + MySQL/MariaDB + PHP. | Y1P2 |
| **Linguagem interpretada** | Interpreted language | Desenvolvimento | Linguagem executada por um interpretador linha a linha, sem compilar para binário antes. | Y1P4 |
| **Lista** | List | Desenvolvimento | Estrutura de dados ordenada e mutável do Python. | Y1P4 |
| **Lista de controle de acesso (ACL)** | Access Control List | Redes | Lista ordenada de regras permit/deny aplicada a uma interface para filtrar tráfego; termina com um deny implícito. | Y1P1 |
| **LSDOU (LSDOU)** | Local, Site, Domain, OU | Sistemas | Ordem de processamento das GPOs; a mais próxima do objeto vence em conflito. | Y1P3 |

## M

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Memória virtual** | Virtual memory | Sistemas | Abstração que dá a cada processo um espaço de endereçamento próprio, mapeado em páginas na memória física ou em disco. | Y1P3 |
| **Modelo OSI (OSI)** | OSI reference model | Redes | Modelo de referência da ISO com 7 camadas (física, enlace, rede, transporte, sessão, apresentação, aplicação). | Y1P1 |
| **Monitoramento** | Monitoring | Resposta a Incidentes | Coleta contínua de métricas e eventos para detectar falhas ou anomalias. | Y1P4 |
| **Máscara curinga** | Wildcard mask | Redes | Máscara usada em ACLs e no OSPF em que 0 = bit deve coincidir e 1 = bit ignorado (o inverso da máscara de sub-rede). | Y1P1 |
| **Máscara de tamanho variável (VLSM)** | Variable Length Subnet Mask | Redes | Divisão de um bloco em sub-redes de tamanhos diferentes conforme a necessidade de cada uma. | Y1P1 |
| **Módulo** | Module | Desenvolvimento | Arquivo .py com funções e variáveis que pode ser importado por outros programas. | Y1P4 |
| **Módulos de autenticação plugáveis (PAM)** | Pluggable Authentication Modules | Sistemas | Framework modular de autenticação do Linux (complexidade de senha, bloqueio após falhas etc.). | Y1P2 |

## N

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Negação de serviço (DoS / DDoS)** | Denial of Service | Ameaças e Ataques | Ataque que esgota recursos de um serviço ou rede para torná-lo indisponível; DDoS usa muitas origens ao mesmo tempo. | Y1P1 |
| **Nessus** | Nessus | GRC | Scanner de vulnerabilidades comercial da Tenable; a versão Essentials é gratuita e limitada. | Y1P4 |
| **Não repúdio** | Non-repudiation | GRC | Garantia de que o autor de uma ação não consegue negar depois que a realizou. | Y1P1 |

## O

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Objeto de política de grupo (GPO)** | Group Policy Object | Sistemas | Conjunto de configurações aplicadas a usuários e computadores do domínio via AD. | Y1P3 |
| **OpenVAS (OpenVAS / GVM)** | Open Vulnerability Assessment Scanner | GRC | Scanner de vulnerabilidades open source do Greenbone Vulnerability Management. | Y1P4 |
| **OpenVPN** | OpenVPN | Redes | VPN de código aberto baseada em SSL/TLS, flexível e muito usada em acesso remoto. | Y1P1 |

## P

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Padrão avançado de criptografia (AES)** | Advanced Encryption Standard | Criptografia | Cifra de bloco simétrica padrão (FIPS 197) com chaves de 128, 192 ou 256 bits. | Y1P4 |
| **Padrão de criptografia de dados (DES)** | Data Encryption Standard | Criptografia | Cifra de bloco simétrica antiga com chave efetiva de 56 bits; hoje é considerada insegura. | Y1P4 |
| **Paginação** | Paging | Sistemas | Divisão da memória em páginas de tamanho fixo mapeadas pela tabela de páginas. | Y1P3 |
| **PAP / CHAP / MS-CHAPv2 (PAP / CHAP)** | Password / Challenge-Handshake Authentication Protocol | Redes | Protocolos de autenticação de acesso remoto: PAP envia senha em texto claro; CHAP e MS-CHAPv2 usam desafio-resposta. | Y1P3 |
| **Parâmetros posicionais** | Positional parameters | Desenvolvimento | Argumentos passados ao script, acessados como $1, $2…, $# (quantidade) e $@ (todos). | Y1P4 |
| **Permissões de arquivo** | File permissions (rwx) | Sistemas | Controle de leitura, escrita e execução para dono, grupo e outros, em notação simbólica ou octal. | Y1P2 |
| **Pilha dupla** | Dual-stack | Redes | Método de transição em que equipamentos rodam IPv4 e IPv6 ao mesmo tempo. | Y1P1 |
| **Pilha TCP/IP (TCP/IP)** | TCP/IP stack | Redes | Arquitetura de protocolos usada na Internet, com 4 camadas: acesso à rede, internet, transporte e aplicação. | Y1P1 |
| **Pipe** | Pipe | Sistemas | Operador | que envia a saída de um comando como entrada do próximo. | Y1P2 |
| **Ponto de acesso não autorizado (Rogue AP)** | Rogue access point | Ameaças e Ataques | AP instalado na rede sem autorização, abrindo uma porta de entrada. | Y1P1 |
| **Port scanner** | Port scanner | Ameaças e Ataques | Ferramenta que testa portas de um host para descobrir quais serviços estão abertos. | Y1P4 |
| **Primeiro o caminho mais curto (OSPF)** | Open Shortest Path First | Redes | IGP de estado de enlace (link-state) que usa o algoritmo de Dijkstra e organiza a rede em áreas (área 0 = backbone). | Y1P1 |
| **Princípio do menor privilégio (PoLP)** | Principle of least privilege | GRC | Dar a cada usuário ou processo apenas as permissões estritamente necessárias. | Y1P2 |
| **Processamento de loopback** | Loopback processing | Sistemas | Modo de GPO que aplica configurações de usuário conforme o computador onde ele faz logon. | Y1P3 |
| **Processo (PID)** | Process (PID) | Sistemas | Programa em execução, identificado por um número (PID). | Y1P2 |
| **Protocolo de autenticação extensível (EAP)** | Extensible Authentication Protocol | Criptografia | Framework de autenticação que suporta certificados, tokens e PEAP; base do 802.1X. | Y1P3 |
| **Protocolo de borda (BGP)** | Border Gateway Protocol | Redes | Protocolo de vetor de caminho usado entre sistemas autônomos; é o roteamento da Internet. | Y1P1 |
| **Protocolo de configuração dinâmica de hosts (DHCP)** | Dynamic Host Configuration Protocol | Redes | Serviço que entrega IP, máscara, gateway e DNS automaticamente aos clientes. | Y1P3 |
| **Protocolo de controle de transmissão (TCP)** | Transmission Control Protocol | Redes | Protocolo de transporte orientado a conexão, com three-way handshake, confirmação e ordenação. | Y1P4 |
| **Protocolo de datagrama de usuário (UDP)** | User Datagram Protocol | Redes | Protocolo de transporte sem conexão e sem garantia de entrega; leve e rápido. | Y1P4 |
| **Protocolo de transferência de arquivos (FTP)** | File Transfer Protocol | Redes | Protocolo de transferência de arquivos (TCP 21) sem criptografia; FTPS adiciona TLS. | Y1P2 |
| **Protocolo de transferência de hipertexto (HTTP)** | Hypertext Transfer Protocol | Redes | Protocolo de aplicação da Web, baseado em requisição/resposta (métodos GET, POST etc.). | Y1P1 |
| **Protocolo Spanning Tree (STP)** | Spanning Tree Protocol | Redes | Protocolo que bloqueia caminhos redundantes entre switches para evitar loops de camada 2. | Y1P1 |
| **Python** | Python | Desenvolvimento | Linguagem interpretada, de alto nível e multiparadigma, muito usada em automação de segurança e ciência de dados. | Y1P4 |

## R

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **RADIUS (RADIUS)** | Remote Authentication Dial-In User Service | Redes | Protocolo AAA (UDP 1812/1813) que combina autenticação e autorização e cifra só a senha; ideal para acesso à rede. | Y1P1 |
| **Ransomware** | Ransomware | Ameaças e Ataques | Malware que cifra os dados (ou o disco inteiro) e exige resgate para liberar. | Y1P1 |
| **Rede de longa distância (WAN)** | Wide Area Network | Redes | Rede que interliga LANs em grandes áreas geográficas. | Y1P1 |
| **Rede local (LAN)** | Local Area Network | Redes | Rede que cobre uma área pequena (casa, andar, empresa) e termina no roteador/gateway. | Y1P1 |
| **Rede local virtual (VLAN)** | Virtual LAN | Redes | Segmentação lógica de um switch em domínios de broadcast separados. | Y1P1 |
| **Rede privada virtual (VPN)** | Virtual Private Network | Redes | Túnel cifrado sobre uma rede pública que liga usuários ou sites como se estivessem na mesma rede. | Y1P1 |
| **Redirecionamento** | Redirection | Sistemas | Envio de entradas ou saídas para arquivos (>, >>, <, 2>&1). | Y1P2 |
| **Registros DNS (RR)** | DNS resource records | Redes | Entradas de uma zona: SOA, NS, A, AAAA, CNAME, MX, PTR, SRV etc. | Y1P3 |
| **Risco** | Risk | GRC | Possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto a um ativo; costuma ser estimado como probabilidade × impacto. | Y1P4 |
| **Risco residual** | Residual risk | GRC | Risco que sobra depois de aplicados os controles. | Y1P4 |
| **Roteamento dinâmico** | Dynamic routing | Redes | Roteadores trocam informações por protocolos e montam as rotas automaticamente. | Y1P1 |
| **Roteamento e acesso remoto (RRAS)** | Routing and Remote Access Service | Redes | Função do Windows Server que provê VPN, NAT e roteamento. | Y1P3 |
| **Roteamento estático** | Static routing | Redes | Rotas configuradas manualmente pelo administrador. | Y1P1 |
| **Roteamento sem classes (CIDR)** | Classless Inter-Domain Routing | Redes | Notação e técnica que define a máscara pelo número de bits de rede (/n), sem depender das classes. | Y1P1 |
| **rsync** | rsync | Sistemas | Ferramenta de cópia e sincronização incremental, local ou remota (via SSH). | Y1P2 |
| **rsyslog** | rsyslog | Forense | Serviço que recebe e grava logs em arquivos de texto ou os encaminha para servidores remotos/SIEM. | Y1P2 |

## S

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **sed** | Stream editor | Sistemas | Editor de fluxo para substituir, apagar ou extrair texto por padrão. | Y1P2 |
| **Segurança de porta** | Port Security | Redes | Limita quais e quantos MACs podem usar uma porta do switch e define a ação em caso de violação. | Y1P1 |
| **Server Message Block (SMB)** | Server Message Block | Redes | Protocolo de compartilhamento de arquivos e impressoras (comum no Windows; Samba no Linux). | Y1P2 |
| **Servidor de políticas de rede (NPS)** | Network Policy Server | Redes | Implementação de RADIUS da Microsoft para autenticar e autorizar VPN, Wi-Fi e 802.1X. | Y1P3 |
| **Servidor web** | Web server | Desenvolvimento | Software que atende requisições HTTP/HTTPS e entrega páginas ou APIs. | Y1P2 |
| **Serviços de Domínio do Active Directory (AD DS)** | Active Directory Domain Services | Sistemas | Função do Windows Server que transforma o servidor em controlador de domínio. | Y1P3 |
| **Serviços de informações da Internet (IIS)** | Internet Information Services | Desenvolvimento | Servidor web da Microsoft. | Y1P3 |
| **SFTP / SCP (SFTP / SCP)** | SSH File Transfer Protocol / Secure Copy | Redes | Transferência de arquivos cifrada que usa o canal SSH. | Y1P2 |
| **Shebang** | Shebang | Desenvolvimento | Primeira linha de um script (#!) que indica qual interpretador deve executá-lo. | Y1P4 |
| **Shell** | Shell | Sistemas | Interpretador de comandos entre o usuário e o kernel; o Bash é o mais comum no Linux. | Y1P2 |
| **Shell Script** | Shell script | Desenvolvimento | Arquivo de comandos de shell executado em sequência para automatizar tarefas. | Y1P4 |
| **Shell seguro (SSH)** | Secure Shell | Redes | Protocolo de acesso remoto cifrado (TCP 22), com autenticação por senha ou chave. | Y1P2 |
| **Sistema autônomo (AS)** | Autonomous System | Redes | Conjunto de redes sob uma única política de roteamento, identificado por um número (ASN). | Y1P1 |
| **Sistema de arquivos** | Filesystem | Sistemas | Estrutura que organiza como os dados são gravados no disco. | Y1P2 |
| **Sistema de arquivos de rede (NFS)** | Network File System | Redes | Protocolo para compartilhar diretórios pela rede, montados como se fossem locais. | Y1P2 |
| **Sistema de detecção de intrusão (IDS)** | Intrusion Detection System | Resposta a Incidentes | Monitora o tráfego ou o host e gera alertas sobre atividade suspeita, sem bloquear (passivo). | Y1P1 |
| **Sistema de nomes de domínio (DNS)** | Domain Name System | Redes | Serviço que traduz nomes em endereços IP de forma hierárquica e distribuída. | Y1P1 |
| **Sistema de pontuação de vulnerabilidades (CVSS)** | Common Vulnerability Scoring System | GRC | Padrão do FIRST que dá uma nota de 0 a 10 à gravidade de uma vulnerabilidade. | Y1P2 |
| **Sistema de prevenção de intrusão (IPS)** | Intrusion Prevention System | Resposta a Incidentes | Fica em linha (inline) e bloqueia em tempo real o tráfego identificado como malicioso. | Y1P1 |
| **Sistema operacional (SO / OS)** | Operating system | Sistemas | Software que gerencia o hardware e oferece abstrações (processos, arquivos, memória) aos programas. | Y1P3 |
| **Socket** | Socket | Redes | Ponto final de comunicação em rede (IP + porta + protocolo) usado pelos programas para trocar dados. | Y1P4 |
| **ss** | Socket statistics | Redes | Lista sockets e portas em escuta ou conexões ativas, junto com o processo dono. | Y1P2 |
| **sudo** | Superuser do | Sistemas | Executa um comando com privilégios de outro usuário (normalmente root), com registro em log. | Y1P2 |
| **SUID (SUID)** | Set User ID | Sistemas | Bit especial que faz um executável rodar com o privilégio do dono do arquivo; alvo comum de escalada de privilégio. | Y1P2 |
| **Superusuário** | Superuser (root) | Sistemas | Conta com privilégio total no sistema (UID 0); deve ser usada só quando necessário. | Y1P2 |
| **sysctl** | sysctl | Sistemas | Comando para ler e ajustar parâmetros do kernel em tempo de execução. | Y1P2 |
| **systemd** | systemd | Sistemas | Sistema de inicialização e gerenciador de serviços (units), dependências e logs do Linux moderno. | Y1P2 |

## T

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Tabela de endereços MAC (CAM)** | MAC address table (CAM table) | Redes | Tabela do switch que associa endereços MAC às portas para encaminhar quadros. | Y1P1 |
| **TACACS+ (TACACS+)** | Terminal Access Controller Access-Control System Plus | Redes | Protocolo AAA (TCP/49) que cifra o pacote inteiro e separa as três funções; ideal para administrar equipamentos. | Y1P1 |
| **tcpdump** | tcpdump | Redes | Capturador de pacotes em linha de comando; grava PCAPs para análise. | Y1P2 |
| **Telnet** | Telnet | Redes | Protocolo antigo de acesso remoto (TCP 23) que trafega tudo em texto claro. | Y1P2 |
| **Teste de intrusão (Pentest)** | Penetration test | Ameaças e Ataques | Ataque simulado e autorizado que explora vulnerabilidades para provar o impacto. | Y1P4 |
| **Texto claro** | Cleartext | Ameaças e Ataques | Dados transmitidos sem criptografia, legíveis por quem capturar o tráfego. | Y1P2 |
| **Thread** | Thread | Sistemas | Linha de execução dentro de um processo; threads compartilham a memória do processo. | Y1P3 |
| **Three-way handshake** | Three-way handshake | Redes | Estabelecimento de conexão TCP: SYN → SYN-ACK → ACK. | Y1P4 |
| **Tomada de conta (ATO)** | Account takeover | Ameaças e Ataques | Uso de credenciais legítimas roubadas para controlar a conta de uma vítima. | Y1P1 |
| **Tradução de endereços de rede (NAT)** | Network Address Translation | Redes | Troca de endereços IP (geralmente privado→público) na borda da rede. | Y1P1 |
| **Tratamento de risco** | Risk treatment | GRC | Decisão sobre um risco: mitigar, transferir, evitar ou aceitar. | Y1P4 |
| **Tronco 802.1Q** | 802.1Q trunk | Redes | Link que transporta várias VLANs entre switches, marcando os quadros com a tag da VLAN. | Y1P1 |
| **Tríade CID (CID / CIA)** | CIA triad | GRC | Os três pilares da segurança da informação: confidencialidade, integridade e disponibilidade. | Y1P1 |

## U

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Unidade organizacional (OU)** | Organizational Unit | Sistemas | Contêiner do AD que organiza objetos e recebe GPOs e delegação de controle. | Y1P3 |

## V

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Varredura de portas** | Port scan | Ameaças e Ataques | Sondagem de hosts para descobrir quais estão ativos e quais serviços/portas estão abertos; costuma ser o primeiro passo de um ataque. | Y1P1 |
| **Vetor de ataque** | Attack vector | Ameaças e Ataques | Caminho ou meio usado pelo atacante para chegar ao alvo. | Y1P1 |
| **vim** | Vi IMproved | Sistemas | Editor de texto do terminal com modos normal, inserção e comando. | Y1P2 |
| **Vulnerabilidade** | Vulnerability | GRC | Fraqueza em sistema, processo ou pessoa que pode ser explorada por uma ameaça. | Y1P4 |
| **Vulnerabilidades e exposições comuns (CVE)** | Common Vulnerabilities and Exposures | GRC | Catálogo público de vulnerabilidades conhecidas, mantido pelo MITRE, com um ID único para cada uma. | Y1P2 |

## W

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Windows Server** | Windows Server | Sistemas | Linha de sistemas operacionais da Microsoft para servidores, com funções como AD, DNS, DHCP, IIS e Hyper-V. | Y1P3 |
| **Windows Server Update Services (WSUS)** | Windows Server Update Services | Sistemas | Serviço que centraliza aprovação e distribuição de atualizações Microsoft na rede. | Y1P3 |
| **Wordlist** | Wordlist | Ameaças e Ataques | Lista de senhas ou palavras usadas em ataques de força bruta ou dicionário. | Y1P4 |
| **WPA2 (WPA2)** | Wi-Fi Protected Access 2 | Criptografia | Padrão de segurança Wi-Fi com AES-CCMP; modos Personal (PSK) e Enterprise (802.1X/RADIUS). | Y1P1 |
| **WPA3 (WPA3)** | Wi-Fi Protected Access 3 | Criptografia | Sucessor do WPA2 com SAE, forward secrecy e opção de 192 bits no modo Enterprise. | Y1P1 |

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
