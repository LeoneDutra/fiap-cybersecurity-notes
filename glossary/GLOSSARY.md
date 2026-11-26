# 📖 Glossary (PT ↔ EN)

> Generated from `glossary.csv` by `scripts/build_glossary.py`. Edit the CSV, not this file.

**56 terms**

[A](#a) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [V](#v) · [W](#w)

## A

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Autenticação simultânea de iguais (SAE)** | Simultaneous Authentication of Equals | Criptografia | Troca de chaves do WPA3-Personal que substitui o PSK e resiste a ataques de dicionário offline. | Y1P1 |
| **Autenticação, autorização e auditoria (AAA)** | Authentication, Authorization and Accounting | GRC | Framework que controla quem acessa (autenticação), o que pode fazer (autorização) e registra o que fez (accounting). | Y1P1 |
| **Autoconfiguração sem estado (SLAAC)** | Stateless Address Autoconfiguration | Redes | Mecanismo IPv6 em que o host gera o próprio endereço a partir do prefixo anunciado pelo roteador. | Y1P1 |

## D

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **DHCP Snooping** | DHCP Snooping | Redes | Recurso do switch que só aceita respostas DHCP de portas confiáveis e monta uma tabela de vínculos IP-MAC-porta. | Y1P1 |

## E

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Encapsulamento** | Encapsulation | Redes | Cada camada acrescenta seu cabeçalho aos dados da camada de cima antes de enviar; o destino faz o processo inverso. | Y1P1 |
| **Endereço IPv4 (IPv4)** | IPv4 address | Redes | Endereço lógico de 32 bits escrito em 4 octetos decimais. | Y1P1 |
| **Endereço IPv6 (IPv6)** | IPv6 address | Redes | Endereço de 128 bits em hexadecimal, em 8 grupos separados por dois-pontos. | Y1P1 |
| **Endereço MAC (MAC)** | MAC address | Redes | Endereço físico de 48 bits da interface de rede, usado na camada 2. | Y1P1 |
| **Endereços privados** | Private addressing (RFC 1918) | Redes | Faixas IPv4 reservadas para uso interno, não roteáveis na Internet: 10/8, 172.16/12, 192.168/16. | Y1P1 |
| **Envenenamento de ARP** | ARP spoofing / ARP poisoning | Ameaças e Ataques | Envio de respostas ARP falsas para associar o MAC do atacante ao IP de outro host (ex.: gateway), permitindo MitM. | Y1P1 |

## F

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Firewall com estado** | Stateful firewall | Redes | Firewall que acompanha o estado das conexões e libera automaticamente o tráfego de retorno. | Y1P1 |
| **Firewall de aplicação web (WAF)** | Web Application Firewall | Desenvolvimento | Filtra requisições HTTP/HTTPS para proteger aplicações web (SQLi, XSS etc.). | Y1P1 |
| **Firewall de próxima geração (NGFW)** | Next-Generation Firewall | Redes | Firewall que soma inspeção de aplicação (camada 7), IPS integrado e controle por usuário/aplicação. | Y1P1 |

## G

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Gêmeo maligno** | Evil twin | Ameaças e Ataques | Ponto de acesso falso com o mesmo SSID de uma rede legítima para atrair vítimas. | Y1P1 |

## H

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Hacktivismo** | Hacktivism | Ameaças e Ataques | Ataques motivados por causas políticas ou sociais, normalmente defacement ou DoS. | Y1P1 |
| **Homem no meio (MitM)** | Man-in-the-Middle | Ameaças e Ataques | Atacante se posiciona entre duas partes para interceptar ou alterar a comunicação. | Y1P1 |

## I

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Inspeção dinâmica de ARP (DAI)** | Dynamic ARP Inspection | Redes | Valida mensagens ARP contra a tabela do DHCP Snooping e descarta as falsificadas. | Y1P1 |
| **IPsec (IPsec)** | Internet Protocol Security | Criptografia | Conjunto de protocolos (IKE, ESP, AH) que cifra e autentica pacotes IP; modos transporte e túnel. | Y1P1 |

## L

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Lista de controle de acesso (ACL)** | Access Control List | Redes | Lista ordenada de regras permit/deny aplicada a uma interface para filtrar tráfego; termina com um deny implícito. | Y1P1 |

## M

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Modelo OSI (OSI)** | OSI reference model | Redes | Modelo de referência da ISO com 7 camadas (física, enlace, rede, transporte, sessão, apresentação, aplicação). | Y1P1 |
| **Máscara curinga** | Wildcard mask | Redes | Máscara usada em ACLs e no OSPF em que 0 = bit deve coincidir e 1 = bit ignorado (o inverso da máscara de sub-rede). | Y1P1 |
| **Máscara de tamanho variável (VLSM)** | Variable Length Subnet Mask | Redes | Divisão de um bloco em sub-redes de tamanhos diferentes conforme a necessidade de cada uma. | Y1P1 |

## N

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Negação de serviço (DoS / DDoS)** | Denial of Service | Ameaças e Ataques | Ataque que esgota recursos de um serviço ou rede para torná-lo indisponível; DDoS usa muitas origens ao mesmo tempo. | Y1P1 |
| **Não repúdio** | Non-repudiation | GRC | Garantia de que o autor de uma ação não consegue negar depois que a realizou. | Y1P1 |

## O

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **OpenVPN** | OpenVPN | Redes | VPN de código aberto baseada em SSL/TLS, flexível e muito usada em acesso remoto. | Y1P1 |

## P

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Pilha dupla** | Dual-stack | Redes | Método de transição em que equipamentos rodam IPv4 e IPv6 ao mesmo tempo. | Y1P1 |
| **Pilha TCP/IP (TCP/IP)** | TCP/IP stack | Redes | Arquitetura de protocolos usada na Internet, com 4 camadas: acesso à rede, internet, transporte e aplicação. | Y1P1 |
| **Ponto de acesso não autorizado (Rogue AP)** | Rogue access point | Ameaças e Ataques | AP instalado na rede sem autorização, abrindo uma porta de entrada. | Y1P1 |
| **Primeiro o caminho mais curto (OSPF)** | Open Shortest Path First | Redes | IGP de estado de enlace (link-state) que usa o algoritmo de Dijkstra e organiza a rede em áreas (área 0 = backbone). | Y1P1 |
| **Protocolo de borda (BGP)** | Border Gateway Protocol | Redes | Protocolo de vetor de caminho usado entre sistemas autônomos; é o roteamento da Internet. | Y1P1 |
| **Protocolo de transferência de hipertexto (HTTP)** | Hypertext Transfer Protocol | Redes | Protocolo de aplicação da Web, baseado em requisição/resposta (métodos GET, POST etc.). | Y1P1 |
| **Protocolo Spanning Tree (STP)** | Spanning Tree Protocol | Redes | Protocolo que bloqueia caminhos redundantes entre switches para evitar loops de camada 2. | Y1P1 |

## R

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **RADIUS (RADIUS)** | Remote Authentication Dial-In User Service | Redes | Protocolo AAA (UDP 1812/1813) que combina autenticação e autorização e cifra só a senha; ideal para acesso à rede. | Y1P1 |
| **Ransomware** | Ransomware | Ameaças e Ataques | Malware que cifra os dados (ou o disco inteiro) e exige resgate para liberar. | Y1P1 |
| **Rede de longa distância (WAN)** | Wide Area Network | Redes | Rede que interliga LANs em grandes áreas geográficas. | Y1P1 |
| **Rede local (LAN)** | Local Area Network | Redes | Rede que cobre uma área pequena (casa, andar, empresa) e termina no roteador/gateway. | Y1P1 |
| **Rede local virtual (VLAN)** | Virtual LAN | Redes | Segmentação lógica de um switch em domínios de broadcast separados. | Y1P1 |
| **Rede privada virtual (VPN)** | Virtual Private Network | Redes | Túnel cifrado sobre uma rede pública que liga usuários ou sites como se estivessem na mesma rede. | Y1P1 |
| **Roteamento dinâmico** | Dynamic routing | Redes | Roteadores trocam informações por protocolos e montam as rotas automaticamente. | Y1P1 |
| **Roteamento estático** | Static routing | Redes | Rotas configuradas manualmente pelo administrador. | Y1P1 |
| **Roteamento sem classes (CIDR)** | Classless Inter-Domain Routing | Redes | Notação e técnica que define a máscara pelo número de bits de rede (/n), sem depender das classes. | Y1P1 |

## S

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Segurança de porta** | Port Security | Redes | Limita quais e quantos MACs podem usar uma porta do switch e define a ação em caso de violação. | Y1P1 |
| **Sistema autônomo (AS)** | Autonomous System | Redes | Conjunto de redes sob uma única política de roteamento, identificado por um número (ASN). | Y1P1 |
| **Sistema de detecção de intrusão (IDS)** | Intrusion Detection System | Resposta a Incidentes | Monitora o tráfego ou o host e gera alertas sobre atividade suspeita, sem bloquear (passivo). | Y1P1 |
| **Sistema de nomes de domínio (DNS)** | Domain Name System | Redes | Serviço que traduz nomes em endereços IP de forma hierárquica e distribuída. | Y1P1 |
| **Sistema de prevenção de intrusão (IPS)** | Intrusion Prevention System | Resposta a Incidentes | Fica em linha (inline) e bloqueia em tempo real o tráfego identificado como malicioso. | Y1P1 |

## T

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Tabela de endereços MAC (CAM)** | MAC address table (CAM table) | Redes | Tabela do switch que associa endereços MAC às portas para encaminhar quadros. | Y1P1 |
| **TACACS+ (TACACS+)** | Terminal Access Controller Access-Control System Plus | Redes | Protocolo AAA (TCP/49) que cifra o pacote inteiro e separa as três funções; ideal para administrar equipamentos. | Y1P1 |
| **Tomada de conta (ATO)** | Account takeover | Ameaças e Ataques | Uso de credenciais legítimas roubadas para controlar a conta de uma vítima. | Y1P1 |
| **Tradução de endereços de rede (NAT)** | Network Address Translation | Redes | Troca de endereços IP (geralmente privado→público) na borda da rede. | Y1P1 |
| **Tronco 802.1Q** | 802.1Q trunk | Redes | Link que transporta várias VLANs entre switches, marcando os quadros com a tag da VLAN. | Y1P1 |
| **Tríade CID (CID / CIA)** | CIA triad | GRC | Os três pilares da segurança da informação: confidencialidade, integridade e disponibilidade. | Y1P1 |

## V

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **Varredura de portas** | Port scan | Ameaças e Ataques | Sondagem de hosts para descobrir quais estão ativos e quais serviços/portas estão abertos; costuma ser o primeiro passo de um ataque. | Y1P1 |
| **Vetor de ataque** | Attack vector | Ameaças e Ataques | Caminho ou meio usado pelo atacante para chegar ao alvo. | Y1P1 |

## W

| Termo (PT) | Term (EN) | Categoria | Definição | Fase |
|---|---|---|---|---|
| **WPA2 (WPA2)** | Wi-Fi Protected Access 2 | Criptografia | Padrão de segurança Wi-Fi com AES-CCMP; modos Personal (PSK) e Enterprise (802.1X/RADIUS). | Y1P1 |
| **WPA3 (WPA3)** | Wi-Fi Protected Access 3 | Criptografia | Sucessor do WPA2 com SAE, forward secrecy e opção de 192 bits no modo Enterprise. | Y1P1 |
