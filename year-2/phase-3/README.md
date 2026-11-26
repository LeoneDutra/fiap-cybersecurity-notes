# Year 2 · Phase 3 — Pentest e Segurança de Active Directory (Penetration Testing & Active Directory Security)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. **Foco conceitual, de detecção e de defesa — não reproduzo procedimentos ofensivos passo a passo. Todo o conteúdo pressupõe ambiente de laboratório isolado e autorização explícita.**

## 🧭 Visão geral

A fase cobre o **ciclo de um teste de intrusão (pentest)** com ênfase no alvo mais comum das empresas: o **Active Directory (AD)**. Começa pelo **reconhecimento** (passivo e ativo), passa pelos conceitos de **exploração** (shells e payloads, Metasploit) e então dedica cinco capítulos ao AD sob a ótica ofensiva **e defensiva**: fundamentos e laboratório, **enumeração**, **exploração** (os ataques clássicos a NTLM e Kerberos), **pós‑exploração** (movimento lateral, credential dumping, persistência) e, por fim, um capítulo inteiro de **defesa e mitigação**. Entender o ataque é o que permite **detectá‑lo e preveni‑lo** — e é esse o enquadramento que adoto aqui.

A ideia central: **o Active Directory é o cofre de identidades da empresa, e a maioria das invasões corporativas é uma cadeia de abusos de configuração do AD**. Saber como essa cadeia funciona é pré‑requisito para quebrá‑la com detecção e endurecimento (hardening).

## 📚 Resumo por material

| # | Tema | O que fica (ênfase defensiva) |
|---|---|---|
| 1 | Abertura — Underworld | Roteiro: reconhecimento → exploração → AD (fundamentos, enumeração, exploração, pós‑exploração, defesa). |
| 2 | Radar Hacker — Reconhecimento | **Reconhecimento passivo** (WHOIS, Shodan, DNSDumpster, certificados SSL/CT, e‑mails) × **ativo** (Google dorks, fingerprint de tecnologias com Wappalyzer/WhatWeb). O ponto defensivo: **minimizar a superfície e a informação exposta** — o que o atacante vê é o que a empresa deixou público. |
| 3 | Pwned — Exploração | Conceitos de **shells** (reverse × bind) e **payloads** (staged × stageless), e o papel do **Metasploit** e do msfvenom. Defensivamente: entender esses mecanismos é entender o que um **EDR/IDS** precisa detectar (conexões de volta, payloads conhecidos). *(Sem receitas de exploração.)* |
| 4 | AD Battleground — Fundamentos | **Active Directory** pela ótica de segurança: **DC**, domínios, **OUs**, **GPO**, florestas, **LDAP**, DNS, roles e níveis funcionais. Protocolos de autenticação: **NTLM** (fluxo challenge‑response e por que é fraco) e **Kerberos** (tickets TGT/TGS). Montagem de um **laboratório** de AD para estudo. |
| 5 | AD Enumeration | **Enumeração** do domínio (o reconhecimento *dentro* da rede): mapear usuários, grupos, membros de Domain Admins, computadores, GPOs e OUs via **LDAP** e ferramentas como **NetExec** e **BloodHound**. Defensivamente: enumeração massiva de LDAP é um **sinal detectável**; contas de serviço e descrições expõem segredos. |
| 6 | AD Exploitation | Os ataques clássicos, descritos **para reconhecê‑los e detectá‑los**: envenenamento de **LLMNR/NBT‑NS**, **NTLM relay**, **pass‑the‑hash**, **AS‑REP roasting** e **Kerberoasting**. Cada um abusa de uma fraqueza de configuração (protocolos legados, contas sem pré‑autenticação, SPNs com senha fraca). |
| 7 | AD Post‑Exploitation | Depois do acesso inicial: **movimento lateral** (RDP, SMB, WinRM), **credential dumping** (Mimikatz/LSASS, Rubeus) e **persistência de domínio** (**Golden/Silver/Diamond Ticket**). O ponto: entender a progressão para **interrompê‑la** com segmentação, menor privilégio e monitoramento. |
| 8 | AD Defense / Mitigations | O capítulo‑chave: como **mitigar** cada ataque anterior — desabilitar LLMNR/NBT‑NS, exigir assinatura SMB/LDAP, proteger contra NTLM relay, corrigir AS‑REP roasting (pré‑autenticação) e Kerberoasting (senhas fortes de contas de serviço, gMSA), política de senhas contra **password spray**, higiene de **DACL**, proteção contra **Golden/Silver Ticket** (rotação do krbtgt) e **endpoint protection**. |

## 🔑 Conceitos-chave (com a lente da defesa)

