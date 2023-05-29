import pandas as pd
import matplotlib.pyplot as plt

def analisar_dados(nome_arquivo):
    try:
        dados = pd.read_csv(nome_arquivo)
        print('Dados carregados com sucesso.')


        print('Estatísticas básicas:')
        print(dados.describe())


        colunas = list(dados.columns)
        print('Colunas disponíveis:', colunas)
        colunas_selecionadas = input('Digite o nome das colunas separadas por vírgula (ou deixe em branco para todas as colunas): ')
        if colunas_selecionadas:
            colunas_selecionadas = [col.strip() for col in colunas_selecionadas.split(',')]
            print('Estatísticas selecionadas:')
            print(dados[colunas_selecionadas].describe())


        filtro_coluna = input('Digite o nome da coluna para aplicar o filtro (ou deixe em branco para não filtrar): ')
        filtro_valor = input('Digite o valor para o filtro (ou deixe em branco para não filtrar): ')
        if filtro_coluna and filtro_valor:
            dados_filtrados = dados[dados[filtro_coluna] == filtro_valor]
            print('Dados filtrados:')
            print(dados_filtrados)


        coluna_x = input('Digite o nome da coluna para o eixo X do gráfico de dispersão: ')
        coluna_y = input('Digite o nome da coluna para o eixo Y do gráfico de dispersão: ')
        dados.plot(x=coluna_x, y=coluna_y, kind='scatter')
        plt.xlabel(coluna_x)
        plt.ylabel(coluna_y)
        plt.title('Gráfico de Dispersão')
        plt.savefig('grafico_dispersao.png')
        plt.show()

    except FileNotFoundError:
        print(f'Arquivo "{nome_arquivo}" não encontrado.')
    except Exception as e:
        print(f'Erro ao analisar os dados: {str(e)}')


nome_arquivo = input('Digite o nome do arquivo CSV: ')
analisar_dados(nome_arquivo)

