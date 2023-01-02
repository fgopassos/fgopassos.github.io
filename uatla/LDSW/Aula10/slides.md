---
author: Fernanda Passos
subtitle: GSC - Programação de Sistemas Web
title: Web Design Responsivo e Bootstrap
institute: Atlântica - Instituto Universitário
logo: ../atlantica_logo2.svg
---

# Web Design Responsivo{.part}


# Reponsividade

:::::{.columns}
::::{.column style="width:50%;"}
- Aquilo que se adapta ao tamanho da janela e ecrã.
	- Através de simplesmente **aumentar** ou **encolher** elementos;
	- Ou **mudar arranjo** dos elementos conforme o tamanho da janela/ecrã.
- Adapta o tamanho dos elementos ao tamanho do ecrã do dispositivo.
	- Especialmente útil para smartphones, portáteis, tablets ...
::::
::::{.column width=50%}
:::::::{.center}
![](imagens/web-design-responsive.png){#wdr width="70%"}
:::::::
::::
:::::

# Web Design Responsivo

- Explora recursos de leiaute flexível.
	1. Grelhas baseadas em proporções fluídas;
	2. Imagens e textos flexíveis;
	3. *Media queries* do CSS3: regras `@media`.
 

# HTML é responsivo?

- Sim!
- É importante definir o *viewport* no *header* do HTML:

:::{.center style="width: 70%;"}
```{.html style="font-size: 80%;"}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
:::

- Responsividade é implementada através de definição de estilos:
	- uso de dimensões percentuais dos elementos (*e.g.*, width: 50%);
	- uso de *media queries* para mudar estilo e arranjo dos elementos;
	- imagens redimensionáveis;
	- textos redimensionáveis;
	- ...

# HTML Responsivo

:::::{.columns}
::::{.column width=50%}
- Alguns modos:
	- Definir **diretamente no CSS**.
	- Uso de *frameworks*: CSS definido por terceiros.
		- Deve-se conhecer os nomes das classes e seus estilos.
		- Alguns usam Javascript além do CSS (para animações).
		- *e.g.*, Bootstrap, W3.CSS (apenas HTML e CSS).
::::
::::{.column width=50%}
:::{.center}
![](imagens/Bootstrap_logo.png){width="35%"}
:::
:::{.center}
![](imagens/w3css.png){width="35%"}
:::
::::
:::::

# Definir CSS Responsivo: Imagens

- Propriedade `width` definida em percentual (*e.g.*, 100%).
	- Largura da imagem varia de acordo com a largura da janela.
	- Pode aumentar a largura para valor maior que a largura original da imagem.
- Propriedade `max-width` definida em percentual (*e.g.*, 100%).
	- Largura da imagem varia de acordo com a largura da janela.
	- Mas a imagem aumenta até o seu tamanho máximo.
- Veja exemplo do w3schools:
	- https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_image_maxwidth

# Definir CSS Responsivo: Texto

- Texto pode ser redimensionado de acordo com as dimensões da janela.
	- Uso da propriedade `vw`.
	- Significa *viewport width*.
	- 1vw = 1% da largura do *viewport*.
		- Se o *viewport* tem 600px de largura, então 1vw é 6px.
		- Se o *viewport* tem 1920px de largura, então 1vw é 19,2px.

```{.html .numberLines style="font-size: 70%;"}
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1 style="font-size:10vw;">Título Responsivo</h1>
        <p style="font-size:5vw;">Texto responsivo: redimensione a janela para ver.</p>
        <p>Este texto terá um tamanho fixo.</p>
    </body>
</html>
```

:::{.center}
<button onclick="window.open('iframes/exemplo01.html','_blank')">Ir para exemplo</button>
:::

# Definir CSS Responsivo: Media Query

- Recurso de estilo (CSS) para manter página web adequada para uma media.
- Dá suporte a diversos **tipos de media** diferentes:
	- `All`: Para todos os dispositivos.
	- `Screen`: Para monitores ou dispositivos com ecrãs coloridos e alta resolução.
	- `Print`: Para impressão em papel.
	- `Braille`: Para dispositivos táteis.
	- `Projection`: Para apresentações como PPS.
	- `Tv`: Para dispositivos como televisores, ou seja, com baixa resolução, quantidade de cores e scroll limitados.
- Atualmente, uso mais comum é para web responsiva.
	- Isto é, adaptar página automaticamente para ecrãs de tamanhos diferentes.

# Definir CSS Responsivo: Sintaxe do Media Query

- Sintaxe dentro do CSS:

```{.css style="font-size: 75%;"}
@media [tipo_de_media] and ([media_feature]){
	/*código CSS*/;
}
```

- Outra forma de uso (no *head* do HTML):

```{.html style="font-size: 75%;"}
<link rel="stylesheet" media="[tipo_de_media] and ([media_feature])" href="meuCSS.css">
```

- *Media queries* são definidas por *media features* que retornam verdadeiro ou falso.
	- Se a *media features* é verdadeira no contexto, então o CSS especificado é aplicado.
- `tipo_de_media` é opcional e tipo `all` é usado por omissão.

# Definir CSS Responsivo: Exemplos de Media Query (I)

- O exemplo a seguir altera a cor da fonte de um h1 para vermelho se o tipo da media for `Screen`.

```{.css style="font-size: 80%;"}
@media Screen {
	h1 {
		font-color: red;
	}
}
```

# Definir CSS Responsivo: Exemplos de Media Query (II)

- O exemplo a seguir altera a cor da fonte de um h1 para vermelho para qualquer tipo de media que tem a largura mínima do *viewport* de 900px.
	- Aplica estilo sempre que largura  mínima for 900px.
	- Em outras palavras, aplica estilo para larguras maiores ou iguais a 900px.

```{.css style="font-size: 80%;"}
@media (min-width: 900px){
	h1 {
		color: red;
	}
}
```

# Definir CSS Responsivo: Algumas *Features Media Query*

::::{.center style="font-size: 60%; width: 95%; line-height: 90%;"}
Feature | Descrição | Valores | Exemplo |
--------|-----------|---------|---------|
`width` | largura exata do *viewport* | Numéricos, geralmente em px | `width: 900px`
`max-width` | largura máxima do *viewport* | Numéricos, geralmente em px | `max-width: 600px`
`min-width` | largura mínima do *viewport* | Numéricos, geralmente em px | `min-width: 900px`
`height` | largura exata do *viewport* | Numéricos, geralmente em px | `height: 400px`
`max-height` | altura máxima do *viewport* | Numéricos, geralmente em px | `max-height: 400px`
`min-height` | altura mínima do *viewport* | Numéricos, geralmente em px | `min-height: 900px`
`orientation` | orientação do *viewport*  | `portrait` ou `landscape` | `orientation: landscape`
`resolution` | densidade do pixel exata do dispositivo | Numéricos, geralmente em dpi | `resolution: 150dpi`
`max-resolution` | densidade do pixel máxima do dispositivo | Numéricos, geralmente em dpi | `max-resolution: 150dpi`
`min-resolution` | densidade do pixel mínima do dispositivo | Numéricos, geralmente em dpi | `min-resolution: 150dpi`
::::

# Definir CSS Responsivo: Operadores Lógicos Media Query

- Os seguintes operadores lógicos podem ser usados na construção do *media query*:
	- `and`
	- `or`
	- `not`

- Exemplo que aplica o CSS para os seguintes casos:
	- se a orientação está em paisagem (*landscape*) ou
	- se a largura do viewport tiver valor mínimo de 900px e valor máximo de 1200px (*i.e.*, entre 900px e 1200px). 

```{.css style="font-size: 75%;"}
@media (orientation: 'landscape') or (min-width: 900px) and (max-width: 1200px) {
	h1 {
		color: red;
	}
}
```

# Definir CSS Responsivo: Operador *only*

- Objetivo de esconder *media queries* de navegadores antigos.
- Uso comum: '`only Screen`'.

```{.css style="font-size: 80%;"}
@media only Screen and (min-width: 900px){
	h1 {
		color: red;
	}
}
```

# *Mobile First Design*

- Sempre fazer o *design* da página para o telemóvel primeiro.
	- Prioridade para ecrãs menores.
- O estilo principal é para telemóvel e modificações são feitas para ecrãs maiores (desktops, portáteis, ...).

```{.css style="font-size: 75%;"}
/* Geral: para telemóveis: */
[class*="col-"] {
  width: 100%;
}

@media only Screen and (min-width: 768px) {
  /* Para desktops e portáteis: */
  .col-3 {width: 25%;}
  .col-6 {width: 50%;}
  .col-9 {width: 75%;}
  .col-12 {width: 100%;}
}
}
```

# Definir CSS Responsivo: Exemplo

```{.css .numberLines style="font-size: 70%;"}
/* Para telemóveis: */
[class*="col-"] { /* Todas as classes que começam com 'col-' */
  width: 100%;
  float: left;
}

