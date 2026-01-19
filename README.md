<h1>📊 Data Intelligence: Dashboard Reclame Aqui</h1>
Este projeto é uma plataforma de Inteligência de Reputação que automatiza a coleta, o processamento e a visualização de indicadores de atendimento ao cliente extraídos do portal Reclame Aqui. Através de uma pipeline robusta, transformamos dados não estruturados da web em insights estratégicos para benchmarking competitivo. </br></br>

<h3>🚀 Tecnologias Utilizadas</h3>
- Interface: Streamlit (Dashboard Interativo)</br>
- Extração de Dados: Selenium WebDriver (Web Scraping)</br>
- Manipulação de Dados: Pandas</br>
- Visualização: Streamlit

<h3>🏗️ Arquitetura do Projeto</h3>
O sistema foi desenhado seguindo princípios de engenharia de dados para garantir a rastreabilidade e integridade da informação:</br></br>

1. <strong>Camada Bronze</strong>: O Selenium captura o conteúdo bruto das páginas e armazena em arquivos JSON.
2. <strong>Camada Silver</strong>: Dados limpos e normalizados são salvos em CSV, prontos para análise estatística.
3. <strong>Camada Gold</strong>: O Dashboard Streamlit consome a camada Silver para gerar rankings e relatórios de performance.

<h3>🛠️ Funcionalidades</h3>
- <strong>Análise Individual</strong>: Pesquisa detalhada de mais de 40 empresas do setor de varejo e tecnologia.</br>
- <strong>Leaderboard Geral</strong>: Ranking dinâmico comparando a performance das empresas já analisadas (Nota, Solução e Fidelidade).</br>
- <strong>Tratamento de Dados Inexistentes</strong>: Lógica inteligente para lidar com empresas "Sem Índice" ou com dados insuficientes, evitando alucinações estatísticas no dashboard.</br>
- <strong>Exportação de Dados</strong>: Funcionalidade de download dos relatórios processados em formato CSV.

<h3>📦 Como Executar</h3>
1. Clone o repositório:</br>
<strong>git clone https://github.com/RaulSMuniz/DataIntelligence-reclameaqui </strong></br></br>
2. Instale as dependências: </br>
<strong>pip install -r requirements.txt </strong> </br></br>
3. Execute o App: </br>
<strong>streamlit run app.py</strong></br></br>

<h3>📈 Roadmap / W.I.P (Work In Progress)</h3>
[ ] Análise de Sentimentos: Implementação de NLP para classificar o tom das reclamações.</br>
[ ] Topic Modeling: Agrupamento automático das principais causas de insatisfação dos clientes.</br>
[ ] Persistência em Nuvem: Integração com Google Sheets ou Banco de Dados para armazenamento de longo prazo.
