import streamlit as st
import pandas as pd
from scraper import capturar_dados_dashboard
from transform import transform_data

st.set_page_config(
    page_title="Análise do Reclame Aqui",
    page_icon="📊",
    layout="wide"
)

if "dados_coletados" not in st.session_state:
    st.session_state.dados_coletados = None

with st.sidebar:
    st.title("Menu Principal")
    aba_selecionada = st.radio(
        "Escolha a visualização:",
        ["🏠 Início", "🔍 Análise Individual de Empresas", "🏆 Leaderboard Geral", "Análise de Sentimentos (W.I.P)"]
    )
    st.markdown("---")
    

    empresas_validadas = {
        "Amazon": "amazon",
        "Mercado Livre": "mercado-livre",
        "Magazine Luiza Loja Online": "magazine-luiza-loja-online",
        "Casas Bahia Loja Online": "casas-bahia-loja-online",
        "Submarino": "submarino",
        "Shoptime": "shoptime",
        "Kabum": "kabum",
        "Shopee": "shopee",
        "AliExpress": "aliexpress",
        "Netshoes": "netshoes",
        "Dafiti": "dafiti",
        "Zattini": "zattini",
        "Centauro Loja Física": "centauro-loja-fisica",
        "Fast Shop": "fast-shop",
        "Havan Loja Física": "havan-loja-fisica",
        "Kalunga": "kalunga",
        "Mobly": "mobly",
        "MadeiraMadeira": "madeiramadeira",
        "Tok&Stok": "tokestok",
        "Leroy Merlin Loja Online": "leroy-merlin-loja-virtual",
        "Decathlon": "decathlon",
        "Pernambucanas": "pernambucanas",
        "Riachuelo Loja Online": "riachuelo-loja-online",
        "Renner": "lojas-renner",
        "C&A Loja Online": "cea-loja-online",
        "Hering Loja Online": "hering-loja-virtual",
        "Polishop": "polishop",
        "Electrolux": "electrolux",
        "Samsung": "samsung",
        "LG Loja Online": "lg-electronics-loja-online",
        "Dell": "dell-computadores",
        "Lenovo": "lenovo-tecnologia-brasil",
        "Positivo": "positivo-informatica",
        "Asus": "asus",
        "Nike Loja Online": "nike-loja-online",
        "Adidas": "adidas",
        "Pichau": "pichau-informatica",
        "Terabyte Shop": "terabyte-shop",
        "Grupo Multilaser": "multilaser-industrial",
        "Philips": "philips-audio-e-video1",
        "Amaro": "amaro",
        "Época Cosméticos": "epoca-cosmeticos-e-perfumaria",
        "Beleza na Web": "beleza-na-web",
        "Enjoei": "enjoei"
    }



if aba_selecionada == "🔍 Análise Individual de Empresas":
    empresa_display = st.selectbox(
         "Selecione a Empresa para Análise:",
        options=list(empresas_validadas.keys())
    )
    empresa_input = empresas_validadas[empresa_display]

    botao_analisar = st.button("🚀 Iniciar Análise", use_container_width=True)

    if st.session_state.dados_coletados:
        if st.button("🗑️ Limpar Resultados", use_container_width=True):
            st.session_state.dados_coletados = None
            st.rerun()

    if botao_analisar:
        if empresa_input:
            try:
                with st.status("Extraindo informações...", expanded=True) as status:
                    st.write("🕵️ Acessando Reclame Aqui...")
                    capturar_dados_dashboard(empresa_input)

                    st.write("🧹 Limpando dados...")
                    dados_limpos = transform_data(empresa_input)    
                    
                    status.update(label="Processamento Concluído!", state="complete", expanded=False)

                st.session_state.dados_coletados = dados_limpos
                st.rerun()
                
            except Exception as e:
                st.error(f"Erro na execução: {e}")
        else:
            st.warning("⚠️ Digite o nome da empresa na barra lateral.")

    if st.session_state.dados_coletados:
        d = st.session_state.dados_coletados

        st.header(f"📊 Relatório de Performance: {d['empresa'].upper()}")

        if d['nota_media'] == 0.0:
            st.warning("🚨 **Atenção:** Esta empresa possui dados insuficientes ou está 'Sem Índice' no Reclame Aqui. As métricas abaixo podem não representar a performance real.")

        st.markdown(f"🔗 **Fonte oficial:** [Acesse a página da {d['empresa'].title()} no Reclame Aqui](https://www.reclameaqui.com.br/empresa/{empresa_input}/)")
        
        col1, col2, col3 = st.columns(3)
        if d['nota_media'] == 0.0:
            col1.metric("Nota Geral", "N/A")
        else:
            col1.metric("Nota Geral", f"{d['nota_media']}/10")
        
        if int(d['total_reclamacoes']) > 0:
            col2.metric("Total de Queixas", int(d['total_reclamacoes']))
        else:
            col2.metric("Total de Queixas", "N/A")
        
  
        if d['indice_solucao'] == 0.0:
            col3.metric("Falta Resolver", "N/A", help="Dados de solução insuficientes para cálculo.")
        else:
            nao_resolvidas_pct = round(100 - d['indice_solucao'], 1)
            col3.metric("Falta Resolver", f"{nao_resolvidas_pct}%", delta="Pendentes", delta_color="inverse")

        st.divider()

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("Eficiência")
            
            dados = []
            if d['respondidas'] > 0:
                dados.append({"Etapa": "Respondidas", "Percentual": d['respondidas']})
            if d['indice_solucao'] > 0:
                dados.append({"Etapa": "Resolvidas", "Percentual": d['indice_solucao']})

            if dados:
                df_gap = pd.DataFrame(dados)
                st.bar_chart(data=df_gap, x="Etapa", y="Percentual", color="#29b5e8")
            else:
                st.info("ℹ️ Dados de eficiência não disponíveis para esta empresa.")

        with c2:
            st.subheader("Fidelização")

            confianca_data = pd.DataFrame({
                "Categoria": ["Voltaram a Comprar"],
                "Valor": [d['voltaram_comprar']]
            })
            
            if d['voltaram_comprar'] > 0:
                st.bar_chart(data=confianca_data, x="Categoria", y="Valor")
            
                if d['voltaram_comprar'] > 80:
                    st.success("✅ Alta Retenção: A empresa possui clientes leais.")
                elif d['voltaram_comprar'] > 50:
                    st.warning("⚠️ Retenção Moderada: Atenção ao pós-venda.")
                else:
                    st.error("🚨 Baixa Retenção: Risco crítico de perda de clientes.")
            else:
                st.info("ℹ️ **Informação não disponível:** Esta empresa ainda não possui dados suficientes no Reclame Aqui para calcular o índice de fidelização (Voltariam a Comprar).")
        st.divider()
        st.subheader("📑 Status Atual de Reclamações")
        
        progresso_resposta = d['respondidas'] / 100
        st.write(f"Taxa de resposta atual: **{d['respondidas']}%**")
        st.progress(progresso_resposta)
        st.write(f"Existem **{int(d['aguardando'])}** pessoas esperando uma resposta neste momento.")
        if d['tempo_resposta'] == 'O tempo médio de resposta é --.':
            st.info(f"⏱️ Essa empresa ainda não respondeu ninguém.")
        else:
            st.info(f"⏱️ **Tempo de Resposta:** \n\n {d['tempo_resposta']}")
        st.divider()
        
        st.subheader("📥 Exportar Resultados")

        df_export = pd.DataFrame([d])
        csv = df_export.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Baixar Dados em CSV",
            data=csv,
            file_name=f"analise_reclameaqui_{empresa_input}.csv",
            mime="text/csv",
        )

