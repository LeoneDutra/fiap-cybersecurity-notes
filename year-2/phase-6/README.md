# Year 2 · Phase 6 — Segurança em Nuvem (AWS) e Segurança de IA/ML (Cloud Security & AI/ML Security)

> Resumo pessoal, escrito com minhas palavras. Termos técnicos em inglês entre parênteses. Foco conceitual e defensivo.

## 🧭 Visão geral

A fase tem duas grandes trilhas. A primeira é **segurança em nuvem (AWS)**: percorre resposta a incidentes, logs e monitoramento, segurança de infraestrutura, **IAM**, proteção de dados, automação de **SDLC/CI‑CD**, **Infraestrutura como Código (IaC)** e **soluções resilientes** — sempre ancorada em serviços concretos da AWS. A segunda é **segurança de IA/ML**: fundamentos de IA e ciência de dados, **machine learning supervisionado**, e então **AI Security** — os três ângulos (segurança **da** IA, IA **para** segurança, IA **como vetor** de ataque), as **ameaças a modelos** (ataques adversariais, data poisoning, model inversion, membership inference, model stealing), a **segurança de dados para IA** e a **segurança de GenAI/LLMs** (prompt injection, jailbreak e defesas por camada).

A ideia central: **a nuvem move a segurança para configuração e identidade, e a IA cria uma superfície de ataque nova — o próprio modelo e seus dados**. Esta é a fase que mais conversa com a **Pós Tech em IA para Segurança**.

## 📚 Resumo por material

| # | Tema | O que fica |
|---|---|---|
| 1 | Abertura — Cloud Sec & IA | Roteiro das duas trilhas: nuvem AWS (caps. 2–9) e IA/ML Security (caps. 10–16). |
| 2 | Cloud Incident Response | Resposta a incidentes na AWS com **CloudTrail** (auditoria de API), **Config** (conformidade de configuração), **CloudWatch** (métricas/alarmes), **Lambda** (automação), **IAM**, **GuardDuty** (detecção de ameaças) e **Systems Manager**. |
| 3 | Cloud Log & Monitoring | **VPC Flow Logs** (tráfego de rede) e **X‑Ray** (rastreio de aplicação), mais desafios com CloudWatch, CloudTrail, GuardDuty e Lambda. |
| 4 | Cloud Infrastructure Security | **KMS** (gestão de chaves) e os modos de criptografia de S3 (**SSE‑S3, SSE‑KMS, SSE‑C**), **WAF** (WebACL), **Shield** (anti‑DDoS) e **Security Hub** (postura central). |
| 5 | Cloud IAM | Gerenciamento de identidade e acesso: **IAM Identity Center/SSO**, **Directory Service**, **Cognito** (identidade de apps), **Secrets Manager** e **STS** (credenciais temporárias). |
| 6 | Cloud Data Protection | **S3**, **Macie** (descoberta de dados sensíveis/PII), **RDS** e criptografia em repouso (S3, RDS, DynamoDB). |
| 7 | Cloud SDLC Automation | Pipeline **CI/CD** na AWS: **CodeCommit**, **CodePipeline**, **CodeBuild**, **CodeDeploy** e **CodeArtifact** — a base de DevSecOps. |
| 8 | Cloud IaC | **Infraestrutura como Código**: **CloudFormation** (templates) e OpsWorks. Por que IaC melhora segurança (repetível, versionado, auditável). |
| 9 | Cloud Resilient Solutions | Alta disponibilidade e continuidade: **Route 53** (DNS), **ELB** (balanceamento), **RDS Multi‑AZ**, **S3 Cross‑Region Replication**, **Aurora Global** e **DynamoDB Global Tables** — o "D" da tríade CID. |
| 10 | Introduction to AI | Revisão dos pilares de segurança e ameaças; definição e história da **IA**; representação do conhecimento (**dado → informação → conhecimento**). |
| 11 | Introduction to Chatbots | **Ciência de dados** (etapas, ferramentas, profissões) e os paradigmas de **machine learning**: **supervisionado**, **não supervisionado** e **por reforço**. |
| 12 | Supervised Machine Learning | ML supervisionado: **dados rotulados**, conjuntos de **treino/teste**, **classificação** (algoritmos, técnicas, métricas) e **regressão**. |
| 13 | AI Security Fundamentals | **AI Security**: os três ângulos (**segurança da IA**, **IA para segurança**, **IA como vetor**), por que IA exige abordagem própria, **Security by Design** e a tríade CID aplicada a modelos. Ameaças (prompt injection, jailbreak, model inversion, membership inference) e governança. |
| 14 | AI/ML Threats and Risks | **Ataques adversariais** (perturbações imperceptíveis, **FGSM**, **PGD**, **BIM**, **JSMA**; direcionados × não), **data poisoning** (ataque causativo, à disponibilidade e integridade), **model inversion**, **membership inference** e **model stealing**. |
| 15 | Data Security for AI | Riscos a dados em IA e **medidas técnicas** (anonimização, controle de acesso, ciclo de vida, defesa ativa); estruturas regulatórias e a própria IA como ferramenta de governança/conformidade. |
| 16 | GenAI & LLM Security | Riscos críticos de **LLMs** (OWASP Top 10 for LLM: **prompt injection**, **jailbreak**, vazamento de dados, output inseguro) e **defesas por camada**: entrada (sanitização/validação), modelo/treino, saída (filtragem/moderação), arquitetura e governança. |

