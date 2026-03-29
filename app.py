import streamlit as st
from datetime import datetime
import time

# Configuração
st.set_page_config(page_title="Para você ❤️", layout="wide")

# 🎨 Estilo geral
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f0f0f;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

[data-testid="stToolbar"] {
    display: none;
}

/* Botão gigante */
div.stButton > button {
    width: 100%;
    background: linear-gradient(45deg, #ff4b6e, #ff758f);
    color: white;
    font-size: 32px;
    padding: 25px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    animation: pulse 1.5s infinite;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0px 0px 40px rgba(255, 75, 110, 0.9);
}

/* Animação botão */
@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 75, 110, 0.7); }
    70% { transform: scale(1.05); box-shadow: 0 0 0 30px rgba(255, 75, 110, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 75, 110, 0); }
}
</style>
""", unsafe_allow_html=True)

# Estado
if "started" not in st.session_state:
    st.session_state.started = False

# 🌑 Tela inicial
if not st.session_state.started:

    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<h1 style='text-align:center; color:white;'>💖</h1>", unsafe_allow_html=True)

        if st.button("💌 Abrir minha surpresa"):
            st.session_state.started = True
            st.rerun()

# 🌸 Conteúdo
else:
    # 🎵 Música (Baco)
    st.markdown("""
    <iframe width="0" height="0"
    src="https://www.youtube.com/embed/tiE3lsIa0Vc?autoplay=1&loop=1&playlist=tiE3lsIa0Vc"
    frameborder="0"
    allow="autoplay">
    </iframe>
    """, unsafe_allow_html=True)

    # 💖 Título
    st.markdown("<h1 style='text-align:center; color:#ff4b6e;'>💖 Para você meu bem 💖</h1>", unsafe_allow_html=True)

    # 💌 Mensagem
    st.markdown("""
    <div style='text-align:center; font-size:20px; color:white;'>
    Desde que você entrou na minha vida, tudo ficou mais bonito e alegre.<br>
    Você é a minha pessoa favorita no mundo inteiro ❤️
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ⏳ Contador
    data_inicio = datetime(2025, 10, 10)
    dias = (datetime.now() - data_inicio).days

    if dias >= 0:
        texto = f"Estamos juntas há {dias} dias 💕"
    else:
        texto = f"Faltam {abs(dias)} dias para o nosso começo 💖"

    st.markdown(f"<h3 style='text-align:center; color:white;'>{texto}</h3>", unsafe_allow_html=True)

    st.write("")

    # 💖 Barra animada
    st.markdown("<h3 style='text-align:center; color:white;'>Nível de amor por você 💖</h3>", unsafe_allow_html=True)

    nivel = 10
    placeholder = st.empty()

    for i in range(1, nivel + 1):
        coracoes = "❤️" * i
        vazios = "🤍" * (nivel - i)

        placeholder.markdown(f"""
        <div style='text-align:center; font-size:30px;'>
        {coracoes}{vazios}
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.3)

    # ⏱️ Espera
    time.sleep(5)

    # 💕 Corações subindo
    st.markdown("""
    <style>
    .heart {
        position: fixed;
        bottom: -50px;
        font-size: 26px;
        animation: floatUp 5s linear infinite;
        opacity: 0.9;
    }

    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-900px); opacity: 0; }
    }
    </style>

    <div>
        <div class="heart" style="left:10%;">❤️</div>
        <div class="heart" style="left:20%; animation-delay:1s;">💖</div>
        <div class="heart" style="left:30%; animation-delay:2s;">❤️</div>
        <div class="heart" style="left:40%; animation-delay:0.5s;">💗</div>
        <div class="heart" style="left:50%; animation-delay:1.5s;">❤️</div>
        <div class="heart" style="left:60%; animation-delay:2.5s;">💖</div>
        <div class="heart" style="left:70%; animation-delay:1s;">❤️</div>
        <div class="heart" style="left:80%; animation-delay:0.3s;">💗</div>
        <div class="heart" style="left:90%; animation-delay:2s;">❤️</div>
    </div>
    """, unsafe_allow_html=True)

    # Rodapé
    st.markdown("""
    <hr>
    <div style='text-align:center; color:white; font-size:20px;'>
    Feito com ❤️ só para você
    </div>
    """, unsafe_allow_html=True)
