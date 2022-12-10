# Deploy de uma aplicacao utilizando o kubernetes
> Projeto pratico em modo de desafio com o deploy de uma API criada em Python em um cluster kubernetes desenvolvido como atividade avaliativa do Bootcamp Engenheiro de Dados da XPEducacao.

## Enunciado do desafio
Você é engenheiro de dados em uma empresa de dados que é referência no
mercado. A empresa está neste momento estudando a possibilidade de trocar
de provedor de nuvem. O diretor da área de dados já demonstrou sua
preocupação com o grande tempo necessário para a migração de todos os
workloads do time de dados para outro provedor de nuvem e designou você
para desenvolver uma POC em uma estrutura “portável” e agnóstica.  

Desse modo, você optou por demonstrar o uso do Kubernetes para soluções
de dados. Você vai implementar um processo de dados simples, encapsular
sua execução em uma imagem docker e implementar sua execução em k8s.  

Você está livre para escolher qual solução será implementada: uma API, um
processo Python com algum tratamento de dados, alguma consulta a um
banco de dados, como preferir. O importante é demonstrar a solução
funcionando no ambiente kubernetes.  

Por se tratar de uma POC e de um processo de dados muito simples, você está
livre para escolher trabalhar em um cluster em nuvem ou em um cluster local
utilizando kind.  

## Como instalar
```bash
# subindo os pods e services
$ make upapi

# desativando os pods e services
$ make downapi
```

## Requerimentos
- Cluster kubernetes em cloud ou local com minikube
