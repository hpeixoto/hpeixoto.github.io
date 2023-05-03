---
layout: post
title: Introdução ao Elastic Stack - Operações CRUD
image: /img/elastic.png
tags: elastic | stack | elasticsearch | kibana
---


### CREATE

#### Criar Documentos e Indices

Irá ser usado um demo de inspeções a restaurantes na cidade de S. Francisco.

Para criar um indice pode ser executado:

~~~javascript
POST /inspections/_doc
{
  "business_address": "660 Sacramento St",
  "business_city": "San Francisco",
  "business_id": "2228",
  "business_latitude": "37.793698",
  "business_location": {
    "type": "Point",
    "coordinates": [
      -122.403984,
      37.793698
    ]
  },
  "business_longitude": "-122.403984",
  "business_name": "Tokyo Express",
  "business_postal_code": "94111",
  "business_state": "CA",
  "inspection_date": "2016-02-04T00:00:00.000",
  "inspection_id": "2228_20160204",
  "inspection_type": "Routine",
  "inspection_score":96,
  "risk_category": "Low Risk",
  "violation_description": "Unclean nonfood contact surfaces",
  "violation_id": "2228_20160204_103142"
}
~~~

Este documento JSON tem geopoints, datas e números.

Para verificar a criação do índice podemos procurar:

~~~javascript
GET /inspections/_search
~~~

Estes primeiros passos demonstram bem a capacidade do elasticsearch em utilizar a API REST para executar as operações base. Neste caso foi utilizado o POST para a criação do documento.
Poderá ser também executada a criação recorrendo ao método PUT.

~~~javascript
PUT /inspections/_doc
{
  "business_address": "660 Sacramento St",
  "business_city": "San Francisco",
  "business_id": "2228",
  "business_latitude": "37.793698",
  "business_location": {
    "type": "Point",
    "coordinates": [
      -122.403984,
      37.793698
    ]
  },
  "business_longitude": "-122.403984",
  "business_name": "Tokyo Express",
  "business_postal_code": "94111",
  "business_state": "CA",
  "inspection_date": "2016-02-04T00:00:00.000",
  "inspection_id": "2228_20160204",
  "inspection_type": "Routine",
  "inspection_score":96,
  "risk_category": "Low Risk",
  "violation_description": "Unclean nonfood contact surfaces",
  "violation_id": "2228_20160204_103142"
}
~~~

!Esta operação devolve um erro! Isto porque ao contrário do POST que cria o ID do documento automaticamente, no método PUT é necessário indicar um id do documento.

POST cria o id do documento por nós:

~~~javascript
POST /inspections/_doc
{
  "business_address": "660 Sacramento St",
  "business_city": "San Francisco",
  "business_id": "2228",
  "business_latitude": "37.793698",
  "business_location": {
    "type": "Point",
    "coordinates": [
      -122.403984,
      37.793698
    ]
  },
  "business_longitude": "-122.403984",
  "business_name": "Tokyo Express",
  "business_postal_code": "94111",
  "business_state": "CA",
  "inspection_date": "2016-02-04T00:00:00.000",
  "inspection_id": "2228_20160204",
  "inspection_type": "Routine",
  "inspection_score":96,
  "risk_category": "Low Risk",
  "violation_description": "Unclean nonfood contact surfaces",
  "violation_id": "2228_20160204_103142"
}
~~~

Também é possivel criar um novo com o método PUT:

~~~javascript
PUT /inspections/_doc/12345
{
  "business_address": "660 Sacramento St",
  "business_city": "San Francisco",
  "business_id": "2228",
  "business_latitude": "37.793698",
  "business_location": {
    "type": "Point",
    "coordinates": [
      -122.403984,
      37.793698
    ]
  },
  "business_longitude": "-122.403984",
  "business_name": "Tokyo Express",
  "business_postal_code": "94111",
  "business_state": "CA",
  "inspection_date": "2016-02-04T00:00:00.000",
  "inspection_id": "2228_20160204",
  "inspection_type": "Routine",
  "inspection_score":96,
  "risk_category": "Low Risk",
  "violation_description": "Unclean nonfood contact surfaces",
  "violation_id": "2228_20160204_103142"
}
~~~

