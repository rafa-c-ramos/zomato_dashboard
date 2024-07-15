# Importar o pacote necessário
import inflection

######## Tratamento de Dados e Criação de Features ########
# Criar o dicionário de países dos restaurantes
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zealand",
162: "Philippines",
166: "Qatar",
184: "Singapore",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

# Criar a função que nomeia os países com base no dicionário
def country_name(country_id):
  return COUNTRIES[country_id]

# Criar a função que categoriza os preços dos restaurantes
def create_price_category(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"
  
# Criar o dicionário das cores
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

# Criar a função que nomeia as cores com base no dicionário
def set_color_name(color_code):
  return COLORS[color_code]

# Criar a função que renomeia as variáveis
def rename_columns(dataframe):
  df = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  snakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(snakecase, cols_old))
  df.columns = cols_new
  return df