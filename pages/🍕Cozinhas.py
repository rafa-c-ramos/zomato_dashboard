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
st.set_page_config(page_title='Cozinhas', layout='wide', page_icon='🍕')

#################### Título do Streamlit ####################
st.markdown('# Dashboard - Cozinhas')

#################### Barra lateral do Streamlit ####################
# Inserir o logo da empresa
image = Image.open('zomato_logo.png')
st.sidebar.image(image, width=200)

# Criar o título e subtítulo da barra lateral
st.sidebar.markdown('# Zomato')
st.sidebar.markdown('## The Fastest Delivery')
st.sidebar.markdown('---')

#################### Layout do Streamlit ####################
# Criar e nomear as tabs (abas) 
tab_1, tab_2 = st.tabs(['Visão Restaurantes', 'Visão Culinárias'])

### Preencher a tab 1 (Visão Restaurantes)     
with tab_1:
  # Criar gráfico da quantidade de avaliações por restaurante (top 20)
  with st.container():
    aux = dados.groupby('restaurant_name')['votes'].sum().sort_values(ascending=False).head(20).reset_index()
    fig = px.bar(aux, x='restaurant_name', y='votes',
             labels = {'restaurant_name':'Restaurante', 'votes':'Quantidade de avaliações'},
             title = 'Top 20 Restaurantes com Mais Avaliações')
    st.plotly_chart(fig, use_container_width=True)
        
  # Criar gráfico do top 20 restaurantes presentes em mais países
  with st.container():
    aux = dados.groupby('restaurant_name')['country_name'].nunique().sort_values(ascending=False).head(20).reset_index()
    fig = px.bar(aux, x='restaurant_name', y='country_name',
             labels = {'restaurant_name':'Restaurante', 'country_name':'Quantidade de países'},
             title = 'Top 20 Restaurantes Presentes em Mais Países')
    st.plotly_chart(fig, use_container_width=True)
    
  # Criar gráfico do top 20 restaurantes presentes em mais cidades
  with st.container():
    aux = dados.groupby('restaurant_name')['city'].nunique().sort_values(ascending=False).head(20).reset_index()
    fig = px.bar(aux, x='restaurant_name', y='city',
             labels = {'restaurant_name':'Restaurante', 'city':'Quantidade de cidades'},
             title = 'Top 20 Restaurantes Presentes em Mais Cidades')
    st.plotly_chart(fig, use_container_width=True)
  
### Preencher a tab 2 (Visão Culinárias)     
with tab_2:
  # Criar gráfico do top 20 culinárias mais avaliadas
  with st.container():
    aux = dados.groupby('cuisines')['votes'].sum().sort_values(ascending=False).head(20).reset_index()
    fig = px.bar(aux, x='cuisines', y='votes',
                 labels = {'cuisines':'Culinária', 'votes':'Quantidade de avaliações'},
                 title = 'Top 20 Culinárias com Mais Avaliações')
    st.plotly_chart(fig, use_container_width=True)
    
  # Criar gráfico do top 20 culinárias mais presentes por país
  with st.container():    
    aux = dados.groupby('cuisines')['country_name'].nunique().sort_values(ascending=False).head(20).reset_index()
    fig = px.bar(aux, x='cuisines', y='country_name',
                 labels = {'cuisines':'Culinária', 'country_name':'Quantidade de países'},
                 title = 'Top 20 Culinárias Presentes em Mais Países')
    st.plotly_chart(fig, use_container_width=True)
    
    # Criar gráfico do top 20 culinárias mais presentes por cidade
    with st.container():    
     aux = dados.groupby('cuisines')['city'].nunique().sort_values(ascending=False).head(20).reset_index()
     fig = px.bar(aux, x='cuisines', y='city',
                  labels = {'cuisines':'Culinária', 'city':'Quantidade de cidades'},
                  title = 'Top 20 Culinárias Presentes em Mais Cidades')
     st.plotly_chart(fig, use_container_width=True)