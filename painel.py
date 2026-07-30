import streamlit as st
from pathlib import Path


st.set_page_config(page_title="Digital Animale", page_icon= "🅰",layout="wide")


SENHA = "animale-ecomm-2026"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

    html, body, [class*="css"], [data-testid] {
        font-family: 'Montserrat', sans-serif !important;
    }

    .login-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 80vh;
    }
    </style>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([2, 1, 2])

    with col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login", width= 600):
            st.markdown("#### Painel de Relatórios")
            st.markdown("Digite a senha para acessar.")
            senha = st.text_input("Senha", type="password")
            entrar = st.form_submit_button("Entrar", use_container_width=True)

        if entrar:
            if senha == SENHA:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Senha incorreta.")

    st.stop()


st.logo(r"LOGO_ANIMALE 1.png")

st.space()



st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

html, body, [class*="css"], [data-testid] {
    font-family: 'Montserrat', sans-serif !important;
}

/* Esconde o header nativo do Streamlit */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Remove espaço que o header deixa */
.block-container {
    padding-top: 0 !important;
}

/* Faixa do topo */
.top-bar {
    background-color: #1a1a1a;
    padding: 18px 40px;
    margin: -1rem -1rem 2rem -1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.top-bar-logo {
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.2em;
    color: #ffffff;
    text-transform: uppercase;
}

.top-bar-subtitle {
    font-size: 12px;
    color: #aaaaaa;
    letter-spacing: 0.05em;
}

/* Título da página */
.top-bar-title {
    font-size: 26px;
    font-weight: 600;
    color: #ffffff;
    margin: 0 0 4px 0;
}

.page-subtitle {
    font-size: 14px;
    color: #777;
    margin: 0 0 2rem 0;
}

/* Card base */
a[data-testid^="stBaseLinkButton"] {
    min-height: 120px !important;
    height: 120px !important;
    width: 100% !important;
    align-items: flex-start !important;
    display: flex !important;
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
    margin: 0 0 10px 0 !important;
    line-height: 1.3 !important;
    color: #1a1a1a !important;
    text-align: center !important;
}

/* Descrição — segundo parágrafo */
a[data-testid^="stBaseLinkButton"] p:nth-child(2) {
    font-size: 15px !important;
    font-weight: 400 !important;
    margin: 10 !important;
    line-height: 1.5 !important;
    color: #1a1a1a!important;
    text-align: center !important;
}

/* Responsável */
a[data-testid^="stBaseLinkButton"] p:last-child {
    font-size: 13px !important;
    font-weight: 400 !important;
    margin: 0 !important;
    line-height: 1.3 !important;
    color: #999!important;
    text-align: center !important;
}

/* Linha separadora das seções */
hr {
    margin: 8px 0 16px 0 !important;
    border: none !important;
    border-top: 1px solid #e0e0e0 !important;
}

</style>

<!-- Faixa do topo -->
<div class="top-bar">
    <span class="top-bar-logo">Animale</span>
    <span class="top-bar-title">Painel de Relatórios</span>
    <span class="top-bar-subtitle">E-commerce & CRM</span>
</div>

""", unsafe_allow_html=True)


# Dashboards organizados por seção
secoes = [
    {
        "titulo": "Geral",
        "dashboards": [
            {
                "nome": "🏪  Dossiê de Lojas",
                "desc": "Diagnóstico por loja: base, frequência, ticket",
                "resp": "Responsável: Theo Pereira",
                "url": "https://supervisao-lojas.netlify.app/",
                "badge": None,
            },
            {
                "nome": "👖  Performance A.J - Coleção",
                "desc": "Animale Jeans — performance por cidade",
                "resp": "Responsável: Theo Pereira",
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
                "resp": "Responsável: Aline Santos",
                "url": "https://performance-animale.netlify.app/",
                "badge": "principal",
            },
            {
                "nome": "🏗️  Visão de Estoque (em construção)",
                "desc": "Cobertura e ruptura por SKU",
                "resp": "Responsável: Aline Santos & Maria Gomes",
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
                "resp": "Responsável: Larissa Queiroz",
                "url": "https://acompanhamento-canais-crm.netlify.app/",
                "badge": None,
            },
            {
                "nome": "👥  Comitê Clientes",
                "desc": "Segmentação e saúde da base ativa",
                "resp": "Responsável: Theo Pereira & Luiz Vieira",
                "url": "https://somagrupo-my.sharepoint.com/:p:/g/personal/theo_pereira_animale_com_br/IQCDHZLjf7GmQpCSL8_RWrvXAb35ZTSUmOfxgV093xX9m64?wdExp=TEAMS-TREATMENT&web=1",
                "badge": None,
            },
            {
                "nome": "👥  A.J x Animale",
                "desc": "Estudo de base ativa e comportamento",
                "resp": "Responsável: Theo Pereira",
                "url": "https://somagrupo.sharepoint.com/:p:/s/DigitalAnimale/IQBxN162k2fyR5lR2IjqT7JJATnDkW92vI7UilnKcSWRulE?e=oK1LK3",
                "badge": None,
            },
            {
                "nome": "👥  Consumidoras Seda",
                "desc": "Análise do perfil de consumo",
                "resp": "Responsável: Luiz Vieira",
                "url": "https://somagrupo.sharepoint.com/:p:/s/DigitalAnimale/IQAK3Sm22jfaTrhsCpNqSDulAU4_ga2KUVsq8odXbgwTD3o?e=hvg2KX",
                "badge": None,
            },
            {
                "nome": "👥  Animale x Off Premium",
                "desc": "Análise cross-brand",
                "resp": "Responsável: Theo Pereira",
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
        cols = st.columns(cols_per_row, gap=10)
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(dashboards):
                break
            d = dashboards[idx]
            with col:
                st.link_button(
                    f"**{d['nome']}**\n\n{d['desc']}\n\n{d['resp']}",
                    d["url"],
                    use_container_width=True
                )

    st.markdown("<br>", unsafe_allow_html=True)