elif aba_selecionada == "🏆 Leaderboard Geral":
    st.header("🏆 Leaderboard de Performance")
    
    try:
        import glob
        arquivos = glob.glob("data/silver/*.csv")
        
        if arquivos:
            lista_df = [pd.read_csv(f) for f in arquivos]
            df_ranking = pd.concat(lista_df, ignore_index=True)
            
            df_ranking = df_ranking.sort_values('data_coleta', ascending=False).drop_duplicates('empresa')
            
            df_ranking = df_ranking.sort_values(by=['nota_media'], ascending=False)
            
            st.dataframe(
                df_ranking[['empresa', 'nota_media', 'indice_solucao', 'voltaram_comprar']],
                column_config={
                    "empresa": "Empresa Analisada",
                    "nota_media": "Nota RA (Geral)",
                    "indice_solucao": "Taxa de Solução (%)",
                    "voltaram_comprar": "Voltaram a Comprar (%)"
                },
                use_container_width=True,
                hide_index=True
            )
            st.info("🛠️ Por padrão, esse ranking é organizado baseado na Nota Média da empresa, em ordem decrescente. Você pode alterar a organização do dashboard entre Nota Média, Taxa de Solução e Voltaram a Comprar")
            st.info("💡 Este ranking é baseado nas empresas que você já analisou e salvou localmente.")
        else:
            st.warning("Nenhum dado encontrado. Analise algumas empresas primeiro!")
            
    except Exception as e:
        st.error(f"Erro ao carregar o ranking: {e}")
elif aba_selecionada == '🏠 Início':
    st.title("Data Intelligence: Reclame Aqui")
    
    st.markdown("""
    ### Bem-vindo ao motor de inteligência de reputação.
    Este projeto automatiza a coleta e análise de dados do portal Reclame Aqui, transformando informações brutas em insights acionáveis para análise de mercado e benchmarking competitivo.
    """)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🕵️ Automação\nExtração em tempo real via Selenium, simulando navegação humana para dados atualizados.")
    with col2:
        st.warning("### 🏗️ Arquitetura\nImplementação seguindo a metodologia Medallion (Bronze/Silver/Gold) para integridade de dados.")

    st.divider()

    with st.expander("🛠️ Como funciona por baixo do capô?"):
        st.write("""
        1. **Extração:** O Selenium acessa a URL oficial da empresa.
        2. **Transformação:** Os dados são limpos e normalizados.
        3. **Visualização:** O dashboard consome a camada 'Silver' para gerar os gráficos que você vê.
        """)

    st.markdown("---")
    st.caption("Desenvolvido por Raul Muniz | Foco em Análise e Engenharia de Dados")
elif aba_selecionada == "Análise de Sentimentos (W.I.P)":
    st.header("Inteligência Artificial: Análise de Sentimentos")
    st.warning("🚧 Esta funcionalidade está atualmente em desenvolvimento (Work In Progress).")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### O que é?
        Além de extrair números, o objetivo desta funcionalidade é utilizar modelos de **Processamento de Linguagem Natural (NLP)** para analisar o conteúdo textual das reclamações.
        
        ### Próximos Passos:
        * **Classificação Automática:** Identificar se o tom do cliente é de frustração, ironia ou apenas informativo.
        * **Extração de Tópicos:** Agrupar automaticamente as causas (ex: "atraso na entrega", "produto defeituoso").
        * **WordClouds Dinâmicas:** Gerar nuvens de palavras baseadas nas queixas mais recentes da empresa.
        """)
    
        
    st.divider()
    st.info("💡 A ideia é ler as últimas 50 reclamações e gerar um resumo executivo sobre a 'dor' atual do cliente dessa empresa.")