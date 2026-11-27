# Year 2 · Phase 1 — Cyber Threat Intelligence e OSINT (Cyber Threat Intelligence & OSINT)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. Foco conceitual, defensivo e ético.

## 🧭 Visão geral

O segundo ano abre virando a chave de **defender o perímetro** para **caçar o adversário**. A fase é toda sobre **Cyber Threat Intelligence (CTI)** e **OSINT (Open Source Intelligence)**. Começa pelos fundamentos da inteligência (raízes militares; a diferença entre **dado, informação e inteligência**; os tipos estratégico/tático/operacional/técnico) e pelos frameworks que organizam a defesa (**MITRE ATT&CK**, **Cyber Kill Chain**, **Diamond Model**, **F3EAD**). Passa por **IoC × IoA** e análise de artefatos, por **OpSec** (operar sem se expor), **contrainteligência** e **deception** (honeypots), por **anonimato** (proxy, VPN, Tor) e por todo o ciclo de **OSINT**: fontes, coleta ética, Shodan/Censys, geolocalização (GEOINT), perfis e sock puppets, vazamentos, e automação com **Maltego, Recon‑ng, theHarvester e MISP**. Em paralelo, corre o projeto transversal de empreendedorismo **Startup One** (capítulos próprios, fora desta pasta).

