---
titulo: IPS - Sistema de Prevenção de Intrusão
categoria: redes
tipo: conceito
nivel: intermediario
versao: 1.0
fontes:
  - NIST
---

# IPS — Sistema de Prevenção de Intrusão

## Definição

IPS (*Intrusion Prevention System*) é uma tecnologia de segurança
capaz de identificar atividades potencialmente maliciosas e aplicar
ações de prevenção ou bloqueio de acordo com as políticas
configuradas.

## Objetivo

Um IPS pode auxiliar na:

- detecção de atividades suspeitas;
- bloqueio de tráfego identificado como malicioso;
- aplicação automática de políticas;
- redução da exposição a determinadas ameaças.

## Funcionamento

De forma simplificada:

```text
Tráfego
   ↓
Análise
   ↓
Regra ou mecanismo de detecção
   ↓
┌───────────────┐
│ Legítimo      │ → Permitir
└───────────────┘

ou

┌───────────────┐
│ Suspeito      │ → Ação de prevenção
└───────────────┘
```

A ação efetivamente realizada depende da solução e da configuração
adotada.

## IPS x IDS

| Tecnologia | Função principal |
|---|---|
| IDS | Detectar e gerar alertas |
| IPS | Detectar e aplicar ações de prevenção |

Uma solução pode possuir funcionalidades de IDS e IPS.

## Riscos de configuração

Um IPS mal configurado pode:

- bloquear tráfego legítimo;
- gerar indisponibilidade;
- produzir grande quantidade de alertas;
- dificultar a identificação de eventos relevantes.

Por isso, políticas devem ser testadas e ajustadas de acordo com o
ambiente.

## Boas práticas

- utilizar regras atualizadas;
- testar alterações antes de aplicá-las em ambientes críticos;
- acompanhar falsos positivos;
- revisar bloqueios;
- registrar alterações de configuração;
- monitorar o impacto operacional.

## Limitação

Um bloqueio realizado por um IPS não comprova necessariamente que
houve uma invasão ou comprometimento.

## Fonte

- NIST — SP 800-94, Guide to Intrusion Detection and Prevention Systems:
  https://csrc.nist.gov/publications/detail/sp/800-94/final
