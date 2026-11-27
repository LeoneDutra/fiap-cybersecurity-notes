# Year 1 · Phase 1 — Redes e Segurança de Redes (Networking & Network Security)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A primeira fase constrói a **base**: o que é segurança da informação e, principalmente, **como uma rede funciona de ponta a ponta**. Para defender uma rede, primeiro é preciso entender como ela funciona. O percurso começa nos conceitos de cibersegurança e no cenário de ameaças. Depois vêm os modelos de referência (OSI e TCP/IP), os equipamentos, os switches e VLANs, o endereçamento IPv4/IPv6 e o roteamento (estático, OSPF, BGP). Por último, entram os **controles de segurança de rede**: ACL, AAA (TACACS+/RADIUS), proteções de camada 2, Wi‑Fi seguro (WPA2/WPA3), VPN (IPsec, OpenVPN) e firewall/IDS/IPS.

A ideia central: **cada camada da rede tem seus ataques e seus controles**. Quem sabe em qual camada um problema acontece sabe onde olhar e qual defesa aplicar.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Mostra a metodologia baseada em projetos (Project Based Learning) e o roteiro da fase: primeiro a fundação de redes, depois a segurança. |
| 2 | Fundamentos de Segurança da Informação | Cibersegurança vai além da tecnologia: envolve gestão, risco e continuidade de negócio. Apresenta os tipos de incidente (DoS, invasão, ataque web/defacement, scan, fraude), casos como WannaCry (SMBv1/EternalBlue) e Petya (ataque à MBR), vetores de ataque (malware, account takeover, ataques direcionados), motivações (cibercrime, hacktivismo) e o enquadramento legal no Brasil (Lei 12.737/2012, extorsão, ameaça). Cita o papel do CERT.br. |
| 3 | Introdução às redes de comunicação | Uma rede é um conjunto de dispositivos interligados que trocam informações e compartilham recursos. Conta a história da ARPANET à Internet e à IoT, explica por que protocolos são necessários e classifica as redes por alcance (PAN, LAN, MAN, WMAN, WAN). |
| 4 | Arquiteturas e modelos de referência | Modelo OSI (7 camadas) × pilha TCP/IP (4 camadas). Encapsulamento passo a passo (aplicação → transporte → rede → acesso à rede) e desencapsulamento no destino. |
| 5 | Dispositivos e meios de transmissão | Dispositivos finais (cliente/servidor) e intermediários (switch L2/L3, roteador, access point, roteador wireless), além dos meios físicos: par trançado, fibra óptica e sem fio. |
| 6 | Switches | Endereço MAC e tabela MAC (CAM), half/full‑duplex, interfaces L3 (SVI), VLANs (por porta, por MAC, por protocolo), trunking (802.1Q) e Spanning Tree (STP) contra loops. |
| 7 | Endereçamento IPv4 | Estrutura de 32 bits, classes A–E, faixas privadas (RFC 1918), loopback, CIDR, sub‑redes e VLSM. |
| 8 | IPv6 e transição (o arquivo tem título de roteamento) | Endereço de 128 bits em hexadecimal, SLAAC × DHCPv6 (stateful), exemplo de OSPFv3, métodos de transição: dual‑stack, tunelamento e NAT64. |
| 9 | Roteamento estático/dinâmico, OSPF e BGP | Estático × dinâmico, laboratório com RIP e EIGRP, OSPF (link‑state, áreas, tipos de roteador, LSAs, sumarização, autenticação, troubleshooting) e BGP (AS, iBGP × eBGP, atributos AS‑PATH/NEXT‑HOP/MED, políticas com route‑maps). |
| 10 | Endereçamento IPv6 e segurança | Distribuição de endereços (IANA/RIRs), comparação com IPv4, IPsec no IPv6, por que varrer uma sub‑rede /64 inteira é inviável e cuidados com firewall em IPv6. |
| 11 | Camada de aplicação | Modelo cliente/servidor, WWW e HTTP (formato das mensagens), DNS e DDNS (componentes e tipos de consulta), FTP e uma introdução a VPN/tunelamento. |
| 12 | Segurança de redes | Tríade CID (confidencialidade, integridade, disponibilidade), autenticação, autorização e não repúdio. ACL padrão: operação, máscara curinga (wildcard mask) e o `deny any` implícito no fim da lista. |
| 13 | Wireless e WPA/WPA2/WPA3 | Bandas de 2,4, 5 e 6 GHz, padrões 802.11 (a/b/g/n/ac/ax), SSID, modos infraestrutura × ad‑hoc. Ameaças: MitM, rogue AP, evil twin, wardriving, sniffing. Evolução WEP → WPA (TKIP) → WPA2 (AES/CCMP, Personal × Enterprise) → WPA3 (SAE, forward secrecy, 192 bits no modo Enterprise). |
| 14 | AAA (TACACS+ e RADIUS) | Autenticação, autorização e auditoria (accounting). O TACACS+ usa TCP, cifra o pacote inteiro e autoriza comando a comando (ideal para administrar equipamentos). O RADIUS usa UDP, cifra só a senha e junta autenticação com autorização (ideal para acesso à rede/802.1X). |
| 15 | Segurança na camada 2 | DHCP Snooping (portas confiáveis × não confiáveis), Dynamic ARP Inspection (contra ARP spoofing), Port Security (limite de MACs e ação em violação), NAC, segmentação e proteção contra loops. |
| 16 | ACLs em detalhe | Tipos de ACL: padrão, estendida, nomeada, reflexiva, dinâmica e por horário (time‑based). Componentes, posicionamento (estendida perto da origem, padrão perto do destino) e cenários práticos. |
| 17 | VPN | Como uma VPN funciona (túnel, criptografia, autenticação). Tipos: pessoal, acesso remoto, móvel e site‑to‑site. Protocolos: PPTP (obsoleto), IPsec (modos transporte e túnel, IKE/ISAKMP) e OpenVPN (SSL/TLS). Laboratórios com túnel IPsec e IPsec + GRE. |
| 18 | Firewall, IDS e IPS | Tipos de firewall: filtragem estática de pacotes, circuit‑level, stateful, proxy, NGFW e híbrido. IDS (NIDS, HIDS, PIDS, APIDS, híbrido), detecção por assinatura × por anomalia, técnicas de evasão, IDS × IPS, WAF e CDN. |

