# Blog 1

## Your team name
Baby Jarvis

## A list of the team's members
Divye Pratap Jain, Vardhman Mehta, Kevin Zhao

## The top three project ideas you’re excited about
- An end-to-end trainable neural task oriented dialogue system that can perform tasks in multiple domains [paper](https://arxiv.org/pdf/1604.04562.pdf)
- A context aware neural dialogue system that can have long conversations [paper](https://arxiv.org/pdf/1608.07076.pdf)
- Implement transformers in a machine translation task [paper](https://arxiv.org/pdf/1706.03762.pdf) 

## A minimal viable action plan with stretch goals for each project idea
### Action Plan 1: Task Oriented Dialogue System
- Determine the task orientation of the dialogue system
  - Start with Restaurant tasks as that is the one mentioned in the reference paper.
- Gather dialogue data surrounding the task
  - Use existing datasets made public by the paper and the Stanford task oriented dataset.
  - Understand the format of the data and parse it to feed the network.
- Project Scope
  - Start by adapting the public version of the model to our own implementation.
  - Adapt to more independent tasks. For example 
  - Have a more generic cross domain performance and see if we can leverage knowledge of one domain to do tasks in another
  - Evaluate the cross domain model using blue evaluation method and human evaluation (Ask our peers)
  - Stretch Goal: Add Active learning for other related domains, as the model should be able to leverage existing domains to learn new tasks quickly.

### Action Plan 2: Conversation Oriented Dialogue System
- Implement  the network and implement a baseline version as discussed in [paper](https://arxiv.org/pdf/1608.07076.pdf) 
- Project Scope
  - Replace RNNs with transformers and evaluate performance changes 
  - Stretch goal: Leverage BERT in combination with this paper to have a more robust and better dialogue system
  - Evaluate our dialogue system (Ask our peers)

### Action Plan 3:
- Determine a suitable language for the a machine translation model (from English)
- Data is available here for a number of English language pairs: [data](https://www.statmt.org/wmt18/translation-task.html)
- Brainstorm the general architecture of the translation model: perhaps taking influence from the model described in the following paper [paper](https://arxiv.org/pdf/1706.03762.pdf)
- Implement the machine translation model with various RNN’s and transformers (with various hyperparameter changes) to determine how each neural architecture performs
- Perhaps implement a user interface for people to test and interact with the best performing model (translation from English to another language)
- Stretch goal: Implement a generic architecture that works with multiple languages (inspired by [GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf))

## The github URL for your project
https://github.com/Divye02/baby-jarvis

## Other relevant links
- https://github.com/shawnwun/NNDIAL
- https://github.com/edward-zhu/dialog/
- https://github.com/MiuLab/TC-Bot
- https://nlp.stanford.edu/blog/a-new-multi-turn-multi-domain-task-oriented-dialogue-dataset/
