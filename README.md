# Excel Manipulation whith Python

## O QUE É?
Essa é uma manipulação de planilha para automatizar o preenchimento dos custos de uma empresa para o setor de contabilidade.

## TEORIA
Cada custo tem seu determinado numero de conta.
Para não precisar fazer o trabalho manualmente e cansativo de colocar um por um, criei esse script em Python que manipula planilhas e vai automatizar todo esse processo de colocar cada custo em seu determinado numero de conta.
Na tabela `CONTA` vem os gastos da empresa e na tabela `CEN. CUSTO` o script vai preencher com o nome daquele determiando custo.
![Screenshot_2](https://github.com/cosmosredshiftsete/ExcelManipulationPy/assets/161028555/fc358cfa-8fe2-4639-ab44-95f10b9f6c2a)

## PRÁTICA 

https://github.com/cosmosredshiftsete/ExcelManipulationPy/assets/161028555/6c620349-fd71-477b-abb2-ad86723f1f2a

O numero da `CONTA` de cada custo e o nome deles você terá que alterar no código para o script consegui identificar na planilha e preencher.

## EXEMPLO


tabela.loc[tabela["`CONTA`"]=="numero do custo", "CEN. CUSTO"] = "`nome do custo`"
```python
tabela.loc[tabela["CONTA"]=="123456789", "CEN. CUSTO"] = "RECURSOS HUMANOS"
tabela.loc[tabela["CONTA"]=="987654321", "CEN. CUSTO"] = "SALARIOS"
tabela.loc[tabela["CONTA"]=="111111111", "CEN. CUSTO"] = "VR"
tabela.loc[tabela["CONTA"]=="000000000", "CEN. CUSTO"] = "FGTS"
```
## IDEIAS
- Após alterar o código e deixar de acordo com os da sua empresa, é possivel fazer o arquivo `.exe` e assim sempre que alguem precisar usar, é só deixar a planilha na mesma pasta do arquivo, no mesmo nome que você colocou no script e só executar ele.
```pyinstaller --onefile``` (no terminal do VSCode)
- É possivel tambem criar uma pop screen que invés de você ter que alterar o nome da planilha e o local dela, você o seleciona através da tela interativa que você criar.
```pyinstaller --onefile -w``` (no terminal do VSCode)

## CRÉDITOS
- @cosmosredshiftsete
