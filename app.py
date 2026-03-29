import streamlit as st
from datetime import datetime

# Configuração
st.set_page_config(page_title="Para você ❤️", layout="centered")

# Fundo
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

# Estado da música
if "play_music" not in st.session_state:
    st.session_state.play_music = False

# Botão para ativar música
if not st.session_state.play_music:
    if st.button("💖 Clique aqui"):
        st.session_state.play_music = True
        st.rerun()

# Música (só toca depois do clique)
if st.session_state.play_music:
    st.markdown("""
        <iframe width="0" height="0"
        src="https://www.youtube.com/embed/6d5SS0gS5bM?autoplay=1&loop=1&playlist=6d5SS0gS5bM"
        frameborder="0"
        allow="autoplay">
        </iframe>
    """, unsafe_allow_html=True)

# Conteúdo
st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>💖 Para você meu bem 💖</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size:18px;'>
Desde que você entrou na minha vida, tudo ficou mais bonito e alegre 😊❤️.<br>
Você é a minha pessoa favorita no mundo inteiro ❤️
</div>
""", unsafe_allow_html=True)

# Contador
data_inicio = datetime(2025, 10, 14)
dias = (datetime.now() - data_inicio).days

st.markdown(f"<h3 style='text-align:center;'>Estamos juntos há {dias} dias 💕</h3>", unsafe_allow_html=True)

# Barra
st.markdown("### Nível de amor por você:")
st.progress(100)

# Rodapé
st.markdown("""
<hr>
<div style='text-align:center;'>
Feito com ❤️ só para você
</div>
""", unsafe_allow_html=True)
