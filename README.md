### Test Técnico - Engenheiro de RPA ###
Este projeto baseado em sate machines, utilizando REFramework

## 🎯 Objetivo:
Este projeto está dividido em 3 repositórios por questões de organização, dois deles contém workflows e o outro o app backend, as divisões foram baseadas nas seguintes tasks:

**1) Repositório atual, workflow utilizando template REF, atua como Dispatcher**
- Data scraping dos dados de CNAE de determinadas seções salvando em um arquivo de excel
- Invocar python script para formatação de dados
- Adicionar os dados formatados do excel em queues no orchestrator 

**2) Repositório do workflow utilizando template REF, atua como Performer [aqui](https://github.com/osmfaria/RoitRPAPerformer)**
- Buscar transaction items na queue do orchestrator
- Enviar dados através de POST requests para a API

**3) Repositório do backend [aqui](https://github.com/osmfaria/roit-api)** 
- Backend em python com um postgreSQL database para armazenar os dados do CNAE

## 📑 State Machines

1. **Initialization**
 - Inclui a execução das atividades de inicialização padrão do template de REFramework, sendo a principal delas a leitura do arquivo Config.xlsx, aqui foram setadas a pasta do orchestrator em que a queue se encontra assim como o nome da queue.
 - Criada variável no Config.xlsx para amazenar quais seções do CNAE devem ser lidas (valor inicial A, B e C)
 - Setado também o número máximo de tentativas caso ocorra uma excenption para 2.
 - Por fim foi criado um kill process para excel e chrome que são os aplicativos utilizados neste workflow.

2. **GET TRANSACTION DATA**
 - Conjunto de loops trabalhando com data scraping e seletores dinâmicos para pecorrer a tabela com os dados CNAE.

3. **PROCESS TRANSACTION**
 + *Process* - Process trasaction and invoke other workflows related to the process being automated 
 + ./Framework/*SetTransactionStatus* - Updates the status of the processed transaction (Orchestrator transactions by default): Success, Business Rule Exception or System Exception

4. **END PROCESS**
 + ./Framework/*CloseAllApplications* - Logs out and closes applications used throughout the process


### For New Project ###

1. Check the Config.xlsx file and add/customize any required fields and values
2. Implement InitiAllApplications.xaml and CloseAllApplicatoins.xaml workflows, linking them in the Config.xlsx fields
3. Implement GetTransactionData.xaml and SetTransactionStatus.xaml according to the transaction type being used (Orchestrator queues by default)
4. Implement Process.xaml workflow and invoke other workflows related to the process being automated
