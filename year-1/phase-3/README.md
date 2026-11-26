# Year 1 · Phase 3 — Windows Server e Active Directory (Windows Server & Active Directory)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A terceira fase troca o pinguim pelo ecossistema Microsoft corporativo. Começa com a instalação do **Windows Server 2019** em VM (com um cliente Windows 10). Depois promove o servidor a **controlador de domínio** com **Active Directory** e organiza usuários, computadores, OUs e grupos. Em seguida sobe os serviços de infraestrutura (**DHCP** com failover e **DNS** com zonas e registros) e os serviços de rede (**VPN + NPS**, **NAT**, **IIS** e **WSUS**). Por fim, padroniza tudo com **GPO**. A fase fecha com fundamentos de **sistemas operacionais**: processos, threads, escalonamento e memória virtual.

A ideia central: **o Active Directory é o coração (e o alvo número 1) de uma rede Windows corporativa**. Quem controla o AD controla identidades, máquinas e políticas, e por isso entender como ele é montado é pré‑requisito para defendê‑lo.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Breve história do Windows Server (NT 3.1 em 1993, AD em 2000, Hyper‑V em 2008) e o roteiro da fase. |
| 2 | Instalação do Windows Server | Requisitos do Windows Server 2019, download das ISOs de avaliação (Server e Windows 10 Pro), criação da VM, instalação, configuração inicial, nome do servidor, IP fixo e idioma. |
| 3 | Controlador de domínio | Conceitos de AD e DNS. **Active Directory** como serviço de diretório; **controlador de domínio** (DC); **domínio**, **árvore** e **floresta**. Instalação da função AD DS, promoção do servidor e ferramentas de administração. |
| 4 | Usuários, OUs e grupos | Criar e editar contas, redefinir senha, usar uma conta modelo, mover entre OUs, grupo primário. **Unidades organizacionais**: criar, mover, remover e **delegar controle**. Ingressar computadores no domínio e redirecionar novos computadores. **Grupos** e aninhamento seguindo **AGDLP/AGUDLP** (conta → global → [universal] → domínio local → permissão). |
| 5 | DHCP e DNS | Funcionamento do DHCP (DORA), escopo, exclusões e reservas, **failover DHCP**. DNS: hierarquia e TLDs, zonas primária/secundária, zonas de pesquisa **direta** e **inversa**, registros (SOA, NS, A, AAAA, CNAME, MX, PTR), servidor secundário e **encaminhadores** (forwarders). |
| 6 | Serviços de rede | **VPN** no Windows Server (PPTP, L2TP/IPsec, SSTP, IKEv2) e opções de autenticação (PAP → CHAP → MS‑CHAPv2 → EAP). **NPS** (o servidor RADIUS da Microsoft) para políticas de acesso. **NAT** via RRAS, servidor web **IIS** e **WSUS** (grupos de computadores, aprovação automática, GPO apontando os clientes para o WSUS). |
| 7 | GPO | O que é uma Group Policy, ordem de processamento **LSDOU** (Local → Site → Domínio → OU; vence a mais próxima), **bloqueio de herança** × **forçado** (enforced), GPMC, armazenamento central, GPO de início (starter), **filtros WMI**, loopback, redirecionamento de pastas, instalação de software, papel de parede e **bloqueio de mídias removíveis**. |
| 8 | Fundamentos de sistemas operacionais (o arquivo tem título de Fortinet) | O SO como abstração e gerenciador de recursos, história em gerações, tipos de SO (grande porte, servidor, embarcado, tempo real, smart card...), **processos** (criação, término, hierarquia, estados), **threads**, **escalonamento** e **gerenciamento de memória**, incluindo **memória virtual** e paginação. |

## 🔑 Conceitos-chave

