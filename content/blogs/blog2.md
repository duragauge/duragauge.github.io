---
title: "Magna"
description: "Lorem Etiam Nullam"
slug: "magna"
image: pic09.jpg
keywords: ""
categories:
    - ""
    - ""
date: 2017-10-31T22:26:09-05:00
draft: false
noindex: true
---
Shortcode Test


{{< highlight html >}}
<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
    {{ range .Pages }}
        {{ .Render "summary"}}
    {{ end }}
  </div>
</section>
{{< /highlight >}}

The `figure` shortcode allows you to add a caption.  Must use absolute address for image
{{< figure src="/img/pic08.jpg" title="Steve Francia is the caption" >}}

Normal Markdown syntax for images works too, but no captions.
![](/img/pic06.jpg)
