import pandas as pd
import openpyxl

#ler o arquivo da planilha
tabela = pd.read_excel("Planilha.xlsx")

#localizar a tabela "CONTA", Identificar contas e atualizar a tabela "CEN. CUSTO"
tabela.loc[tabela["CONTA"]=="01.00.000", "CEN. CUSTO"] = "CUSTOS"
tabela.loc[tabela["CONTA"]=="01.01.000", "CEN. CUSTO"] = "CUSTO MERCADORIAS COMPRAS"
tabela.loc[tabela["CONTA"]=="01.01.001", "CEN. CUSTO"] = "COMPRA MERCADORIA A PRAZO"
tabela.loc[tabela["CONTA"]=="01.01.002", "CEN. CUSTO"] = "COMPRA MERCADORIA A VISTA"
tabela.loc[tabela["CONTA"]=="01.01.003", "CEN. CUSTO"] = "BONIFICACOES RECEBIDAS"
tabela.loc[tabela["CONTA"]=="01.01.004", "CEN. CUSTO"] = "FRETE SOBRE COMPRAS"
tabela.loc[tabela["CONTA"]=="01.01.005", "CEN. CUSTO"] = "COMPRA USO/CONS LOJA"
tabela.loc[tabela["CONTA"]=="01.01.006", "CEN. CUSTO"] = "RETORNO DE GARANTIA"
tabela.loc[tabela["CONTA"]=="01.01.007", "CEN. CUSTO"] = "DEVOLUÇÃO FORNECEDOR"
tabela.loc[tabela["CONTA"]=="01.01.008", "CEN. CUSTO"] = "COMPRA MERCADORIA ENTRE LOJAS"
tabela.loc[tabela["CONTA"]=="02.00.000", "CEN. CUSTO"] = "DESPESAS OPERACIONAIS - FIXA"
tabela.loc[tabela["CONTA"]=="02.01.000", "CEN. CUSTO"] = "RECURSOS HUMANOS"
tabela.loc[tabela["CONTA"]=="02.01.001", "CEN. CUSTO"] = "SALARIOS"
tabela.loc[tabela["CONTA"]=="02.01.002", "CEN. CUSTO"] = "GPS"
tabela.loc[tabela["CONTA"]=="02.01.003", "CEN. CUSTO"] = "FGTS"
tabela.loc[tabela["CONTA"]=="02.01.004", "CEN. CUSTO"] = "FERIAS"
tabela.loc[tabela["CONTA"]=="02.01.005", "CEN. CUSTO"] = "13 SALARIOS"
tabela.loc[tabela["CONTA"]=="02.01.006", "CEN. CUSTO"] = "CONTRIBUIÇÃO ASSISTENCIAL"
tabela.loc[tabela["CONTA"]=="02.01.007", "CEN. CUSTO"] = "CONTRIBUIÇÃO SINDICAL"
tabela.loc[tabela["CONTA"]=="02.01.008", "CEN. CUSTO"] = "ESOCIAL"
tabela.loc[tabela["CONTA"]=="02.01.009", "CEN. CUSTO"] = "INSS DARF"
tabela.loc[tabela["CONTA"]=="02.01.010", "CEN. CUSTO"] = "RESCISAO CONTRATUAL"
tabela.loc[tabela["CONTA"]=="02.01.011", "CEN. CUSTO"] = "EXAME DEMISSIONAL / ADMISSIONA"
tabela.loc[tabela["CONTA"]=="02.01.012", "CEN. CUSTO"] = "HOSPEDAGEM"
tabela.loc[tabela["CONTA"]=="02.01.013", "CEN. CUSTO"] = "ADIANTAMENTO DE SALARIO"
tabela.loc[tabela["CONTA"]=="02.01.014", "CEN. CUSTO"] = "REPRESENTANTES"
tabela.loc[tabela["CONTA"]=="02.01.015", "CEN. CUSTO"] = "CONVENIO ODONTOLOGICO"
tabela.loc[tabela["CONTA"]=="02.01.016", "CEN. CUSTO"] = "COMISSÃO BOCA CAIXA"
tabela.loc[tabela["CONTA"]=="02.01.017", "CEN. CUSTO"] = "VALE TRANSPORTE"
tabela.loc[tabela["CONTA"]=="02.01.018", "CEN. CUSTO"] = "PROLABORE"
tabela.loc[tabela["CONTA"]=="02.01.019", "CEN. CUSTO"] = "PLANO DE SAÚDE"
tabela.loc[tabela["CONTA"]=="02.01.020", "CEN. CUSTO"] = "VALE ALIMENTAÇÃO"
tabela.loc[tabela["CONTA"]=="02.01.021", "CEN. CUSTO"] = "MEDICINA NO TRABALHO"
tabela.loc[tabela["CONTA"]=="02.01.022", "CEN. CUSTO"] = "VALE SALARIAL"
tabela.loc[tabela["CONTA"]=="02.01.023", "CEN. CUSTO"] = "PONTO MAIS (PONTO DIGITAL)"
tabela.loc[tabela["CONTA"]=="02.01.024", "CEN. CUSTO"] = "BONUS"
tabela.loc[tabela["CONTA"]=="02.01.025", "CEN. CUSTO"] = "HORA EXTRA"
tabela.loc[tabela["CONTA"]=="02.01.026", "CEN. CUSTO"] = "TMAGNA"
tabela.loc[tabela["CONTA"]=="02.01.027", "CEN. CUSTO"] = "RETIRADA DE SOCIOS"
tabela.loc[tabela["CONTA"]=="02.02.000", "CEN. CUSTO"] = "INVESTIMENTOS"
tabela.loc[tabela["CONTA"]=="02.02.001", "CEN. CUSTO"] = "FINANCIAMENTO VEICULOS"
tabela.loc[tabela["CONTA"]=="02.02.002", "CEN. CUSTO"] = "RENDIMENTO DE INVESTIMENTOS"
tabela.loc[tabela["CONTA"]=="02.02.003", "CEN. CUSTO"] = "CONSORCIO"
tabela.loc[tabela["CONTA"]=="02.02.004", "CEN. CUSTO"] = "IMPLANTAÇÃO SISTEMA CITEL"
tabela.loc[tabela["CONTA"]=="02.02.005", "CEN. CUSTO"] = "MÁQUINAS E EQUIPAMENTOS"
tabela.loc[tabela["CONTA"]=="02.02.006", "CEN. CUSTO"] = "LOGOMARCA"
tabela.loc[tabela["CONTA"]=="02.02.007", "CEN. CUSTO"] = "INVESTIMENTO IMOVEIS"
tabela.loc[tabela["CONTA"]=="02.02.009", "CEN. CUSTO"] = "CAPACITACAO"
tabela.loc[tabela["CONTA"]=="02.04.000", "CEN. CUSTO"] = "DESPESAS ADMINISTRATIVAS"
tabela.loc[tabela["CONTA"]=="02.04.001", "CEN. CUSTO"] = "ALUGUEL"
tabela.loc[tabela["CONTA"]=="02.04.002", "CEN. CUSTO"] = "TELEFONE FIXO"
tabela.loc[tabela["CONTA"]=="02.04.003", "CEN. CUSTO"] = "AGUA"
tabela.loc[tabela["CONTA"]=="02.04.004", "CEN. CUSTO"] = "ENERGIA ELETRICA"
tabela.loc[tabela["CONTA"]=="02.04.005", "CEN. CUSTO"] = "SOFTWARE - CITEL"
tabela.loc[tabela["CONTA"]=="02.04.006", "CEN. CUSTO"] = "SERASA / SCPC"
tabela.loc[tabela["CONTA"]=="02.04.007", "CEN. CUSTO"] = "DIARISTA"
tabela.loc[tabela["CONTA"]=="02.04.008", "CEN. CUSTO"] = "MATERIAL DE ESCRITORIO"
tabela.loc[tabela["CONTA"]=="02.04.009", "CEN. CUSTO"] = "ESCRITORIO DE CONTABILIDADE"
tabela.loc[tabela["CONTA"]=="02.04.010", "CEN. CUSTO"] = "TELEFONIA MOVEL"
tabela.loc[tabela["CONTA"]=="02.04.011", "CEN. CUSTO"] = "VIAGENS E DESLOCAMENTO"
tabela.loc[tabela["CONTA"]=="02.04.012", "CEN. CUSTO"] = "MONITORAMENTO E ALARME"
tabela.loc[tabela["CONTA"]=="02.04.013", "CEN. CUSTO"] = "ARMAZENAMENTO NOTAS CITEL"
tabela.loc[tabela["CONTA"]=="02.04.014", "CEN. CUSTO"] = "SEGURO PREDIAL"
tabela.loc[tabela["CONTA"]=="02.04.015", "CEN. CUSTO"] = "ALVARA / BOMBEIROS"
tabela.loc[tabela["CONTA"]=="02.04.016", "CEN. CUSTO"] = "ASSOCIAÇÃO COMERCIAL"
tabela.loc[tabela["CONTA"]=="02.04.017", "CEN. CUSTO"] = "MERCADO"
tabela.loc[tabela["CONTA"]=="02.04.018", "CEN. CUSTO"] = "GRAFICA"
tabela.loc[tabela["CONTA"]=="02.04.019", "CEN. CUSTO"] = "LANCHES E REFEIÇÕES"
tabela.loc[tabela["CONTA"]=="02.04.021", "CEN. CUSTO"] = "USO/CONS LOJA"
tabela.loc[tabela["CONTA"]=="02.04.022", "CEN. CUSTO"] = "CORREIOS E TELEGRAFOS"
tabela.loc[tabela["CONTA"]=="02.04.023", "CEN. CUSTO"] = "PEDAGIO"
tabela.loc[tabela["CONTA"]=="02.04.024", "CEN. CUSTO"] = "MANUTENÇÃO LOJA"
tabela.loc[tabela["CONTA"]=="02.04.025", "CEN. CUSTO"] = "ALUGUEL MAQUINA CARTAO"
tabela.loc[tabela["CONTA"]=="02.04.026", "CEN. CUSTO"] = "ADVOGADO - COBRANÇA / HONORARI"
tabela.loc[tabela["CONTA"]=="02.04.027", "CEN. CUSTO"] = "ESTACIONAMENTO"
tabela.loc[tabela["CONTA"]=="02.04.028", "CEN. CUSTO"] = "UNIFORMES E EQUIP DE TRABALHO"
tabela.loc[tabela["CONTA"]=="02.04.029", "CEN. CUSTO"] = "SERVICOS TI"
tabela.loc[tabela["CONTA"]=="02.04.030", "CEN. CUSTO"] = "MANUT E CONSERV DE MAQUINAS"
tabela.loc[tabela["CONTA"]=="02.04.031", "CEN. CUSTO"] = "RECARGA EXTINTORES"
tabela.loc[tabela["CONTA"]=="02.04.032", "CEN. CUSTO"] = "SERV TECNICO PROFISSIONAL"
tabela.loc[tabela["CONTA"]=="02.04.033", "CEN. CUSTO"] = "CARTORIO"
tabela.loc[tabela["CONTA"]=="02.04.034", "CEN. CUSTO"] = "RENOVAÇÃO CERTIFICADO DIGITAL"
tabela.loc[tabela["CONTA"]=="02.04.035", "CEN. CUSTO"] = "MATERIAL DE LIMPEZA"
tabela.loc[tabela["CONTA"]=="02.04.036", "CEN. CUSTO"] = "MANUTENÇÃO DE VEÍCULOS- HIGIENIZAÇÃO"
tabela.loc[tabela["CONTA"]=="02.04.037", "CEN. CUSTO"] = "AGUA MINERAL"
tabela.loc[tabela["CONTA"]=="02.04.038", "CEN. CUSTO"] = "DOAÇÃO"
tabela.loc[tabela["CONTA"]=="02.04.039", "CEN. CUSTO"] = "INTERNET"
tabela.loc[tabela["CONTA"]=="02.04.040", "CEN. CUSTO"] = "SEGURO VIDA FUNCIONARIOS"
tabela.loc[tabela["CONTA"]=="02.04.042", "CEN. CUSTO"] = "SINDICATO - MENSALIDADE"
tabela.loc[tabela["CONTA"]=="02.04.043", "CEN. CUSTO"] = "MANUTENÇÃO DE COMPUTADORES"
tabela.loc[tabela["CONTA"]=="02.04.044", "CEN. CUSTO"] = "INFORMATICA"
tabela.loc[tabela["CONTA"]=="02.04.045", "CEN. CUSTO"] = "SEGURANÇA"
tabela.loc[tabela["CONTA"]=="02.04.046", "CEN. CUSTO"] = "GAS"
tabela.loc[tabela["CONTA"]=="02.04.047", "CEN. CUSTO"] = "FRETADO"
tabela.loc[tabela["CONTA"]=="02.04.048", "CEN. CUSTO"] = "MONITORAMENTO VEICULOS"
tabela.loc[tabela["CONTA"]=="02.04.049", "CEN. CUSTO"] = "ETIQUETAS"
tabela.loc[tabela["CONTA"]=="02.04.050", "CEN. CUSTO"] = "LOCAÇAO DE GERADOR"
tabela.loc[tabela["CONTA"]=="02.04.051", "CEN. CUSTO"] = "TV POR ASSINATURA"
tabela.loc[tabela["CONTA"]=="02.04.052", "CEN. CUSTO"] = "SEGURO DE VIDA"
tabela.loc[tabela["CONTA"]=="02.04.053", "CEN. CUSTO"] = "SOFTWARE"
tabela.loc[tabela["CONTA"]=="02.04.054", "CEN. CUSTO"] = "MANUTENÇÃO PREDIAL"
tabela.loc[tabela["CONTA"]=="02.04.055", "CEN. CUSTO"] = "REUNIAO VIRTUAL"
tabela.loc[tabela["CONTA"]=="02.04.056", "CEN. CUSTO"] = "PROVEDOR DE INTERNET"
tabela.loc[tabela["CONTA"]=="02.04.057", "CEN. CUSTO"] = "MOTOBOY"
tabela.loc[tabela["CONTA"]=="02.04.058", "CEN. CUSTO"] = "LOCAÇÃO DE IMPRESSORAS"
tabela.loc[tabela["CONTA"]=="02.04.059", "CEN. CUSTO"] = "LOCAÇÃO DE PABX"
tabela.loc[tabela["CONTA"]=="02.04.060", "CEN. CUSTO"] = "EMBALAGENS"
tabela.loc[tabela["CONTA"]=="02.04.061", "CEN. CUSTO"] = "ARQUITETA"
tabela.loc[tabela["CONTA"]=="02.04.062", "CEN. CUSTO"] = "TRIBUNAL DE JUSTIÇA"
tabela.loc[tabela["CONTA"]=="02.04.063", "CEN. CUSTO"] = "LOCAÇÃO DE ANDAIMES"
tabela.loc[tabela["CONTA"]=="02.04.064", "CEN. CUSTO"] = "PREMIAÇÃO"
tabela.loc[tabela["CONTA"]=="02.04.065", "CEN. CUSTO"] = "REFORMA"
tabela.loc[tabela["CONTA"]=="02.04.066", "CEN. CUSTO"] = "EMPRESTIMO"
tabela.loc[tabela["CONTA"]=="02.04.067", "CEN. CUSTO"] = "OBRA"
tabela.loc[tabela["CONTA"]=="02.04.068", "CEN. CUSTO"] = "LOCAÇAO DE EMPILHADEIRA"
tabela.loc[tabela["CONTA"]=="02.04.069", "CEN. CUSTO"] = "PGTO CARTAO DE CREDITO"
tabela.loc[tabela["CONTA"]=="02.04.070", "CEN. CUSTO"] = "PROCESSO TRABALIHISTA"
tabela.loc[tabela["CONTA"]=="02.04.071", "CEN. CUSTO"] = "GOOGLE MAPS"
tabela.loc[tabela["CONTA"]=="02.04.072", "CEN. CUSTO"] = "JUNTOS SOMOS MAIS"
tabela.loc[tabela["CONTA"]=="02.04.073", "CEN. CUSTO"] = "VISTORIAS VEICULARES"
tabela.loc[tabela["CONTA"]=="02.04.074", "CEN. CUSTO"] = "DESPESAS COM BOMBEIRO"
tabela.loc[tabela["CONTA"]=="02.04.075", "CEN. CUSTO"] = "REGULARIZAÇÃO PALANQUE"
tabela.loc[tabela["CONTA"]=="02.04.076", "CEN. CUSTO"] = "LOCAÇAO DE MAQUINAS"
tabela.loc[tabela["CONTA"]=="02.04.077", "CEN. CUSTO"] = "CONSULTORIA  ADMINISTRATIVA"
tabela.loc[tabela["CONTA"]=="02.04.078", "CEN. CUSTO"] = "MARCAS E PATENTES"
tabela.loc[tabela["CONTA"]=="02.05.000", "CEN. CUSTO"] = "DESPESAS MARKETING"
tabela.loc[tabela["CONTA"]=="02.05.001", "CEN. CUSTO"] = "PATROCINIOS DIVERSOS"
tabela.loc[tabela["CONTA"]=="02.05.002", "CEN. CUSTO"] = "PUBLICIDADE"
tabela.loc[tabela["CONTA"]=="02.05.003", "CEN. CUSTO"] = "DIVULGACAO INTERNET"
tabela.loc[tabela["CONTA"]=="02.05.004", "CEN. CUSTO"] = "FESTAS E CONFRATERNIZAÇOES"
tabela.loc[tabela["CONTA"]=="02.05.005", "CEN. CUSTO"] = "COMISSOES E CORRETAGENS"
tabela.loc[tabela["CONTA"]=="02.05.006", "CEN. CUSTO"] = "PROMOTOR MARKETING"
tabela.loc[tabela["CONTA"]=="02.05.007", "CEN. CUSTO"] = "BRINDES PROMOCIONAIS"
tabela.loc[tabela["CONTA"]=="02.05.008", "CEN. CUSTO"] = "PRESTAÇÃO DE SERVIÇOS - MARKETING"
tabela.loc[tabela["CONTA"]=="02.05.009", "CEN. CUSTO"] = "EVENTO"
tabela.loc[tabela["CONTA"]=="02.06.000", "CEN. CUSTO"] = "DESPESAS FINANCEIRAS"
tabela.loc[tabela["CONTA"]=="02.06.001", "CEN. CUSTO"] = "TAXAS BANCARIAS"
tabela.loc[tabela["CONTA"]=="02.06.002", "CEN. CUSTO"] = "TAXA ANTECIPACAO DUPLICATA/CHEQUE"
tabela.loc[tabela["CONTA"]=="02.06.003", "CEN. CUSTO"] = "DESCONTOS CONCEDIDOS"
tabela.loc[tabela["CONTA"]=="02.06.004", "CEN. CUSTO"] = "TAXA CARTAO"
tabela.loc[tabela["CONTA"]=="02.06.005", "CEN. CUSTO"] = "JUROS - ATRASO PAGTO TITULOS"
tabela.loc[tabela["CONTA"]=="02.06.006", "CEN. CUSTO"] = "TAXAS BOLETOS EMITIDOS"
tabela.loc[tabela["CONTA"]=="02.06.007", "CEN. CUSTO"] = "TAXA ANTECIPACAO CARTAO CREDITO"
tabela.loc[tabela["CONTA"]=="02.06.008", "CEN. CUSTO"] = "TAXA MERCADO LIVRE - VENDA INTERNET"
tabela.loc[tabela["CONTA"]=="02.06.009", "CEN. CUSTO"] = "TAXA BOLETO ENVIO CARTORIO"
tabela.loc[tabela["CONTA"]=="02.06.010", "CEN. CUSTO"] = "TAXA ALPE"
tabela.loc[tabela["CONTA"]=="02.06.011", "CEN. CUSTO"] = "DEVOLUÇÃO DE TAXA DE CARTORIO"
tabela.loc[tabela["CONTA"]=="02.06.012", "CEN. CUSTO"] = "DEVOLUÇÃO DE TITULO PAGO EM CARTORIO"
tabela.loc[tabela["CONTA"]=="02.07.000", "CEN. CUSTO"] = "RECEBIVEIS NAO RECUPERADOS"
tabela.loc[tabela["CONTA"]=="02.07.001", "CEN. CUSTO"] = "PERDAS DE COBRANCA"
tabela.loc[tabela["CONTA"]=="02.07.002", "CEN. CUSTO"] = "PERDAS COM CHEQUES"
tabela.loc[tabela["CONTA"]=="02.07.003", "CEN. CUSTO"] = "QUEBRA DE CAIXA"
tabela.loc[tabela["CONTA"]=="03.00.000", "CEN. CUSTO"] = "RECEITAS"
tabela.loc[tabela["CONTA"]=="03.01.000", "CEN. CUSTO"] = "RECEITAS BRUTAS COM VENDAS"
tabela.loc[tabela["CONTA"]=="03.01.001", "CEN. CUSTO"] = "VENDAS A VISTA"
tabela.loc[tabela["CONTA"]=="03.01.002", "CEN. CUSTO"] = "VENDAS A PRAZO"
tabela.loc[tabela["CONTA"]=="03.01.003", "CEN. CUSTO"] = "BRINDES E BONIFICACOES RECEBID"
tabela.loc[tabela["CONTA"]=="03.01.004", "CEN. CUSTO"] = "VENDAS CARTAO"
tabela.loc[tabela["CONTA"]=="03.01.005", "CEN. CUSTO"] = "VENDAS CHEQUE"
tabela.loc[tabela["CONTA"]=="03.01.006", "CEN. CUSTO"] = "DEPOSITO EM CONTA (CLIENTE)"
tabela.loc[tabela["CONTA"]=="03.01.007", "CEN. CUSTO"] = "VENDA VALE FUNCIONARIO"
tabela.loc[tabela["CONTA"]=="03.01.008", "CEN. CUSTO"] = "CREDITO FORNECEDOR"
tabela.loc[tabela["CONTA"]=="03.01.009", "CEN. CUSTO"] = "TAXA DE CARTORIO RECEBIDA"
tabela.loc[tabela["CONTA"]=="03.01.010", "CEN. CUSTO"] = "COMISSÃO PROFISSIONAL"
tabela.loc[tabela["CONTA"]=="03.01.011", "CEN. CUSTO"] = "VENDAS A PRAZO BOLETO"
tabela.loc[tabela["CONTA"]=="03.01.012", "CEN. CUSTO"] = "MAQUINA TINTOMETRICA"
tabela.loc[tabela["CONTA"]=="03.01.013", "CEN. CUSTO"] = "RECEBIMENTO REFERENTE A LICITAÇÕES"
tabela.loc[tabela["CONTA"]=="03.01.014", "CEN. CUSTO"] = "FRETE SOBRE VENDA"
tabela.loc[tabela["CONTA"]=="03.01.015", "CEN. CUSTO"] = "CREDITO ALPE"
tabela.loc[tabela["CONTA"]=="03.02.000", "CEN. CUSTO"] = "RECEITAS FINANCEIRAS"
tabela.loc[tabela["CONTA"]=="03.02.001", "CEN. CUSTO"] = "DESCONTOS OBTIDOS"
tabela.loc[tabela["CONTA"]=="03.02.002", "CEN. CUSTO"] = "JUROS ATIVOS"
tabela.loc[tabela["CONTA"]=="03.02.003", "CEN. CUSTO"] = "MULTA JUROS S/ TITULOS VENCIDO"
tabela.loc[tabela["CONTA"]=="03.02.004", "CEN. CUSTO"] = "RECEBIMENTO DE SEGUROS"
tabela.loc[tabela["CONTA"]=="03.03.000", "CEN. CUSTO"] = "DEDUÇÕES DA RECEITA"
tabela.loc[tabela["CONTA"]=="03.03.001", "CEN. CUSTO"] = "VENDAS CANCELADAS E DEVOLUÇÕES"
tabela.loc[tabela["CONTA"]=="03.04.000", "CEN. CUSTO"] = "EMPRESTIMOS"
tabela.loc[tabela["CONTA"]=="03.04.001", "CEN. CUSTO"] = "EMPRESTIMO"
tabela.loc[tabela["CONTA"]=="03.04.002", "CEN. CUSTO"] = "DEVOLUÇÃO DE EMPRESTIMO"
tabela.loc[tabela["CONTA"]=="03.04.003", "CEN. CUSTO"] = "FURTO"
tabela.loc[tabela["CONTA"]=="03.04.004", "CEN. CUSTO"] = "TROCA"
tabela.loc[tabela["CONTA"]=="03.05.000", "CEN. CUSTO"] = "ALUGUEIS"
tabela.loc[tabela["CONTA"]=="03.05.001", "CEN. CUSTO"] = "ALUGUEIS RECEBIDOS"
tabela.loc[tabela["CONTA"]=="04.00.000", "CEN. CUSTO"] = "CONTAS TRANSITORIAS"
tabela.loc[tabela["CONTA"]=="04.01.000", "CEN. CUSTO"] = "MOVIMENTACAO ENTRE BANCOS"
tabela.loc[tabela["CONTA"]=="04.01.001", "CEN. CUSTO"] = "CHEQUE DEVOLVIDO"
tabela.loc[tabela["CONTA"]=="04.01.004", "CEN. CUSTO"] = "TRANSFERENCIA ENTRE CONTAS"
tabela.loc[tabela["CONTA"]=="04.01.005", "CEN. CUSTO"] = "DEPOSITO DE CHEQUES"
tabela.loc[tabela["CONTA"]=="04.01.006", "CEN. CUSTO"] = "REPASSE DE CHEQUE P/ FORNECEDO"
tabela.loc[tabela["CONTA"]=="04.01.007", "CEN. CUSTO"] = "TROCA DE CHEQUE"
tabela.loc[tabela["CONTA"]=="05.00.000", "CEN. CUSTO"] = "TRIBUTOS"
tabela.loc[tabela["CONTA"]=="05.01.000", "CEN. CUSTO"] = "IMPOSTOS FEDERAIS"
tabela.loc[tabela["CONTA"]=="05.01.001", "CEN. CUSTO"] = "SIMPLES NACIONAL"
tabela.loc[tabela["CONTA"]=="05.01.002", "CEN. CUSTO"] = "DARF 0561 (IRRF)"
tabela.loc[tabela["CONTA"]=="05.01.003", "CEN. CUSTO"] = "DARF 2089 (IRPJ)"
tabela.loc[tabela["CONTA"]=="05.01.004", "CEN. CUSTO"] = "DARF 2172 (COFINS)"
tabela.loc[tabela["CONTA"]=="05.01.005", "CEN. CUSTO"] = "DARF 2372 (CSLL)"
tabela.loc[tabela["CONTA"]=="05.01.006", "CEN. CUSTO"] = "DARF 5856 (COFINS)"
tabela.loc[tabela["CONTA"]=="05.01.007", "CEN. CUSTO"] = "DARF 8109 (PIS)"
tabela.loc[tabela["CONTA"]=="05.01.008", "CEN. CUSTO"] = "DARF 5952 (CRF)"
tabela.loc[tabela["CONTA"]=="05.01.009", "CEN. CUSTO"] = "DARF 1708 (IRRF)"
tabela.loc[tabela["CONTA"]=="05.01.010", "CEN. CUSTO"] = "DARF 6912 (PIS)"
tabela.loc[tabela["CONTA"]=="05.01.011", "CEN. CUSTO"] = "DARF 1345"
tabela.loc[tabela["CONTA"]=="05.01.012", "CEN. CUSTO"] = "DARF 0220 (IRPJ)"
tabela.loc[tabela["CONTA"]=="05.01.013", "CEN. CUSTO"] = "DARF 6012 (CSLL)"
tabela.loc[tabela["CONTA"]=="05.01.014", "CEN. CUSTO"] = "DARF 8045 IRRF"
tabela.loc[tabela["CONTA"]=="05.01.015", "CEN. CUSTO"] = "DARF 2203"
tabela.loc[tabela["CONTA"]=="05.02.000", "CEN. CUSTO"] = "IMPOSTOS ESTADUAIS"
tabela.loc[tabela["CONTA"]=="05.02.001", "CEN. CUSTO"] = "ICMS"
tabela.loc[tabela["CONTA"]=="05.02.002", "CEN. CUSTO"] = "ICMS ST"
tabela.loc[tabela["CONTA"]=="05.02.003", "CEN. CUSTO"] = "ICMS DIFERENÇA DE ALIQUOTA"
tabela.loc[tabela["CONTA"]=="05.02.004", "CEN. CUSTO"] = "GNRE ST"
tabela.loc[tabela["CONTA"]=="05.02.005", "CEN. CUSTO"] = "GNRE DIFAL"
tabela.loc[tabela["CONTA"]=="05.02.006", "CEN. CUSTO"] = "GNRE FCP"
tabela.loc[tabela["CONTA"]=="05.02.007", "CEN. CUSTO"] = "GNRE"
tabela.loc[tabela["CONTA"]=="05.02.008", "CEN. CUSTO"] = "DARE - SP"
tabela.loc[tabela["CONTA"]=="05.03.000", "CEN. CUSTO"] = "IMPOSTOS MUNICIPAIS"
tabela.loc[tabela["CONTA"]=="05.03.001", "CEN. CUSTO"] = "IPTU"
tabela.loc[tabela["CONTA"]=="05.03.002", "CEN. CUSTO"] = "ISS TRIBUTO MUNICIPAL/FEDERAL"
tabela.loc[tabela["CONTA"]=="05.03.003", "CEN. CUSTO"] = "TAXA DE FUNCIONAMENTO"
tabela.loc[tabela["CONTA"]=="05.03.004", "CEN. CUSTO"] = "TFE TAXA DE FISCALIZ DE ESTABELECIMENTO"
tabela.loc[tabela["CONTA"]=="05.03.005", "CEN. CUSTO"] = "ITBI"
tabela.loc[tabela["CONTA"]=="05.03.006", "CEN. CUSTO"] = "MULTAS DE TRANSITO"
tabela.loc[tabela["CONTA"]=="05.03.007", "CEN. CUSTO"] = "DESDOBRO DE LOTE"
tabela.loc[tabela["CONTA"]=="05.03.008", "CEN. CUSTO"] = "MULTA DE ESTABELECIMENTO IRREGULAR"
tabela.loc[tabela["CONTA"]=="06.00.000", "CEN. CUSTO"] = "DESPESAS VARIAVEIS"
tabela.loc[tabela["CONTA"]=="06.01.000", "CEN. CUSTO"] = "MANUTENÇÃO DE VEICULOS"
tabela.loc[tabela["CONTA"]=="06.01.001", "CEN. CUSTO"] = "MANUTENÇÃO DE VEICULOS"
tabela.loc[tabela["CONTA"]=="06.01.002", "CEN. CUSTO"] = "MANUTENÇAO EMPILHADEIRA"
tabela.loc[tabela["CONTA"]=="06.01.003", "CEN. CUSTO"] = "TACOGRAFO"
tabela.loc[tabela["CONTA"]=="06.01.004", "CEN. CUSTO"] = "MANUTENÇÃO ELEVADOR"
tabela.loc[tabela["CONTA"]=="06.01.005", "CEN. CUSTO"] = "MANUTENÇÃO CARRINHO HIDRAULICO"
tabela.loc[tabela["CONTA"]=="06.03.000", "CEN. CUSTO"] = "COMBUSTIVEL FROTA"
tabela.loc[tabela["CONTA"]=="06.03.001", "CEN. CUSTO"] = "COMBUSTIVEL FROTA"
tabela.loc[tabela["CONTA"]=="06.03.002", "CEN. CUSTO"] = "VALE COMBUSTIVEL"
tabela.loc[tabela["CONTA"]=="06.04.000", "CEN. CUSTO"] = "IPVA, LICENCIMENTO + SEG. OBRI"
tabela.loc[tabela["CONTA"]=="06.04.001", "CEN. CUSTO"] = "IPVA"
tabela.loc[tabela["CONTA"]=="06.04.002", "CEN. CUSTO"] = "LICENCIAMENTO"
tabela.loc[tabela["CONTA"]=="06.05.000", "CEN. CUSTO"] = "SEGURO VEICULOS"
tabela.loc[tabela["CONTA"]=="06.05.001", "CEN. CUSTO"] = "SEGURO VEICULOS"
tabela.loc[tabela["CONTA"]=="06.05.002", "CEN. CUSTO"] = "SEGURO CARGA"
tabela.loc[tabela["CONTA"]=="06.06.000", "CEN. CUSTO"] = "MULTAS VEICULOS"
tabela.loc[tabela["CONTA"]=="06.06.001", "CEN. CUSTO"] = "MULTAS VEICULOS"
tabela.loc[tabela["CONTA"]=="07.00.000", "CEN. CUSTO"] = "DIRETORIA"
tabela.loc[tabela["CONTA"]=="07.01.000", "CEN. CUSTO"] = "RETIRADA"
tabela.loc[tabela["CONTA"]=="07.01.003", "CEN. CUSTO"] = "RETIRADA EXTRA"
tabela.loc[tabela["CONTA"]=="07.01.004", "CEN. CUSTO"] = "PARTICIPACAO NOS LUCROS"
tabela.loc[tabela["CONTA"]=="10.00.000", "CEN. CUSTO"] = "CENTRO CAMPESTRE"
tabela.loc[tabela["CONTA"]=="10.01.000", "CEN. CUSTO"] = "CENTRO CAMPESTRE"
tabela.loc[tabela["CONTA"]=="10.01.001", "CEN. CUSTO"] = "CENTRO CAMPESTRE DESPESAS"
tabela.loc[tabela["CONTA"]=="99.00.000", "CEN. CUSTO"] = "GRUPO-CONTA CONVERSAO"
tabela.loc[tabela["CONTA"]=="99.99.000", "CEN. CUSTO"] = "SUB.GRUPO-CONTA CONVERSAO"
tabela.loc[tabela["CONTA"]=="99.99.999", "CEN. CUSTO"] = "CONTA CONVERSAO"



#Criar arquivo com tudo feito
tabela.to_excel("Planilha_pandas.xlsx", index=False)