- **Serviço de diretório**: o AD é um banco central de objetos (usuários, computadores, grupos, OUs) que autentica pelo **Kerberos** e aplica políticas. O DC guarda uma cópia do banco e replica com os outros DCs.
- **Domínio × árvore × floresta**: o domínio é a fronteira administrativa (ex.: `empresa.local`). A árvore reúne domínios com namespace contíguo. A floresta é o limite máximo de confiança e de schema.
- **OU × grupo**: a OU **organiza** objetos e recebe GPOs e delegação. O grupo **dá permissão** a recursos. Os dois não se confundem.
- **AGDLP**: as contas entram em grupos globais (por função), os globais entram em grupos de domínio local (por recurso), e a permissão vai para o domínio local. Isso escala e facilita a auditoria.
- **Delegação de controle**: dar a um time (ex.: helpdesk) só o poder de resetar senhas numa OU aplica o menor privilégio no AD.
- **DHCP (DORA)**: Discover → Offer → Request → Acknowledge. O failover garante que a rede continue recebendo IP se um servidor cair.
- **DNS é dependência crítica do AD**: os clientes acham os DCs por registros SRV. Uma zona inversa (PTR) ajuda na investigação; forwarders resolvem nomes externos.
- **GPO e LSDOU**: as políticas são aplicadas em camadas, e a última aplicada (a mais próxima do objeto) vence, a menos que alguma esteja **enforced** ou haja **block inheritance**.
- **Gestão de patches (WSUS)**: aprovar e distribuir atualizações de forma centralizada reduz a janela de exposição a CVEs conhecidas.
- **Processo × thread × memória virtual**: o processo tem espaço de endereçamento próprio; as threads compartilham esse espaço. A memória virtual mapeia páginas lógicas em molduras físicas. Esses conceitos são a base para análise de malware e forense de memória.

## 🛠️ Ferramentas e comandos

**Ambiente:** VirtualBox com Windows Server 2019 (DC + DHCP + DNS + RRAS/NPS + IIS + WSUS) e cliente Windows 10 Pro.

**Consoles:** Server Manager · Active Directory Users and Computers (ADUC) · DHCP · DNS Manager · Routing and Remote Access (RRAS) · NPS · IIS Manager · WSUS · Group Policy Management (GPMC).

```powershell
# Rede e identidade
ipconfig /all; ipconfig /release; ipconfig /renew; ipconfig /flushdns
hostname; whoami /groups; systeminfo
Rename-Computer -NewName SERV-01 -Restart
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.1 -PrefixLength 24 -DefaultGateway 192.168.1.254

# AD DS
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "empresa.local"
New-ADOrganizationalUnit -Name "TI"; New-ADUser -Name "ana" -Path "OU=TI,DC=empresa,DC=local"
Add-ADGroupMember -Identity "GG_TI" -Members ana; Get-ADUser -Filter * | Select Name
Add-Computer -DomainName empresa.local -Restart          # no cliente
redircmp "OU=Computadores,DC=empresa,DC=local"           # novos computadores

# DNS / DHCP
nslookup serv-01.empresa.local; nslookup 192.168.1.1
Get-DhcpServerv4Scope; Get-DhcpServerv4Lease -ScopeId 192.168.1.0

# GPO
gpupdate /force; gpresult /r; gpresult /h relatorio.html; rsop.msc
```

## 🧪 Atividades / CTFs

A pasta `CTF` desta fase está vazia. A prática vem dos **laboratórios guiados** dos materiais:

- Instalar o Windows Server 2019 e um cliente Windows 10 em VM, com IP fixo e nome no servidor.
- Promover o servidor a DC (nova floresta) e criar OUs, usuários, computadores e grupos no modelo AGDLP.
- Delegar a redefinição de senhas de uma OU.
- Configurar DHCP (escopo, reserva e failover) e DNS (zonas direta e inversa, registros, servidor secundário e forwarders).
- Montar uma VPN com RRAS e NPS e conectar o Windows 10. Configurar NAT, publicar um site no IIS e montar o WSUS com aprovação automática e GPO.
- Criar GPOs: papel de parede, bloqueio de USB, redirecionamento de pastas, instalação de software, filtro WMI, block inheritance e enforced.

> 💡 Dica de homelab: monte o mesmo AD e depois rode **PingCastle** ou **BloodHound** (em modo de auditoria) para ver como um atacante enxergaria o domínio. Ative a auditoria avançada e o Sysmon e encaminhe os eventos para um SIEM gratuito (Wazuh, Splunk Free) para treinar detecção.

## ❓ Perguntas de revisão

1. **Qual a diferença entre domínio, árvore e floresta no AD?**
   O domínio é a unidade administrativa e de replicação. A árvore é um conjunto de domínios com namespace contíguo (`empresa.local`, `rh.empresa.local`). A floresta reúne uma ou mais árvores que compartilham schema e confiança, e é a verdadeira fronteira de segurança.
