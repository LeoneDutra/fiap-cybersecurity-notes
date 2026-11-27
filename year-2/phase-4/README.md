# Year 2 · Phase 4 — Segurança de Aplicações Web e Mobile (Web & Mobile Application Security)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. **Foco conceitual, de correção e de defesa. Todo teste pressupõe aplicação própria/autorizada em laboratório.**

## 🧭 Visão geral

A fase tem duas metades: **segurança de aplicações web** e **segurança mobile (Android)**. Na web, parte dos fundamentos (HTTP/HTTPS, metodologia **PTES**, **OWASP Top 10**), passa pelas ferramentas de avaliação (**Burp Suite**, gobuster/FFUF para descoberta, fuzzing) e estuda as **vulnerabilidades web mais comuns** — cada uma com "exemplo" e, principalmente, **"como corrigir"**: bypass de autenticação/autorização, command injection, directory traversal, LFI/RFI, **SQL injection** (incl. blind), **XSS**, **CSRF**, **XXE** e **SSRF** — além da automação (WPScan, Nuclei, Metasploit). Na parte mobile, cobre a **arquitetura de segurança do Android** (sandbox, permissões, assinatura de app, SEAndroid), a **montagem do laboratório** (ADB, JADX, APKTool, Android Studio) e a **análise híbrida** (estática + dinâmica) de um APK, incluindo o **AndroidManifest** e seus componentes (Activity, Service, Content Provider, Broadcast Receiver, Intent).

A ideia central: **a aplicação é a superfície mais exposta e mais atacada**. Entender a vulnerabilidade é o pré‑requisito para **corrigi‑la no código** — e esta fase sempre liga o "como se explora" ao "como se conserta".

## 📚 Resumo por material

| # | Tema | O que fica (ênfase em correção) |
|---|---|---|
| 1 | Abertura — Hacker Attack | Roteiro: fundamentos web → ferramentas → ataques comuns → automação → mobile (Android). |
| 2 | Web Scope e Metodologias | **HTTP/HTTPS** e utilitários de linha de comando; o que é **pentest** e seus tipos; a metodologia **PTES** (fases) e o **OWASP Top 10** como mapa das vulnerabilidades prioritárias. |
| 3 | Web Assessment Basics | **Proxy de interceptação** e o **Burp Suite** (Community × Pro, interceptar HTTP/HTTPS). Descoberta de arquivos/diretórios ocultos (**gobuster**, **FFUF**), métodos de autenticação web e **fuzzing** com Burp Intruder/FFUF. |
| 4 | Common Web Attacks | O coração da fase: **bypass de auth**, **command injection**, **directory traversal**, **LFI/RFI**, **SQL injection** e **blind SQLi** (e o sqlmap), **XSS**, **CSRF**, **XXE** e **SSRF**. Para **cada** uma: código vulnerável, como ocorre e **como corrigir** (validação, parametrização, codificação de saída, allowlists, tokens anti‑CSRF, desabilitar entidades XML externas etc.). |
| 5 | Automate Web Attacks | Automação da avaliação: **WPScan** (CMS WordPress), **Nuclei** (templates de detecção) e **Metasploit**. A leitura defensiva: a mesma velocidade que o atacante tem para varrer é a que o time de segurança precisa para achar e corrigir antes. |
| 6 | Mobile Security Basics | **Arquitetura do Android**: kernel Linux, HAL, **ART**, bibliotecas nativas, Java API Framework, system apps. **Sandbox** por app, **permissões**, **SEAndroid**, verificação de integridade e o **processo de assinatura** (v1/v2/v3) com boas práticas de segurança. |
| 7 | Mobile Assessment Configuration | Montar o laboratório Android: **ADB** (comandos de conexão, instalar APK, shell), **JADX** (decompilar para Java), **APKTool** (desmontar/remontar recursos e smali) e **Android Studio**/emulador. |
| 8 | Android Hybrid Analysis | **Análise estática + dinâmica** de um APK (app de treino InjuredAndroid). O **AndroidManifest.xml**: estrutura, componentes (**Activity, Service, Content Provider, Broadcast Receiver**) e **Intents**; vulnerabilidades detectáveis no manifest (componentes exportados, `debuggable`, `allowBackup`) e como achá‑las. |

## 🔑 Conceitos-chave

