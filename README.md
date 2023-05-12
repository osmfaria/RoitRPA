### Test Técnico - Engenheiro de RPA ###
Este projeto foi realizado com base state machines, utilizando REFramework

## 🎯 Objetivo:
Este projeto está dividido em 3 repositórios por questões de organização, dois deles contém workflows e o outro o app backend, as divisões foram baseadas nas seguintes tasks:

**1) Repositório atual, workflow utilizando template REF, atua como Dispatcher**
- Data scraping dos dados de CNAE do website do IBGE salvando em um arquivo de excel;
- Invocar python script para formatação de dados;
- Adicionar os dados formatados do excel em uma queue no orchestrator.

**2) Repositório do workflow utilizando template REF, atua como Performer [aqui](https://github.com/osmfaria/RoitRPAPerformer)**
- Buscar transaction items na queue do orchestrator;
- Enviar dados através de POST requests para a API.

**3) Repositório do backend | API [aqui](https://github.com/osmfaria/roit-api)** 
- Backend em python com um postgreSQL database para armazenar os dados do CNAE.

## 📑 State Machines
Nesta sessão serão descritos as principais tasks realizadas por cada state machine do REF deste repositório

**1. INITIALIZATION**
 - Inclui a execução das atividades de inicialização padrão do template de REFramework, sendo a principal delas a leitura do arquivo Config.xlsx, aqui foram setadas a pasta do orchestrator em que a queue se encontra assim como o nome da queue;
 - Criada variável no Config.xlsx para amazenar quais seções do CNAE devem ser lidas (valor inicial A, B e C);
 - Setado também o número máximo de tentativas caso ocorra uma excenption para 2;
 - Por fim foi criado um kill process para excel e chrome que são os aplicativos utilizados neste workflow.

**2. GET CNAE DATA**
 - Conjunto de loops trabalhando com data scraping e seletores dinâmicos para pecorrer a tabela com os dados CNAE e criar uma data table.

**3. PROCESS CNAE DATA**
- Invoca workflow para formatar dados do excel com um script em python;
- Invocar workflow para adicionar bulk Queue Items ao orchestrator.

**4. END PROCESS**
 - Fecha chome browser e excel.


## 📋 Guia de instalação
Para executar localmente este app, siga as intruções abaixo:

- Clone este repositório;
- Para executar localmente, certifique-se de ter o Python instalado em seu sistema;
- No arquivo Config.xlsx os seguintes campos devem ser preenchidos: 
    - SectionSelection (quais seções do CNAE devem ser percorridas, ex: A B C, devem estaR separados somente por espaço)
    - PythonLibraryPath (caminho para a pasta onde o arquivo python*.dll, na pasta onde o python está instalado)
    - PythonPath (caminho para a pasta onde o python está instalado)
    - WorkingFolder (caminha para a pasta principal do projeto)
    - OrchestratorQueueName (Criei uma Queue no orchestrator e indique aqui o nome)
    - OrchestratorQueueFolder (Indique qual pasta está sendo utilizada no orchestrator)