Ao indexar os documentos anteriores é automaticamente criado o indice: **_inspections_**

Em vez de criar um indice dinâmico podemos criar um índice previamente:

~~~javascript
DELETE /inspections

PUT /inspections
{
  "settings": {
    "index.number_of_shards": 1,
    "index.number_of_replicas": 0
  }
}
~~~

Não é aconselhavel usar estas configurações em produção!!

#### Importação em bulk

~~~javascript
POST /inspections/_bulk
{ "index": { "_id": 1 }}
{"business_address":"315 California St","business_city":"San Francisco","business_id":"24936","business_latitude":"37.793199","business_location":{"type":"Point","coordinates":[-122.400152,37.793199]},"business_longitude":"-122.400152","business_name":"San Francisco Soup Company","business_postal_code":"94104","business_state":"CA","inspection_date":"2016-06-09T00:00:00.000","inspection_id":"24936_20160609","inspection_score":77,"inspection_type":"Routine - Unscheduled","risk_category":"Low Risk","violation_description":"Improper food labeling or menu misrepresentation","violation_id":"24936_20160609_103141"}
{ "index": { "_id": 2 }}
{"business_address":"10 Mason St","business_city":"San Francisco","business_id":"60354","business_latitude":"37.783527","business_location":{"type":"Point","coordinates":[-122.409061,37.783527]},"business_longitude":"-122.409061","business_name":"Soup Unlimited","business_postal_code":"94102","business_state":"CA","inspection_date":"2016-11-23T00:00:00.000","inspection_id":"60354_20161123","inspection_type":"Routine", "inspection_score": 95}
{ "index": { "_id": 3 }}
{"business_address":"2872 24th St","business_city":"San Francisco","business_id":"1797","business_latitude":"37.752807","business_location":{"type":"Point","coordinates":[-122.409752,37.752807]},"business_longitude":"-122.409752","business_name":"TIO CHILOS GRILL","business_postal_code":"94110","business_state":"CA","inspection_date":"2016-07-05T00:00:00.000","inspection_id":"1797_20160705","inspection_score":90,"inspection_type":"Routine - Unscheduled","risk_category":"Low Risk","violation_description":"Unclean nonfood contact surfaces","violation_id":"1797_20160705_103142"}
{ "index": { "_id": 4 }}
{"business_address":"1661 Tennessee St Suite 3B","business_city":"San Francisco Whard Restaurant","business_id":"66198","business_latitude":"37.75072","business_location":{"type":"Point","coordinates":[-122.388478,37.75072]},"business_longitude":"-122.388478","business_name":"San Francisco Restaurant","business_postal_code":"94107","business_state":"CA","inspection_date":"2016-05-27T00:00:00.000","inspection_id":"66198_20160527","inspection_type":"Routine","inspection_score":56 }
{ "index": { "_id": 5 }}
{"business_address":"2162 24th Ave","business_city":"San Francisco","business_id":"5794","business_latitude":"37.747228","business_location":{"type":"Point","coordinates":[-122.481299,37.747228]},"business_longitude":"-122.481299","business_name":"Soup House","business_phone_number":"+14155752700","business_postal_code":"94116","business_state":"CA","inspection_date":"2016-09-07T00:00:00.000","inspection_id":"5794_20160907","inspection_score":96,"inspection_type":"Routine - Unscheduled","risk_category":"Low Risk","violation_description":"Unapproved or unmaintained equipment or utensils","violation_id":"5794_20160907_103144"}
{ "index": { "_id": 6 }}
{"business_address":"2162 24th Ave","business_city":"San Francisco","business_id":"5794","business_latitude":"37.747228","business_location":{"type":"Point","coordinates":[-122.481299,37.747228]},"business_longitude":"-122.481299","business_name":"Soup-or-Salad","business_phone_number":"+14155752700","business_postal_code":"94116","business_state":"CA","inspection_date":"2016-09-07T00:00:00.000","inspection_id":"5794_20160907","inspection_score":96,"inspection_type":"Routine - Unscheduled","risk_category":"Low Risk","violation_description":"Unapproved or unmaintained equipment or utensils","violation_id":"5794_20160907_103144"}
~~~

