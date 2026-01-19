<h1>📊 Data Intelligence: Reclame Aqui</h1>
Este projeto é uma plataforma de Inteligência de Reputação que automatiza a coleta, o processamento e a visualização de indicadores de atendimento ao cliente extraídos do portal Reclame Aqui. Através de uma pipeline robusta, transformamos dados não estruturados da web em insights estratégicos para benchmarking competitivo. </br>

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

<h3>Features:</h3>
<h5>Menu Inicial:</h5><p>Overview sobre as funcionalidades deste projeto.</p>
<img width="1434" height="698" alt="image" src="https://github.com/user-attachments/assets/4cf877e0-d1e9-4ab8-8810-199d115637fa" />
<h5>Análise Individual de Empresas:</h5><p>Menu de seleção múltipla para escolher qual empresa será analisada. Contém KPIs importantes e insights gerais sobre a empresa.</p>

![Data-Intelligence-Análise-Individual](https://github.com/user-attachments/assets/e64376ad-9820-4b41-8071-11ad927492ba)

<h5>Leaderboard Geral:</h5><p>Contém um leaderboard organizado das empresas que já foram analisadas. Nativamente já vem com algumas empresas analisadas na data 19/01/2026, e conforme mais empresas são analisadas, mais empresas são adicionadas ao leaderboard.</p>
<img width="1434" height="645" alt="image" src="https://github.com/user-attachments/assets/8e66ade3-b43f-4c34-ab08-2edcd7f42f89" />

<h5>Análise de Sentimentos (W.I.P):</h5><p>O objetivo é realizar a classificação automática de empresas baseadas em CloudWords, utilizando NLP (Processamento de Linguagem Natural)</p>
<img width="1425" height="647" alt="image" src="https://github.com/user-attachments/assets/bc5107f8-2904-4a95-a81d-ece3196b4221" />




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
