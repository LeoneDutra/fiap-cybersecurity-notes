# Year 1 · Phase 5 — Arquitetura, Binários e Segurança de Memória (Computer Architecture, Binaries & Memory Safety)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. Foco conceitual e defensivo — sem passo a passo ofensivo.

## 🧭 Visão geral

A quinta fase desce para o nível mais baixo da máquina. Começa pela **arquitetura de computadores** (história, x86/ARM/AVR, organização da CPU, ciclo de instrução, pipelining) e segue para o **gerenciamento de memória** (alocação, paginação, VA/RVA, proteções DEP e ASLR) e os **registradores x86**. Depois estuda os formatos de executável (**PE** no Windows e **ELF/COFF** no Linux), uma introdução a **Assembly x86** (pilha, chamadas de função, convenções de chamada, laços) e o uso de **debuggers** (x32dbg, GDB). O fechamento é a **segurança de memória**: as classes de bug de corrupção (buffer overflow, use‑after‑free, double free, race condition, ponteiros pendentes), por que elas acontecem e **como são mitigadas**.

A ideia central: **o software roda em memória, e memória mal gerenciada é a raiz de uma classe inteira de vulnerabilidades**. Entender registradores, pilha e formato de binário é o que permite analisar malware, fazer engenharia reversa e entender a razão de existirem DEP, ASLR, stack canaries e as linguagens memory‑safe.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura da fase | Roteiro: arquitetura → memória → registradores → binários → Assembly → debugger → corrupção de memória. |
| 2 | Arquitetura de computadores | Gerações de computadores (do ábaco ao ENIAC, transistores, circuitos integrados, microprocessadores), tipos de computador (microcontroladores, móveis, servidores, edge, mainframes), arquiteturas **x86**, **ARM** e **AVR**, organização da CPU, **ciclo de busca e execução** (fetch–decode–execute), pipelining e paralelismo. |
| 3 | Gerenciamento de memória | Técnicas de alocação (contígua, partições fixas e dinâmicas, desfragmentação, first fit × best fit, desalocação), **memória virtual**, **paginação** e **swapping**, endereço virtual (**VA**) × endereço virtual relativo (**RVA**), alocação no Windows e no Linux, o conceito do ataque **fork bomb** (exaustão de recursos) e proteções: garbage collection, **DEP** e **ASLR**. |
| 4 | Registradores | Notação AT&T × Intel. Registradores de uso geral (EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP), registradores de segmento e o registrador de flags **EFLAGS**. |
| 5 | Binários Windows | Tipos de binário: **EXE**, **DLL**, **LIB** e **SYS**. Formato **PE**: DOS Header/Stub, Rich Header, NT Headers (File e Optional Header, Data Directories), seções, tabelas de importação (**IDT/ILT/IAT**), relocação de base. Executar binários Windows no Linux com o **Wine**. |
| 6 | Binários Linux | Tipos de binário. Formato **ELF** (cabeçalho, program headers, section headers, tabelas de símbolos/strings, relocação, dynamic tags, notes) e **COFF**. Compatibilidade binária: ABI, interface de system calls e compatibilidade de bibliotecas. |
| 7 | Assembly x86 | Por que aprender Assembly (reversing, análise de malware, entender vulnerabilidades). Registradores e **EIP**, instruções aritméticas, **pilha**, chamadas de função (prólogo/epílogo), condicionais e saltos, **convenções de chamada** (cdecl, stdcall, fastcall), laços. Ferramentas: **IDA**, **Ghidra**, **x64dbg**, Godbolt e Dogbolt. |
| 8 | Debugger no Windows e stack | Revisão de debuggers. Interface do **x32dbg**: registradores, pilha, dump de memória e breakpoints. Exercício de **crackme** fácil para observar, num debugger, como uma comparação de senha decide o fluxo do programa. |
| 9 | Corrupção de memória | As classes mais comuns: **buffer overflow**, **use‑after‑free (UAF)**, **double free**, **condição de corrida** (race condition) e **ponteiros pendentes** (dangling pointers): o que as causa, qual o impacto e como preveni‑las. |
| 10 | Buffer overflow (teoria) | "Intuição de segurança" com metodologia científica (hipótese → teste → conclusão). Por que certas funções de C (`gets`, `strcpy`, `sprintf`, `scanf`...) são inseguras, como um overflow de pilha pode sobrescrever o endereço de retorno, o conceito de **fuzzing** e a ideia de um alvo de laboratório (**Vulnserver**). Visão geral de heap overflow e variantes. |
| 11 | Buffer overflow no Windows (lab guiado) | Estudo de caso, em ambiente isolado, de como uma entrada sem validação pode levar ao controle do fluxo de execução e à importância das mitigações. *Não reproduzo aqui o procedimento de exploração nem o código; registro apenas os conceitos e as defesas.* |

