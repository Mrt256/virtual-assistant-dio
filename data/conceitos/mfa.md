---
titulo: Autenticação Multifator (MFA)
categoria: conceitos
tipo: mfa
nivel: basico
versao: 1.0
fontes:
  - CISA
  - CERT.br
---

# Autenticação Multifator (MFA)

## Objetivo

Explicar o conceito de autenticação multifator e sua importância para
reduzir o risco associado ao comprometimento de credenciais.

## O que é MFA

MFA, ou autenticação multifator, é um mecanismo que exige dois ou mais
fatores de autenticação independentes para permitir o acesso a uma conta
ou serviço.

Os fatores normalmente pertencem a categorias como:

- algo que o usuário sabe, como uma senha;
- algo que o usuário possui, como um dispositivo autenticador;
- algo que o usuário é, como uma característica biométrica.

## Por que utilizar MFA

Uma senha pode ser descoberta, reutilizada, roubada por phishing ou
exposta em um vazamento.

Com MFA, o comprometimento de apenas um fator não necessariamente
permite o acesso à conta.

MFA reduz o risco, mas não elimina todas as possibilidades de ataque.

## Exemplos

Podem ser utilizados como segundo fator:

- aplicativo autenticador;
- chave de segurança;
- código de uso único;
- confirmação em dispositivo previamente registrado;
- biometria, conforme o serviço.

## Boas práticas

- habilitar MFA em contas importantes;
- priorizar métodos resistentes a phishing quando disponíveis;
- manter métodos de recuperação protegidos;
- não compartilhar códigos de autenticação;
- desconfiar de solicitações inesperadas de aprovação;
- revisar dispositivos e sessões autorizadas.

## MFA e phishing

Um usuário pode ser induzido a aprovar uma solicitação de autenticação
fraudulenta.

Por isso, a presença de MFA não elimina a necessidade de treinamento,
senhas fortes e atenção a solicitações de autenticação inesperadas.

## Limitação

A disponibilidade e os métodos de MFA variam conforme cada serviço.
O CyberGuard AI deve recomendar somente procedimentos compatíveis com
o serviço identificado ou explicar quando não possui essa informação.

## Fontes

- CISA — More Than a Password:
  https://www.cisa.gov/mfa
- CERT.br:
  https://cartilha.cert.br/
