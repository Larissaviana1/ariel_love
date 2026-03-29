import time

st.markdown(""
<h3 style='text-align:center;'>
    Nível de amor por você 💖
</h3>
""", unsafe_allow_html=True)

nivel = 10  # total de corações
placeholder = st.empty()

for i in range(1, nivel + 1):
    coracoes = "❤️" * i
    vazios = "🤍" * (nivel - i)

    placeholder.markdown(f"""
    <div style='text-align:center; font-size:28px;'>
    {coracoes}{vazios}
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.3)  # velocidade da animação
