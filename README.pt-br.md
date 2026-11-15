# Trakt to Letterboxd Exporter 🎬

Uma ferramenta simples e rápida para exportar o seu histórico de filmes assistidos e avaliações do [Trakt](https://trakt.tv/) para o [Letterboxd](https://letterboxd.com/).

*(Read in [English](README.md))*

---

## 🚀 Como usar (Passo a Passo)

Siga os passos abaixo para gerar a sua planilha de importação:

### 1. Baixe seus dados do Trakt
1. Acesse o site do [Trakt](https://trakt.tv/) e faça login na sua conta.
2. Vá até as configurações da sua conta e solicite/baixe a exportação dos seus dados pessoais.
3. Extraia o arquivo `.zip` baixado no seu computador.

### 2. Prepare os arquivos
1. Localize os arquivos extraídos chamados **`watched-movies.json`** e **`ratings-movies.json`**.
2. Copie e cole esses dois arquivos dentro da pasta **`in/`** deste projeto.

### 3. Execute o programa
Abra o terminal (ou prompt de comando) na pasta do projeto e execute o comando:

```bash
python main.py
```

### 4. Importe no Letterboxd
1. O programa vai gerar um arquivo pronto em **`out/movies.csv`**.
2. Acesse a sua conta no **Letterboxd** e vá em **Settings > Import & Export**.
3. Na seção de importação, selecione o arquivo gerado (`movies.csv`) e confirme.

---

## 📋 Requisitos
* **Python 3** instalado no seu computador (nenhuma biblioteca externa é necessária).

---

## ⚠️ Limitações Atuais
* Exporta datas de visualização e avaliações, **sem comentários/resenhas**.

---

## 🤝 Contribuindo
Encontrou algum problema ou tem sugestões de melhoria? Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.

## 📄 Licença
Este projeto está sob a licença [MIT](LICENSE).