Verificar novamente a criação dos documentos:


### READ

~~~javascript
GET /inspections/_search
~~~


Pesquisar todos os documentos cujo **_business_name_** contém a palavra _soup_.

~~~javascript
GET /inspections/_search
{
  "query": {
    "match": {
      "business_name": "soup"
    }
  }
}
~~~

Pesquisar todos os documentos cujo **_business_name_** contém a cidade _san francisco_. Dado que são duas palavras temos de usar o _match_phrase_.

~~~javascript
GET /inspections/_search
{
  "query": {
    "match_phrase": {
      "business_name": "san francisco"
    }
  }
}
~~~

Na pesquisa de texto os resultados são rankeados. Isto é, é atribuido um valor ao match encontrado e os resultados devolvidos são ordenados por esse valor:

~~~javascript
GET /inspections/_search
{
  "query": {
    "match": {
      "business_name": "soup"
    }
  }
}
~~~

**Nota:** [!mais informação - relevance!](https://www.elastic.co/guide/en/elasticsearch/guide/current/relevance-intro.html)


Existe também a possibilidade de executar a combinação booleana de pesquisas. Vamos procurar todos os documentos que contêm a palavra **soup** e **san francisco** no _business name_:

~~~javascript
GET /inspections/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "business_name": "soup"
          }
        },
        {
          "match_phrase": {
            "business_name": "san francisco"
          }
        }
      ]
    }
  }
}
~~~

Ou podemos encontrar documentos que não possuam a palavra _soup_ no nome:

~~~javascript
GET /inspections/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "match": {
            "business_name": "soup"
          }
        }
      ]
    }
  }
}
~~~

É possível fazer alterar o peso atribuido à pesquisa. Por exemplo podemos atribuir um peso superior à pesquisa _soup_ :

~~~javascript
GET /inspections/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match_phrase": {
            "business_name": {
              "query": "soup",
              "boost" : 3
            }
          }
        },
        {
          "match_phrase": {
            "business_name": {
              "query": "san francisco"
            }
          }
        }
      ]
    }
  }
}
~~~


Pode por vezes ser dificil perceber o que está a ser pesquisado. Aqui está um exemplo que pode ser utilizado para integração direta no frontend com enfatização da palavra pesquisada:

~~~javascript
GET /inspections/_search
{
  "query" : {
    "match": {
      "business_name": "soup"
    }
  },
  "highlight": {
    "fields": {
      "business_name": {}
    }
  }
}
~~~

Pode ser também executada a pesquisa por filtros, quando não queremos pesquisa por texto. Por exemplo a pesquisa pelos valores da inspeção:

~~~javascript
GET /inspections/_search
{
  "query": {
      "range": {
        "inspection_score": {
          "gte": 80
        }
      }
  },
  "sort": [
    { "inspection_score" : "desc" }
  ]
}
~~~

Neste caso está ordenado pelo inspection score.

