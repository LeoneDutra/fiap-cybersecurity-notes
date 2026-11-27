# Year 1 · Phase 6 — Criptografia, Análise de Tráfego e Ataques TCP/IP (Cryptography, Traffic Analysis & TCP/IP Attacks)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A sexta fase junta três pilares práticos do dia a dia de segurança. Primeiro, os **princípios de segurança da informação** (menor privilégio, defesa em profundidade, elo mais fraco, segregação de funções, ROSI) e a diferença entre *cybersecurity* e *information security*. Segundo, **criptografia** de ponta a ponta: da cifra de César e Enigma aos sistemas simétricos (DES, AES, Blowfish) e assimétricos (Diffie‑Hellman, RSA, DSA), hashing, esteganografia e quebra de hashes. Terceiro, **análise de tráfego e ataques na pilha TCP/IP**: captura com tcpdump/Wireshark, ataques de camada 2/3 (ARP poisoning, SYN flood, Smurf, Fraggle, ICMP redirect) e inspeção profunda de pacotes (DPI). Fecha com um capítulo de **mercado de TI e carreira**.

A ideia central: **ler tráfego e entender criptografia são as duas lentes com que um analista enxerga o que está acontecendo na rede** — e os mesmos conceitos explicam tanto o ataque quanto a defesa.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Roteiro: princípios de SI, criptografia, análise de pacotes, ataques TCP/IP, esteganografia, hashes, DPI e carreira. |
| 2 | Cybersecurity × Information Security | Segurança da informação é mais que tecnologia: envolve pessoas, processos e estratégia. **ROSI** (retorno do investimento em segurança). **Princípios**: menor privilégio, defesa em profundidade, elo mais fraco, ponto de verificação, segurança por obscuridade (e por que não basta), KISS e segregação de funções (SoD). |
| 3 | Criptografia — o segredo de César | História: cifra de **César** (substituição), **Vigenère** (polialfabética) e **Enigma**. Conceitos: simétrico (chave privada) × assimétrico (chave pública). Algoritmos simétricos (DES/3DES, RC2/4/5, IDEA, Blowfish, **AES**) e assimétricos (**Diffie‑Hellman**, **RSA**, SSL/TLS, DSA). Hashing e tipos de cifra (transposição × substituição). |
| 4 | O "canivete suíço" | Análise de pacotes TCP/IP na prática: **port mirroring** (SPAN), sniffers e analisadores de protocolo, **tcpdump** e montagem do alvo **Metasploitable2**. Estudo de uma sessão **FTP** capturada, mostrando credenciais em texto claro. |
| 5 | TCP/IP sob ataque | Como a falha de configuração vira vulnerabilidade. Ataques de rede local: **DoS**, **sniffing** e **brute force**. **ARP cache poisoning** (para DoS e para MitM/sniffing) e variações de DoS: **Smurf**, **SYN flood**, **ICMP redirect** e **Fraggle**. Mitigação do ARP poisoning (DAI, entradas estáticas). |
| 6 | Mercado de TI e carreira | Cibersegurança como área aquecida, a importância da **reputação digital** (o "currículo digital"), diversidade e inclusão (comunidades de mulheres na tecnologia, inclusão de PcD). |
| 7 | Crypto e privacidade | Revisão de simétrico × assimétrico com o exemplo Alice/Bob, algoritmos populares, papel da **VPN**, a **deep web** × **dark web** (e o Tor), e um laboratório prático com **GnuPG (GPG)**: gerar par de chaves, cifrar e assinar. |
| 8 | Esteganografia | Arte de **ocultar** a informação (não embaralhar). Métodos (LSB em imagens, áudio), diferença entre esteganografia (esconde a existência) e criptografia (esconde o conteúdo), **esteganálise** (detecção) e laboratório com **Steghide**. |
| 9 | Cracking Hash | O que é hash e por que **hash não é criptografia** (é unidirecional). Algoritmos (MD5, SHA‑1/2), hashes do **Windows** (NTLM) e do **Linux** (`/etc/shadow`, `$6$` = SHA‑512), quebra por dicionário/força bruta, **rainbow tables** e o papel do **salt**. Laboratório com **John the Ripper**. |
| 10 | Packet Inspection | O que é inspeção de pacotes e seus usos (segurança, desempenho, análise de protocolo, identificação de aplicação, troubleshooting). Métodos: tempo real, captura e armazenamento, análise de fluxo (flow) e **Deep Packet Inspection (DPI)**. **Wireshark** (interface, painéis, filtros) e **tshark** na linha de comando. |