## 🔑 Conceitos-chave

- **Modelo de responsabilidade compartilhada**: na nuvem, o provedor protege a infraestrutura ("segurança **da** nuvem") e o cliente protege o que coloca nela ("segurança **na** nuvem") — configurações, dados e identidades são do cliente.
- **Identidade é o novo perímetro**: na AWS, o **IAM** (usuários, roles, políticas, STS, menor privilégio) é o controle central. A maioria dos incidentes de nuvem vem de credenciais e permissões excessivas.
- **Logs são a base de detecção**: **CloudTrail** (quem fez qual chamada de API), **VPC Flow Logs** (tráfego), **CloudWatch** (métricas) e **GuardDuty** (detecção gerenciada) são o equivalente nuvem do SIEM e dos sensores.
- **Criptografia e KMS**: proteger dados em repouso e em trânsito; o **KMS** gerencia as chaves, e os modos SSE‑S3/SSE‑KMS/SSE‑C diferem em quem controla a chave.
- **IaC e DevSecOps**: descrever infraestrutura em código (CloudFormation) e automatizar o pipeline (CI/CD) torna a segurança repetível, versionada e auditável — e permite "shift‑left" (checar cedo).
- **Resiliência = disponibilidade**: Multi‑AZ, replicação cross‑region e balanceamento garantem continuidade; é segurança no sentido da disponibilidade.
- **Três ângulos da IA e segurança**: **segurança da IA** (proteger o modelo/dados), **IA para segurança** (usar ML em defesa, como detecção de anomalia) e **IA como vetor** (o atacante usando IA, ou o modelo sendo o alvo).
- **ML supervisionado**: aprende de **dados rotulados**; separar treino/teste evita overfitting; classificação e regressão são os dois tipos; métricas (acurácia, precisão, recall, F1) medem a qualidade. A qualidade do dado define a qualidade do modelo — e a sua segurança.
- **Ataques a modelos**: **adversarial** (perturbar a entrada para enganar o modelo — FGSM/PGD), **data poisoning** (contaminar o treino), **model inversion** (reconstruir dados de treino), **membership inference** (descobrir se um dado estava no treino) e **model stealing** (copiar o modelo pela API).
- **Segurança de LLM/GenAI**: **prompt injection** (instruções maliciosas na entrada que subvertem o sistema) e **jailbreak** (burlar as salvaguardas) são os riscos centrais; a defesa é em camadas — validar entrada, endurecer o modelo/treino, filtrar a saída e cercar com arquitetura e governança (OWASP Top 10 for LLM, NIST AI RMF).

## 🛠️ Ferramentas e serviços

**AWS — segurança/operação:** IAM, IAM Identity Center, STS, Cognito, Secrets Manager, KMS, CloudTrail, CloudWatch, Config, GuardDuty, Security Hub, Macie, WAF, Shield, VPC Flow Logs, X‑Ray, Systems Manager. **Automação/resiliência:** CodePipeline/CodeBuild/CodeDeploy, CloudFormation (IaC), Route 53, ELB, RDS Multi‑AZ, Aurora Global, DynamoDB Global Tables. **IA/ML:** Python, scikit‑learn/pandas (ML supervisionado); referências de segurança **OWASP Top 10 for LLM**, **MITRE ATLAS**, **NIST AI RMF**.

```text
Nuvem — postura defensiva (conceitos):
Identidade  → IAM com menor privilégio, roles em vez de chaves, MFA, STS temporário
Detecção    → CloudTrail + GuardDuty + Config + Security Hub; alarmes no CloudWatch
Dados       → KMS, criptografia em repouso/trânsito, Macie para PII
Rede/edge   → WAF (WebACL), Shield (DDoS), VPC Flow Logs
Entrega     → IaC (CloudFormation) + CI/CD com checagens de segurança (shift-left)
Resiliência → Multi-AZ, cross-region, ELB, Route 53

IA/ML — superfície e defesas (conceitos):
Dados       → qualidade e proveniência; anonimização; proteger o dataset de treino
Modelo      → robustez adversarial; limitar acesso à API (anti model stealing)
LLM/GenAI   → validar entrada (anti prompt injection), filtrar saída, guardrails,
              least-privilege nas ferramentas/plugins, monitorar e registrar
Governança  → OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF
```

## ❓ Perguntas de revisão

