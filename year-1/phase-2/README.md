# Year 1 · Phase 2 — Linux: Administração, Serviços e Hardening (Linux Administration, Services & Hardening)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses.

## 🧭 Visão geral

A segunda fase transforma o Linux em ferramenta de trabalho. A jornada vai da história do Unix/GNU/Linux e da instalação de um servidor (família Red Hat/CentOS, com DNF) e de um desktop (Debian) em máquina virtual até o **domínio do terminal**: comandos básicos, permissões, usuários, vim, systemd, logs, discos/LVM, kernel e performance. Depois vem o shell avançado (pipes, redirecionamento, awk/sed). Com o sistema dominado, a fase **sobe serviços** (SSH, FTP/SFTP, rsync, NFS, cron, Apache/NGINX, MySQL), estuda **por que esses serviços são atacados** (texto claro, injeção, CVE/CVSS) e termina no **hardening** com CIS Benchmark, política de senhas (PAM), firewalld e auditd.

A ideia central: **todo serviço exposto é superfície de ataque**. Quem sabe instalar, configurar e ler os logs de um serviço também sabe protegê‑lo e investigá‑lo.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Roteiro: dominar o sistema operacional Linux, seus protocolos e serviços, para chegar às primeiras análises de tráfego e vulnerabilidades. |
| 2 | História e instalação | Da Multics ao Unix (Bell Labs), MINIX, Linus Torvalds e o projeto GNU (GNU/Linux). Uso profissional do Linux (servidores, embarcados, cloud). Instalação passo a passo de um servidor e de um desktop em VirtualBox, com boas práticas de particionamento/LVM, senha de root, atualização e primeiro acesso remoto. |
| 3 | Bash e comandos básicos | Shell × terminal × console, usuário comum × root, sintaxe de comandos, `man`/`--help`. Administração (`sudo`, `su`, `df`, `id`, `w`, `ip`, `top`, `ps`, `kill`, `dnf`), arquivos e permissões (`ls`, `cp`, `mv`, `rm`, `ln`, `chown`, `chmod`), visualização (`cat`, `tail`, `head`), `tar`/`gzip`/`find` e usuários/grupos (`useradd`, `usermod`, `groupadd`, `passwd`, `getent`). |
| 4 | Administração do sistema | Editor vim (modos normal, inserção e comando). Inventário de hardware/kernel, hostname, DNS, interfaces e rotas. **systemd**: units `.service` e `systemctl` (start/stop/restart/enable/disable). Logs com `journalctl` e `rsyslogd`. |
| 5 | Discos, kernel e performance | Particionamento (MBR/GPT, boot × dados), **LVM** (PV → VG → LV, aumentar volume e filesystem), EXT4 × XFS, hierarquia **FHS**, `/etc/fstab`, `mount`/`umount`. Ajuste de kernel com `sysctl` (ex.: `vm.swappiness`). Performance com `iostat`, `sar`, `vmstat`; rede com `ss` e `tcpdump`. |
| 6 | Shell avançado | Fluxos padrão (stdin 0, stdout 1, stderr 2) e descritores de arquivo, pipes, `wc`/`cut`/`grep`/`sort`/`uniq`. Globbing, variáveis, aliases, redirecionamento, histórico (Ctrl+R) e atalhos. Geração e cálculo de texto (`echo`, `printf`, `seq`, `expr`, `bc`) e transformação (`tr`, `rev`, `awk`, `sed`). |
| 7 | Serviços essenciais | OpenSSH (`sshd`, cliente `ssh`), Telnet (e por que não usar), transferência com SCP/SFTP, FTP/FTPS (`vsftpd`, `lftp`) e `rsync` local/remoto. Compartilhamento com NFS (exportar e montar). Agendamento com `cron`/`crontab`. |
| 8 | Stack web (LAMP) | Instalação e configuração do Apache HTTP Server e do NGINX (arquivos de configuração, troca do site padrão). MySQL Server: `mysql_secure_installation`, criação de usuário, liberação de acesso externo e teste de conexão. |
| 9 | Serviços de rede ameaçados | **CVE** (catálogo público mantido pelo MITRE) e **CVSS** (nota de 0 a 10 mantida pelo FIRST). Riscos por protocolo: HTTP em texto claro × HTTPS e injeção em aplicações web; POP/IMAP/SMTP; FTP × FTPS; NFSv3/NFSv4 e SMB; SSH × Telnet. Relatórios Shadowserver sobre serviços expostos. |
| 10 | Hardening e firewall | Conceito de **hardening** e o **CIS Benchmark** como referência. Política de senhas (`login.defs`, `chage`, padrões do `useradd`, PAM/pwquality). **firewalld** com `firewall-cmd`: zonas, regras runtime × permanentes. Auditoria com **auditd** (`auditd.conf`, regras, `auditctl`, leitura dos logs de auditoria). |
| — | Cheat sheet de CTF | Guia de comandos para manipular texto e dados: `grep`, `cut`, `sort`/`uniq`, `awk`, `sed`, `tr`, `wc`, `file`/`strings`, `xxd`/`hexdump`, `base64`. |

