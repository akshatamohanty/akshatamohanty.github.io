---
title: "Choosing an API backend?"
description: Beginner's guide to the main concepts in GraphQL
date: 2021-04-08
layout: posts/default
tags:
  - fullstack-engineering
published: false
---

<why is graphql gaining popularity>
who created graphql?
During one of my night-time scavengings on the internet, I stumbled upon an article by Netflix on Microservices in GraphQL. It advocated the usage of this pattern as a way to develop services faster. Obviously, I was interested. Developing fast is the need of the hour. So I decided to take GraphQL for a spin.

Here's what I learned.

<which companies are using it>

<how much network bandwidth does it save>

<rest api primer>
what is the principal difference between rest and graphql?
We live in a world called the "internet". Actually, we live in a world with internet - but I guess the latter works too. So, what is the internet? It is a network of connected computers. Like modern-day walkie-talkie systems. We spend our days sitting infront of boxes that allow us to exchange information without moving an inch from our seats.

Usually, humans speak to exchange information. Every dialogue is a bid or answer to a request. The internet works the same way. Every network transaction is a conversation. Sometimes - we have one main guy - transacting with several other guys. That's your server. The other little guys making bids for information - they are the clients.

Now that we have agreed upon this need for transacting information - or communicating. We come to the common language. How do we know what information this other person has? And how do we ask for it? For example, when you go to the doctor and ask for a diagnosis - he will under what you want. Because that's his API. If you went to the carpenter, and asked for a "diagnosis" - chances are you'll get a bland look.

Servers on the internet are like the doctor. And the language they communicate in is called the API. The API is a set format - the agreed upon code - to get your answers.

So now that we know what an API is. This language can differ. Think of it as dialects. The purpose however is the same - to recover information from the server.

Most commmonly used these days is the REST Api patterns. Here's what it looks like

`{address}/{resource}/subresource`

It's like an address location, to fetch information about resources. The concept of resources is important here. The world is built upon data models. and then hosted on the internet.

So, if you want your own information from the internet,
you'll probably go:

`{facebook}/users/akshata`

and this will give you all your information - that you can now render somewhere, display somewhere.

People were fine with this paradigm for sometime. But things started to get a little messy after a while.

### why should they care? what is the problem?

For instance, notice that when i call the api above, i get all the information about the user akshata - even things I don't need. That's not good for two reasons:

- it's wasteful, it's consuming network resources, it's also transferring more data than required. we like to work with as little data as possible
- there could be trimmed down versions of the responses, but it would require platform development effort

what if now you needed an api, which required only akshata's name + her friends ... you'd now need to make two api calls - /akshata + /akshata/friends

but if you look at it - it's not necessary to be so strict if how we allow clients to retrieve information. the format doesn't need to be so stricts. since we already know the data models and relationships - can we make this more flexible? so as to allow the clients to decide how they want to fetch resources?

Hence, enter graphql which works on this paradigm

### what is the idea/solution?

who came up with it? when?
netflix and coursera had their own solutions

graphql emphasizes the paradigm of models. it has three fundamental concepts - the query, modifications and subscriptions. any request to a graphql server needs to specify one of these

### what does a frontend call look like?

this is what a graphql request looks like:

```

```

for our akshata + friends example, now we could do it this way, in a single network call:

```

```

### what is a graphql server

a server capable of handling graphql requests

#### what is a query?

a query is nothing but the equivalent of a GET request in REST terms

#### what is modifier?

anything that modifies the resources on the server

#### what is a subscription

a constant connection with the server

#### resolver

so that's all the request types. what about the other side. the connection between the server and the datasource. that's where the resolver comes in. the resolver is basically telling you to get a particular model.

this is what a resolver might look like:

```

```

### example api

you'll need a graphql schema that the server can interprt. the options for a graphql server are as below
apolo server can be replaced by anything else
prisma can be replaced by anything else.

### how to design a graphql schema api

### takeaway

it's easy, fast with a lot of support. the fixes validated concerns around network bandwidth and flexibility
however, since all resolvers are discrete - i wonder if it loses some benefits around querying databases - due to this discrete nature?
what are the drawbacks of graphql?
it might also explode without consolidation
caching