1. **O que é o modelo de responsabilidade compartilhada na nuvem?**
   O provedor é responsável pela segurança *da* nuvem (infraestrutura física, hipervisor); o cliente é responsável pela segurança *na* nuvem (configurações, dados, identidades e acessos). A maioria das falhas está no lado do cliente.
2. **Por que o IAM é o controle central de segurança na AWS?**
   Porque identidade é o perímetro: quem pode fazer o quê. Políticas de menor privilégio, roles em vez de chaves estáticas, MFA e credenciais temporárias (STS) evitam a causa mais comum de incidentes — credenciais e permissões excessivas.
3. **Para que servem CloudTrail, GuardDuty e Config?**
   CloudTrail registra todas as chamadas de API (quem fez o quê); GuardDuty detecta atividade maliciosa de forma gerenciada; Config avalia e alerta sobre configurações fora de conformidade. Juntos formam a base de detecção.
4. **Qual a diferença entre SSE‑S3, SSE‑KMS e SSE‑C?**
   Todos cifram em repouso no S3; diferem em quem controla a chave: SSE‑S3 (chave gerida pela AWS), SSE‑KMS (chave no KMS, com auditoria e política), SSE‑C (chave fornecida pelo cliente).
5. **Por que IaC e CI/CD melhoram a segurança?**
   Porque a infraestrutura vira código versionado, repetível e auditável, e o pipeline pode incluir checagens de segurança cedo (shift‑left), reduzindo erro manual e desvio de configuração.
6. **Quais são os três ângulos da relação entre IA e segurança?**
   Segurança *da* IA (proteger o modelo e os dados), IA *para* segurança (usar ML na defesa) e IA *como vetor* (a IA sendo usada para atacar, ou o modelo sendo o alvo).
7. **O que é um ataque adversarial e como ele funciona (ex.: FGSM)?**
   É alterar a entrada com perturbações imperceptíveis para fazer o modelo errar. O FGSM usa o gradiente da função de perda para calcular a perturbação que mais engana o modelo com a menor mudança visível.
8. **Diferencie data poisoning, model inversion, membership inference e model stealing.**
   Poisoning contamina os dados de treino para degradar ou enviesar o modelo; model inversion reconstrói dados de treino a partir do modelo; membership inference descobre se um registro estava no treino (risco de privacidade); model stealing copia o modelo consultando sua API.
9. **O que é prompt injection e por que é o risco central de LLMs?**
   É inserir instruções maliciosas na entrada (direta ou vinda de conteúdo externo) para subverter o comportamento do LLM — vazar dados, ignorar regras, executar ações. É central porque o modelo não separa bem "dados" de "instruções".
10. **Como se defende um sistema de GenAI/LLM?**
    Em camadas: validar e sanitizar a entrada (anti prompt injection), endurecer modelo/treino, filtrar e moderar a saída, aplicar menor privilégio às ferramentas/plugins, e cercar com arquitetura e governança (OWASP LLM Top 10, NIST AI RMF), além de monitorar e registrar.

## 💼 Conexão com o mercado

- **Cloud Security / SOC em nuvem**: domínio de IAM, logging (CloudTrail/GuardDuty), criptografia (KMS) e postura (Security Hub) é requisito do mercado. Mapeia para certificações **AWS Security Specialty**, **Security+** (cloud) e CCSP.
- **AI Security (emergente e quente)**: proteger modelos e dados, e usar IA na defesa, é uma das áreas que mais cresce. OWASP Top 10 for LLM, MITRE ATLAS e NIST AI RMF são as referências que os empregadores citam.
- **Pós Tech em IA para Segurança**: esta é literalmente a fase‑ponte. ML supervisionado, ataques adversariais, data poisoning, segurança de LLM e governança de IA são o núcleo da pós. A combinação nuvem + IA é onde a maioria dos sistemas modernos (e seus riscos) vive.

## 📖 Termos da fase

Modelo de responsabilidade compartilhada · IAM · Role · STS · SSO / Identity Center · Cognito · Secrets Manager · KMS · SSE‑S3 / SSE‑KMS / SSE‑C · CloudTrail · CloudWatch · AWS Config · GuardDuty · Security Hub · Macie · WAF (WebACL) · Shield · VPC Flow Logs · X‑Ray · S3 / RDS / DynamoDB · CI/CD (CodePipeline/CodeBuild/CodeDeploy) · DevSecOps · Infraestrutura como Código (IaC) · CloudFormation · Route 53 · ELB · Multi‑AZ · Cross‑region replication · Inteligência Artificial · Ciência de dados · Machine learning (supervisionado/não supervisionado/reforço) · Dados rotulados · Treino/teste · Classificação · Regressão · AI Security · Security by Design · Ataque adversarial · FGSM / PGD / BIM / JSMA · Data poisoning · Model inversion · Membership inference · Model stealing · LLM · Prompt injection · Jailbreak · OWASP Top 10 for LLM · MITRE ATLAS · NIST AI RMF · Guardrails

➡️ Definições completas no [glossário](../../glossary/GLOSSARY.md).