- **Fases do pentest**: reconhecimento → enumeração → exploração → pós‑exploração → (relatório). A defesa espelha isso: reduzir exposição, detectar enumeração, bloquear exploração, conter movimento lateral.
- **Passivo × ativo**: o reconhecimento passivo não toca o alvo (OSINT, Shodan, CT logs); o ativo interage (dorks, fingerprint). Quanto menos a empresa expõe publicamente, menos o atacante começa sabendo.
- **NTLM é frágil**: baseado em challenge‑response e no hash da senha; é vulnerável a **pass‑the‑hash** e **relay**. A direção é desativar NTLM onde possível, exigir assinatura (SMB/LDAP signing) e usar Kerberos.
- **Kerberos e seus abusos**: **AS‑REP roasting** abusa de contas sem pré‑autenticação; **Kerberoasting** pede tickets de serviço (SPN) e quebra a senha offline. Mitigação: ativar pré‑autenticação, usar senhas longas/gMSA para contas de serviço e monitorar pedidos de ticket anômalos.
- **LLMNR/NBT‑NS poisoning**: protocolos de resolução de nomes legados respondem a qualquer um na LAN, permitindo capturar hashes. Mitigação: **desabilitar LLMNR e NBT‑NS** por GPO.
- **BloodHound e caminhos de ataque**: a enumeração monta um grafo de "quem pode chegar a Domain Admin". O mesmo grafo serve ao **defensor** para encontrar e cortar caminhos de escalonamento e **DACLs** perigosas.
- **Credential dumping**: extrair hashes/tickets da memória (LSASS). Mitigação: Credential Guard, LSASS protegido, menor privilégio e EDR.
- **Movimento lateral**: reuso de credenciais por SMB/WinRM/RDP para pular de máquina em máquina. Mitigação: contas locais únicas (LAPS), segmentação, Tier Model e restrição de logon.
- **Persistência de domínio (Golden Ticket)**: com o hash da conta **krbtgt**, o atacante forja tickets Kerberos válidos. A resposta é **rotacionar o krbtgt duas vezes** e detectar tickets anômalos.
- **Menor privilégio e Tier Model**: separar contas de administração por nível impede que o comprometimento de uma estação chegue ao DC. É a defesa estrutural mais importante.
- **Detecção**: os ataques de AD deixam rastros nos **logs de evento** (4768/4769 para Kerberos, 4624/4625 para logon, 4662 para acesso a objetos). Um SIEM com regras certas detecta roasting, spray e uso de tickets forjados.

## 🛠️ Ferramentas e abordagem

**Ferramentas citadas** (contexto de laboratório autorizado): Nmap, Shodan, DNSDumpster, Wappalyzer, WhatWeb, Metasploit, NetExec, BloodHound, PowerView, ldapsearch, Impacket, Rubeus, Mimikatz. **Do lado da defesa**: GPO, LAPS, gMSA, Microsoft Defender for Identity, SIEM, e as auditorias do próprio AD.

> ⚠️ Este README descreve as técnicas **no nível de conceito, detecção e mitigação**. Não inclui comandos de exploração, geração de payloads ou procedimentos de ataque passo a passo. A prática ocorre **somente** em laboratório próprio e isolado, ou em engajamentos com autorização escrita.

**Postura defensiva, item a item:**

```text
LLMNR / NBT-NS  → desabilitar por GPO; monitorar respostas forjadas na LAN
NTLM relay      → exigir SMB signing e LDAP signing/channel binding; reduzir NTLM
AS-REP roasting → exigir pré-autenticação Kerberos em todas as contas
Kerberoasting   → senhas longas/gMSA em contas de serviço; alertar em 4769 anômalos
Password spray  → política de senha forte, lockout, MFA; alertar em muitos 4625
DACL abuse      → revisar ACLs do AD (BloodHound); princípio do menor privilégio
Golden/Silver   → rotacionar krbtgt 2x; Tier Model; detectar tickets anômalos
Credential dump → Credential Guard, LSASS protegido, EDR, menor privilégio
Lateral movement→ LAPS, segmentação, restrição de logon por tier
```

## 🧪 Atividades / CTFs

Não há pasta de CTF nesta fase; a prática é o **laboratório de AD** montado nos materiais (VMs isoladas). Exercícios, sempre com foco em entender para defender:

