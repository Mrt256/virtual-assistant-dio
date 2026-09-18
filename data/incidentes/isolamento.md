---
titulo: Isolamento e Contenção de Dispositivos
categoria: incidentes
tipo: procedimento
nivel: intermediario
versao: 1.0
fontes:
  - CISA
  - CERT.br
---

# Isolamento e Contenção de Dispositivos

## Objetivo

Apresentar conceitos e orientações gerais relacionados ao isolamento
de dispositivos durante a resposta a um possível incidente de
segurança.

O isolamento é uma medida de contenção. Sua aplicação deve considerar
o tipo de incidente, o ambiente e a necessidade de preservar
evidências.

## O que é isolamento

Isolamento é a separação de um dispositivo, conta ou recurso
potencialmente comprometido de outros recursos do ambiente.

O objetivo pode ser reduzir a possibilidade de:

- propagação de malware;
- comunicação com infraestrutura maliciosa;
- acesso indevido a outros recursos;
- alteração ou exfiltração adicional de dados.

## Quando o isolamento pode ser considerado

A equipe responsável pode considerar isolamento quando houver indícios
de comprometimento que possam representar risco para outros sistemas.

Exemplos:

- suspeita de malware ativo;
- atividade de rede anômala associada a um incidente;
- comprometimento de uma estação;
- comportamento incompatível com o uso normal;
- suspeita de acesso não autorizado.

A decisão deve considerar o impacto operacional e a necessidade de
investigação.

## Antes de isolar

Sempre que possível, a equipe responsável deve avaliar:

- qual dispositivo está envolvido;
- qual é sua função;
- se o equipamento é crítico;
- se existem processos importantes em execução;
- se há necessidade de preservar evidências;
- qual método de isolamento é adequado.

Em alguns incidentes, desligar imediatamente um equipamento pode
eliminar informações voláteis importantes para a investigação.

Por isso, ações de contenção devem seguir procedimentos definidos por
profissionais responsáveis pelo incidente.

## Formas de contenção

Dependendo do ambiente, podem existir diferentes mecanismos:

- isolamento por ferramentas de segurança;
- remoção controlada da rede;
- bloqueio de comunicação;
- suspensão de uma conta;
- alteração ou revogação de credenciais;
- segmentação de rede.

A técnica adequada depende da infraestrutura e do incidente.

## O que o usuário deve fazer

Se um usuário comum suspeitar que seu equipamento esteja
comprometido:

1. Interrompa atividades suspeitas.
2. Não execute arquivos desconhecidos.
3. Não tente investigar ou remover a ameaça por conta própria,
   caso não tenha conhecimento ou autorização.
4. Comunique imediatamente o suporte ou responsável pela segurança.
5. Siga as orientações recebidas.

## O que o usuário NÃO deve fazer

Evite, sem orientação:

- formatar o equipamento;
- apagar arquivos suspeitos;
- apagar logs;
- instalar diversos programas de segurança;
- alterar configurações de rede;
- reiniciar repetidamente o equipamento;
- conectar mídias externas;
- copiar arquivos suspeitos para outros dispositivos.

Essas ações podem alterar evidências ou aumentar o risco.

## Após o isolamento

Depois da contenção, a equipe responsável pode realizar:

1. análise do dispositivo;
2. identificação da causa;
3. avaliação do impacto;
4. erradicação da ameaça;
5. recuperação;
6. monitoramento.

O dispositivo não deve retornar à operação normal apenas porque o
comportamento suspeito deixou de ocorrer.

## Limitação

O isolamento é uma medida técnica que deve ser adaptada ao contexto.
Em ambientes corporativos ou críticos, siga sempre o plano de
resposta a incidentes e as orientações da equipe responsável.

## Fontes

- CISA — Incident Response:
  https://www.cisa.gov/topics/cyber-threats-and-advisories/incident-response
- CISA — Cybersecurity Incident & Vulnerability Response Playbooks:
  https://www.cisa.gov/resources-tools/resources/cybersecurity-incident-vulnerability-response-playbooks
- CERT.br — Cartilha de Segurança para Internet:
  https://cartilha.cert.br/
