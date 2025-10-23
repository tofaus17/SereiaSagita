# SereiaSagita - Landing Page Mapa Astral

Este é um projeto de Landing Page desenvolvido em **Django** e **HTML/CSS** com foco em vendas de consultas de Mapa Astral. O design é místico e profissional, conforme solicitado.

## Requisitos

*   Python 3.x
*   Django (será instalado automaticamente com o `pip`)

## Configuração e Execução (Passo a Passo)

1.  **Instalar o Django:**
    Certifique-se de ter o Python instalado. Em seguida, instale o Django e o `pip` (se ainda não tiver):
    ```bash
    pip install django
    ```

2.  **Navegar para o Diretório do Projeto:**
    Descompacte o arquivo ZIP e navegue até o diretório principal `SereiaSagita/`:
    ```bash
    cd SereiaSagita
    ```

3.  **Executar o Servidor de Desenvolvimento:**
    Inicie o servidor local do Django.
    ```bash
    python3 manage.py runserver
    ```

4.  **Acessar a Landing Page:**
    Abra seu navegador e acesse o endereço:
    ```
    http://127.0.0.1:8000/
    ```

## Estrutura do Projeto

*   `SereiaSagita/`: Diretório principal do projeto Django.
    *   `settings.py`: Configurações do projeto (o app `landing_page` e o diretório de templates já estão configurados).
    *   `urls.py`: Roteamento principal (aponta a raiz `/` para a `landing_page`).
*   `landing_page/`: O aplicativo Django que contém a lógica da landing page.
    *   `views.py`: Contém a função `index` que renderiza o template.
    *   `urls.py`: Roteamento do app (define a URL raiz `''` para o `views.index`).
*   `templates/landing_page/`: Contém o arquivo `index.html` com o layout e conteúdo.
*   `static/landing_page/`: Contém os arquivos estáticos.
    *   `css/style.css`: O arquivo de estilo com o tema místico (roxo, dourado, estrelas).
    *   `img/background.jpg`: A imagem de fundo mística usada no topo da página.

## Detalhes da Configuração

*   **Terapeuta:** SereiaSagita (8 anos de experiência).
*   **Preço:** R$ 250,00 (parcelamento em até 10x).
*   **Link de Contato:** O botão de WhatsApp está configurado para o número **(21) 98744-7397**.
    *   *Link:* `https://api.whatsapp.com/send?phone=21987447397&text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20minha%20Leitura%20Completa%20do%20Mapa%20Astral%20com%20a%20SereiaSagita.`

Para alterar o número do WhatsApp, edite o arquivo `templates/landing_page/index.html` e substitua o número `21987447397` nos três locais onde ele aparece.
