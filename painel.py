import streamlit as st
from pathlib import Path
from supabase import create_client


st.set_page_config(page_title="Digital Animale", page_icon= "🅰",layout="wide")


SENHA = "animale@2145"

# Ordem fixa das seções no painel (mesma ordem de hoje)
ORDEM_SECOES = ["Geral", "E-commerce", "CRM & Clientes"]


@st.cache_data(ttl=300)
def carregar_relatorios():
    supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_ANON_KEY"])
    response = (
        supabase.table("relatorios")
        .select("*")
        .order("created_at")
        .execute()
    )
    return response.data

try:
    relatorios = carregar_relatorios()
except Exception as e:
    st.error(f"Erro ao carregar relatórios: {e}")
    relatorios = []

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if not st.session_state.autenticado:
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
        width: 800vh;
    }

    button[aria-label="visibility"] span,
    button[aria-label="visibility_off"] span {
        display: none !important;
    }

    div[data-testid="stTextInput"] button span {
        display: none !important;
        font-size: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
    }

    div[data-testid="stTextInput"] button {
        overflow: hidden !important;
    }
    </style>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login", width=800):
            st.markdown("#### Painel de Relatórios")
            st.markdown("Digite a senha para acessar.")
            senha = st.text_input("Senha", type="password", width=800)
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

header[data-testid="stHeader"] {
    display: none !important;
}

.block-container {
    padding-top: 0 !important;
}

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

a[data-testid^="stBaseLinkButton"] {
    min-height: 120px !important;
    height: auto !important;
    width: 100% !important;
    align-items: flex-start !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    padding: 20px !important;
    border-radius: 18px !important;
    border: 2px solid #999 !important;
    background-color: #f5f5f5 !important;
    transition: border-color 0.15s !important;
    box-sizing: border-box !important;
    overflow-wrap: break-word !important;
    word-break: break-word !important;    
}

a[data-testid^="stBaseLinkButton"]:hover {
    border-color: #6E6E6E !important;
    background-color: #E3E3E3 !important;
}

a[data-testid^="stBaseLinkButton"] p:first-child {
    font-size: 15px !important;
    font-weight: 600 !important;
    margin: 0 0 10px 0 !important;
    line-height: 1.3 !important;
    color: #1a1a1a !important;
    text-align: center !important;
}

a[data-testid^="stBaseLinkButton"] p:nth-child(2) {
    font-size: 15px !important;
    font-weight: 400 !important;
    margin: 10 !important;
    line-height: 1.5 !important;
    color: #1a1a1a!important;
    text-align: center !important;
}

a[data-testid^="stBaseLinkButton"] p:nth-child(3) {
    font-size: 13px !important;
    font-weight: 400 !important;
    margin: 0 !important;
    line-height: 1.3 !important;
    color: #999 !important;
    text-align: center !important;
}

/* Data de atualização — quarto parágrafo */
a[data-testid^="stBaseLinkButton"] p:last-child {
    font-size: 11px !important;
    font-weight: 400 !important;
    margin: 0 !important;
    line-height: 1.3 !important;
    color: #999 !important;
    text-align: center !important;
}

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


# Agrupa os relatórios vindos do Supabase nas mesmas seções de sempre.
# A ordem dentro de cada seção segue a ordem de criação (created_at),
# que é a mesma ordem em que os relatórios originais foram cadastrados.
agrupado = {titulo: [] for titulo in ORDEM_SECOES}
for r in relatorios:
    titulo = r.get("secao") or "Geral"
    agrupado.setdefault(titulo, []).append(r)

secoes = [
    {"titulo": titulo, "dashboards": dashboards}
    for titulo, dashboards in agrupado.items()
    if dashboards
]


st.space()
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
                icone = d.get("icone") or ""
                nome_exibicao = f"{icone}  {d['nome']}" if icone else d["nome"]
                data = d.get("ultima_atualizacao") or "—"
                url = d.get("url") or "https://dashboard-em-construcao.netlify.app/"
                st.link_button(
                    f"**{nome_exibicao}**\n\n{d['descricao']}\n\nResponsável: {d['responsavel']}\n\nAtualizado em: {data}",
                    url,
                    use_container_width=True
                )

    st.markdown("<br>", unsafe_allow_html=True)
