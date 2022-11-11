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
	- Útil para smartphones, portáteis, tablets ...
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
- É necessário definir o *viewport* no *header* do HTML:

:::{.center style="width: 70%;"}
```{.html style="font-size: 24px;"}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
:::

- Através de definição de estilos:
	- uso de dimensões percentuais dos elementos (*e.g.*, width: 50%);
	- uso de *media queries* para mudar arranjo dos elementos;
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

```{.html .numberLines style="font-size: 18px;"}
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

```{.css style="font-size: 22px;"}
@media [tipo_de_media] and ([media_feature]){
	/*código CSS*/;
}
```

- Outra forma de uso (no *head* do HTML):

```{.html style="font-size: 22px;"}
<link rel="stylesheet" media="[tipo_de_media] and ([media_feature])" href="meuCSS.css">
```

- *Media queries* são definidas por *media features* que retornam verdadeiro ou falso.
	- Se a *media features* é verdadeira no contexto, então o CSS especificado é aplicado.
- `tipo_de_media` é opcional e tipo `all` é usado por omissão.

# Definir CSS Responsivo: Exemplos de Media Query (I)

- O exemplo a seguir altera a cor da fonte de um h1 para vermelho se o tipo da media for `Screen`.

```{.css style="font-size: 22px;"}
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

```{.css style="font-size: 22px;"}
@media (min-width: 900px){
	h1 {
		color: red;
	}
}
```

# Definir CSS Responsivo: Features Media Query

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

- Podem ser usados os operadores lógicos:
	- `and`
	- `or`
	- `not`

- Exemplo que aplica o CSS para os seguintes casos:
	- orientação em paisagem (*landscape*) ou
	- a largura do viewport estiver valor mínimo de 900px e valor máximo de 1200px (*i.e.*, entre 900px e 1200px). 

```{.css style="font-size: 22px;"}
@media (orientation: 'landscape') or (min-width: 900px) and (max-width: 1200px) {
	h1 {
		color: red;
	}
}
```
# Definir CSS Responsivo: Mais Exemplos com Media Query

- Incluir exemplo de tamanho de janela
- Incluir exemplo de tamanho de imagem?

# Bootstrap{.part}

# Bootstrap

- *Framework* mais popular para criar *websites* **responsivos**.
- Versões: 3, 4, 5.
- Versão 5:
	- Mais atual (*release* de 2021).
- Tutorial no W3Schools: https://www.w3schools.com/bootstrap5/index.php
- Exemplo de uso do bootstrap:
	- https://www.w3schools.com/bootstrap5/tryit.asp?filename=trybs_default&stacked=h

# Instalação

- Incluir ao menos dois ficheiros:
	- O CSS do Bootstrap: para aplicar os estilos pré-definidos;
	- O Javascript do Bootstrap: para efeitos visuais de alguns elementos.
- Incluir no head da página HTML (uso de CDN):

```{.html}
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
```

# 

# Exercício

1. Verifique se sua página de login/registo já desenvolvida é responsiva.
1. Inclua o bootstrap nestas páginas e altere-as se conforme for necessário.
