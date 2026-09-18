---
titulo: Boas Práticas de Backup
categoria: backup
tipo: boas_praticas
nivel: basico
versao: 1.0
fontes:
  - CERT.br
  - CISA
---

# Boas Práticas de Backup

## Objetivo

Apresentar boas práticas para criação, proteção, manutenção e
recuperação de cópias de segurança.

Backups são uma medida importante para reduzir o impacto de eventos
como falhas de hardware, exclusão acidental, perda de dispositivos,
corrupção de dados e incidentes de segurança.

## O que é backup

Backup é uma cópia de dados mantida com o objetivo de possibilitar
sua recuperação caso os dados originais sejam perdidos, danificados
ou se tornem indisponíveis.

O backup deve ser tratado como parte de uma estratégia de proteção
de dados e não como substituto de outras medidas de segurança.

## Por que realizar backups

Um backup adequado pode auxiliar na recuperação após situações como:

- falha de hardware;
- exclusão acidental;
- corrupção de arquivos;
- perda ou roubo de dispositivo;
- ransomware;
- outros incidentes que tornem os dados indisponíveis.

## Regra 3-2-1

Uma estratégia conhecida de backup utiliza o princípio 3-2-1:

- manter pelo menos **3 cópias** dos dados;
- utilizar pelo menos **2 tipos ou meios diferentes** de armazenamento;
- manter pelo menos **1 cópia fora do ambiente principal**.

A aplicação exata deve considerar os requisitos e riscos de cada
organização.

## Backup não é o mesmo que sincronização

Sincronização mantém dados semelhantes entre locais, mas alterações
ou exclusões podem ser propagadas para todos os locais sincronizados.

Um backup deve possuir características que permitam recuperar uma
versão anterior dos dados quando necessário.

Por isso, sincronização não deve ser automaticamente considerada um
substituto de backup.

## Tipos de backup

### Backup completo

Copia todos os dados selecionados.

### Backup incremental

Copia os dados que foram alterados desde o backup anterior,
considerando a estratégia adotada pela solução.

### Backup diferencial

Copia os dados alterados desde um backup completo de referência.

A escolha depende de fatores como volume de dados, tempo disponível,
armazenamento e necessidade de recuperação.

## Proteção contra ransomware

Backups podem ser utilizados na recuperação após um ataque de
ransomware, mas somente serão úteis se estiverem disponíveis e não
tiverem sido comprometidos pelo incidente.

Sempre que possível:

- mantenha cópias protegidas contra alteração ou exclusão indevida;
- restrinja o acesso à infraestrutura de backup;
- utilize credenciais separadas e protegidas;
- monitore atividades relacionadas aos backups;
- teste regularmente a recuperação.

## Teste de restauração

Um backup que nunca foi restaurado não deve ser considerado
automaticamente confiável.

Realize testes periódicos para verificar:

- se os arquivos podem ser recuperados;
- se os dados estão íntegros;
- se os procedimentos estão documentados;
- quanto tempo a recuperação exige;
- se a recuperação atende aos requisitos do ambiente.

## Controle de acesso

O acesso aos backups deve ser restrito às pessoas e sistemas que
realmente necessitem dele.

Boas práticas incluem:

- utilizar contas individuais;
- aplicar menor privilégio;
- proteger credenciais;
- utilizar autenticação forte quando disponível;
- monitorar acessos;
- evitar compartilhamentos desnecessários.

## Criptografia

Quando apropriado, dados de backup podem ser protegidos por
criptografia, especialmente quando armazenados fora do ambiente
principal ou em locais com maior exposição.

A estratégia deve considerar também o gerenciamento seguro das
chaves ou credenciais necessárias para recuperação.

## Retenção

A organização deve definir por quanto tempo diferentes cópias serão
mantidas.

A política de retenção deve considerar:

- requisitos operacionais;
- necessidade de recuperação;
- requisitos legais ou regulatórios aplicáveis;
- espaço disponível;
- risco de perda de dados.

## Documentação

A estratégia de backup deve registrar, quando aplicável:

- quais dados são protegidos;
- frequência dos backups;
- local de armazenamento;
- responsável pelo processo;
- política de retenção;
- procedimento de restauração;
- resultado dos testes de recuperação.

## Checklist

- [ ] Existem cópias de segurança dos dados importantes?
- [ ] As cópias estão separadas do ambiente principal?
- [ ] Existe mais de um meio ou local de armazenamento?
- [ ] O acesso aos backups é restrito?
- [ ] Existem cópias protegidas contra alterações indevidas?
- [ ] A restauração já foi testada?
- [ ] O procedimento de recuperação está documentado?
- [ ] Existe uma política de retenção?

## Limitação

A existência de um backup não garante automaticamente a recuperação
dos dados. A qualidade da estratégia depende de fatores como
integridade, disponibilidade, proteção, retenção e capacidade de
restauração.

## Fontes

- CERT.br — Cartilha de Segurança para Internet:
  https://cartilha.cert.br/
- CISA — Data Backup Options:
  https://www.cisa.gov/stopransomware/ransomware-guide
- CISA — Ransomware Guide:
  https://www.cisa.gov/stopransomware/ransomware-guide
