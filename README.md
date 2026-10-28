# Inventário de jogo — projeto em dupla

Programa de terminal que guarda os itens do seu jogo numa matriz
(`[item, quantidade, raridade]`). Cada pessoa da dupla programa **arquivos
diferentes**, e é isso que evita conflito no Git.

## 1. Quem faz o quê

| Quem | Arquivos | O que a função faz |
|---|---|---|
| **Aluno A** | `adicionar.py` e `remover.py` | acrescenta uma linha; apaga uma linha |
| **Aluno B** | `listar.py` e `editar.py` | mostra todas as linhas; troca a quantidade |

Em **trio**: A fica com `adicionar.py` e `remover.py`, B com `editar.py` e C com
`listar.py`.

O `main.py` já está pronto: **não edite o `main.py`**. Como ninguém mexe nele,
vocês nunca vão mexer no mesmo arquivo.

## 2. Antes de começar

**Quem cria o repositório (Aluno A):** no GitHub, clique em **Use this template**
e depois em **Create a new repository**. Marque **Private**: só a dupla vai ver.
Depois, em **Settings > Collaborators**, convide o colega, que aceita o convite.

**Em cada computador (uma vez):**

```
git clone <endereço do repositório da dupla>
cd <nome-do-repositório>
git config user.name "Seu Nome"
git config user.email "ID+SEU-USUARIO@users.noreply.github.com"
git config pull.rebase true
```

Configure só neste repositório (sem --global), porque o computador do
laboratório é de todo mundo.

O e-mail `noreply` é um endereço do próprio GitHub. Ele aparece em cada commit no
lugar do seu e-mail pessoal, que fica escondido. Se a sua conta tem a opção
**Keep my email address private** ligada, o endereço está em **Settings > Emails**.

**Primeiro commit (aquecimento):** escreva seu nome na linha `# Autor:` dos seus
arquivos e envie (passo 3).

## 3. Cada vez que for trabalhar

1. `git pull` — traz o que o colega já enviou
2. edite o **seu** arquivo
3. `git status` — confira o que mudou
4. `git add adicionar.py` — troque pelo nome do seu arquivo
5. `git commit -m "adicionar: guarda o item"`
6. `git pull` — de novo, **antes** de enviar
7. `git push` — envia para o GitHub

> **Pull antes de push.**

## 4. Se o push for rejeitado

Aparece algo como `! [rejected] main -> main (fetch first)`. Não é erro grave:
seu colega enviou antes. Rode `git pull` e depois `git push` de novo.

## 5. Testar o programa

Depois de um `git pull`, rode `python main.py`. Com todas as funções prontas
(as suas e as do colega), o menu funciona de ponta a ponta. Digite `0` para sair.

## 6. Checklist de entrega

- pelo menos **4 commits** (`git log --oneline`)
- **2 autores** diferentes no `git log`
- `python main.py` roda depois de um `git pull` final

## 7. No fim da aula

O computador do laboratório é compartilhado: saia da sua conta do GitHub (no
VS Code e no Gerenciador de Credenciais do Windows) antes de levantar.
