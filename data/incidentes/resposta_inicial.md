---
titulo: Resposta Inicial a Incidentes de Segurança
categoria: incidentes
tipo: procedimento
nivel: basico
versao: 1.0
fontes:
  - CERT.br
  - CISA
---

# Resposta Inicial a Incidentes de Segurança

## Objetivo

Orientar sobre as primeiras medidas diante da suspeita ou confirmação
de um incidente de segurança da informação.

Este documento apresenta uma orientação geral. Procedimentos
específicos devem seguir as políticas e o plano de resposta a
incidentes da organização.

## O que é um incidente de segurança

Um incidente de segurança é um evento que pode comprometer a
confidencialidade, integridade ou disponibilidade de informações,
sistemas ou serviços.

Exemplos podem incluir:

- comprometimento de uma conta;
- infecção por código malicioso;
- acesso não autorizado;
- vazamento de informações;
- indisponibilidade causada por um evento de segurança;
- perda ou roubo de dispositivo;
- tentativa de phishing com possível comprometimento.

## Princípio geral

Diante de um possível incidente:

1. Mantenha a calma.
2. Interrompa atividades potencialmente prejudiciais.
3. Preserve informações relevantes.
4. Comunique o incidente ao responsável.
5. Siga o procedimento oficial de resposta.
6. Evite realizar ações não autorizadas que possam prejudicar a
   investigação.

## Etapa 1 — Identificar o ocorrido

Registre, quando possível:

- o que aconteceu;
- quando o comportamento foi percebido;
- qual equipamento ou conta está envolvido;
- quais ações foram realizadas antes do problema;
- mensagens ou alertas apresentados;
- arquivos ou serviços afetados.

Não é necessário determinar a causa do incidente antes de comunicá-lo.

## Etapa 2 — Conter o incidente

A contenção deve buscar reduzir a possibilidade de continuidade ou
propagação do incidente.

As medidas dependem da situação e devem seguir as orientações da
equipe responsável.

Exemplos de medidas que podem ser determinadas por uma equipe de
segurança incluem:

- isolamento de um dispositivo;
- bloqueio ou suspensão de uma conta;
- revogação de credenciais comprometidas;
- bloqueio de indicadores associados ao incidente.

O usuário não deve executar medidas técnicas de contenção por conta
própria quando não tiver autorização ou conhecimento para isso.

## Etapa 3 — Preservar evidências

Quando houver possibilidade de investigação, preserve informações
relevantes.

Podem ser úteis:

- mensagens recebidas;
- e-mails;
- cabeçalhos de e-mail;
- registros de horário;
- capturas de tela;
- alertas apresentados;
- nomes de arquivos;
- registros de sistemas, quando disponíveis.

Evite apagar, alterar ou formatar dispositivos antes de consultar
a equipe responsável, salvo quando houver procedimento específico
determinando a ação.

## Etapa 4 — Comunicar

Em ambiente corporativo, comunique o incidente utilizando o canal
definido pela organização.

Forneça informações objetivas:

- descrição do problema;
- equipamento ou conta afetada;
- horário aproximado;
- ações realizadas;
- evidências disponíveis.

## Etapa 5 — Recuperação

A recuperação deve ser realizada de acordo com o plano de resposta
a incidentes.

Pode envolver:

- remoção da ameaça;
- restauração de sistemas;
- recuperação de dados;
- redefinição de credenciais;
- aplicação de atualizações;
- monitoramento posterior.

O procedimento adequado depende da natureza e da extensão do incidente.

## Após o incidente

Quando aplicável, registre:

- causa identificada;
- sistemas afetados;
- impacto;
- medidas realizadas;
- medidas preventivas;
- lições aprendidas.

Essas informações podem ajudar a reduzir a probabilidade de
recorrência.

## O que o CyberGuard deve evitar

O agente não deve afirmar que ocorreu um incidente confirmado
baseando-se apenas em uma descrição genérica.

Também não deve recomendar ações destrutivas, como formatação,
exclusão de logs ou remoção indiscriminada de arquivos, sem contexto
e autorização apropriados.

## Limitação

Este documento fornece orientação inicial e não substitui um plano
formal de resposta a incidentes ou a análise realizada por uma
equipe especializada.

## Fontes

- CERT.br — Cartilha de Segurança para Internet:
  https://cartilha.cert.br/
- CISA — Incident Response:
  https://www.cisa.gov/topics/cyber-threats-and-advisories/incident-response
