---
published: false

group: blog1
title:  Using the Trello API
subtitle: Trello API to collect all cards and make a checklist
date:   2018-05-11
categories: snippet
type: snippet
tags: trello
---

```
// Get all of the information about the list from a public board
var success = function(successMsg) {
  //asyncOutput(successMsg);
  var books = [];
  for( var i=0; i < successMsg.length; i++){
     var card = successMsg[i];
     if (card.idLabels[0] == "<-->")
     {
        books.push(card.shortUrl);
        Trello.put('/cards/' + card.id + '/closed?value=true', success, error);
     }
  }
  asyncOutput(books);
};

var error = function(errorMsg) {
  asyncOutput(errorMsg);
};


var list_id = "<-->";
var label = "<-->";
Trello.get('/lists/' + list_id + '/cards', success, error);
```
