import streamlit as st
from pathlib import Path

SENHA = "animale-ecomm-2026"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False


    with st.form("login"):
        senha = st.text_input("Senha", type="password")
        entrar = st.form_submit_button("Entrar")

    if entrar:
        if senha == SENHA:
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta.")

    st.stop()


st.logo(r"LOGO_ANIMALE 1.png")

st.title("Painel de Dashboards")

st.divider(width="stretch")



st.markdown("""
<style>

/* Card base */
a[data-testid^="stBaseLinkButton"] {
    min-height: 120px !important;
    height: 120px !important;
    width: 260px;
    display: flex !important;
    align-items: flex-start !important;
    justify-content: flex-start !important;
    padding: 20px !important;
    border-radius: 18px !important;
    border: 2px solid #999 !important;
    background-color: #f5f5f5 !important;
    transition: border-color 0.15s !important;
}

a[data-testid^="stBaseLinkButton"]:hover {
    border-color: #6E6E6E !important;
    background-color: #E3E3E3 !important;
}

/* Título — primeiro parágrafo */
a[data-testid^="stBaseLinkButton"] p:first-child {
    font-size: 15px !important;
    font-weight: 600 !important;
    margin: 0 0 10px 0 !important;   /* <-- só aqui tem margem inferior */
    line-height: 1.3 !important;
    color: #1a1a1a !important;
    text-align: center !important;
}

/* Descrição — segundo parágrafo */
a[data-testid^="stBaseLinkButton"] p:last-child {
    font-size: 15px !important;
    font-weight: 400 !important;
    margin: 10 !important;
    line-height: 1.5 !important;
    color: #1a1a1a!important;
    text-align: center !important;
}

/* Linha separadora das seções */
hr {
    margin: 8px 0 16px 0 !important;
    border: none !important;
    border-top: 1px solid #e0e0e0 !important;
}

</style>
""", unsafe_allow_html=True)


# Dashboards organizados por seção
secoes = [
    {
        "titulo": "Geral",
        "dashboards": [
            {
                "nome": "🏪  Dossiê de Lojas",
                "desc": "Diagnóstico por loja: base, frequência, ticket",
                "url": "https://supervisao-lojas.netlify.app/",
                "badge": None,
            },
            {
                "nome": "👖  Performance A.J - Coleção",
                "desc": "Animale Jeans — performance por cidade",
                "url": "https://aj-colecao.netlify.app/",
                "badge": "novo",
            },
        ],
    },
    {
        "titulo": "E-commerce",
        "dashboards": [
            {
                "nome": "📊  Analytics Dashboard",
                "desc": "Visão geral de vendas, clientes e performance",
                "url": "https://performance-animale.netlify.app/",
                "badge": "principal",
            },

            {
                "nome": "🏗️  Visão de Estoque (em construção)",
                "desc": "Cobertura e ruptura por SKU",
                "url": "https://performance-animale.netlify.app/",
                "badge": None,
            },
        ],
    },
    {
        "titulo": "CRM & Clientes",
        "dashboards": [
            {
                "nome": "📈  Monitor de Canais — CRM",
                "desc": "Performance e base ativa por canal",
                "url": "https://acompanhamento-canais-crm.netlify.app/",
                "badge": None,
            },
            {
                "nome": "👥  Comitê Clientes",
                "desc": "Segmentação e saúde da base ativa",
                "url": "https://somagrupo-my.sharepoint.com/:p:/g/personal/theo_pereira_animale_com_br/IQCDHZLjf7GmQpCSL8_RWrvXAb35ZTSUmOfxgV093xX9m64?wdExp=TEAMS-TREATMENT&web=1",
                "badge": None,
            },
            {
                "nome": "👥  A.J x Animale",
                "desc": "Estudo de base ativa e comportamento",
                "url": "https://somagrupo.sharepoint.com/:p:/s/DigitalAnimale/IQBxN162k2fyR5lR2IjqT7JJATnDkW92vI7UilnKcSWRulE?e=oK1LK3",
                "badge": None,
            },   
            { 
                "nome": "👥  Consumidoras Seda",
                "desc": "Análise do perfil de consumo",
                "url": "https://somagrupo.sharepoint.com/:p:/s/DigitalAnimale/IQAK3Sm22jfaTrhsCpNqSDulAU4_ga2KUVsq8odXbgwTD3o?e=hvg2KX",
                "badge": None,
            },  
            {
                "nome": "👥  Animale x Off Premium",
                "desc": "Análise cross-brand",
                "url": "https://somagrupo.sharepoint.com/:p:/s/DigitalAnimale/IQC9O5hcJqajSrT7Wfv5-qCpAeB8MqoiKN7q_rJwoGYHC48?e=TQ2ifb",
                "badge": None,
            },                      
        ],
    },
]



st.space()
# Renderiza em linhas de 3 colunas
cols_per_row = 3

for secao in secoes:
    st.subheader(secao["titulo"])
    st.divider()


    dashboards = secao["dashboards"]

    for i in range(0, len(dashboards), cols_per_row):
        cols = st.columns(cols_per_row, gap=150)
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(dashboards):
                break
            d = dashboards[idx]
            with col:
                st.link_button(
                    f"**{d['nome']}**\n\n{d['desc']}",
                    d["url"],
                    use_container_width=True
                )

    st.markdown("<br>", unsafe_allow_html=True) 