## 🔑 Conceitos-chave

- **Kernel × distribuição**: o Linux é o kernel. A distribuição junta kernel, ferramentas GNU, gerenciador de pacotes (DNF/RPM na família Red Hat, APT/DEB no Debian) e configurações.
- **Tudo é arquivo**: dispositivos (`/dev`), processos (`/proc`), configurações (`/etc`) e logs (`/var/log`) seguem a hierarquia FHS. Saber onde fica cada coisa é metade da investigação.
- **Permissões (DAC)**: dono/grupo/outros × leitura/escrita/execução (`rwx`, octal 755/644). Bits especiais: SUID, SGID e sticky bit. O princípio do menor privilégio (least privilege) começa aqui: use `sudo`, não fique logado como root.
- **systemd**: gerencia serviços (units), dependências, inicialização e logs (journal). `enable` controla se o serviço sobe no boot; `start`, se ele roda agora.
- **Logs**: `journalctl` e `/var/log/*` (rsyslog) são a primeira fonte de evidência. É neles que aparecem tentativas de login, quedas de serviço e erros.
- **LVM**: separa discos físicos de volumes lógicos e permite crescer filesystems sem reformatar.
- **Filosofia Unix**: ferramentas pequenas combinadas por pipes. `grep | cut | sort | uniq -c | sort -n` vira um mini‑SIEM no terminal.
- **Texto claro (cleartext)**: Telnet, FTP, HTTP, POP/IMAP sem TLS expõem credenciais para qualquer sniffer. A troca é SSH, SFTP/FTPS, HTTPS e versões com TLS.
- **CVE × CVSS**: o CVE identifica a vulnerabilidade (CVE‑ano‑número); o CVSS mede a gravidade (0–10: baixa, média, alta, crítica) e ajuda a priorizar patches.
- **Hardening**: reduzir a superfície de ataque com serviços mínimos, senhas fortes, firewall default‑deny, atualizações e auditoria. O CIS Benchmark dá a lista de verificação.
- **Runtime × permanente (firewalld)**: uma regra sem `--permanent` some no próximo reload/reboot.

## 🛠️ Ferramentas e comandos

**Ambiente:** VirtualBox com um servidor da família Red Hat/CentOS (DNF) e um desktop Debian. Ferramentas: Bash, vim, OpenSSH, vsftpd, lftp, rsync, NFS, cron, Apache, NGINX, MySQL, firewalld, auditd, tcpdump.

```bash
# Sistema e processos
uname -r; cat /etc/os-release; lscpu; free -h; df -h; lsblk
ps aux | grep sshd; top; kill -15 <pid>; id; w; who
sudo dnf update; sudo dnf install httpd

# Arquivos e permissões
ls -la; chmod 640 arquivo; chown user:grupo arquivo; ln -s alvo link
find / -perm -4000 -type f 2>/dev/null        # binários SUID (auditoria)
tar -czvf backup.tar.gz /etc

# Usuários
useradd -m -s /bin/bash ana; passwd ana; usermod -aG wheel ana; getent passwd ana
chage -l ana; chage -M 90 ana                  # política de expiração

# Serviços e logs
systemctl status|start|enable sshd; systemctl list-units --type=service
journalctl -u sshd --since today; tail -f /var/log/secure

# Rede
ip a; ip route; ss -tulpn; tcpdump -i eth0 port 22 -nn

# Discos / LVM
pvcreate /dev/sdb; vgcreate vgdados /dev/sdb; lvcreate -L 5G -n lvapp vgdados
mkfs.xfs /dev/vgdados/lvapp; mount /dev/vgdados/lvapp /app; lvextend -r -L +2G /dev/vgdados/lvapp
sysctl -a | grep swappiness; sysctl -w vm.swappiness=10

# Shell / texto (análise de log)
grep "Failed password" /var/log/secure | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
cut -d: -f1 /etc/passwd; sed 's/http:/https:/g' arq; echo dGVzdGU= | base64 -d

# Serviços
ssh user@host; scp arq user@host:/tmp; sftp user@host; rsync -avz dir/ user@host:/bkp/
crontab -e    # 0 2 * * * /usr/local/bin/backup.sh
mysql_secure_installation

# Hardening
firewall-cmd --get-active-zones; firewall-cmd --list-all
firewall-cmd --add-service=http --zone=public --permanent; firewall-cmd --reload
auditctl -w /etc/passwd -p wa -k passwd_changes; ausearch -k passwd_changes
```

## 🧪 Atividades / CTFs

- **CTF de Linux**: a pasta da fase tem uma cheat sheet de manipulação de texto e dados, que é o tipo de habilidade cobrada no desafio. Os temas: filtrar logs de autenticação (ex.: falhas de login em FTP), extrair IPs e usuários, contar ocorrências, identificar tipos de arquivo, extrair strings de binários e decodificar hex/Base64. *(Sem respostas aqui.)*
- **Labs práticos dos materiais**: instalar servidor e desktop em VM; criar usuários e permissões; configurar a rede; criar PV/VG/LV e montar via fstab; subir SSH, vsftpd, NFS e cron; publicar um site em Apache/NGINX e conectar ao MySQL remotamente; aplicar política de senhas, regras do firewalld e regras do auditd.

