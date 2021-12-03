
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import requests
from math import ceil
import io
from functools import reduce
import streamlit.components.v1 as cmpt


def git_index():
    """funcao para buscar o arquivo index.csv  no github e retorna um dataframe"""

    url_index = f'https://raw.githubusercontent.com/Edmilson-Filimone/datasets/main/crio_index.csv'
    fil = requests.get(url_index).content
    dfi = pd.read_csv(io.StringIO(fil.decode('utf-8')))
    return dfi


def git_busca():
    """funcao para buscar o arquivo criobank.csv  no github e retorna um dataframe"""
    url_index = f'https://raw.githubusercontent.com/Edmilson-Filimone/datasets/main/criobank.csv'
    fil = requests.get(url_index).content
    df = pd.read_csv(io.StringIO(fil.decode('utf-8')))
    return df


def logo():
    col1, col2, col3 = st.sidebar.columns(3)
    url = 'https://github.com/Edmilson-Filimone/datasets/raw/main/logo.png'
    pic_content = requests.get(url).content
    with open('image.png', 'wb') as file:
        foto = file.write(pic_content)
        file.close()

    pil = Image.open('image.png')
    col2.image(pil, use_column_width=True, clamp=True)
    col1.write('')


def div(h, cor, texto, curva):
    """funcao div - retorna uma string do texto HTML com propiedades
        ajustaveis(h-titulo(h1,h2)/paragrafo(p), cor, texto)"""

    main = f"""<div style="background-color:{cor};border-radius:{curva}px;padding-top:1.5%;padding-bottom:0.5%;font-family:arial;
            width:100%">
            <{h} style="color:white;text-align:center;">{texto}</{h}>
            </div>"""
    return main


def html_main_body(data_frame):
    # soma total de cada categoria no dataframe -- para o painel
    Filtrado = data_frame[data_frame['Isolado']!='<vazio>']
    criotubos = len(Filtrado['Isolado'])
    caixas = ceil(len(Filtrado['Caixa'])/25)
    isolados = len(Filtrado['Isolado'].unique())

    # Estrutura em HTML/CSS do painel #33F65C '#c9ddc9' #99ff99 ##404340 ##464e5F #F4D44E
    html_cpainel = f"""

<html lang="pt-br">
<head>
    <!-- title>Admin panel dashboard card design usign html and css - www.pakainfo.com</title--->
    <meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<link href="https://fonts.googleapis.com/css?family=Raleway:100,200,400,500,600" rel="stylesheet" type="text/css">
</head>

<body>
<div class="main-part">
<div class="cpanel">
<div class="icon-part">
<i class="fa fa-database" aria-hidden="true"></i><br>
<small style="color: white">Criotubos</small>
<p>{criotubos}</p>
</div>
<div class="card-content-part">
<a href="#">Unidades</a>
</div>
</div>
<div class="cpanel cpanel-green">
<div class="icon-part">
<i class="fa fa-cubes" aria-hidden="true"></i><br>
<small style="color: white">Caixas</small>
<p>{caixas}</p>
</div>
<div class="card-content-part">
<a href="#">Unidades</a>
</div>
</div>
<div class="cpanel cpanel-orange">
<div class="icon-part">
<i class="fa fa-flask" aria-hidden="true"></i><br>
<small style="color: white">Isolados</small>
<p>{isolados}</p>
</div>
<div class="card-content-part">
<a href="#">Unidades</a>
</div>
</div>
</div>
</body>
"""

    css_cpainel = """

<style type="text/css">
    body{
background:#eee;
font-family: 'Raleway', sans-serif;
}
.main-part{
width:80%;
margin:0 auto;
text-align: center;
padding: 0px 5px;
}
.cpanel{
width:32%;
display: inline-block;
background-color:#34495E;
color:#fff;
margin-top: 50px;
}
.icon-part i{
font-size: 30px;
padding:10px;
border:1px solid #fff;
border-radius:50%;
margin-top:-25px;
margin-bottom: 10px;
background-color:#34495E;
}
.icon-part p{
margin:0px;
font-size: 20px;
padding-bottom: 10px;
}
.card-content-part{
background-color: #2F4254;
padding: 5px 0px;
}
.cpanel .card-content-part:hover{
background-color: #5a5a5a;
cursor: pointer;
}
.card-content-part a{
color:#fff;
text-decoration: none;
}
.cpanel-green .icon-part,.cpanel-green .icon-part i{
background-color: #16A085;
}
.cpanel-green .card-content-part{
background-color: #149077;
}
.cpanel-orange .icon-part,.cpanel-orange .icon-part i{
background-color: #F39C12;
}
.cpanel-orange .card-content-part{
background-color: #DA8C10;
}
</style>"""

    st.markdown(html_cpainel, True)
    st.markdown(css_cpainel, True)


