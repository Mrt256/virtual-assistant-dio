---
titulo: Portas e Serviços de Rede
categoria: redes
tipo: conceito
nivel: basico
versao: 1.0
fontes:
  - IANA
  - NIST
---

# Portas e Serviços de Rede

## Definição

Em redes baseadas em TCP e UDP, portas são identificadores utilizados
para diferenciar serviços ou aplicações associados a uma comunicação
de rede.

As portas fazem parte da identificação de conexões e ajudam os
sistemas a direcionar o tráfego para o serviço apropriado.

## Faixas de portas

As portas TCP e UDP possuem valores de 0 a 65535.

A IANA organiza as portas em três faixas:

- **0–1023:** System Ports;
- **1024–49151:** User Ports;
- **49152–65535:** Dynamic and/or Private Ports.

A associação de uma porta a um serviço não significa que todo sistema
que utilize aquela porta esteja necessariamente executando o serviço
esperado.

## Exemplos conhecidos

Algumas portas frequentemente associadas a serviços incluem:

| Porta | Protocolo | Serviço tradicional |
|---:|---|---|
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |

Essas associações são referências tradicionais. A utilização de uma
porta deve ser confirmada no contexto do sistema analisado.

## Porta aberta

Uma porta pode ser considerada aberta quando existe um serviço
aceitando conexões naquele endereço e porta.

Uma porta aberta não significa automaticamente que exista uma
vulnerabilidade.

Entretanto, serviços desnecessariamente expostos podem aumentar a
superfície de ataque.

## Porta fechada

Uma porta fechada normalmente indica que não existe um serviço
aceitando conexões naquela porta, embora o sistema possa responder
de alguma forma à tentativa de conexão.

## Porta filtrada

Em determinadas ferramentas de análise, uma porta pode ser indicada
como filtrada quando mecanismos de filtragem, como firewalls,
impedem determinar claramente seu estado.

## Segurança

Ao administrar um sistema:

- exponha somente os serviços necessários;
- restrinja acesso por firewall quando apropriado;
- mantenha serviços atualizados;
- utilize autenticação adequada;
- desative serviços desnecessários;
- monitore serviços expostos.

## Interpretação de uma varredura

O resultado de uma ferramenta de análise de portas deve ser
interpretado junto com o contexto do ambiente.

Uma porta aberta não comprova, por si só:

- existência de vulnerabilidade;
- comprometimento;
- atividade maliciosa.

Da mesma forma, uma porta fechada não significa que o sistema esteja
completamente seguro.

## Limitação

Informações sobre portas devem ser utilizadas para diagnóstico e
administração autorizada de sistemas.

## Fontes

- IANA — Service Name and Transport Protocol Port Number Registry:
  https://www.iana.org/assignments/service-names-port-numbers/
- NIST — Guide to Enterprise Telework, Remote Access, and BYOD Security:
  https://csrc.nist.gov/publications/detail/sp/800-46/rev-2/final
