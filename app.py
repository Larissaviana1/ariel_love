import streamlit as st
from datetime import datetime

# Configuração
st.set_page_config(page_title="Para você ❤️", layout="centered")

# Fundo romântico
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .main {
        background-color: #fff0f5;
    }
    </style>
""", unsafe_allow_html=True)

# Estado inicial
if "started" not in st.session_state:
    st.session_state.started = False

# Tela inicial
if not st.session_state.started:
    st.markdown("<h1 style='text-align: center;'>💖</h1>", unsafe_allow_html=True)
    
    if st.button("Clique aqui"):
        st.session_state.started = True
        st.rerun()

# Conteúdo após clique
else:
    # Música
    st.markdown("""
        <iframe width="0" height="0"
        src="https://www.youtube.com/embed/6d5SS0gS5bM?autoplay=1&loop=1&playlist=6d5SS0gS5bM"
        frameborder="0"
        allow="autoplay">
        </iframe>
    """, unsafe_allow_html=True)

    # Título
    st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>💖 Para você meu bem 💖</h1>", unsafe_allow_html=True)

    # Mensagem
    st.markdown("""
    <div style='text-align: center; font-size:18px;'>
    Desde que você entrou na minha vida, tudo ficou mais bonito e alegre.<br>
    Você é a minha pessoa favorita no mundo inteiro ❤️
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Contador
    data_inicio = datetime(2025, 10, 10)
    dias = (datetime.now() - data_inicio).days

    if dias >= 0:
        texto = f"Estamos juntos há {dias} dias 💕"
    else:
        texto = f"Faltam {abs(dias)} dias para o nosso começo 💖"

    st.markdown(f"<h3 style='text-align:center;'>{texto}</h3>", unsafe_allow_html=True)

    st.write("")

    # Título da barra
    st.markdown("""
    <h3 style='text-align:center;'>
        Nível de amor por você 💖
    </h3>
    """, unsafe_allow_html=True)

    # Barra de corações
    nivel = 10  # pode mudar se quiser 😏

    coracoes = "❤️" * nivel
    vazios = "🤍" * (10 - nivel)

    st.markdown(f"""
    <div style='text-align:center; font-size:28px;'>
    {coracoes}{vazios}
    </div>
    """, unsafe_allow_html=True)

    # Rodapé
    st.markdown("""
    <hr>
    <div style='text-align:center;'>
    Feito com ❤️ só para você
    </div>
    """, unsafe_allow_html=True)