def download_button(data, nome):
    file = data.to_csv().encode('utf-8')

    st.download_button(label='Baixar os dados', data=file, file_name=nome, mime='csv')


def main_criobank():
    # side-bar label
    global select_box_cp, select_box_local, select_box_ano, select_box_resist, select_box_especie, sub_3, select_box_animal


    st.sidebar.markdown(div(h='h2', cor='#464e5F', curva=0, texto='Crio-Bank'), unsafe_allow_html=True)
    st.sidebar.text('')

    df = git_busca()
    dfi = git_index()
    lista_1 = list(dfi['Canister'].unique())
    lista_2 = list(dfi['Caixa'].unique())
    lista_3 = list(df['Isolado'].unique())
    lista_4 = list(df['Especie'].unique())
    lista_5 = list(df['Status_de_resistencia'].unique())
    lista_6 = list(df['Ano_de_criopreservacao'].unique())
    lista_7 = list(df['Local_de_colheita'].unique())
    lista_8 = list(df['Animal_de_colheita'].unique())
    lista_9 = list(df['Agente_crioprotector'].unique())
    # side-bar form, select-box, botao da form:

    # Form 1 - Caixas
    forma_1 = st.sidebar.form(key='form-1')
    forma_1.markdown("**Menu**")
    select_box_canister = forma_1.selectbox(label='Canister', options=lista_1)
    select_box_caixa = forma_1.selectbox(label='Caixa', options=lista_2)
    col1,col2 = forma_1.columns(2)
    sub = col1.form_submit_button('---ver---')
    #Button for general_report function
    butao = col2.form_submit_button('Panorama')

    # Form 2 - Isolados
    forma_2 = st.sidebar.form(key='form-2')
    # forma_2.markdown("**Isolados**")
    select_box_isolados = forma_2.selectbox(label='Isolados', options=lista_3)
    sub_2 = forma_2.form_submit_button('---ver---')

    # Check-box - pesquisa profunda
    # marco = st.sidebar.checkbox(label='Pesquisa profunda (varios parametros)')
    select_box_cp = select_box_local = select_box_ano = select_box_resist = select_box_especie = select_box_animal = sub_3 = st.empty  # solvinng escope issues

    # Form 3 - Isolados
    forma_3 = st.sidebar.form(key='form-3')
    exp = forma_3.expander('Pesquisa profunda')
    exp.markdown("**Filtrar os dados**")
    select_box_especie = exp.selectbox(label='Especie', options=lista_4)
    select_box_resist = exp.selectbox(label='Status de resistencia', options=lista_5)
    select_box_ano = exp.selectbox(label='Ano de criopreservacao', options=lista_6)
    select_box_local = exp.selectbox(label='Proveniencia', options=lista_7)
    select_box_animal = exp.selectbox(label='Animal de colheita', options=lista_8)
    select_box_cp = exp.selectbox(label='Crioprotector', options=lista_9)
    sub_3 = forma_3.form_submit_button('---ver---')

    # Condicoes da forms:
    if butao:
      general_report()

    # form-1:
    elif sub:

        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto='Painel do banco de isolados de tripanossoma'),
                    unsafe_allow_html=True)
        st.text('')
        # dataframe filtring
        if select_box_caixa == 'Todas':
            df_filtrado = df[df['Canister'] == select_box_canister]
        else:
            df_filtrado = df[(df['Canister'] == select_box_canister) & (df['Caixa'] == select_box_caixa)]

        # Agregacao
        # agg = df_filtrado.groupby('Isolado').agg({'Caixa': 'count', 'Isolado': 'count'})
        agg = df_filtrado['Isolado'].value_counts()

        # html_body
        html_main_body(df_filtrado)
        st.text('')  # espaco

        # cabecalho para o dataframe
        st.markdown(div(h='h6', cor='#464e5F', curva=0,
                        texto=f'Tabela com os dados do {select_box_canister} | {select_box_caixa}'),
                    True)
        st.text('')

        st.dataframe(df_filtrado, width=1400, height=500)
        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto=f'Resumo - Somatororio'),
                    True)
        st.dataframe(agg.reset_index(), width=1400, height=200)
        download_button(data=df_filtrado, nome=f'Ficha_{select_box_canister}_{select_box_caixa}.csv')

    elif sub_2:
        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto='Painel do banco de isolados de tripanossoma'),
                    unsafe_allow_html=True)
        st.text('')
        df_filtrado = df[df['Isolado'] == select_box_isolados]
        agg = df_filtrado['Isolado'].value_counts()

        # html_body
        html_main_body(df_filtrado)
        st.text('')

        # cabecalho para o dataframe
        st.markdown(div(h='h6', cor='#464e5F', curva=7, texto=f'Tabela com os dados do isolado {select_box_isolados}'),
                    True)
        st.text('')
        st.dataframe(df_filtrado, width=1400, height=500)
        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto=f'Resumo - Somatororio'),
                    True)
        st.dataframe(agg.T, width=1400, height=500)
        download_button(data=df_filtrado, nome=f'Ficha_{select_box_isolados}.csv')

    elif sub_3:
        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto='Painel do banco de isolados de tripanossoma'),
                    unsafe_allow_html=True)
        st.text('')
        # criando varios dataframes para cada pesquisa
        df1 = df.loc[df['Especie'] == select_box_especie.replace('Todos', '')]
        df2 = df.loc[df['Status_de_resistencia'] == select_box_resist.replace('Todos', '')]
        df3 = df.loc[df['Ano_de_criopreservacao'] == select_box_ano.replace('Todos', '')]
        df4 = df.loc[df['Local_de_colheita'] == select_box_local.replace('Todos', '')]
        df5 = df.loc[df['Animal_de_colheita'] == select_box_animal.replace('Todos', '')]
        df6 = df.loc[df['Agente_crioprotector'] == select_box_cp.replace('Todos', '')]

        colunas = ['Canister', 'Canister-Level', 'Caixa', 'Posicao do Criotubo', 'Isolado',
                   'Especie', 'Status_de_resistencia', 'Local_de_colheita', 'Provincia',
                   'Animal_de_colheita', 'Ano_de_criopreservacao', 'Agente_crioprotector',
                   'Volume/tubo','Data','Observacao']

        colunas_x = ['Canister_x', 'Canister-Level_x', 'Caixa_x', 'Posicao do Criotubo_x', 'Isolado_x', 'Especie_x',
                     'Status_de_resistencia_x', 'Local_de_colheita_x', 'Animal_de_colheita_x',
                     'Ano_de_criopreservacao_x',
                     'Agente_crioprotector_x', 'Volume/tubo_x']

        # juntando todos os dataframes (pd.merge()) com base na coluna ID
        data_frames = [df1, df2, df3, df4, df5, df6]
        new_data = []

        for data in data_frames:
            if data.size > 0:
                new_data.append(data)

        # aglutinando os dataframes (funcao reduce e lambda para agrupar varios dataframes)
        # fonte: https://newbedev.com/merging-multiple-dataframes-in-pandas-code-example
        df_merged = reduce(lambda left, right: pd.merge(left, right, on=['id'], how='inner'), new_data)
        numero_de_colunas = len(df_merged.columns)

        df_merged.columns = [list(range(numero_de_colunas))]
        df_merged = df_merged[list(range(15))]
        df_merged.columns = colunas
        df_filtrado = df_merged

        # agg = df_filtrado.groupby('Isolado').agg({'Caixa': 'count', 'Isolado': 'count', 'Especie': 'count',
        #                                          'Status_de_resistencia': 'count'})
        agg = df_filtrado['Isolado'].value_counts()

        # html_body
        html_main_body(df_filtrado)
        st.text('')

        # cabecalho para o dataframe
        st.markdown(div(h='h6', cor='#464e5F', curva=7, texto=f'Tabela com os dados do isolado {select_box_especie}'),
                    True)
        st.text('')
        st.dataframe(df_filtrado, width=1400, height=500)
        st.markdown(div(h='h6', cor='#464e5F', curva=0, texto=f'Resumo - Somatororio'),
                    True)
        st.dataframe(agg.T, width=1400, height=500)
        download_button(data=df_filtrado, nome=f'Ficha_{select_box_especie}_filtro.csv')
    else:
        st.markdown("""

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <style>.bcontent {margin-top: 5px; margin-left:0px; margin=right: 0px;}</style>
</head>
<body>
    <div class="container bcontent">
        <div class="jumbotron">
            <h1>Bem vindo ao Criobank! </h1>
            <p class="lead">Para monitorar o crescente número de isolados de tripanossoma armazenados no banco de isolados do CB-UEM,
                foi criado este espaço virtual onde você pode ficar a par de todos os regitros através do nosso painel.</p>
            <hr>
            <a class="btn btn-success btn-lg" href="http://www.cb.uem.mz/" role="button" style="color:white;">Sobre nós</a>
        </div>
    </div>
</body>
</html>""", True)

        st.markdown("""
##### **Como proceder ?**
- Para ver a informação: escolha o conteúdo que deseja ver atraves dos submenus do painel e pressione o botão “ver”
##### **O que você vai encontrar ?**
- Todos os registros devidamente organizados e sumarizados
- Três submenus para filtrar o conteudo:\n
- Um painel indicador\n
        - Número de caixas em uso\n
        - Número total de criotubos\n  
        - Número de isolados criopreservados
        """, True)
        
        st.markdown("""
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <style>.fa {padding: 10px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;
                          margin: 5px 5px;border-radius: 40px}
                          .fa:hover {opacity: 0.7;}
                          .fa-facebook {background: #3B5998;color: white;}
                          .fa-twitter {background: #55ACEE;color: white;}
                          .fa-google {background: #dd4b39;color: white;}
                          .fa-instagram {background: #125688;color: white;}
                </style>
</head>                
				<body>
    				<!-- Add font awesome icons -->
    				<h6> Encontre nos aqui tambem 😄 👇</h6>
					<a href="https://facebook.com/" class="fa fa-facebook" style="color:white"></a>
					<a href="https://twitter.com/" class="fa fa-twitter" style="color:white"></a>
					<a href="https://google.com/" class="fa fa-google" style="color:white"></a>
					<a href="https://instagram.com/" class="fa fa-instagram" style="color:white"></a>
				</body>				
</html>"""
, unsafe_allow_html=True)
        

