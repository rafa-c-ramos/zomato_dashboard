#################### Bibliotecas e Módulos ####################
# Fazer os imports necessários
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px

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
st.set_page_config(page_title='Internacional', layout='wide', page_icon='🌎')

#################### Título da página do Streamlit ####################
st.markdown('# Dashboard - Internacional')

#################### Barra lateral do Streamlit ####################
# Inserir o logo da empresa
image = Image.open('zomato_logo.png')
st.sidebar.image(image, width=200)

# Criar o título e subtítulo da barra lateral
st.sidebar.markdown('# Zomato')
st.sidebar.markdown('## The Fastest Delivery')
st.sidebar.markdown('---')

# Criar o filtro do país
filtro_pais = st.sidebar.multiselect('Selecione os países:',
                                     ['India', 'United States of America', 'Philippines',
                                      'South Africa', 'England', 'New Zealand',
                                      'United Arab Emirates', 'Australia', 'Brazil',
                                      'Canada', 'Indonesia', 'Turkey',
                                      'Qatar', 'Singapore', 'Sri Lanka'],
                                     default=['India', 'United States of America', 'Philippines',
                                      'South Africa', 'England', 'New Zealand',
                                      'United Arab Emirates', 'Australia', 'Brazil',
                                      'Canada', 'Indonesia', 'Turkey',
                                      'Qatar', 'Singapore', 'Sri Lanka'])

linhas_selecionadas = dados['country_name'].isin(filtro_pais)
dados = dados.loc[linhas_selecionadas, :]
st.sidebar.markdown('---')

#################### Layout do Streamlit ####################
# Criar e nomear as tabs (abas) 
tab_1, tab_2 = st.tabs(['Visão Países', 'Visão Cidades'])

### Preencher a tab 1 (Visão Países)
with tab_1:
  # Criar gráfico da quantidade de cidades registradas por país
  with st.container():
    aux = dados.groupby(['country_name'])['city'].nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(aux, x='country_name', y='city',
             labels = {'country_name':'País', 'city':'Quantidade de cidades'},
             title = 'Quantidade de Cidades Registradas por País')
    st.plotly_chart(fig, use_container_width=True)
    
  # Criar gráfico da quantidade de restaurantes registrados por país
  with st.container():
    aux = dados.groupby(['country_name'])['restaurant_id'].nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(aux, x='country_name', y='restaurant_id',
             labels = {'country_name':'País', 'restaurant_id':'Quantidade de restaurantes'},
             title = 'Quantidade de Restaurantes Registrados por País')
    st.plotly_chart(fig, use_container_width=True)

  # Criar gráfico da distribuição das avaliações dos restaurantes por país
  with st.container():
    fig = px.box(dados, x='country_name', y='aggregate_rating',
             labels = {'country_name':'País', 'aggregate_rating':'Avaliações agregadas'},
             title = 'Avaliações Agregadas por País')
    st.plotly_chart(fig, use_container_width=True)
    
### Preencher a tab 2 (Visão Cidades)
with tab_2:
  # Criar gráfico da quantidade da quantidade de avaliações por cidade e país
  with st.container():
    aux = dados.groupby(['city', 'country_name'])['votes'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(aux, x='city', y='votes', color='country_name',
                 color_discrete_sequence=px.colors.qualitative.G10,
             labels = {'city':'Cidade', 'votes':'Quantidade de avaliações', 'country_name':'País'},
             title = 'Quantidade de Avaliações por Cidade e País')
    st.plotly_chart(fig, use_container_width=True)
    
  # Criar gráfico da quantidade de restaurantes por cidade e país
  with st.container():
    aux = dados.groupby(['city', 'country_name'])['restaurant_id'].nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(aux, x='city', y='restaurant_id', color='country_name',
                 color_discrete_sequence=px.colors.qualitative.G10,
             labels = {'city':'Cidade', 'restaurant_id':'Quantidade de restaurantes', 'country_name':'País'},
             title = 'Quantidade de Restaurantes por Cidade e País')
    st.plotly_chart(fig, use_container_width=True)

  # Criar gráfico da quantidade de culinárias por cidade e país
  with st.container():
    aux = dados.groupby(['city', 'country_name'])['cuisines'].nunique().sort_values(ascending=False).reset_index()
    fig = px.bar(aux, x='city', y='cuisines', color='country_name',
                 color_discrete_sequence=px.colors.qualitative.G10,
             labels = {'city':'Cidade', 'cuisines':'Quantidade de culinárias', 'country_name':'País'},
             title = 'Quantidade de Culinárias por Cidade e País')
    st.plotly_chart(fig, use_container_width=True)
                   
    