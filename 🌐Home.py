#################### Bibliotecas e Módulos ####################
# Fazer os imports necessários
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# Importar o módulo de tratamento dos dados
import tratamento

#################### Leitura e Tratamento dos Dados ####################
# Ler os dados originais
dados_originais = pd.read_csv('zomato.csv')

# Tratar os dados originais com as funções criadas
dados_originais['country_name'] = dados_originais['Country Code'].map(tratamento.country_name)
dados_originais['price_category'] = dados_originais['Price range'].map(tratamento.create_price_category)
dados_originais['price_color_name'] = dados_originais['Rating color'].map(tratamento.set_color_name)
dados = tratamento.rename_columns(dados_originais)

#################### Configurações da página do Streamlit ####################
# Ajustar a configuração do Streamlit
st.set_page_config(page_title='Home', layout='wide', page_icon='🌐')

#################### Título da página do Streamlit ####################
st.markdown('# Zomato Growth Dashboard')

#################### Barra lateral do Streamlit ####################
# Criar o título e subtítulo da barra lateral do Streamlit
st.sidebar.markdown('# Zomato')
st.sidebar.markdown('## The Fastest Delivery')
st.sidebar.markdown('---')

# Inserir o logo da empresa no Streamlit
image = Image.open('zomato_logo.png')
st.sidebar.image(image, width=200)

# Escrever as informações na página
st.markdown("""
            Encontre seu restaurante favorito ao redor do mundo!
            """)

# Criar as métricas gerais
with st.container():
    st.title('Métricas Gerais')
    col_1, col_2, col_3, col_4, col_5 = st.columns(5, gap='large')
    
    # Criar a métrica de restaurantes registrados
    with col_1:
        n_restaurantes = dados['restaurant_id'].nunique()
        col_1.metric('Total de Restaurantes:', n_restaurantes)
        
    # Criar a métrica de países registrados
    with col_2:
        n_paises = dados['country_name'].nunique()
        col_1.metric('Total de Países:', n_paises)
        
    # Criar a métrica de cidades registrados
    with col_3:
        n_cidades = dados['city'].nunique()
        col_1.metric('Total de Cidades:', n_cidades)
        
    # Criar a métrica do total de avaliações feitas
    with col_4:
        n_avaliacoes = dados['votes'].sum()
        col_1.metric('Total de Avaliações:', n_avaliacoes)
          
    # Criar a métrica do total de tipos de culinária
    with col_5:
        n_culinarias = dados['cuisines'].nunique()
        col_1.metric('Total de Culinárias:', n_culinarias)    
        
# Escrever as informações na página
st.markdown("""            
            ### Ajuda
            GitHub: rafa-c-ramos.
            """)
    
    