## 🔑 Conceitos-chave

- **Princípios de SI**: menor privilégio, defesa em profundidade e segregação de funções aparecem em toda arquitetura segura. "Segurança por obscuridade" não é controle por si só; a segurança não pode depender de o atacante não conhecer o sistema.
- **Simétrico × assimétrico**: o simétrico (AES) é rápido e usa uma chave compartilhada — o desafio é **distribuir a chave**. O assimétrico (RSA) usa par de chaves público/privado e resolve a troca de chaves e a assinatura digital, mas é mais lento. Na prática usam‑se juntos (TLS: assimétrico negocia a chave, simétrico cifra os dados).
- **Confidencialidade × integridade × autenticidade**: cifrar dá confidencialidade; o hash dá integridade; a assinatura digital (hash + chave privada) dá autenticidade e não repúdio.
- **Hash não é criptografia**: é uma função unidirecional, sem chave e sem volta. Serve para integridade e para armazenar senhas — nunca para "cifrar" algo que precise ser recuperado.
- **Salt**: valor aleatório único somado à senha antes do hash. Faz senhas iguais terem hashes diferentes e **inutiliza rainbow tables**. Hoje usa‑se também KDFs lentas (bcrypt, scrypt, Argon2).
- **Esteganografia × criptografia**: a criptografia deixa claro que *há* um segredo (texto embaralhado); a esteganografia **esconde que existe mensagem**. As duas se combinam: cifrar e depois esconder.
- **Sniffing e texto claro**: protocolos sem TLS (FTP, Telnet, HTTP, POP) expõem credenciais a quem captura o tráfego. Um PCAP de uma sessão FTP mostra usuário e senha legíveis.
- **ARP poisoning**: como o ARP não tem autenticação, o atacante associa seu MAC ao IP do gateway e passa a interceptar (MitM) ou derrubar (DoS) o tráfego. Mitigação: **DAI**, DHCP snooping e entradas ARP estáticas.
- **DoS de rede**: SYN flood (esgota a tabela de conexões meio‑abertas), Smurf e Fraggle (amplificação por broadcast), ICMP redirect (desvia rotas). As defesas incluem SYN cookies, filtragem de broadcast e rate limiting.
- **DPI × inspeção simples**: a inspeção comum olha cabeçalhos (IP, porta); o DPI inspeciona o **payload** (camada 7), permitindo identificar aplicações e assinaturas — base de IDS/IPS e também de censura.
- **Wireshark é o microscópio da rede**: filtros de exibição (`ip.addr == x`, `tcp.port == 80`, `http`), *Follow TCP Stream* e estatísticas transformam captura em evidência.

## 🛠️ Ferramentas e comandos

**Ambiente:** VM de ataque (Kali) + alvo **Metasploitable2** em rede isolada. Ferramentas: tcpdump, Wireshark/tshark, GnuPG, Steghide, John the Ripper, hashcat.

```bash
# Captura e análise de tráfego (em rede autorizada/isolada)
sudo tcpdump -i eth0 -nn -s0 -w captura.pcap 'tcp port 21'
tshark -r captura.pcap -Y "ftp" -T fields -e ftp.request.command -e ftp.request.arg
# Wireshark: filtros de exibição
ip.addr == 192.168.56.102   ·   tcp.flags.syn == 1 && tcp.flags.ack == 0   ·   http.request

# Criptografia com GnuPG
gpg --full-generate-key
gpg --armor --export "Nome" > chave_publica.asc
gpg --encrypt --recipient "Nome" arquivo.txt
gpg --decrypt arquivo.txt.gpg
gpg --sign documento.txt            # assinatura digital

# Esteganografia (estudo)
steghide embed -cf imagem.jpg -ef segredo.txt      # embutir (em arquivo próprio, lab)
steghide extract -sf imagem.jpg                    # extrair
steghide info imagem.jpg

# Hashes (em laboratório, com arquivos próprios)
mkpasswd -m sha-512; sha256sum arquivo
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --show hashes.txt
hashcat -m 1800 hashes.txt rockyou.txt             # $6$ = sha512crypt
```

## ❓ Perguntas de revisão

1. **Qual a diferença entre criptografia simétrica e assimétrica, e por que o TLS usa as duas?**
   A simétrica usa uma única chave (rápida, mas precisa distribuir a chave com segurança); a assimétrica usa par público/privado (resolve a troca de chaves e a assinatura, mas é lenta). O TLS usa a assimétrica para negociar com segurança uma chave de sessão e a simétrica para cifrar os dados daí em diante.