## 🔑 Conceitos-chave

- **Tríade CID (CIA triad)**: confidencialidade, integridade e disponibilidade. Junto com autenticação, autorização e não repúdio, forma o vocabulário básico de toda a área.
- **Camadas e encapsulamento**: cada camada acrescenta seu cabeçalho. A PDU muda de nome conforme a camada: dados → segmento → pacote → quadro → bits. Para diagnosticar ou investigar, comece perguntando "em que camada está?".
- **Endereçamento**: o MAC (camada 2) identifica a placa de rede dentro do enlace. O IP (camada 3) identifica o host entre redes. A porta (camada 4) identifica o serviço.
- **Sub‑redes e CIDR/VLSM**: dividir um bloco de endereços conforme a necessidade. A máscara define quantos bits são de rede e quantos são de host (hosts úteis = 2ⁿ − 2).
- **Switching × routing**: o switch encaminha quadros pela tabela MAC dentro da LAN. O roteador encaminha pacotes pela tabela de rotas entre redes.
- **Segmentação**: VLANs, sub‑redes e ACLs reduzem o domínio de broadcast e a superfície de ataque, e dificultam o movimento lateral (lateral movement).
- **IGP × EGP**: OSPF é um protocolo de estado de enlace (link‑state) usado dentro de um sistema autônomo (AS). BGP é um protocolo de vetor de caminho (path‑vector) usado entre ASs, ou seja, é a "cola" da Internet.
- **Defesa em profundidade (defense in depth)**: camada 2 (port security, DAI, DHCP snooping) + camada 3/4 (ACL, firewall stateful) + camada 7 (NGFW, WAF) + monitoramento (IDS/IPS) + acesso (AAA, VPN, WPA3).
- **Stateless × stateful**: uma ACL avalia cada pacote isoladamente. Um firewall stateful acompanha o estado da conexão e libera automaticamente o tráfego de retorno.
- **Assinatura × anomalia**: a detecção por assinatura é precisa contra ameaças já conhecidas. A detecção por anomalia pega o desconhecido, mas gera mais falsos positivos.

## 🛠️ Ferramentas e comandos

**Ferramenta principal:** Cisco Packet Tracer (simulação de topologias). Também aparecem `ping`, `traceroute`/`tracert`, Wireshark e clientes OpenVPN.

Comandos Cisco IOS praticados (exemplos genéricos):

```text
enable / configure terminal / end / write memory
interface g0/0 → ip address 10.0.0.1 255.255.255.0 → no shutdown
ip route 0.0.0.0 0.0.0.0 <next-hop>                      ! rota estática / default
router ospf 1 → router-id 1.1.1.1 → network 10.0.0.0 0.0.0.255 area 0
ipv6 unicast-routing → ipv6 router ospf 1                ! OSPFv3
router bgp 65001 → neighbor <ip> remote-as 65002
access-list 10 permit 192.168.10.0 0.0.0.255             ! ACL padrão
ip access-list extended WEB → permit tcp any host <ip> eq 443
interface g0/1 → ip access-group 10 out
switchport mode access / switchport port-security maximum 2
switchport port-security violation shutdown
ip dhcp snooping / ip dhcp snooping vlan 10 / ip dhcp snooping trust
ip arp inspection vlan 10
aaa new-model / tacacs-server host <ip> key <chave> / radius-server host <ip> key <chave>
crypto isakmp policy 10 → encryption aes / hash sha / authentication pre-share / group 2
crypto ipsec transform-set TS esp-aes esp-sha-hmac
crypto map VPN 10 ipsec-isakmp → set peer <ip> / set transform-set TS / match address 110
show ip route | show ip ospf neighbor | show ip bgp summary | show access-lists
show port-security interface f0/1 | show ip dhcp snooping binding | show crypto isakmp sa
```

