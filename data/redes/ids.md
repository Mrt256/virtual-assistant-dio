---
titulo: IDS - Sistema de Detecção de Intrusão
categoria: redes
tipo: conceito
nivel: intermediario
versao: 1.0
fontes:
  - NIST
---

# IDS — Sistema de Detecção de Intrusão

## Definição

IDS (*Intrusion Detection System*) é um sistema destinado a detectar
eventos ou padrões que possam indicar atividades suspeitas ou
maliciosas em sistemas ou redes.

O IDS pode analisar eventos, tráfego ou atividades de sistemas e
gerar alertas para investigação.

## Objetivo

Um IDS pode auxiliar na:

- detecção de atividades suspeitas;
- identificação de possíveis ataques;
- geração de alertas;
- investigação de eventos;
- monitoração da segurança do ambiente.

## Tipos principais

### NIDS

Um NIDS (*Network Intrusion Detection System*) monitora tráfego de
rede em pontos definidos da infraestrutura.

### HIDS

Um HIDS (*Host Intrusion Detection System*) monitora atividades em
um equipamento específico.

## Detecção baseada em regras

Soluções de IDS podem utilizar assinaturas ou regras conhecidas para
identificar padrões associados a ameaças.

Essa abordagem pode ser eficiente para ameaças já conhecidas, mas
depende da qualidade e atualização das regras.

## Detecção baseada em comportamento

Algumas soluções podem identificar desvios em relação a padrões
esperados de atividade.

Essa abordagem pode ajudar na identificação de comportamentos
desconhecidos, mas também pode gerar falsos positivos.

## Alertas

Um alerta de IDS indica que determinada regra ou mecanismo de
detecção foi acionado.

Um alerta não significa necessariamente que um ataque foi
bem-sucedido.

O evento precisa ser analisado considerando:

- origem;
- destino;
- horário;
- protocolo;
- regra acionada;
- contexto;
- outros registros disponíveis.

## Falsos positivos

Um falso positivo ocorre quando uma atividade legítima é identificada
como potencialmente maliciosa.

Por isso, alertas devem ser analisados antes de concluir que ocorreu
um incidente.

## IDS x IPS

Um IDS normalmente tem como função principal **detectar e alertar**.

Um IPS (*Intrusion Prevention System*) acrescenta mecanismos de
prevenção ou bloqueio do tráfego considerado malicioso.

## Boas práticas

- manter regras atualizadas;
- revisar alertas;
- correlacionar eventos com outras fontes;
- ajustar regras para reduzir falsos positivos;
- registrar decisões tomadas durante a investigação.

## Limitação

Um IDS não detecta necessariamente todas as ameaças e um alerta
isolado não confirma um comprometimento.

## Fonte

- NIST — SP 800-94, Guide to Intrusion Detection and Prevention Systems:
  https://csrc.nist.gov/publications/detail/sp/800-94/final
