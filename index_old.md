---
page: Home
title: Homepage
layout: none
artwork:
  - warehouse
  - marina
  - fairytale
  - forest
---

{% include head.html %}

<body>
  {% include navigation.html %}

  <main style="text-align: center">
    <h1>Latest Posts</h1>
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
                <div>{{ post.content | truncatewords:20 | strip_html }}</div>
              </a>
            {% else %}
              <a href="{{post.link}}" target='_blank' rel='nofollow' style="display: block; width: 100%; margin: 40px 0; text-align: center;">
                <div>
                  {{ post.date | date: "%b'%y" }}
                  {% if post.category == 'public' %}
                    | {{ post.type }}, {{ post.where }}
                  {% endif %}
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
      <h1>Latest Captures</h1>
      <p>Follow me on <a href='https://www.instagram.com/iamaatoh/' target='_blank' rel='nofollow' style='color: blue; text-decoration: underline;'>Instagram</a>.</p>
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