- **OWASP Top 10**: o consenso das falhas mais críticas em aplicações web (Broken Access Control, Injection, SSRF etc.). É o checklist de partida tanto para atacar quanto para **priorizar correções**.
- **PTES**: metodologia de pentest em fases (pré‑engajamento, coleta, modelagem de ameaça, análise de vulnerabilidade, exploração, pós‑exploração, relatório). Dá rigor e escopo.
- **Proxy de interceptação (Burp)**: fica entre o navegador e o servidor para ler e modificar requisições — a ferramenta central do teste web. A defesa: validar **sempre no servidor**, pois o cliente é controlável pelo atacante.
- **Injection (a mãe de várias falhas)**: SQLi, command injection, LFI/RFI e XXE têm a mesma raiz — **entrada não confiável tratada como código/consulta**. A correção também é comum: separar dados de instruções (queries parametrizadas/prepared statements, APIs seguras, allowlists, parsers sem entidades externas).
- **SQL Injection × Blind SQLi**: na clássica, o resultado aparece; na blind, infere‑se pela resposta/tempo. Correção: **prepared statements/ORM**, menor privilégio no banco, validação.
- **XSS**: injetar script que roda no navegador da vítima. Correção: **codificação de saída** por contexto, Content Security Policy (CSP) e sanitização de HTML.
- **CSRF**: fazer o navegador autenticado da vítima enviar uma ação sem querer. Correção: **tokens anti‑CSRF**, `SameSite` nos cookies e revalidação de ações sensíveis.
- **XXE**: abuso de entidades externas em XML para ler arquivos ou fazer SSRF. Correção: **desabilitar entidades externas** no parser.
- **SSRF**: forçar o servidor a fazer requisições para destinos internos. Correção: **allowlist de destinos**, bloquear IPs internos/metadados de cloud, validar URLs.
- **Modelo de segurança do Android**: cada app roda em **sandbox** com UID próprio; recursos sensíveis exigem **permissões**; o SO verifica a **assinatura** do APK. Falhas comuns do app vêm de **componentes exportados** sem proteção e de armazenamento inseguro.
- **Análise estática × dinâmica (mobile)**: a estática lê o código (JADX/APKTool, manifest); a dinâmica observa o app rodando (ADB, instrumentação). Juntas, dão o quadro completo — e revelam onde o desenvolvedor precisa corrigir.

## 🛠️ Ferramentas e abordagem

**Web:** Burp Suite, gobuster, FFUF, sqlmap, WPScan, Nuclei, Metasploit, curl. **Mobile:** ADB, JADX, APKTool, Android Studio/emulador, app de treino InjuredAndroid. **Tudo em aplicações próprias ou autorizadas, em laboratório.**

```bash
# Web — reconhecimento e avaliação (em alvo autorizado)
curl -i https://alvo.exemplo/                     # ver cabeçalhos / respostas HTTP
gobuster dir -u https://alvo.exemplo -w wordlist.txt       # diretórios ocultos
ffuf -u https://alvo.exemplo/FUZZ -w wordlist.txt          # fuzzing de caminhos
# Burp Suite: interceptar, repetir (Repeater) e fuzzing (Intruder)

# Automação (defensiva: rodar contra os próprios ativos para achar antes)
wpscan --url https://meusite.exemplo --enumerate vp        # vulnerabilidades do WordPress
nuclei -u https://meusite.exemplo -t cves/                 # templates de detecção
# sqlmap só contra aplicação própria/autorizada, para validar a correção

# Mobile — laboratório Android (APK próprio/de treino)
adb devices ; adb install app.apk ; adb shell
apktool d app.apk            # desmontar recursos + smali
jadx -d saida app.apk        # decompilar para Java (análise estática)
# inspecionar o AndroidManifest.xml: componentes exported, debuggable, allowBackup
```

**Padrões de correção (o que a fase enfatiza):**

```text
Injection/SQLi → prepared statements/ORM; validação; menor privilégio no banco
Command inj.   → evitar shell; APIs seguras; allowlist de argumentos
Path traversal → canonicalizar e validar caminhos; allowlist; sem concatenar input
XSS            → output encoding por contexto; CSP; sanitização de HTML
CSRF           → token anti-CSRF; cookies SameSite; reautenticar ações sensíveis
XXE            → desabilitar DTD/entidades externas no parser XML
SSRF           → allowlist de destinos; bloquear IP interno/metadados; validar URL
Android        → não exportar componentes sem necessidade; sem debuggable/allowBackup
                 em produção; armazenamento seguro; validar input de Intents
```

