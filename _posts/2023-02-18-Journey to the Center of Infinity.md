---
layout: distill
title: Journey to the Center of Infinity
description: So... are we there yet?
tags: Mathematics Physics
giscus_comments: true
date: 2023-02-17
img:
bibliography: 2023-02-18-Journey_to_the_Center_of_Infinity.bib

authors:
  - name: Roberto A. Gambarini
    affiliations:
      name: Imperial College London

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: What is Information?
  - name: The Intuitionists against the Formalists

# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }

---

## It is way Bigger than you Think

Think of the biggest number possible. Let me give you some help. A googolplex is the largest named number that is equal to 10 raised to the power of a googol ($$ \text{googol} = 10^{100} $$) <d-cite key="kasner2001mathematics"></d-cite>. To put it into perspective, there are around $$ 10^{80} $$ atoms in the known <d-cite key="universe davies1978tailor"></d-cite>. 

$$ \text{googolplex} = 10^{\text{googol}} $$

Then there is Graham's number, which was derived by Ronald Graham in the late 1970s . Graham's number is connected to a problem in [Ramsey theory](https://en.wikipedia.org/wiki/Ramsey_theory), which is an area in mathematics that deals with [combinatorial](https://en.wikipedia.org/wiki/Combinatorics) objects <d-cite key="graham1991ramsey"></d-cite>. The problem deals with finding the nodes in an [n-dimensional hypercube](https://en.wikipedia.org/wiki/Hypercube). Graham's number is the upper bound of this problem <d-cite key="griess1973schur"></d-cite>. This number is so extremely large that it can't even be written exactly <d-cite key="graham1989concrete"></d-cite>. 

Problem

You might be thinking that this doesn't make much sense, but in the same way that one would instinctively know that an adult has to be taller than a baby, we can also intuitively define that this upper bound is much bigger than any other quantity. So large in fact, that there is no physical analogy that I can give you. If we were to pixelate the entire universe in the [smallest possible size](https://en.wikipedia.org/wiki/Planck_units) allowed in quantum physics, that would still only give us a mere $$ 10^{184} $$ <d-cite key="ade2016planck"></d-cite>. Which is only slightly bigger than a googolplex, and minuscule compared to Graham's number.

Let's take Graham's number and see how much bigger we can go. We could simply have Graham's number to the power of itself, but lets just use an even more powerful tool. The [hyperoperators](https://en.wikipedia.org/wiki/Hyperoperation). The Knuth arrow notation ($$ \uparrow $$)  might not be a symbol you are used to, but it can be used to represent a nested exponentiation in a concise manner <d-cite key="knuth1984mathematics"></d-cite>.

* The single arrow ($$ \uparrow $$) represents exponentiation:

$$ 2 \uparrow 4 = 2\times(2\times(2\times 2)) = 2^4 = 16 $$

* Two arrows, one right after another, ($$ \uparrow \uparrow $$)  represents tetration:

$$ 2 \uparrow\uparrow 4 =  2 \uparrow (2 \uparrow (2 \uparrow 2))= 2^{2^{2^{2}}} = 2^{16} = 65,536 $$

* Three arrows ($$ \uparrow\uparrow\uparrow $$) represents pentation. As much as I want to give you the final answer of this example... it's just ridiculously big:
 
$$ 2 \uparrow\uparrow\uparrow 4 = 2 \uparrow\uparrow (2 \uparrow\uparrow (2 \uparrow\uparrow 2 )) = 2 \uparrow\uparrow 65,536 $$

Although these hyperoperations can be powered up even further using the [conway chained arrow notation](https://en.wikipedia.org/wiki/Conway_chained_arrow_notation), this should suffice for now. Now let's try applying this tool to the already ridiculously big Graham's number. Consider using it as a base for the pentation and itself for the pentation exponent. And just for kicks, lets just take the factorial of this:

$$ (G \uparrow \uparrow \uparrow G)! = \text{An impossibly large number}  $$

Even after defining an already impossibly large number and using an operator that skyrockets it to a power of itself, this is still microscopic when compared to infinity. Graham's number goes beyond a number that would be possible in this universe, so it is quite a challenge to comprehend the vastness of infinity. Yet we use infinity constantly in mathematics. Its use dates back to the 4th century BC with Euclid's fundamental work in geometry and is also the basis in the development of Calculus by Newton and Leibniz around 350 years ago <d-cite key="dunham1991journey"></d-cite>. Infinity's abstract and unmeasurable essence defines many fundamental tools in mathematics, but its purely conceptual nature sparked a loud debate. This became the *casus belli* for a war that endangered the very nature of mathematics <d-cite key="kleiner2007history"></d-cite>.

***

## The Intuitionists against the Formalists

What later became known as the "Foundational Crisis of Mathematics" (personally a bit much), was a conflict between formalists and intuitionists that lasted from the late 19th century to the mid-20th century. On one side of the ring you had the "formalists", who believed that infinity was just a symbol, a tool used to make calculations easier. And at the other end were the "intuitionists" who believed that infinity was a real entity, that it existed in a Platonic sense. There were several factors that sparked this debate, such as the discovery of applications for Non-Euclidian geometry and a search for better defined mathematical limits, but the biggest instigator was German mathematician Georg Cantor. 

***

 <d-cite key=""></d-cite>

## Citations

Citations are then used in the article body with the `<d-cite>` tag.
The key attribute is a reference to the id provided in the bibliography.
The key attribute can take multiple ids, separated by commas.

The citation is presented inline like this: <d-cite key="gregor2015draw"></d-cite> (a number that displays more information on hover).
If you have an appendix, a bibliography is automatically created and populated in it.

Distill chose a numerical inline citation style to improve readability of citation dense articles and because many of the benefits of longer citations are obviated by displaying more information on hover.
However, we consider it good style to mention author last names if you discuss something at length and it fits into the flow well — the authors are human and it’s nice for them to have the community associate them with their work.

***

## Footnotes

Just wrap the text you would like to show up in a footnote in a `<d-footnote>` tag.
The number of the footnote will be automatically generated.<d-footnote>This will become a hoverable footnote.</d-footnote>

***

## Code Blocks

Syntax highlighting is provided within `<d-code>` tags.
An example of inline code snippets: `<d-code language="html">let x = 10;</d-code>`.
For larger blocks of code, add a `block` attribute:

<d-code block language="javascript">
  var x = 25;
  function(x) {
    return x * x;
  }
</d-code>

**Note:** `<d-code>` blocks do not look good in the dark mode.
You can always use the default code-highlight using the `highlight` liquid tag:

{% highlight javascript %}
var x = 25;
function(x) {
  return x * x;
}
{% endhighlight %}

***

## Interactive Plots

You can add interative plots using plotly + iframes :framed_picture:

<div class="l-page">
  <iframe src="{{ '/assets/plotly/demo.html' | relative_url }}" frameborder='0' scrolling='no' height="500px" width="100%" style="border: 1px dashed grey;"></iframe>
</div>

The plot must be generated separately and saved into an HTML file.
To generate the plot that you see above, you can use the following code snippet:

{% highlight python %}
import pandas as pd
import plotly.express as px
df = pd.read_csv(
  'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv'
)
fig = px.density_mapbox(
  df,
  lat='Latitude',
  lon='Longitude',
  z='Magnitude',
  radius=10,
  center=dict(lat=0, lon=180),
  zoom=0,
  mapbox_style="stamen-terrain",
)
fig.show()
fig.write_html('assets/plotly/demo.html')
{% endhighlight %}

***

## Layouts

The main text column is referred to as the body.
It is the assumed layout of any direct descendants of the `d-article` element.

<div class="fake-img l-body">
  <p>.l-body</p>
</div>

For images you want to display a little larger, try `.l-page`:

<div class="fake-img l-page">
  <p>.l-page</p>
</div>

All of these have an outset variant if you want to poke out from the body text a little bit.
For instance:

<div class="fake-img l-body-outset">
  <p>.l-body-outset</p>
</div>

<div class="fake-img l-page-outset">
  <p>.l-page-outset</p>
</div>

Occasionally you’ll want to use the full browser width.
For this, use `.l-screen`.
You can also inset the element a little from the edge of the browser by using the inset variant.

<div class="fake-img l-screen">
  <p>.l-screen</p>
</div>
<div class="fake-img l-screen-inset">
  <p>.l-screen-inset</p>
</div>

The final layout is for marginalia, asides, and footnotes.
It does not interrupt the normal flow of `.l-body` sized text except on mobile screen sizes.

<div class="fake-img l-gutter">
  <p>.l-gutter</p>
</div>

***

## Other Typography?

Emphasis, aka italics, with *asterisks* (`*asterisks*`) or _underscores_ (`_underscores_`).

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links.
http://www.example.com or <http://www.example.com> and sometimes
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

Here's our logo (hover to see the title text):

Inline-style:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style:
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

Inline `code` has `back-ticks around` it.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.


Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