2. **Por que "hash não é criptografia"?**
   Porque o hash é uma função unidirecional, sem chave: não existe operação de "desfazer". Serve para verificar integridade e armazenar senhas, não para proteger algo que precise ser recuperado.
3. **Para que serve o salt e o que ele impede?**
   É um valor aleatório único adicionado à senha antes do hash. Faz senhas iguais gerarem hashes diferentes e inutiliza rainbow tables, obrigando o atacante a quebrar cada hash individualmente.
4. **Qual a diferença entre esteganografia e criptografia?**
   A criptografia embaralha o conteúdo (fica claro que há um segredo); a esteganografia esconde a própria existência da mensagem dentro de outro arquivo. Podem ser combinadas.
5. **Como funciona o ARP cache poisoning e como mitigá‑lo?**
   O atacante envia respostas ARP falsas associando seu MAC a um IP legítimo (ex.: o gateway), passando a interceptar ou derrubar o tráfego. Mitiga‑se com Dynamic ARP Inspection, DHCP snooping e entradas ARP estáticas.
6. **O que é um SYN flood?**
   Um ataque de DoS que envia muitos SYN sem completar o handshake, esgotando a tabela de conexões meio‑abertas do servidor. SYN cookies e rate limiting ajudam a mitigar.
7. **Por que uma sessão FTP é perigosa numa rede compartilhada?**
   Porque o FTP transmite usuário, senha e dados em texto claro. Qualquer sniffer na rede lê as credenciais. O correto é usar SFTP ou FTPS.
8. **O que é Deep Packet Inspection e no que difere da inspeção comum?**
   A inspeção comum analisa apenas cabeçalhos (IP, portas); o DPI examina o conteúdo (payload, camada 7), permitindo identificar aplicações e assinaturas. É base de IDS/IPS e NGFW — e também de censura.
9. **No Wireshark, como isolar o tráfego HTTP de um host específico?**
   Com um filtro de exibição combinando host e protocolo, por exemplo `ip.addr == 192.168.1.10 && http`, e usando *Follow TCP Stream* para remontar a conversa.
10. **O que é o princípio da defesa em profundidade?**
    Empilhar múltiplas camadas de controle (rede, host, aplicação, pessoas) para que a falha de uma não comprometa todo o sistema. Combina com menor privilégio e segregação de funções.

## 💼 Conexão com o mercado

- **SOC (analista N1/N2)**: análise de PCAP é habilidade central da triagem. Reconhecer ARP poisoning, SYN flood, varreduras e exfiltração num Wireshark/Zeek, e entender onde a criptografia (TLS) protege ou esconde o tráfego, é trabalho diário. Quebra de hashes aparece em respostas a incidentes com credenciais vazadas.
- **CompTIA Security+ (SY0‑701)**: criptografia (simétrico/assimétrico, PKI, hashing, salt, assinatura digital), ataques de rede (DoS/DDoS, on‑path/MitM, ARP poisoning), princípios (menor privilégio, defesa em profundidade, SoD) e esteganografia caem em *General Security Concepts*, *Threats* e *Security Architecture*.
- **Pós Tech em IA para Segurança**: features de tráfego (tamanho de pacote, inter‑arrival, flags, entropia do payload) alimentam modelos de NDR e detecção de túneis/exfiltração. DPI e análise de fluxo são exatamente a fonte desses dados; entender criptografia ajuda a reconhecer tráfego cifrado sem conseguir lê‑lo.

## 📖 Termos da fase

Information security × cybersecurity · ROSI · Menor privilégio · Defesa em profundidade · Elo mais fraco · Segregação de funções (SoD) · KISS · Segurança por obscuridade · Cifra de César · Vigenère · Enigma · Criptografia simétrica · Criptografia assimétrica · Chave pública/privada · DES/3DES · AES · Blowfish · RC4 · Diffie‑Hellman · RSA · DSA · SSL/TLS · Assinatura digital · PKI · Hash · MD5 · SHA · NTLM · Salt · Rainbow table · KDF (bcrypt/Argon2) · John the Ripper · hashcat · Esteganografia · Esteganálise · LSB · Steghide · GnuPG (GPG) · VPN · Tor / dark web · Sniffing · tcpdump · Wireshark · tshark · Port mirroring (SPAN) · Metasploitable2 · ARP cache poisoning · DoS / DDoS · SYN flood · Smurf · Fraggle · ICMP redirect · Brute force · Deep Packet Inspection (DPI) · Análise de fluxo

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
