---
titulo: Firewall
categoria: redes
tipo: conceito
nivel: basico
versao: 1.0
fontes:
  - NIST
  - CERT.br
---

# Firewall

## Definição

Firewall é um mecanismo de segurança utilizado para controlar o
tráfego de rede entre diferentes redes, sistemas ou segmentos.

O controle pode considerar características como endereços, portas,
protocolos e outros atributos definidos pelas regras de segurança.

## Objetivo

Um firewall pode ser utilizado para:

- controlar conexões permitidas e bloqueadas;
- restringir acessos entre redes;
- reduzir a exposição de serviços;
- segmentar ambientes;
- registrar determinados eventos de tráfego.

## Firewall não é uma proteção isolada

Um firewall é apenas um dos componentes de uma estratégia de
segurança.

Ele não elimina riscos relacionados a:

- malware;
- phishing;
- credenciais comprometidas;
- vulnerabilidades de aplicações;
- ameaças internas;
- configurações incorretas.

## Regras de firewall

As regras devem ser definidas de acordo com as necessidades do
ambiente e com o princípio do menor privilégio.

Uma regra pode considerar, por exemplo:

- origem;
- destino;
- protocolo;
- porta;
- direção do tráfego;
- ação permitida ou bloqueada.

## Princípio do menor privilégio

Sempre que possível, deve ser permitido somente o tráfego necessário
para o funcionamento do serviço.

Regras excessivamente amplas podem aumentar a superfície de exposição.

## Firewall e NAT

NAT (Network Address Translation) é uma técnica de tradução de
endereços de rede e não deve ser confundida com firewall.

Uma configuração de NAT pode encaminhar conexões para um serviço,
enquanto as regras de firewall determinam se o tráfego correspondente
será permitido.

## Logs

Registros de firewall podem ajudar na identificação de:

- conexões bloqueadas;
- conexões permitidas;
- tentativas de acesso;
- padrões anormais;
- problemas de configuração.

A disponibilidade e o nível de detalhe dos registros dependem da
solução utilizada e de sua configuração.

## Boas práticas

- manter regras documentadas;
- revisar regras periodicamente;
- remover regras desnecessárias;
- evitar regras excessivamente amplas;
- limitar serviços expostos;
- manter o firewall atualizado;
- monitorar registros relevantes;
- separar redes quando necessário.

## Limitação

A presença ou ausência de uma regra de firewall não permite concluir,
sozinha, que um sistema está seguro ou comprometido.

## Fontes

- NIST — SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy:
  https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final
- CERT.br — Cartilha de Segurança para Internet:
  https://cartilha.cert.br/
