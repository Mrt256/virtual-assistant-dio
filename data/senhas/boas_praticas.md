---
titulo: Boas Práticas de Senhas e Autenticação
categoria: senhas
tipo: boas_praticas
nivel: basico
versao: 1.0
fontes:
  - CERT.br
---

# Boas Práticas de Senhas e Autenticação

## Objetivo

Apresentar práticas para reduzir o risco de acesso indevido a contas
e dispositivos por meio do fortalecimento de senhas e da autenticação.

## 1. Utilize senhas fortes

Uma senha deve ser difícil de adivinhar e não deve ser baseada em
informações pessoais facilmente associadas ao usuário.

Boas práticas incluem:

- utilizar senhas longas;
- evitar nomes, datas, sobrenomes e outras informações pessoais;
- evitar sequências óbvias;
- evitar senhas previsíveis;
- utilizar senhas diferentes para contas diferentes.

Senhas longas e únicas reduzem o impacto de ataques baseados em
tentativas de descoberta e do reaproveitamento de credenciais vazadas.

## 2. Não reutilize senhas

A mesma senha não deve ser utilizada em várias contas.

Se uma senha for descoberta ou vazada, um atacante poderá tentar
utilizá-la em outros serviços nos quais o usuário tenha conta.

Por esse motivo, cada serviço deve possuir uma senha própria.

## 3. Utilize um gerenciador de senhas

Quando houver muitas senhas diferentes para memorizar, um gerenciador
de senhas pode auxiliar no armazenamento e na criação de credenciais.

O gerenciador deve ser protegido por uma credencial forte e pelos
mecanismos adicionais de autenticação disponíveis.

Ao escolher um gerenciador, considere sua reputação, modelo de
segurança, opções de recuperação e mecanismos de proteção disponíveis.

## 4. Utilize autenticação em duas etapas ou multifator

Sempre que disponível, habilite uma segunda etapa de autenticação.

A autenticação multifator adiciona uma camada de proteção além da
senha e pode reduzir o impacto de uma senha comprometida.

Exemplos de fatores adicionais incluem:

- aplicativo autenticador;
- chave de segurança física;
- outros mecanismos oferecidos pelo serviço.

## 5. Proteja o processo de recuperação

A recuperação de conta também deve ser protegida.

Mantenha atualizados os meios de recuperação e evite utilizar
informações facilmente descobertas por terceiros.

## 6. Não compartilhe senhas

Senhas são credenciais pessoais e não devem ser compartilhadas por
mensagens, e-mail ou outros meios.

Uma organização que necessite conceder acesso deve utilizar mecanismos
apropriados de gerenciamento de usuários e permissões, em vez de
compartilhar uma senha entre pessoas.

## 7. Tenha cuidado com páginas de login

Antes de informar uma senha:

- verifique o endereço do site;
- confirme se o domínio é o esperado;
- observe se a conexão está sendo realizada pelo endereço oficial;
- desconfie de links recebidos inesperadamente.

Uma página visualmente semelhante à original não garante que seja
legítima.

## 8. O que fazer se uma senha puder ter sido comprometida

Se houver suspeita de que uma senha foi descoberta, vazada ou
utilizada em um dispositivo potencialmente comprometido:

1. Acesse o serviço por um canal oficial.
2. Altere a senha.
3. Altere a mesma senha em outros serviços, caso ela tenha sido
   reutilizada.
4. Habilite autenticação multifator, quando disponível.
5. Verifique atividades e acessos recentes, quando o serviço
   oferecer esse recurso.
6. Em ambiente corporativo, comunique o suporte ou responsável
   pela segurança.

## 9. Sobre troca periódica de senhas

A troca de senha deve ser orientada pelo contexto e pelas políticas
do serviço ou organização.

Uma senha não deve ser trocada simplesmente por uma rotina automática
se isso levar o usuário a escolher senhas previsíveis ou reutilizadas.

Trocas imediatas são especialmente importantes quando houver indícios
de comprometimento, vazamento ou uso indevido.

## 10. Para administradores e organizações

Contas administrativas e contas com privilégios elevados merecem
proteção adicional.

Boas práticas incluem:

- utilizar autenticação multifator;
- evitar compartilhamento de contas;
- aplicar o princípio do menor privilégio;
- separar contas administrativas de contas de uso cotidiano;
- monitorar autenticações quando houver recursos para isso;
- utilizar políticas de acesso adequadas ao ambiente.

## Checklist

- [ ] Minha senha é longa e difícil de adivinhar?
- [ ] Uso uma senha diferente para cada serviço?
- [ ] Evito informações pessoais nas senhas?
- [ ] Utilizo um gerenciador de senhas quando necessário?
- [ ] Ativei autenticação multifator nas contas importantes?
- [ ] Sei reconhecer o endereço oficial dos serviços que utilizo?
- [ ] Sei o que fazer caso uma senha seja comprometida?

## Limitação

Estas orientações são gerais. Requisitos específicos podem variar de
acordo com o serviço, sistema ou política de segurança da organização.

## Fonte

- CERT.br — Fascículo Autenticação:
  https://cartilha.cert.br/fasciculos/autenticacao/
- CERT.br — Fascículo Proteção de Dados:
  https://cartilha.cert.br/fasciculos/protecao-de-dados/