def general_report():
  df = git_busca()
  st.markdown(div(h='h6', cor='#464e5F', curva=0, texto='Dados Gerais'), unsafe_allow_html=True)
  html_main_body(df)
  st.markdown('<hr>', True)
  st.markdown(div(h='p', cor='#464e5F', curva=0, texto='Lista de isolados (15+)'), unsafe_allow_html=True)
  agg_1 = df[df['Isolado']!='<vazio>']
  agg = pd.DataFrame(agg_1['Isolado'].value_counts()).nlargest(n=15, columns='Isolado')
  agg.reset_index(inplace=True)
  agg.columns = ['Isolados','Total']
  fig1 = plt.figure(figsize=(6, 4), dpi=420)
  sns.set_style('darkgrid')
  sns.lineplot(data=agg, x='Isolados', y='Total',linewidth=1.8, marker='o', markersize=14)
  #plt.fill_between(x=agg['Isolados'], y1=agg['Total'], color='#CCCCFF')
  plt.xticks(rotation=80)
  plt.xlabel('')
  plt.ylabel('')
  
  col1,col2 = st.columns((1,2))

  tabela = pd.DataFrame(agg_1['Isolado'].value_counts())
  tabela.reset_index(inplace=True)
  tabela.columns = ['Isolados','Total']

  file = tabela.to_csv().encode('utf-8')
  
  col1.dataframe(tabela, height=500)
  col1.markdown('<hr>', True)
  col1.download_button(label='Baixar os dados', data=file, file_name='Numero_de_isolados.csv', mime='csv')
  
  col2.pyplot(fig1, clear_figure=True, use_container_width=True)  # plotando
  st.markdown('<hr>', unsafe_allow_html=True)
  

def info():
    expander = st.sidebar.expander('Notas importantes')
    expander.markdown('**Informação**')
    expander.info("""- Para mudar o tema
                    selecione: Settings->Theme""")
    expander.warning("""- No Mobile: selecione a opção "vista para site de computador":
    para melhor enquadramento""")
    expander_2 = st.sidebar.expander('Sobre')
    expander_2.info("""- Criobank Monitor v.1.0 
                        Desenvolvido em Python 3 | Streamlit framework, et al|      
                        Dev: Edmilson Filimone
                        Correspondência: philimone99@gmail.com""")


if __name__ == '__main__':
    st.set_page_config(page_title='CB-CrioBank',
                       layout='wide',
                       page_icon='https://github.com/Edmilson-Filimone/datasets/raw/main/image_2021-11-04_115813.png'
                       )
    logo()
    main_criobank()
    info()
    # st.error('Oopahhh!!! Problemas com a rede...')
    # st.info('Tente novamente...')
    # st.info('Para suporte: philimone99@gmail.com')