## ❓ Perguntas de revisão

1. **Qual a diferença entre o modelo OSI e o TCP/IP?**
   O OSI é um modelo de referência com 7 camadas. O TCP/IP é a pilha usada de fato, com 4 camadas: as camadas de aplicação, apresentação e sessão do OSI viram "aplicação", e as camadas física e de enlace viram "acesso à rede".
2. **Quantos hosts utilizáveis existem em uma /26?**
   Sobram 6 bits de host: 2⁶ = 64 endereços, menos o de rede e o de broadcast, o que dá 62 hosts.
3. **Por que o WannaCry se espalhou tão rápido?**
   Porque era um worm: explorava uma falha no SMBv1 (EternalBlue) e se propagava sozinho pela rede, sem depender de phishing. Desativar o SMBv1 e aplicar o patch MS17‑010 resolvia.
4. **OSPF × BGP: quando usar cada um?**
   O OSPF (IGP, link‑state, algoritmo de Dijkstra) roteia dentro da organização ou AS e converge rápido. O BGP (EGP, path‑vector) troca rotas entre ASs e permite políticas com atributos como AS‑PATH e MED.
5. **O que o DHCP Snooping e o DAI fazem, e como um ajuda o outro?**
   O DHCP Snooping bloqueia servidores DHCP falsos em portas não confiáveis e monta uma tabela de vínculos IP↔MAC↔porta. O DAI usa essa tabela para descartar respostas ARP falsificadas, o que impede ARP spoofing e ataques MitM.
6. **TACACS+ ou RADIUS para controlar quem roda comandos em switches?**
   TACACS+. Ele separa as funções de AAA, cifra o pacote inteiro (sobre TCP 49) e autoriza comando a comando. O RADIUS é melhor para acesso à rede (802.1X, VPN, Wi‑Fi).
7. **O que o WPA3 traz de novo em relação ao WPA2?**
   O SAE (Simultaneous Authentication of Equals) substitui o PSK e resiste a ataques de dicionário offline. Também traz forward secrecy (capturar o tráfego hoje não permite decifrá‑lo depois) e criptografia de 192 bits no modo Enterprise.
8. **Onde posicionar uma ACL estendida e uma ACL padrão?**
   A estendida fica perto da origem, porque filtra por origem, destino e porta e descarta o tráfego cedo. A padrão fica perto do destino, porque filtra só pela origem e, colocada perto da origem, bloquearia acessos legítimos.
9. **IDS × IPS?**
   O IDS monitora uma cópia do tráfego (SPAN/TAP) e gera alertas, de forma passiva. O IPS fica em linha (inline) e bloqueia o tráfego malicioso em tempo real. A contrapartida: um falso positivo no IPS derruba tráfego legítimo.
10. **IPsec em modo túnel × modo transporte?**
    No modo transporte, só o payload é protegido e o cabeçalho IP original é mantido (uso host a host). No modo túnel, o pacote inteiro é encapsulado em um novo cabeçalho IP (padrão em VPN site‑to‑site entre gateways).

## 💼 Conexão com o mercado

- **SOC (analista N1/N2)**: os alertas de firewall, IDS/IPS e proxy só fazem sentido para quem entende IP, portas, protocolos e fluxo TCP. Port scan, ARP spoofing, DoS e beaconing estão entre os eventos mais comuns na triagem. Saber ler uma ACL ou regra de firewall e um PCAP é rotina.
- **CompTIA Security+ (SY0‑701)**: esta fase cobre boa parte do domínio de *Security Architecture* (segmentação, VLAN, firewall, IDS/IPS, VPN, 802.1X/RADIUS, WPA3) e parte de *Threats, Vulnerabilities & Mitigations* (MitM, rogue AP, evil twin, DoS, ransomware). A tríade CID e o AAA aparecem em *General Security Concepts*.
- **Pós Tech em IA para Segurança**: detecção por anomalia é a porta de entrada para machine learning em segurança, como NDR e modelos que aprendem o "normal" do tráfego (NetFlow/Zeek) para apontar desvios. Para criar features de tráfego de rede, é preciso dominar exatamente o que esta fase ensina.

## 📖 Termos da fase

Tríade CID (CIA triad) · Não repúdio (non‑repudiation) · DoS/DDoS · Ransomware · Vetor de ataque (attack vector) · Hacktivismo (hacktivism) · Port scan · Modelo OSI · TCP/IP · Encapsulamento (encapsulation) · LAN/WAN · Endereço MAC · VLAN · Trunk 802.1Q · STP · IPv4 · CIDR · VLSM · IPv6 · SLAAC · NAT · Roteamento estático/dinâmico · OSPF · BGP · Sistema autônomo (AS) · DNS · HTTP · ACL · Máscara curinga (wildcard mask) · AAA · TACACS+ · RADIUS · DHCP Snooping · DAI · ARP spoofing · Port Security · WPA2 · WPA3 · SAE · Evil twin · Rogue AP · VPN · IPsec · OpenVPN · Firewall stateful · NGFW · IDS · IPS · WAF

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