**Nota:** [!mais informação - pesquisa estruturada!](https://www.elastic.co/guide/en/elasticsearch/guide/current/structured-search.html)

Exemplo de utilização de query SQL no elastic:

~~~javascript
POST /_xpack/sql?format=txt
{
    "query": "SELECT business_name, inspection_score FROM inspections ORDER BY inspection_score DESC LIMIT 5"
}
~~~

**Agregações:**

Pesquisar documentos que possuam a palavra soup, mas de seguida queremos contabilizar quais deles estão entre 0-80 , 81-90, 91-100 na classificação da inspeção:

~~~javascript
GET /inspections/_search
{
  "query": {
    "match": {
      "business_name": "soup"
    }
  }
 ,"aggregations" : {
    "inspection_score" : {
      "range" : {
        "field" : "inspection_score",
        "ranges" : [
          {
            "key" : "0-80",
            "from" : 0,
            "to" : 80
          },
          {
            "key" : "81-90",
            "from" : 81,
            "to" : 90
          },
          {
            "key" : "91-100",
            "from" : 91,
            "to" : 100
          }
        ]
      }
    }
  }
}
~~~

Outro potencial de utilização é a geo localização. Vamos tentar encontrar restaurantes perto de nós.

Primeiro vamos encontrar todos os restaurantes:

~~~javascript
GET /inspections/_search
~~~

~~~javascript
GET /inspections/_search
{
  "query": {
    "match": { "business_name": "soup"}
  },
  "sort": [
    {
      "_geo_distance": {
        "coordinates": {
          "lat":  37.783527,
          "lon": -122.409061
        },
        "order":         "asc",
        "unit":          "km"
      }
    }
    ]
}

// Output:
// Error! Elasticsearch doesn't know the field is a geopoint
// We must define this field as a geo point using mappings
// Mapping are helpful for defining the structure of our document, and more efficiently storing/searching the data within our index
// We have numbers/dates/strings, and geopoints, let's see what elasticsearch thinks our mapping is

~~~

Verificar os tipos dos objetos que foram definidos:

~~~javascript
GET /inspections/_mapping/
~~~

Vamos alterar os mapeamentos executados de forma automática! Para isso precisamos de eliminar o indice e criar novamente, efetuando o mapeamento correto!

~~~javascript
DELETE inspections

PUT /inspections

PUT inspections/_mapping/
{
      "properties": {
          "business_address": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_city": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_latitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "coordinates": {
              "type": "geo_point"
          },
          "business_longitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_phone_number": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_postal_code": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_state": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "inspection_date": {
            "type": "date"
          },
          "inspection_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "inspection_score": {
            "type": "long"
          },
          "inspection_type": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "risk_category": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "violation_description": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "violation_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          }
        }
}
~~~


Agora podemos importar novamente os documentos e executar novamente a pesquisa:

~~~javascript
GET /inspections/_search
{
  "query": {
    "match": { "business_name": "soup"}
  },
  "sort": [
    {
      "_geo_distance": {
        "coordinates": {
          "lat":  37.783527,
          "lon": -122.409061
        },
        "order":         "asc",
        "unit":          "km",
        "distance_type": "plane"
      }
    }
    ]
}
~~~

### UPDATE

Vamos adicionar uma flag ao documento com o _id_ = 5:

~~~javascript
GET /inspections/_search

POST /inspections/_update/5
{
   "doc" : {
      "flagged" : true,
      "views": 0
   }
}
~~~

Para verificar a alteração podemos procurar o documento:

~~~javascript
GET /inspections/_doc/5
~~~

### DELETE

Para remover um documento podemos utilizar o método **DELETE**.

DELETE /inspections/_doc/5

# That completed the CRUD section

## Analyzers
# Tokenization parte as frases em tokens

~~~javascript
GET /inspections/_analyze
{
  "tokenizer": "standard",
  "text": "my email address test123@company.com"
}

GET /inspections/_analyze
{
  "tokenizer": "whitespace",
  "text": "my email address test123@company.com"
}

GET /inspections/_analyze
{
  "tokenizer": "standard",
  "text": "Brown fox brown dog"
}
~~~

É possível aplicar filtros para manipular os tokens:

~~~javascript
GET /inspections/_analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase"],
  "text": "Brown fox brown dog"
}

GET /inspections/_analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase", "unique"],
  "text": "Brown brown brown fox brown dog"
}
~~~

[Mais informação - TOKENS](https://www.elastic.co/guide/en/elasticsearch/guide/current/_controlling_analysis.html)