## ❓ Perguntas de revisão

1. **O que é o OWASP Top 10 e para que serve?**
   É a lista de consenso das vulnerabilidades mais críticas em aplicações web. Serve como mapa de prioridade tanto para testar quanto para corrigir e treinar desenvolvedores.
2. **Qual a raiz comum de SQLi, command injection, LFI/RFI e XXE, e a direção de correção?**
   Entrada não confiável tratada como código/consulta/caminho. A correção separa dados de instruções: prepared statements, APIs seguras, allowlists e parsers sem entidades externas.
3. **Como se corrige SQL Injection de forma robusta?**
   Com prepared statements/consultas parametrizadas (ou ORM), validação de entrada e menor privilégio da conta de banco. Concatenar input na query é o antipadrão.
4. **Qual a diferença entre SQLi clássico e blind, e como detectar o blind?**
   No clássico o resultado volta na resposta; no blind, infere‑se pela diferença de comportamento (booleano) ou pelo tempo de resposta (time‑based). A correção é a mesma.
5. **O que é XSS e como mitigá‑lo?**
   Injeção de script que executa no navegador da vítima. Mitiga‑se com codificação de saída por contexto, Content Security Policy (CSP) e sanitização de HTML; nunca confiar em validação só no cliente.
6. **O que é CSRF e quais as defesas?**
   Forçar o navegador autenticado da vítima a executar uma ação indesejada. Defesas: tokens anti‑CSRF, cookies `SameSite` e reautenticação de ações sensíveis.
7. **O que é SSRF e como se defende?**
   Fazer o servidor emitir requisições a destinos escolhidos pelo atacante (muitas vezes internos/metadados de cloud). Defesa: allowlist de destinos, bloquear faixas internas e validar/normalizar URLs.
8. **Como o modelo de sandbox e permissões do Android protege o usuário?**
   Cada app roda isolado com UID próprio e só acessa recursos sensíveis mediante permissões concedidas; o SO valida a assinatura do APK. Isso limita o que um app malicioso (ou comprometido) alcança.
9. **Por que o AndroidManifest é central na análise de segurança de um app?**
   Porque declara componentes (Activity, Service, Content Provider, Broadcast Receiver), permissões e flags. Componentes exportados sem proteção, `debuggable` e `allowBackup` em produção são achados comuns.
10. **Qual a diferença entre análise estática e dinâmica de um APK?**
    A estática examina o código e os recursos sem executar (JADX, APKTool, manifest); a dinâmica observa o app em execução (ADB, instrumentação, tráfego). A híbrida combina as duas para um retrato completo.

## 💼 Conexão com o mercado

- **AppSec / Pentester web e mobile**: é a base direta do analista de segurança de aplicações. Testar contra o OWASP Top 10, usar Burp, triar achados de Nuclei/WPScan e, acima de tudo, **recomendar a correção no código** são tarefas diárias. A parte mobile atende ao mercado crescente de segurança de apps (OWASP MASVS/MASTG).
- **CompTIA PenTest+ / Security+**: ataques a aplicações web, injeção, XSS/CSRF, ferramentas de avaliação, e segurança mobile aparecem em *Attacks and Exploits* e *Security Architecture*. A ênfase em secure coding conecta com *Software/Systems security*.
- **Pós Tech em IA para Segurança**: WAFs modernos e scanners (DAST) usam ML para reduzir falso‑positivo e detectar payloads ofuscados; LLMs já revisam código em busca das falhas desta fase. A análise de apps em escala (triagem de milhares de APKs) é um problema clássico de ML.

## 📖 Termos da fase

HTTP/HTTPS · Pentest web · PTES · OWASP Top 10 · Proxy de interceptação · Burp Suite · gobuster · FFUF · Web fuzzing · Broken Access Control · Bypass de autenticação/autorização · Command injection · Directory traversal · LFI / RFI · SQL Injection · Blind SQLi · sqlmap · XSS · CSP · CSRF · SameSite · XXE · SSRF · WPScan · Nuclei · Metasploit · Searchsploit · Segurança mobile · Arquitetura do Android · ART · Sandbox de app · Permissões Android · SEAndroid · Assinatura de APK (v1/v2/v3) · ADB · JADX · APKTool · smali · Android Studio / emulador · Análise estática × dinâmica · AndroidManifest.xml · Activity · Service · Content Provider · Broadcast Receiver · Intent · Componente exportado · InjuredAndroid

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
