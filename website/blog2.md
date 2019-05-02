## Blog 2

### An end-to-end trainable neural task oriented dialogue system that can perform tasks in multiple domains [paper](https://arxiv.org/pdf/1604.04562.pdf)

#### Pro: 
- Able to understand how context and memory can be used to make an assistant like product.
- How to work with complex models in NLP.
- Integrate multiple models together that can be trained end-to-end.
- Can be made into a product by the end of class.
- Data is open source for a particular task (restaurants) [data](https://www.repository.cam.ac.uk/handle/1810/260970).

#### Cons:
- Hard to implement even with available code.
- Since the idea uses multiple models together, it is difficult to find all the pretrained submodels (word embeddings, paragram …).
- Difficult to evaluate each submodule of the overall model and their respective performances (how to train each one of them).
- Requires a convoluted human evaluation scheme to evaluate the model performance.

### A context aware neural dialogue system that can have long conversations [paper1](https://arxiv.org/pdf/1608.07076.pdf) [paper2](https://aclweb.org/anthology/W18-5020)

#### Pro:
- Relatively easier to implement than our first idea.
- Focuses on the same issue of using context and memory to make an dialogue system.
- Data is open-source.

#### Cons:
- Hard to evaluate each submodule of the overall model and their respective performances (how to train each one of them).
- Requires a convoluted human evaluation scheme to evaluate the model performance.
- Difficult to come up with various metrics to judge the performance of the model.

### Implement transformers in a machine translation task [paper](https://arxiv.org/pdf/1706.03762.pdf) 

#### Pro:
- Data is readily available and performance evaluation is straightforward.
- Easy to establish various baselines by substituting in and out various encoders/decoders.
- Model could be interacted with making for an interesting presentation (real-time translations from English).

#### Cons:
- Implementing a transformer could be difficult.
- Not exactly an entirely new topic to explore.
- May be difficult to beat or come close to the current best machine translation models.
- Requires substantial understanding of the two languages involved with the translation.

### Lecture: 
Transformers and evaluation metrics like BLEU score.
