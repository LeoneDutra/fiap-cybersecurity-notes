# Year 2 · Phase 2 — Resposta a Incidentes e Forense Digital / DFIR (Incident Response & Digital Forensics)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A fase é dedicada a **DFIR (Digital Forensics & Incident Response)**: o que fazer quando o ataque acontece e como investigá‑lo com rigor forense. Começa pelos fundamentos de **resposta a incidentes** (o que é um incidente, seu ciclo de vida, conter → erradicar → recuperar → aprender) e pela **análise de logs** (web, firewall, IDS/IPS) com **SIEM (Splunk)**. Depois mergulha na **perícia digital**: o processo pericial, a **cadeia de custódia**, a **ordem da volatilidade**, a **forense de rede** (metodologia **OSCAR**, Wireshark, NetworkMiner), a aquisição de **evidências voláteis** (análise *in‑vivo*, memória RAM) e a análise **post‑mortem** de imagens de disco com **Volatility**, **FTK Imager**, **Guymager** e **Autopsy**. Fecha com a **forense de artefatos do Windows** (Registro, logs de evento, USB, e‑mail e navegador) — o "CSI Windows".

A ideia central: **toda ação do atacante deixa rastro, e todo rastro conta uma história — se for coletado e preservado corretamente**. Sem cadeia de custódia e sem respeitar a ordem da volatilidade, a melhor evidência vira inútil.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura — Para o alto e avante | Roteiro da fase: resposta a incidentes → logs/SIEM → perícia → rede → memória → post‑mortem → artefatos Windows. |
| 2 | Fundamentos e Resposta a Incidentes | Conceitos (risco, vulnerabilidade, ameaça, ataque), controles físicos/lógicos/administrativos, legislação e normas. O que é um **incidente**, seus tipos e **ciclo de vida**; objetivos da resposta (minimizar impacto, **conter**, **erradicar**, **recuperar**, **aprender**); plano de resposta (alinhado ao NIST SP 800‑61 e SANS PICERL). Estudos de caso. |
| 3 | Análise e Extração de Logs | Tipos de log (**servidores web** com códigos HTTP, **firewall**, **IDS/IPS Snort**), extração e preparação, e análise. Uso de **SIEM (Splunk)**: instalação, ingestão, busca e correlação de eventos para achar o que importa no meio do volume. |
| 4 | Perícia Digital e Forense | O **processo pericial** e o papel do perito; cenários (crime cibernético, vazamento, investigação interna, fraude). **Fontes de evidência** e a **ordem da volatilidade** (coletar primeiro o que some mais rápido). Introdução à **cadeia de custódia**. |
| 5 | Investigação de Tráfego e Redes | **Forense de rede**: análise de tráfego, detecção de intrusão, reconstrução de eventos e coleta de evidências. Metodologia **OSCAR** (Obtain, Strategize, Collect, Analyze, Report) em detalhe. Frameworks e ferramentas (**Wireshark**, **NetworkMiner**). Casos: DDoS e vazamento de dados. |
| 6 | Evidências Voláteis | **Análise *in‑vivo*** ("a quente"): aquisição de dados voláteis com o sistema ligado. Técnicas e ferramentas de aquisição de **memória RAM** e estado do sistema em **Windows** e **Linux**, respeitando a ordem da volatilidade. Boas práticas. |
| 7 | Artefatos e Evidências Post‑Mortem | **Perícia de memória RAM**: análise com **Volatility**/Rekall (processos, conexões, injeção, malware). Aquisição de **imagem forense** de disco (`dd`, **FTK Imager**, **Guymager**) com hash de integridade; análise de **sistemas de arquivos**; **relatório forense** e cadeia de custódia. Casos: Poison Ivy, WannaCry, fraude financeira. |
| 8 | CSI Windows | Forense de artefatos do Windows: **Registro** (chaves de execução, USBSTOR), **logs de evento** (.evtx), artefatos de rede e **dispositivos USB**. **Forense de e‑mail** (cabeçalhos, metadados, recuperação de deletados) e de **navegador** (histórico, cache, cookies, downloads, extensões). |

## 🔑 Conceitos-chave