2. **OU ou grupo: qual usar para aplicar uma GPO e qual para dar acesso a uma pasta?**
   A GPO e a delegação são vinculadas a **OUs**. A permissão em recursos (pastas, impressoras) vai para **grupos**.
3. **Explique o modelo AGDLP.**
   As contas (A) entram em grupos globais (G) por função. Os globais entram em grupos de domínio local (DL) por recurso, e a permissão (P) é dada ao DL. Em várias florestas/domínios, entra um grupo universal (U): AGUDLP.
4. **Quais são as quatro mensagens do DHCP?**
   DORA: Discover (o cliente procura um servidor), Offer (o servidor oferece um IP), Request (o cliente pede o IP oferecido) e Acknowledge (o servidor confirma a concessão).
5. **Para que servem a zona de pesquisa inversa e os forwarders?**
   A zona inversa resolve IP → nome (registros PTR), o que ajuda em logs e investigações. Os forwarders mandam para outro DNS (ex.: do provedor) as consultas de nomes que o servidor local não conhece.
6. **Em que ordem as GPOs são processadas e qual vence em conflito?**
   LSDOU: Local → Site → Domínio → OU (pai, depois filha). Em conflito vence a última aplicada, ou seja, a mais próxima do objeto, a não ser que uma GPO superior esteja marcada como *Enforced*.
7. **Qual a diferença entre Block Inheritance e Enforced?**
   O Block Inheritance (na OU) impede que GPOs de níveis acima sejam herdadas. O Enforced (no link da GPO) faz a política valer mesmo com bloqueio de herança e ganhar dos conflitos nos níveis abaixo.
8. **Por que o PAP é o protocolo de autenticação de VPN menos seguro?**
   Porque envia a senha em texto claro. CHAP e MS‑CHAPv2 usam desafio‑resposta, e EAP (com certificados ou PEAP) é a opção mais robusta.
9. **Qual o papel do NPS e do WSUS na segurança?**
   O NPS é o servidor RADIUS da Microsoft: centraliza a autenticação e as políticas de acesso para VPN, Wi‑Fi e 802.1X. O WSUS centraliza a aprovação e distribuição de patches, o que reduz a exposição a vulnerabilidades conhecidas.
10. **Qual a diferença entre processo e thread?**
    O processo é um programa em execução com espaço de memória e recursos próprios. A thread é uma linha de execução dentro do processo: várias threads compartilham a memória do mesmo processo, então são mais leves de criar e alternar.

## 💼 Conexão com o mercado

- **SOC (analista N1/N2)**: a maioria das empresas usa AD, e grande parte dos incidentes envolve credenciais e movimento lateral no domínio. É rotina investigar eventos de logon (4624/4625), bloqueio de conta (4740), criação ou alteração de usuário e grupo (4720/4728/4732) e alterações de GPO. Também é preciso reconhecer abuso de contas privilegiadas e de delegação. DNS e DHCP são fontes de log essenciais para dizer "qual máquina tinha esse IP".
- **CompTIA Security+ (SY0‑701)**: gestão de identidade e acesso (contas, grupos, menor privilégio, delegação), serviços de diretório e Kerberos, políticas de grupo como controle de configuração, gestão de patches, VPN e protocolos de autenticação (PAP/CHAP/EAP, RADIUS) caem em *Security Architecture* e *Security Operations*.
- **Pós Tech em IA para Segurança**: as soluções de UEBA e ITDR usam modelos que aprendem o comportamento normal de logon no AD (horários, máquinas, volume) para detectar comprometimento de conta. Os conceitos de processo, thread e memória são a base para modelos de detecção de malware em endpoint (EDR).

## 📖 Termos da fase

Windows Server · Active Directory (AD) · AD DS · Controlador de domínio (DC) · Domínio · Árvore · Floresta · Kerberos · Unidade organizacional (OU) · Grupo global / domínio local / universal · AGDLP · Delegação de controle · DHCP · DORA · Failover DHCP · Zona DNS (direta/inversa) · Registros DNS (A, PTR, SRV, MX, CNAME, SOA) · Forwarder · VPN (PPTP, L2TP, SSTP, IKEv2) · PAP/CHAP/MS‑CHAPv2/EAP · NPS · RRAS · IIS · WSUS · GPO · GPMC · LSDOU · Block inheritance · Enforced · Filtro WMI · Loopback · Sistema operacional · Processo · Thread · Escalonamento · Memória virtual · Paginação

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
