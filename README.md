# ExcelManipulationPy

# O QUE É?
Essa é uma manipulação de planilha para automatizar o preenchimento dos custos de uma empresa para o setor de contabilidade.

# TEORIA
Cada custo tem seu determinado numero de conta.
Para não precisar fazer o trabalho manualmente e cansativo de colocar um por um, criei esse script em Python que manipula planilhas e vai automatizar todo esse processo de colocar cada custo em seu determinado numero de conta.
Na tabela `CONTA` vem os gastos da empresa e na tabela `CEN. CUSTO` o script vai preencher com o nome daquele determiando custo.
![Screenshot_2](https://github.com/cosmosredshiftsete/ExcelManipulationPy/assets/161028555/fc358cfa-8fe2-4639-ab44-95f10b9f6c2a)

# PRÁTICA 
https://github.com/cosmosredshiftsete/ExcelManipulationPy/assets/161028555/6c620349-fd71-477b-abb2-ad86723f1f2a
O numero da `CONTA` de cada custo e o nome deles você terá que alterar no código como aqui por exemplo:

```python
tabela.loc[tabela["CONTA"]=="02.00.000", "CEN. CUSTO"] = "DESPESAS OPERACIONAIS - FIXA"
tabela.loc[tabela["CONTA"]=="02.01.000", "CEN. CUSTO"] = "RECURSOS HUMANOS"
tabela.loc[tabela["CONTA"]=="02.01.001", "CEN. CUSTO"] = "SALARIOS"
tabela.loc[tabela["CONTA"]=="02.01.002", "CEN. CUSTO"] = "GPS"
tabela.loc[tabela["CONTA"]=="02.01.003", "CEN. CUSTO"] = "FGTS"
```
