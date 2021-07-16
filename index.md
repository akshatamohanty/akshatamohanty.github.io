---
page: Home
title: Homepage
layout: none
artwork:
  - bird
  - balloons
  - rainwalk
  - shading
  - flowers
---

{% include head.html %}

<body>
  {% include navigation.html %}

  <main style="text-align: center">
    <h1>Recent happenings,</h1>
    <br />
    <br />
    <ul>
      {% for post in site.posts limit: 3 %}
        <li>
          <center>
            {% if post.category == 'blog' %}
              {{ post.date | date: "%b'%y" }} | From the Blog
              <a href="{{post.url}}">
                <h2>{{ post.title }}</h2>
                {{ post.content | truncatewords:25 | strip_html }}
              </a>
            {% else %}
              <a href="{{post.link}}" style="display: block; width: 100%; margin: 40px 0; text-align: center;">
                <div>
                  {{ post.date | date: "%b'%y" }} | {{ post.type }}, {{ post.where }}
                  <h2 style="margin-bottom: 8px">{{ post.title }}</h2>
                </div>
                <div style="position:relative; height: 300px">
                  {{post.embed}}
                  {% if post.image %}
                    <img src="{{post.image}}" style="height: 100%; max-width: 100%;" />
                  {% endif %}
                </div>
              </a>
            {% endif %}
          </center>
          <br />
          <br />
        </li>
      {% endfor %}
    </ul>
    <br><br>
    <!-- art -->
    <section>
      <h1>From the gallery,</h1>
      <p>I paint with water colors. Here's some of my latest randomness.</p>
      <!-- gallery -->
      <div class='gallery'>
        {% for name in page.artwork %}
          {% include artwork.html %}
        {% endfor %}
      </div>
    </section>
  </main>

  {% include footer.html %}
</body>