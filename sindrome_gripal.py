import requests
import json
import pandas as pd

# API DATASUS
url = "https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_search"

payload = json.dumps({
  "size": 10000
})
headers = {
  'Authorization': 'Basic dXNlci1wdWJsaWMtbm90aWZpY2Fjb2VzOlphNHFOWGR5UU5TYTlZYUE=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data_json = response.json()
sources = data_json['hits']['hits']

# Extraindo e salvando os dados DataSUS
sup = []
for source in sources:
   sup.append(source.get('_source'))

# Normalizando o json
sup_data = pd.json_normalize(sup)
print('source: ', sup_data)

# Salvando o arquivo em csv
sup_data.to_csv('datasus_pacientes.csv', index=False)