> 💡 Dica de homelab: repetir tudo numa VM Rocky/AlmaLinux (substitutos do CentOS) e numa Debian/Ubuntu. Depois, rodar um scanner como Lynis ou o CIS‑CAT Lite e comparar a nota antes e depois do hardening.

## ❓ Perguntas de revisão

1. **Qual a diferença entre `systemctl start` e `systemctl enable`?**
   `start` sobe o serviço agora; `enable` faz ele subir automaticamente no boot. Os dois são independentes (`enable --now` faz ambos).
2. **O que significa a permissão `750` em um diretório?**
   Dono: rwx (7); grupo: r‑x (5); outros: nenhuma (0). O grupo pode entrar e listar, mas não pode escrever, e os demais usuários não acessam.
3. **Por que procurar binários SUID numa auditoria?**
   Um binário SUID roda com o privilégio do dono (muitas vezes root). Se for vulnerável ou mal configurado, vira caminho de escalada de privilégio (privilege escalation).
4. **O que acontece com stdout e stderr em `cmd > saida.txt 2>&1`?**
   O stdout (fd 1) vai para o arquivo, e o stderr (fd 2) é redirecionado para onde o fd 1 aponta. Ou seja, as duas saídas vão para `saida.txt`.
5. **Como montar um pipeline que conta tentativas de login falhas por IP?**
   `grep "Failed password" /var/log/secure | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`: filtra, extrai o campo do IP, agrupa e ordena pelo número de ocorrências.
6. **Quais são as camadas do LVM e qual a vantagem dele?**
   Physical Volume (disco/partição) → Volume Group (pool) → Logical Volume (onde fica o filesystem). A vantagem é crescer ou mover volumes sem reparticionar, por exemplo com `lvextend -r`.
7. **Por que Telnet e FTP são considerados inseguros?**
   Transmitem usuário, senha e dados em texto claro; qualquer um que capture o tráfego (sniffing/MitM) lê as credenciais. Os substitutos são SSH e SFTP/FTPS.
8. **Qual a diferença entre CVE e CVSS?**
   O CVE é o identificador único de uma vulnerabilidade conhecida (catálogo do MITRE). O CVSS é a nota de 0 a 10 que mede a gravidade dela e orienta a prioridade de correção.
9. **Uma regra criada com `firewall-cmd --add-port=80/tcp` sobrevive a um reboot?**
   Não. Ela é de runtime. É preciso repetir o comando com `--permanent` (ou usar `--runtime-to-permanent`) e depois `--reload`.
10. **Para que serve o auditd e um exemplo de regra útil?**
    Ele registra eventos de segurança no nível do kernel (acesso a arquivos, chamadas de sistema). Exemplo: `auditctl -w /etc/passwd -p wa -k passwd_changes` registra qualquer escrita ou alteração de atributo no arquivo de usuários.

## 💼 Conexão com o mercado

- **SOC (analista N1/N2)**: boa parte dos servidores, appliances e sensores (SIEM, IDS, proxies) roda Linux. Em uma investigação, é comum ter que acessar via SSH, ler `/var/log/secure` ou `auth.log`, o `journalctl` e os logs do auditd, e montar pipelines com grep/awk para triagem rápida. Detectar força bruta em SSH/FTP é um caso de uso clássico.
- **CompTIA Security+ (SY0‑701)**: hardening, baseline (CIS), menor privilégio, protocolos seguros × inseguros (SSH × Telnet, SFTP × FTP, HTTPS × HTTP), gestão de vulnerabilidades (CVE/CVSS), política de senhas e logs de auditoria aparecem em *Security Operations* e *Security Architecture*.
- **Pós Tech em IA para Segurança**: pipelines de dados de segurança, coleta de logs e treino de modelos rodam quase sempre em Linux. Saber transformar logs brutos (awk/sed, journald) em dados estruturados é pré‑requisito para usar ML em detecção de anomalias de autenticação.

## 📖 Termos da fase

Kernel · Distribuição (distro) · GNU/Linux · Shell/Bash · Root · sudo · Gerenciador de pacotes (DNF/APT) · Permissões rwx · chmod/chown · SUID · Menor privilégio (least privilege) · Processo/PID · Sinal (signal) · Daemon · systemd · systemctl · journalctl · rsyslog · vim · FHS · Sistema de arquivos (EXT4/XFS) · fstab · LVM (PV/VG/LV) · sysctl · ss · tcpdump · stdin/stdout/stderr · Pipe · Redirecionamento · Globbing · awk · sed · grep · Base64 · SSH · Telnet · SFTP/SCP · FTP/FTPS · rsync · NFS · cron · LAMP · Apache · NGINX · MySQL · Texto claro (cleartext) · Injeção (injection) · CVE · CVSS · Hardening · CIS Benchmark · PAM · firewalld · auditd

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