## 🔑 Conceitos-chave

- **Bases numéricas**: binário (base 2), decimal (base 10) e hexadecimal (base 16, um dígito = 4 bits). Endereços e opcodes aparecem sempre em hex.
- **Ciclo de instrução**: buscar (fetch), decodificar e executar. O **EIP/RIP** (instruction pointer) aponta a próxima instrução. O ponto central da fase é entender por que **controlar o instruction pointer significa controlar o fluxo do programa** — e por isso protegê‑lo é prioridade.
- **Pilha (stack)**: estrutura LIFO que cresce para endereços menores. `ESP` aponta o topo e `EBP` a base do frame. Uma chamada (`call`) empilha o **endereço de retorno**; o `ret` o desempilha de volta para o EIP.
- **Heap**: memória alocada dinamicamente (`malloc`/`free`, `HeapAlloc`). Erros como UAF e double free acontecem aqui.
- **Endianness**: o x86 é **little‑endian** (o byte menos significativo vem primeiro), o que explica a ordem "invertida" dos endereços em dumps de memória.
- **VA × RVA**: VA é o endereço virtual absoluto; RVA é o deslocamento relativo à base de carga do módulo (ImageBase). Com ASLR, essa base muda a cada execução.
- **PE × ELF**: são os formatos de executável do Windows e do Linux. Ambos descrevem cabeçalhos, seções (`.text` = código, `.data`/`.rdata` = dados) e **importações**. A IAT (Windows) e a PLT/GOT (Linux) revelam quais funções de API o binário usa, o que já é um indicador forte na análise de malware.
- **Convenções de chamada**: definem como os argumentos são passados (pilha ou registradores) e quem limpa a pilha (cdecl: quem chama; stdcall: a função chamada).
- **Classe de bug de corrupção de memória**: ocorre quando um programa escreve ou lê fora dos limites previstos (overflow, UAF, double free). O impacto vai de crash a execução de código, e é por isso que essa classe motivou tantas mitigações.
- **Mitigações (o foco defensivo da fase)**: **DEP/NX** (dados não executáveis), **ASLR** (endereços aleatórios), **stack canaries** (`/GS`, `-fstack-protector`), **SafeSEH/CFG**, uso de funções seguras (`strncpy`, `fgets`, `snprintf`) e, acima de tudo, **linguagens memory‑safe** (Rust, Go, linguagens gerenciadas).
- **Fuzzing**: enviar entradas malformadas ou crescentes até o programa falhar. É uma técnica central tanto para atacantes quanto para quem testa e endurece software (ex.: OSS‑Fuzz).

## 🛠️ Ferramentas e comandos

**Ambiente:** VM isolada para análise de binários; Kali/Linux com as ferramentas de inspeção; debuggers no Windows. Tudo em rede fechada, apenas para estudo.

```bash
# Inspeção estática de binários (defensiva)
file binario; strings -n 6 binario | less; xxd binario | head
readelf -h binario; readelf -S binario; objdump -d -M intel binario | less
ldd binario; checksec --file=binario          # mostra NX, PIE, canary, RELRO
nm -D binario                                 # símbolos dinâmicos importados

# Depuração para entender o programa
gdb -q ./binario   →   break main / run / info registers / x/20wx $esp / disas main

# Executar binários Windows no Linux
sudo apt install wine; wine programa.exe
```

```text
# Análise de PE/ELF e Assembly
Ghidra · IDA Free · x32dbg/x64dbg · PE-bear / CFF Explorer · Godbolt (C → Assembly)

# Verificar mitigações de um binário
checksec (Linux)  ·  "!mona modules" no Immunity (lista DEP/ASLR/SafeSEH por módulo)
```

## ❓ Perguntas de revisão