- **Ciclo de resposta a incidentes (PICERL / NIST)**: Preparação → Identificação → Contenção → Erradicação → Recuperação → Lições aprendidas. Preparação e lições aprendidas são o que faz a resposta melhorar a cada incidente.
- **Conter antes de erradicar**: parar a propagação (isolar o host) vem antes de limpar, para não perder evidência nem deixar o atacante reagir.
- **Ordem da volatilidade**: colete primeiro o que desaparece mais rápido — registradores/cache → RAM → estado da rede/conexões → processos → disco → backups/mídia. Reiniciar a máquina destrói a memória, que muitas vezes é a evidência mais rica.
- **Cadeia de custódia (chain of custody)**: registrar quem coletou, quando, como e onde cada evidência ficou guardada. Sem isso, a evidência não tem valor legal.
- **Integridade por hash**: calcular MD5/SHA‑256 da imagem no momento da coleta e revalidar depois prova que nada foi alterado. Trabalhe sempre sobre uma **cópia**, nunca no original (write blocker).
- **In‑vivo × post‑mortem**: a análise in‑vivo captura o sistema vivo (RAM, conexões, processos) e perde‑se ao desligar; a post‑mortem analisa a imagem de disco com calma, mas não vê o que estava só na memória.
- **Forense de memória**: a RAM revela processos ocultos, injeção de código, malware sem arquivo (fileless), chaves de criptografia e conexões de C2 que não aparecem no disco. O Volatility é a ferramenta de referência.
- **SIEM e correlação**: um log isolado diz pouco; o valor está em correlacionar logs de várias fontes (web, firewall, IDS, endpoint) no tempo para reconstruir o ataque. Splunk, Elastic e Wazuh fazem isso.
- **OSCAR (forense de rede)**: Obtain information → Strategize → Collect evidence → Analyze → Report. Dá método à investigação de tráfego.
- **Artefatos do Windows contam a história**: o Registro, os logs .evtx, o histórico de navegador, os registros de USB e os metadados de e‑mail mostram o que foi executado, conectado e acessado — a base da timeline do incidente.
- **Timeline e relatório**: o produto final da perícia é uma linha do tempo reconstruída e um relatório claro, reprodutível e defensável, que qualquer perito possa auditar.

## 🛠️ Ferramentas e comandos

**Ferramentas:** Splunk (SIEM), Snort (IDS), Wireshark e NetworkMiner (rede), Volatility/Rekall (memória), FTK Imager/Guymager/`dd` (imagem), Autopsy/Sleuth Kit (disco), KAPE (coleta de artefatos Windows). Sempre sobre **cópias** e com **cadeia de custódia**.

```bash
# Integridade e imagem forense (sobre cópia; usar write blocker no original)
sha256sum evidencia.img
sudo dd if=/dev/sdb of=/casos/caso01.img bs=4M conv=noerror,sync status=progress
# (preferir FTK Imager / Guymager, que já geram hash e formato E01)

# Aquisição de memória (in-vivo)
# Windows: FTK Imager / WinPmem   ·   Linux: LiME, avml

# Análise de memória com Volatility 3
vol -f memoria.raw windows.info
vol -f memoria.raw windows.pslist          # processos
vol -f memoria.raw windows.netscan         # conexões de rede
vol -f memoria.raw windows.malfind         # injeção de código / fileless
vol -f memoria.raw windows.cmdline         # linha de comando dos processos

# Forense de disco e artefatos
mmls caso01.img ; fls -r -o <offset> caso01.img          # Sleuth Kit
# Autopsy para timeline, carving e navegação no sistema de arquivos

# Logs / SIEM (Splunk SPL)
index=web status=404 | stats count by clientip | sort -count     # varredura
index=firewall action=blocked | timechart count by dest_port     # picos / scan

# Rede
tshark -r captura.pcap -q -z conv,tcp        # conversas TCP
# NetworkMiner: extrair arquivos, credenciais e sessões de um PCAP
```

Códigos HTTP úteis em log de servidor web: **200** (ok), **401/403** (auth/proibido), **404** (não encontrado — varredura), **429** (rate limit), **500/503** (erro/indisponível).

## ❓ Perguntas de revisão

1. **Quais são as fases do ciclo de resposta a incidentes (PICERL/NIST)?**
   Preparação, Identificação (detecção), Contenção, Erradicação, Recuperação e Lições Aprendidas. A preparação e as lições aprendidas alimentam a melhoria contínua.
