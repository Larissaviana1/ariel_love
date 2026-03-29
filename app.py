import streamlit as st
from datetime import datetime
import time

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
    # 🎵 Música
    st.markdown("""
    <iframe width="0" height="0"
    src="https://www.youtube.com/embed/6d5SS0gS5bM?autoplay=1&loop=1&playlist=6d5SS0gS5bM"
    frameborder="0"
    allow="autoplay">
    </iframe>
    """, unsafe_allow_html=True)

    # 💖 Título
    st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>💖 Para você meu bem 💖</h1>", unsafe_allow_html=True)

    # 💌 Mensagem
    st.markdown("""
    <div style='text-align: center; font-size:18px;'>
    Desde que você entrou na minha vida, tudo ficou mais bonito e alegre.<br>
    Você é a minha pessoa favorita no mundo inteiro ❤️
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ⏳ Contador
    data_inicio = datetime(2025, 10, 10)
    dias = (datetime.now() - data_inicio).days

    if dias >= 0:
        texto = f"Estamos juntos há {dias} dias 💕"
    else:
        texto = f"Faltam {abs(dias)} dias para o nosso começo 💖"

    st.markdown(f"<h3 style='text-align:center;'>{texto}</h3>", unsafe_allow_html=True)

    st.write("")

    # 💖 Barra animada de amor
    st.markdown("<h3 style='text-align:center;'>Nível de amor por você 💖</h3>", unsafe_allow_html=True)

    nivel = 10
    placeholder = st.empty()

    for i in range(1, nivel + 1):
        coracoes = "❤️" * i
        vazios = "🤍" * (nivel - i)

        placeholder.markdown(f"""
        <div style='text-align:center; font-size:28px;'>
        {coracoes}{vazios}
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.3)

    # ⏱️ Espera 5 segundos antes da animação final
    time.sleep(5)

    # 💕 Corações subindo
    st.markdown("""
    <style>
    .heart {
        position: fixed;
        bottom: -50px;
        font-size: 24px;
        animation: floatUp 5s linear infinite;
        opacity: 0.8;
    }

    @keyframes floatUp {
        0% {
            transform: translateY(0) scale(1);
            opacity: 1;
        }
        100% {
            transform: translateY(-800px) scale(1.5);
            opacity: 0;
        }
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
    <div style='text-align:center;'>
    Feito com ❤️ só para você
    </div>
    """, unsafe_allow_html=True)
