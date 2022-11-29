---
page: The Lab
title: "My Experiments with Life and Truth"
description: "Personal learnings and un-categorizable random musings."
listing_type: "The Lab"
layout: none
---

<!DOCTYPE html>
<html>
  {% include head.html %}

  <body>
    {% include navigation.html %}
    <main style="margin-top: 52px;">
      <section class="hero is-medium is-link">
        <div class="hero-body">
          <h1 class="title is-1">
            {{ page.title | capitalize }}
          </h1>
          <p class="subtitle">
            {{ page.description }}
          </p>
        </div>
      </section>
      <section class="section is-medium">
        <ul class="columns is-multiline">
          {% assign categories_list = site.categories %}
          {% for post in site.categories["the-lab"]  %}
            <li class="column is-full">
                <div>
                    <div class="title is-3">{{post.title}}</div>
                    <div class="block">{{post.content | truncatewords:40 | strip_html}}</div>
                </div>
                <div class="block">
                    <a href="{{post.url}}" class="button is-small is-link">Read</a>
                </div>
            </li>
          {% endfor %}
          </ul>
      </section>
    </main>

  </body>

{% include footer.html %}

</html>
