---
titulo: Ransomware
categoria: conceitos
tipo: ransomware
nivel: intermediario
versao: 1.0
fontes:
  - CERT.br
  - CISA
---

# Ransomware

## Objetivo

Explicar o conceito de ransomware e apresentar medidas defensivas para
prevenção, contenção inicial e recuperação.

## O que é

Ransomware é um tipo de malware que pode impedir o acesso a arquivos,
sistemas ou dispositivos, frequentemente por meio de criptografia dos
dados.

Algumas campanhas também podem buscar roubar informações antes ou
durante a indisponibilização dos dados.

## Possíveis impactos

Um incidente de ransomware pode causar:

- indisponibilidade de sistemas;
- perda temporária de acesso a arquivos;
- interrupção de atividades;
- custos de recuperação;
- exposição de informações;
- necessidade de restauração de backups.

O impacto real depende do ambiente e do incidente específico.

## Vetores de entrada

Ransomware pode chegar ao ambiente por diferentes meios, incluindo:

- phishing;
- credenciais comprometidas;
- vulnerabilidades exploráveis;
- acesso remoto mal protegido;
- arquivos ou programas maliciosos.

Não é possível determinar a causa de um incidente apenas observando
que arquivos foram criptografados.

## Prevenção

Medidas defensivas incluem:

- manter sistemas atualizados;
- utilizar autenticação forte;
- proteger acessos remotos;
- restringir privilégios;
- manter backups protegidos;
- testar restaurações;
- monitorar eventos de segurança;
- capacitar usuários.

## Durante um possível incidente

Prioridades iniciais podem incluir:

1. confirmar os sinais observados sem realizar ações destrutivas;
2. acionar a equipe ou responsável por segurança;
3. avaliar a necessidade de isolamento dos sistemas afetados;
4. preservar informações relevantes para investigação;
5. proteger os backups ainda disponíveis;
6. documentar ações e horários;
7. seguir o plano de resposta a incidentes.

A decisão de desligar, desconectar ou isolar um sistema deve considerar
o ambiente e os procedimentos de resposta existentes.

## Recuperação

A recuperação deve considerar:

- identificar cópias confiáveis;
- verificar a integridade dos backups;
- corrigir ou eliminar a causa do comprometimento quando identificada;
- restaurar de maneira controlada;
- monitorar o ambiente após a recuperação;
- documentar o incidente e as lições aprendidas.

## Limitação

O CyberGuard AI não deve afirmar que um ambiente está comprometido
somente porque apresenta sintomas compatíveis com ransomware.

Quando houver indícios relevantes, a recomendação deve priorizar
contenção segura, preservação de evidências e acionamento dos
responsáveis pelo ambiente.

## Fontes

- CERT.br:
  https://cartilha.cert.br/
- CISA — StopRansomware:
  https://www.cisa.gov/stopransomware/