- Montar um **laboratório de AD** (DC + estações) e explorar sua estrutura (OUs, grupos, GPOs) com LDAP/BloodHound.
- Mapear **caminhos de ataque** no BloodHound e, como defensor, propor onde cortá‑los.
- Reproduzir, em lab, a captura por **LLMNR/NBT‑NS** e aplicar a mitigação por GPO, verificando que a captura para.
- Identificar contas vulneráveis a **AS‑REP roasting**/**Kerberoasting** e corrigi‑las (pré‑auth, gMSA).
- Escrever regras de **detecção** (eventos 4768/4769/4625) num SIEM para os ataques estudados.

> 💡 Dica de homelab: use o **GOAD (Game of Active Directory)** ou o laboratório **AD** do próprio material, sempre isolado. Para treinar **defesa e detecção**, combine com o **Atomic Red Team** (simula técnicas ATT&CK) e colete os eventos num SIEM. Para prática legal e guiada, os módulos de AD do **TryHackMe/HackTheBox Academy**.

## ❓ Perguntas de revisão

1. **Quais são as fases de um pentest e como a defesa espelha cada uma?**
   Reconhecimento, enumeração, exploração, pós‑exploração e relatório. A defesa responde reduzindo exposição pública, detectando enumeração, bloqueando exploração (patch/config), contendo movimento lateral e aprendendo com o relatório.
2. **Por que o NTLM é considerado fraco e qual a direção de mitigação?**
   Porque usa o hash da senha em challenge‑response, o que permite pass‑the‑hash e relay. A direção é reduzir/desabilitar NTLM, exigir assinatura (SMB/LDAP) e usar Kerberos.
3. **O que é LLMNR/NBT‑NS poisoning e como mitigá‑lo?**
   São protocolos legados de resolução de nomes que respondem a qualquer host da LAN, permitindo capturar hashes. Mitiga‑se desabilitando LLMNR e NBT‑NS por GPO.
4. **Qual a diferença entre AS‑REP roasting e Kerberoasting?**
   O AS‑REP roasting abusa de contas sem pré‑autenticação Kerberos; o Kerberoasting pede tickets de serviço (SPN) e quebra a senha offline. Mitigações: ativar pré‑autenticação e usar senhas fortes/gMSA em contas de serviço.
5. **O que o BloodHound revela e como o defensor o usa?**
   Monta um grafo de caminhos de privilégio ("quem chega a Domain Admin"). O defensor usa o mesmo grafo para encontrar e cortar caminhos de escalonamento e DACLs perigosas.
6. **O que é pass‑the‑hash e como reduzir o risco?**
   Autenticar usando o hash NTLM sem conhecer a senha. Reduz‑se com menor privilégio, contas locais únicas (LAPS), Credential Guard e segmentação por tier.
7. **O que é um Golden Ticket e qual a resposta defensiva?**
   Um ticket Kerberos forjado com o hash da conta krbtgt, dando acesso quase irrestrito. A resposta é rotacionar o krbtgt duas vezes, aplicar o Tier Model e detectar tickets anômalos.
8. **Como o movimento lateral acontece e como contê‑lo?**
   Reusando credenciais por SMB/WinRM/RDP para pular entre máquinas. Contém‑se com LAPS, segmentação de rede, restrição de logon por tier e monitoramento.
9. **Que eventos do Windows ajudam a detectar ataques de AD?**
   4768/4769 (pedidos de ticket Kerberos — roasting), 4624/4625 (logons bem‑sucedidos/falhos — spray) e 4662 (acesso a objetos — abuso de DACL), correlacionados num SIEM.
10. **Qual é a defesa estrutural mais importante no AD?**
    O menor privilégio aplicado com o Tier Model: separar contas de administração por nível para que o comprometimento de uma estação não alcance o DC.

## 💼 Conexão com o mercado

- **Red Team / Pentester e Blue Team**: esta fase é a base tanto do pentester de AD quanto do defensor que precisa detectá‑lo. Em quase toda empresa, o AD é o alvo central; conhecer a cadeia de ataque é o que permite escrever detecções, endurecer GPOs e priorizar correções. É também o conteúdo de certificações ofensivas (OSCP, CRTP/CRTE) e defensivas.
- **CompTIA Security+ / PenTest+**: fases do pentest, reconhecimento passivo × ativo, ataques a credenciais e a Kerberos, movimento lateral, persistência e as mitigações aparecem em *Security Operations* e *Security Architecture*. A ênfase em mitigação conecta com *Governance/Hardening*.
- **Pós Tech em IA para Segurança**: a detecção de ataques de AD é um caso forte de ML/UEBA — modelar o comportamento normal de autenticação (horário, origem, volume de tickets) para apontar roasting, spray e uso de tickets forjados. Os grafos de caminho de ataque (BloodHound) são, literalmente, análise de grafos aplicável a IA.

## 📖 Termos da fase

Pentest (teste de intrusão) · Reconhecimento passivo × ativo · OSINT · Google dorks · Fingerprint de tecnologia · Shell (reverse × bind) · Payload (staged × stageless) · Metasploit · msfvenom · Active Directory (AD) · Domain Controller (DC) · OU · GPO · Floresta · LDAP · Nível funcional · NTLM · Kerberos (TGT/TGS) · Enumeração de AD · NetExec · BloodHound · PowerView · LLMNR/NBT‑NS poisoning · NTLM relay · SMB/LDAP signing · Pass‑the‑hash · AS‑REP roasting · Kerberoasting · SPN · Password spray · DACL · Movimento lateral · RDP/SMB/WinRM · Credential dumping · Mimikatz · LSASS · Rubeus · Persistência de domínio · Golden/Silver/Diamond Ticket · krbtgt · LAPS · gMSA · Tier Model · Credential Guard · Menor privilégio

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
