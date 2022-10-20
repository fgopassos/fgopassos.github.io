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

- Texto pode ser redimensionado de acordo com as

# Bootstrap{.part}

# Bootstrap

- *Framework* mais popular para criar *websites* **responsivos**.

# Versões do Bootstrap

- Versão 3 
- Versão 4
- Versão 5
	- Mais atual (2022).

# Instalação



# Exercício

1. Criar uma página HTML simples de registo.
	- Campos: e-mail, nome do utilizador e palavra-passe.
	- Botão para cancelar e outro para enviar (ainda sem ação associada).
2. Criar uma página HTML simples de login.
	- Campos: e-mail e palavra-passe.
	- Checkbox "Lembrar-me" (ainda sem ação associada).
	- Botão para cancelar e outro para enviar (ainda sem ação associada).
3. Criar um ficheiro de estilo para cada página (um para cada ou apenas um para os dois).
4. Crie uma página Web em HTML simples para conversação via texto (chat).
