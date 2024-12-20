---
title: Math Sample
subtitle: Using KaTeX

image: pic02.jpg
noindex: true
draft: true
---

KaTeX can be used to generate complex math formulas server-side.

<div class="alert alert-success" role="alert">
  <strong>Well done!</strong> You successfully read this important alert message.
  $$
  \phi = \frac{(1+\sqrt{5})}{2} = 1.6180339887\cdots
  $$
</div>

How do we get inline math to work??  $\phi = \frac{(1+\sqrt{5})}{2} = 1.6180339887\cdots$  Does this show up?

Additional details can be found on [GitHub](https://github.com/Khan/KaTeX) or on the [Wiki](http://tiddlywiki.com/plugins/tiddlywiki/katex/).
<!--more-->

### Example 1

If the text between $$ contains newlines it will rendered in display mode:
```
$$
f(x) = \int_{-\infty}^\infty\hat f(\xi) \thinspace e^{2 \pi i \xi x} \thinspace d\xi
$$
```
$$
f(x) = \int_{-\infty}^\infty\hat f(\xi) \thinspace e^{2 \pi i \xi x} \thinspace d\xi
$$


### Example 2
```
$$
\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\cdots} } } }
$$
```
​​$$
\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\cdots} } } }
$$
​​

### Example 3
```
$$
1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for }\lvert q\rvert<1.
$$
```
$$
1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for }\lvert q\rvert<1.
$$