A ideia central: **inteligência é dado transformado em decisão**. Saber antecipar o movimento do adversário — e investigar fontes abertas sem se tornar alvo — é o que separa reagir a alertas de caçar ameaças.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura — Restarting | Missão dupla da fase: dominar CTI/caça a ameaças e iniciar a startup (Startup One, em squads). |
| 2 | Estratégia e Fundamentos | Origens militares da inteligência; **dado → informação → inteligência**; tipos (estratégica, tática, operacional, técnica). Definição e papel da **CTI**; diferença entre CTI e monitoramento. Frameworks: **Cyber Kill Chain**, **MITRE ATT&CK**, **Diamond Model**, **F3EAD** e o modelo 6Ds de transformação digital. |
| 3 | Rastros e OpSec | **IoA × IoC** (indicadores de ataque × de comprometimento): diferenças, fontes, tipos, uso e reporte. Análise de artefatos (estática e dinâmica) para extrair IoCs e documentá‑los; compartilhamento (feeds). **OpSec**: montar um laboratório para investigar sem se expor. |
| 4 | Infiltração e Contrainteligência | Técnicas de **engenharia social** que o atacante usa (PNL, persuasão). Defesas de **contrainteligência**: compartimentalização, verificação de fontes, higiene de OpSec, *need‑to‑know*/*need‑to‑share*, análise de confiabilidade e **deception**. Metodologia investigativa (PIRs, coleta multicanal, enriquecimento, ética e legalidade). |
| 5 | A Arte da Invisibilidade | Rastreabilidade além do IP (fingerprint, cookies, metadados). **Proxy**, **VPN** (e suas falhas) e **Tor**; encadeamento **Tor‑over‑VPN × VPN‑over‑Tor**; privacidade × anonimato; OpSec de rede para o investigador; e como um **SOC detecta** quem tenta se esconder. Laboratório de ocultação com baselines. |
| 6 | O Poder do OSINT | Fontes de coleta: tradicionais, digitais abertas (**WHOIS**, domínios, certificados), redes sociais, repositórios de código, **operadores de busca (dorks)**, frameworks (Maltego, SpiderFoot), **Shodan/Censys** e Dark Web. **Ciclo de vida do OSINT**: requisitos (PIRs) → coleta → processamento → análise → produção → disseminação → feedback. Estudo de caso Wirecard. |
| 7 | Investigação Avançada | **GEOINT** (geolocalizar por imagens/metadados), análise de **perfis** reais × falsos (**sock puppets**) e *due diligence*, OSINT em mídias sociais, dados empresariais e **domínios/subdomínios**, e rastreamento de **vazamentos** (cloud storage, repositórios). |
| 8 | Escala Máxima | **Automação** da coleta em CTI (vantagens, riscos, boas práticas, pipelines). Ferramentas: **Maltego** (pivotagem, clusterização, link analysis), **Recon‑ng** (framework Python), **theHarvester** (e-mails/subdomínios via buscadores e crt.sh), **Shodan** e **MISP**. Integração das ferramentas num fluxo; estudo de caso da campanha de ransomware **Ryuk**. |

## 🔑 Conceitos-chave

- **Dado → informação → inteligência**: dado é bruto (um IP); informação é dado com contexto (esse IP fez login à meia‑noite); inteligência é informação analisada que apoia uma decisão (esse IP é de um grupo que ataca o seu setor — bloqueie e cace).
- **Tipos de CTI**: **estratégica** (tendências, para a diretoria), **operacional** (campanhas e TTPs de um grupo), **tática** (TTPs e comportamento, para o time de defesa) e **técnica** (IoCs específicos, para alimentar ferramentas).
- **Cyber Kill Chain**: as 7 fases de um ataque (reconhecimento → armamento → entrega → exploração → instalação → C2 → ações no objetivo). Serve para pensar onde quebrar a corrente.
- **MITRE ATT&CK**: base de conhecimento de táticas (o "porquê") e técnicas (o "como") reais dos adversários. É a linguagem comum para mapear detecção e cobertura defensiva.
- **Diamond Model**: relaciona os quatro vértices de uma intrusão — adversário, capacidade, infraestrutura e vítima — para correlacionar e pivotar entre eventos.
- **F3EAD**: ciclo que une inteligência e ação — Find, Fix, Finish, Exploit, Analyze, Disseminate.
- **IoC × IoA**: o IoC é a evidência do que **já aconteceu** (hash, IP, domínio malicioso); o IoA descreve o **comportamento/intenção** em andamento (ex.: processo tentando despejar credenciais). IoA detecta mais cedo; IoC confirma e caça retroativamente.
- **OpSec**: proteger a própria operação de investigação. Um investigador que usa sua conta ou IP reais entrega o alvo e a si mesmo. Compartimentalizar identidades e infraestrutura é essencial.
- **Privacidade × anonimato**: privacidade é esconder o **conteúdo**; anonimato é esconder **quem** você é. Uma VPN muda o IP de saída, mas não anonimiza por si só; o Tor foca anonimato de identidade. Cada técnica tem trade‑offs e pegadas detectáveis.
- **Ciclo de OSINT**: requisitos (PIRs) direcionam a coleta; sem pergunta clara, OSINT vira acúmulo de dado inútil. Coleta ética e legal é regra, não opção.
- **Sock puppet**: persona falsa, isolada e consistente, usada para investigar sem expor a identidade real. Due diligence distingue perfis reais de fabricados.
- **Automação com cuidado**: Maltego, Recon‑ng e theHarvester escalam a coleta, mas geram ruído, podem violar termos de uso e precisam de validação humana. MISP centraliza e compartilha IoCs entre organizações.

## 🛠️ Ferramentas e comandos

**Ferramentas:** Shodan, Censys, Maltego, SpiderFoot, Recon‑ng, theHarvester, MISP, Tor Browser, VPN, crt.sh, WHOIS, Google dorks. Tudo usado de forma **ética, legal e sobre alvos autorizados**.

```bash
# OSINT de infraestrutura (fontes públicas)
whois exemplo.com
dig exemplo.com ANY +noall +answer
curl -s "https://crt.sh/?q=%25.exemplo.com&output=json" | jq -r '.[].name_value' | sort -u   # subdomínios por CT logs
theHarvester -d exemplo.com -b bing,crtsh -l 500

# Recon-ng (framework de OSINT em Python)
recon-ng
# marketplace install all; modules load recon/domains-hosts/hackertarget; run

# Operadores de busca (dorks) — descoberta de exposição
site:exemplo.com filetype:pdf
intitle:"index of" "backup"            # só em alvos autorizados

# Anonimato / OpSec (do lado do investigador)
tor + Tor Browser; verificar vazamento de DNS/WebRTC; checar o IP de saída
# nunca misturar identidade real com a persona de investigação (sock puppet)
```

Shodan/Censys (web): buscar por `org:"Empresa"`, `port:`, `ssl.cert.subject.cn:`, para mapear a superfície de ataque exposta — apenas para reconhecimento autorizado.

## ❓ Perguntas de revisão

1. **Qual a diferença entre dado, informação e inteligência?**
   Dado é o fato bruto (um IP); informação é o dado com contexto (o IP acessou às 3h); inteligência é a análise que orienta uma decisão (o IP pertence a um grupo que ataca seu setor, então bloqueie e investigue).
2. **Quais são os quatro tipos de CTI e para quem servem?**
   Estratégica (diretoria, tendências e risco), operacional (resposta/caça, campanhas e intenção de grupos), tática (defensores, TTPs e comportamento) e técnica (ferramentas, IoCs específicos).
3. **Qual a diferença entre IoC e IoA?**
   O IoC é evidência do que já ocorreu (hash, IP, domínio malicioso); o IoA descreve o comportamento/intenção em andamento (ex.: tentativa de dump de credenciais). O IoA permite detecção mais precoce.
4. **O que a Cyber Kill Chain e o MITRE ATT&CK trazem de diferente?**
   A Kill Chain é um modelo linear das fases de um ataque (bom para pensar onde interromper). O ATT&CK é uma matriz detalhada de táticas e técnicas reais dos adversários (bom para mapear detecção e cobertura).
5. **O que é o Diamond Model?**
   Um modelo que liga adversário, capacidade, infraestrutura e vítima numa intrusão, permitindo correlacionar eventos e pivotar (de uma infraestrutura para outras vítimas, por exemplo).
6. **Por que OpSec é essencial numa investigação de OSINT?**
   Porque usar IP, conta ou navegador reais pode alertar o alvo e expor o investigador. Compartimentalizar identidade e infraestrutura (sock puppets, VMs, VPN/Tor) evita contaminar a investigação e virar vítima.
7. **Privacidade é o mesmo que anonimato? E uma VPN garante anonimato?**
   Não. Privacidade esconde o conteúdo; anonimato esconde a identidade. Uma VPN muda o IP de saída e protege em trânsito, mas o provedor sabe quem você é e há pegadas (DNS, fingerprint); não garante anonimato sozinha.
8. **Quais etapas formam o ciclo de vida do OSINT?**
   Requisitos (PIRs) → coleta → processamento/normalização → análise → produção de inteligência → disseminação → feedback e melhoria contínua.
9. **O que é um sock puppet e por que a verificação de perfis importa?**
   É uma persona falsa e isolada usada para investigar sem expor a identidade real. A verificação (due diligence) distingue perfis genuínos de fabricados, evitando desinformação e armadilhas.
10. **Que cuidados a automação de coleta (Maltego, Recon‑ng, theHarvester) exige?**
    Validar os dados (evitar falsos positivos), respeitar termos de uso e a lei, controlar o ruído e o rate limit, e manter o investigador no circuito para interpretar os resultados em vez de só acumulá‑los.

## 💼 Conexão com o mercado

- **SOC e Threat Intelligence (analista de CTI / threat hunter)**: esta é a base direta da função. Produzir e consumir inteligência, mapear atividade no ATT&CK, extrair e compartilhar IoCs via MISP/STIX, enriquecer alertas com OSINT e caçar proativamente são tarefas de N2/N3 e de times de TI. A OpSec protege o próprio analista.
- **CompTIA Security+ (SY0‑701)** e além: threat intelligence, fontes OSINT, frameworks (ATT&CK, Kill Chain), IoC/IoA e threat hunting aparecem em *Security Operations*; esta fase também prepara para certificações específicas de CTI/OSINT. Ética e legalidade da investigação tocam *Security Program Management*.
- **Pós Tech em IA para Segurança**: CTI é um dos campos que mais adota IA — classificação e correlação de IoCs, enriquecimento automático, análise de linguagem em fóruns e dark web, e deduplicação de feeds. O ciclo de OSINT (coleta → processamento → análise) é, na prática, um pipeline de dados que LLMs e ML aceleram.

## 📖 Termos da fase

Cyber Threat Intelligence (CTI) · Dado × informação × inteligência · CTI estratégica/tática/operacional/técnica · Cyber Kill Chain · MITRE ATT&CK · TTP · Diamond Model · F3EAD · PIR (Priority Intelligence Requirements) · IoC · IoA · Análise estática × dinâmica · Feed de ameaças · MISP · STIX/TAXII · OpSec · Contrainteligência · Deception · Honeypot · Engenharia social · OSINT · Ciclo de vida do OSINT · WHOIS · Certificate Transparency (crt.sh) · Google dorks · Shodan · Censys · GEOINT · Sock puppet · Due diligence · Dark web · Maltego · SpiderFoot · Recon‑ng · theHarvester · Pivotagem · Link analysis · Proxy · VPN · Tor · Privacidade × anonimato · Fingerprinting

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