2. **Por que conter vem antes de erradicar?**
   Para parar a propagação e preservar a evidência antes de limpar. Erradicar sem conter pode espalhar o problema, alertar o atacante e destruir rastros.
3. **O que é a ordem da volatilidade e por que importa?**
   É a prioridade de coleta do mais volátil para o mais estável (RAM e conexões antes do disco). Importa porque dados voláteis somem ao desligar — reiniciar a máquina apaga a memória, muitas vezes a evidência mais valiosa.
4. **O que é cadeia de custódia e por que é essencial?**
   É o registro documentado de quem coletou, manuseou e guardou cada evidência, quando e como. Sem ela, a evidência pode ser contestada e perder validade legal.
5. **Por que se trabalha sobre uma cópia e com hash?**
   Para preservar o original intacto (usando write blocker) e provar, pelo hash calculado na coleta e revalidado depois, que a cópia analisada não foi alterada.
6. **Qual a diferença entre análise in‑vivo e post‑mortem?**
   A in‑vivo coleta o sistema ligado (RAM, processos, conexões) e capta o que só existe em execução; a post‑mortem analisa a imagem de disco com o sistema desligado, com mais calma, mas sem a memória volátil.
7. **O que a forense de memória revela que o disco não mostra?**
   Processos ocultos, injeção de código, malware sem arquivo (fileless), chaves de criptografia em uso e conexões de C2 ativas — tudo que vive na RAM e não é gravado no disco.
8. **O que é a metodologia OSCAR?**
   Um método de forense de rede: Obtain information, Strategize, Collect evidence, Analyze, Report. Organiza a investigação de tráfego do planejamento ao relatório.
9. **Como um SIEM ajuda numa investigação?**
   Centraliza e correlaciona logs de várias fontes no tempo, permitindo reconstruir a sequência do ataque e achar o relevante no meio do volume — em vez de olhar cada log isolado.
10. **Cite três artefatos do Windows úteis numa investigação e o que revelam.**
    O Registro (programas executados, dispositivos USB conectados), os logs de evento .evtx (logons, serviços, erros) e o histórico/cache do navegador (sites e downloads). Metadados de e‑mail revelam origem e trânsito das mensagens.

## 💼 Conexão com o mercado

- **SOC / DFIR (analista de resposta a incidentes / perito forense)**: esta é a fase mais diretamente profissional. Triagem de alertas, investigação com SIEM, coleta de evidências, análise de memória e disco, e produção de relatórios forenses são o dia a dia de N2/N3, times de IR e de perícia. A cadeia de custódia é requisito legal.
- **CompTIA Security+ (SY0‑701)** e CySA+: resposta a incidentes (ciclo, playbooks), análise de logs e SIEM, forense digital, cadeia de custódia e ordem da volatilidade aparecem em *Security Operations*. Esta fase também prepara para certificações de DFIR (GCFA, GCIH, GNFA).
- **Pós Tech em IA para Segurança**: DFIR gera volumes enormes de logs e telemetria — terreno fértil para ML (detecção de anomalia, clustering de eventos, triagem automática de alertas) e para LLMs que resumem incidentes e aceleram a investigação. A forense de memória e a correlação de logs são fontes de dados para esses modelos.

## 📖 Termos da fase

Incidente de segurança · Ciclo de resposta a incidentes (PICERL) · NIST SP 800‑61 · Contenção · Erradicação · Recuperação · Lições aprendidas · Playbook · SIEM · Splunk · SPL · Correlação de eventos · Log de servidor web · Código HTTP · Snort (IDS/IPS) · Log de firewall · Perícia digital (forense) · Processo pericial · Cadeia de custódia · Ordem da volatilidade · Write blocker · Integridade por hash · Imagem forense · dd · FTK Imager · Guymager · Autopsy / Sleuth Kit · Forense de rede · Metodologia OSCAR · Wireshark · NetworkMiner · Reconstrução de eventos · Análise in‑vivo · Evidência volátil · Forense de memória RAM · Volatility · Rekall · Fileless malware · Análise post‑mortem · Sistema de arquivos · Forense de artefatos do Windows · Registro do Windows · Log de evento (.evtx) · Forense de USB · Forense de e‑mail · Forense de navegador · Timeline · Relatório forense

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
