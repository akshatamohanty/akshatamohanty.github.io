---
title: "Applications of Topological Sorting."
description: "Topological sorting is a way to sort nodes in a graph with the number of connections they have in a particular direction. It is incredibly useful in visualization and this is how we used it."
date: 24-1-2018
layout: post
tags:
  - cs-basics
published: false
---

### Topological Sorting

```
		let rankedNodeOrder: number[] = [];
		let n_map = [];

		n_map = this._nodes.map(function(node, index){
			return {prevArr: [], nextArr: [], id: index};
		})

		for(let c=0; c < this._edges.length; c++){
			let edge: IEdge = this._edges[c];
			let out_nodeIndex = edge.output_address[0];
			let in_nodeIndex = edge.input_address[0];

			if(n_map[out_nodeIndex].nextArr.indexOf(in_nodeIndex) == -1){
				n_map[out_nodeIndex].nextArr.push(in_nodeIndex);
			}

			if(n_map[in_nodeIndex].prevArr.indexOf(out_nodeIndex) == -1){
				n_map[in_nodeIndex].prevArr.push(out_nodeIndex);
			}

		}

		/*let id_resolved: number[] = [];
		let sort_map = n_map.sort(function(a, b){
			return a.prevArr.length - b.prevArr.length;
		})*/

		let sortO = n_map[0].prevArr.concat([n_map[0].id]).concat(n_map[0].nextArr);
		for(let i=1; i < n_map.length; i++){
			let o = n_map[i];

			if(sortO.indexOf(o.id) == -1){
				sortO.push(o.id);
			}

			let el_pos = sortO.indexOf(o.id);

			if(o.prevArr.length == 0 && el_pos !== 0){
				sortO.splice(el_pos, 1);
				sortO.unshift(o.id);
			}

			o.prevArr.map(function(r){

				let index = sortO.indexOf(r);

				if(index == -1){
					sortO.splice(el_pos -1, 1,  r);
				}
				else{
					if(index > el_pos){
						sortO.splice(index, 1);
						sortO.splice(el_pos -1, 1, r);
					}
					else{
						// do nothing
					}
				}

			});

		}
```
