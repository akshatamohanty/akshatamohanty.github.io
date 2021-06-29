---
page: Home
title: Homepage
layout: none
---

{% include head.html %}

<body>
  {% include navigation.html %}

  <main>
    <h1 style="text-align: center">Recent happenings,</h1>
    <br />
    <br />
    <ul>
      {% for post in site.posts limit: 4 %}
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
  </main>

  {% include footer.html %}
</body>