---
layout: post
showcase: true
size: 4
group: works
marker: ai | certification
title:  udacity's ai nanodegree
summary: compilation of 7 ai/ml projects covering topics - search and planning, game playing agents, image recognition, natural language processing and voice user interfaces
role: Artificial Intelligence and Machine Learning
projecturl: https://github.com/akshatamohanty/udacity-ai-nanodegree
description: Udacity is a for-profit educational organization founded by Sebastian Thrun, David Stavens, and Mike Sokolsky offering massive open online courses (MOOCs). This specialization was offered by Udacity as six-month, 2-semester program, covering topics in Artificial Intelligence and Machine Learning, as well as a Specialization in either Computer Vision, Natural Language Processing or Voice User Interfaces. I completed the nanodegree by completing 7 required projects with a capstone project in Voice User Interfaces. This is a collection of all my work towards the degree.
date:   2018-06-02
categories: post
type: project
tags:
- search
- game-playing-agents
- deep-learning
- vui
---

# Artificial Intelligence Nanodegree

<br />
### Project 1: Sudoku Solver, using constraint propagation technique
This was an introductory project to build a Sudoku Solver using contraint propagation. Template code was provided with python functions that needed to be completed. Students were also expected to answer questions about Constraint Propogation. Find my Python solution [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-01-sudoku/solution.py) and my assignments [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-01-sudoku/README.md)

<br />

### Project 2: Game Playing Agent, using min-max and alpha-beta pruning strategies
This was the second project in the nanodegree and we were required to build an adverserial game playing agent for the game. To build the isolation agent - I explored combinations of various strategies such as min-max search, alpha beta pruning with iterative deeping and evaluated 5-6 heuristics to determine the best performing one for position evalution. Find my game [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/game_agent.py) and a report for my heuristic analysis [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/heuristic_analysis.pdf). I also summarized a research paper on Game Playing Agents and provide a report analyzing different heuristics for game board evaluation: [Research Review: Game Tree Searching by MinMax Approximation by Ron Rivest](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/research_review.pdf)

<br />

### Project 3: Optimal Airplane Routes, using search algorithms
The third project was to implement heuristic and non-heuristic planning searches for a airplane cargo problem. The algorithms I implemented were ([code])(https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/game_agent.py)
 - breadth first search
 - depth first search
 - A* star search
 - A* with level sum search
 - depth limited search
 - uniform cost search

The report analyzing the performance of the different search algorithms is here: [Heuristic Analysis](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/heuristic_analysis.pdf). I also wrote a report on historical developments in AI: [Research Review: Historical Developments in AI](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/research_review.pdf)

<br />

### Project 4: Sign Language Recognizer, using probabilistic models
I used **hidden Markov models** in this project, to output translations for videos with people communicating using the Amerial Sign Langugage. I explored different feature sets using this data, progressed to training models for each word using `hmm` and implemented and analyzed three different methods for model selection - cross validation folds, Bayesian Information Criterion and Discriminative Information Criterion. Finally, I put the feature set and models together to build an [ASL recognizer](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-04-recognizer/asl_recognizer.ipynb)

<br />
### Project 5: Dog Breed Classifier, using Convolutional Neural Networks (CNNs)
This was the first project in the degree, using deep neural networks. I used a Convolutional Neural Networks using Keras, to create an image classfiier for dogs. I explored various concepts such as data augmentation, transfer learning, haarcascades, object detection and recognition to create a [model](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/game_agent.py) that  could predict if it was a human or a dog, and the resemblance of either, to a dog breed.

<br />
### Project 6a: Stockprice Prediction, using RNNs for time series prediction
In this project, I used Apple Stock Prices as time series data and created a model to predict future prices. The constructed model was an RNN, built with Keras, using LSTM units of specified dimensions. Find my model [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-06-aind2-rnn/StockPricePrediction.ipynb)

<br />
### Project 6b: Text Generation, using RNNs
For this project, I created a set of functions to properly window a large input text corpus for certain given dimensions. Then, I constructed an RNN model in Keras, using LSTM cells, to perform multiclass classification. Using this model, I generated text by progressiving giving it a variety of input sequences, demostrated [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/game_agent.py)


<br />
### Capstone Project: Speech Recognition [Specialization: Voice User Interfaces]
This was the final capstone project for the nanodegree. The project was to build a deep neural network that functions as part of an end-to-end automatic speech recognition (ASR) pipeline! I experimented with five models using various layers and configurations such as RNNs (GRU, LSTM), Bidirectional RNNs, CNN + RNNs, RNN + Time Distributed Dense, Dropout, Batch Normalization, etc. I also evaluated and analyzed the performance of each of these models and suggested ways of improving the same. Find this project [here](https://github.com/akshatamohanty/udacity-ai-nanodegree/blob/master/project-02-isolation/game_agent.py).

<br />

### Certificate!!
My certificate lives [here](https://confirm.udacity.com/QEJPWSRW)!