1. **O que são `ESP`, `EBP` e `EIP`?**
   `ESP` aponta o topo da pilha, `EBP` a base do frame atual e `EIP` (instruction pointer) o endereço da próxima instrução a ser executada.
2. **Por que o x86 é little‑endian importa na prática?**
   Porque os bytes de um valor multibyte são armazenados do menos significativo para o mais significativo. Ao ler um dump ou montar um valor na memória, é preciso considerar essa ordem "invertida".
3. **Qual a diferença entre pilha (stack) e heap?**
   A pilha é LIFO, gerenciada automaticamente (variáveis locais, endereços de retorno) e cresce para endereços menores. A heap é alocada manualmente em tempo de execução (`malloc`/`free`) e é onde ocorrem UAF e double free.
4. **O que a seção `.text` e a IAT dizem sobre um binário?**
   A `.text` contém o código executável. A IAT (Import Address Table) lista as funções de API importadas de outras DLLs, o que ajuda a inferir o comportamento do programa na análise de malware.
5. **O que é um use‑after‑free?**
   É usar um ponteiro depois que a memória que ele apontava já foi liberada. Se um atacante conseguir reocupar aquela região, pode levar o programa a usar dados controlados.
6. **Como um buffer overflow de pilha pode mudar o fluxo de um programa?**
   Escrevendo além do buffer, ele sobrescreve valores salvos na pilha, inclusive o endereço de retorno. Quando a função retorna, a execução segue para onde esse endereço aponta.
7. **O que o DEP/NX faz e qual sua limitação?**
   Marca regiões de dados (como a pilha) como não executáveis, impedindo rodar código injetado ali. Sua limitação é que não impede técnicas de reaproveitamento de código já existente, por isso vem acompanhado de ASLR e CFG.
8. **Para que serve o ASLR?**
   Para aleatorizar os endereços de carga de módulos, pilha e heap a cada execução, de modo que o atacante não saiba de antemão onde está o código ou os dados que precisaria referenciar.
9. **O que é um stack canary?**
   Um valor secreto colocado entre as variáveis locais e o endereço de retorno. Antes de a função retornar, ele é checado; se foi sobrescrito, o programa aborta, detectando o overflow.
10. **Por que linguagens memory‑safe reduzem essa classe de vulnerabilidade?**
    Porque fazem verificação de limites e gerenciam a memória automaticamente (ou com regras de posse, como o Rust), eliminando por construção a maior parte dos overflows, UAF e double free.

## 💼 Conexão com o mercado

- **SOC / Blue team**: entender PE/ELF, importações e Assembly é a base da **análise de malware** e do **triage de binários suspeitos**. Saber o que são DEP, ASLR e canaries ajuda a interpretar alertas de EDR sobre exploração de memória e a priorizar patches de RCE.
- **CompTIA Security+ (SY0‑701)**: buffer overflow, race condition, e as mitigações de memória aparecem em *Threats, Vulnerabilities & Mitigations*; a análise de malware e a engenharia reversa dão base para *Security Operations*. O conceito de software seguro (funções inseguras, memory‑safe) toca *Secure coding*.
- **Pós Tech em IA para Segurança**: modelos de detecção de malware usam features extraídas justamente de cabeçalhos PE/ELF, sequências de opcodes e chamadas de API. O fuzzing moderno é cada vez mais guiado por ML, e esta fase dá o vocabulário para construir esses datasets.

## 📖 Termos da fase

Arquitetura x86 / ARM / AVR · Ciclo de instrução (fetch–decode–execute) · Pipelining · Registrador · Registradores de uso geral · EFLAGS · EIP (instruction pointer) · Pilha (stack) · Heap · ESP / EBP · Endereço de retorno · Little‑endian · Hexadecimal · Memória virtual · Paginação · Swapping · VA / RVA · Fork bomb · DEP / NX · ASLR · Stack canary · Garbage collection · Binário · PE · EXE / DLL / LIB / SYS · IAT / IDT / ILT · ELF · COFF · ABI · System call · Wine · Assembly x86 · Convenção de chamada (cdecl/stdcall/fastcall) · Debugger · Crackme · Engenharia reversa · Corrupção de memória · Buffer overflow · Use‑after‑free · Double free · Condição de corrida · Ponteiro pendente · Fuzzing · Shellcode

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