@media only Screen and (min-width: 600px) {
  /* Para desktops/portáveis: */
  .col-1 {width: 8.33%;}
  .col-2 {width: 16.66%;}
  .col-3 {width: 25%;}
  .col-4 {width: 33.33%;}
  .col-5 {width: 41.66%;}
  .col-6 {width: 50%;}
  .col-7 {width: 58.33%;}
  .col-8 {width: 66.66%;}
  .col-9 {width: 75%;}
  .col-10 {width: 83.33%;}
  .col-11 {width: 91.66%;}
  .col-12 {width: 100%;}
}
```

:::{.center}
<button onclick="window.open('iframes/exemploWDR.html','_blank')">Ir para página HTML</button>
<button onclick="window.open('iframes/styles.css','_blank')">Ir para CSS</button>
:::

# Bootstrap{.part}

# Bootstrap

- *Framework* mais popular para criar *websites* **responsivos**.
- Versões: 3, 4, 5.
- Versão 5:
	- Mais atual (*release* de 2021).
- Documentação: 
	- Oficial: https://getbootstrap.com/docs/5.0
	- Tutorial no W3Schools: https://www.w3schools.com/bootstrap5/index.php
- Exemplo de uso do bootstrap:
	- https://www.w3schools.com/bootstrap5/tryit.asp?filename=trybs_default&stacked=h

# Instalação

- Incluir ao menos dois ficheiros:
	- O CSS do Bootstrap: para aplicar os estilos pré-definidos;
	- O Javascript do Bootstrap: para efeitos visuais de alguns elementos.
- Incluir no head da página HTML (uso de CDN):

```{.html style="font-size: 80%;"}
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
```

# Classes do Bootstrap

- A ideia do Bootstrap é disponibilizar classes com estilos previamente definidos.
- As classes são muitas vezes usadas com as *tags* **div** e **span**.
- Existem vários tipos:
	- Contêineres;
	- Grelha básica;
	- Tipografia: títulos de texto;
	- Tabelas com estilos específicos;
	- Imagens;
	- Botões;
	- Menus de navegação;
	- Modais: imita uma janela sobre a página;
	- Mensagens de alerta; 
	- ...

# Bootstrap: Breakpoints

- São larguras customizadas que determinam laiaute da página.
	- Usam *media queries* e *mobile first responsive design*.
	- Representados por prefixos utilizados com outros elementos.

:::{.center style="font-size: 70%; line-height: 80%;"}
| Breakpoint        | Prefixo da classe | Dimensões |
|-------------------|-------------|------------|
| X-Small           | Não há      | <576px     |
| Small             | `sm`          | ≥576px     |
| Medium            | `md`          | ≥768px     |
| Large             | `lg`          | ≥992px     |
| Extra large       | `xl`          | ≥1200px    |
| Extra extra large | `xxl`         | ≥1400px    |
:::

# Bootstrap: Contêineres (I)

- Blocos base de conteúdo do Bootstrap.
	- São necessários para usar o sistema de grelhas.
- Três tipos:
	- `.container`: aplica uma margem no *breakpoint* (exceto para x-small).
	- `.container-fluid`: ocupa 100% (`width=100%`) do ecrã, para todos os *breakpoints*.
	- `.container-{breakpoint}`: ocupa 100% (`width=100%`) até a dimensão do *breakpoint*.
		- `{breakpoint}` é substituído por `sm|md|lg|xl|xxl`.

# Bootstrap: Contêineres (II)

:::{.center style="font-size: 70%; line-height: 130%;"}
|                  | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | X-Large ≥1200px | XX-Large ≥1400px |
|------------------|--------------------|--------------|---------------|--------------|-----------------|------------------|
| .container       | 100%               | 540px        | 720px         | 960px        | 1140px          | 1320px           |
| .container-sm    | 100%               | 540px        | 720px         | 960px        | 1140px          | 1320px           |
| .container-md    | 100%               | 100%         | 720px         | 960px        | 1140px          | 1320px           |
| .container-lg    | 100%               | 100%         | 100%          | 960px        | 1140px          | 1320px           |
| .container-xl    | 100%               | 100%         | 100%          | 100%         | 1140px          | 1320px           |
| .container-xxl   | 100%               | 100%         | 100%          | 100%         | 100%            | 1320px           |
| .container-fluid | 100%               | 100%         | 100%          | 100%         | 100%            | 100%             |
:::

# Exercício (I)

1. Crie uma página com Bootstrap com 4 linhas.
	- Linha 1: Título e imagem circulada (ver documentação do BS5).
	- Linha 2: Usar um nav.
	- Linha 3: parte do conteúdo em 4 colunas iguais.
	- Linha 4: rodapé com 3 colunas: contatos, copyrights e ícones de parceiros.
	- Consulte em: https://getbootstrap.com/docs/5.0/layout/grid/

# Exercício (II)

1. Verifique se sua página de login/registo já desenvolvida é responsiva.
1. Inclua o bootstrap nestas páginas e altere-as conforme for necessário.
