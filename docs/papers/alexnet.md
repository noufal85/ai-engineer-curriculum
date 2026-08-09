# AlexNet

**Paper:** *ImageNet Classification with Deep Convolutional Neural Networks* · Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton · 2012

## The paper in one sentence

A large convolutional neural network, trained efficiently on GPUs with several practical tricks, dramatically improved large-scale image classification.

## The problem

An image is a grid containing millions of numbers. A classifier must turn those pixels into a label such as `tiger`, `school bus`, or `coffee mug`, even when the object moves, changes size, or appears against a different background.

Earlier systems often depended on human-designed visual features. Researchers chose rules for detecting edges, textures, and shapes, then passed those features to a classifier. The question was whether a deep network could learn the useful features directly from enough labeled images.

## The core idea

AlexNet stacks **convolutional layers**. Early layers learn small local patterns such as edges. Later layers combine them into textures, parts, and object-level evidence.

```mermaid
flowchart LR
    A["Pixels"] --> B["Edges and colors"]
    B --> C["Textures and corners"]
    C --> D["Object parts"]
    D --> E["Class scores"]
    E --> F["Predicted label"]
```

The breakthrough was not one isolated invention. It was a combination that worked at scale: a deep CNN, a huge dataset, GPU training, ReLU activations, data augmentation, and dropout.

## How it works

### 1. Convolution searches for a pattern everywhere

A small learned filter slides across an image. The same filter is reused at every location, so an edge detector can recognize an edge near the top or bottom without learning two separate rules.

### 2. Layers build a hierarchy

One layer's output becomes the next layer's input. A later detector can combine several earlier patterns—for example, curves and texture—to recognize something more meaningful.

### 3. Pooling reduces detail

Max pooling keeps strong signals while shrinking the spatial grid. It reduces computation and makes small movements matter less, although some exact location information is lost.

### 4. ReLU keeps useful gradients flowing

The activation `max(0, x)` is simple: negative values become zero and positive values pass through. It was faster and easier to optimize than commonly used saturating activations of the time.

### 5. Regularization fights memorization

**Data augmentation** creates altered training views by cropping and reflecting images. **Dropout** randomly hides some activations during training so the network cannot depend too heavily on a single pathway.

### 6. GPUs make the experiment practical

Convolutions contain many repeated numeric operations. GPUs perform this kind of parallel work well. AlexNet split the model across two GPUs because of the hardware limits available at the time.

!!! note "One level deeper"
    The network had five convolutional layers followed by three fully connected layers and a 1,000-class softmax output. Its importance is less about copying that exact layout today and more about proving that learned hierarchical features, sufficient data, and accelerator compute could decisively outperform the previous approach.

## What changed after this paper

- Deep learning became the dominant direction in computer vision.
- GPUs became central tools for training neural networks.
- Learned representations displaced many hand-engineered vision pipelines.
- ImageNet performance became a major architecture benchmark.
- The practical recipe—data, compute, architecture, and regularization—became as important as any single algorithm.

## What the paper does not solve

- The model needs many labeled examples.
- It can learn dataset shortcuts rather than robust visual understanding.
- Classification gives one label; it does not automatically locate or describe every object.
- The model is expensive and large by the standards of its time.
- Better benchmark accuracy does not guarantee safe or fair behavior in a real application.

## Check your understanding

1. Why is reusing one convolutional filter across an image useful?
2. What kinds of patterns might early and late layers learn?
3. Why do data augmentation and dropout help?
4. Was AlexNet's success caused by one new idea or by a working combination?

## Read the original

- [Paper page and PDF](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)
- Recommended first pass: abstract → Figure 2 → Sections 3–4 → conclusion

[← Back to the paper catalog](index.md) · [Next: Generative Adversarial Networks →](generative-adversarial-networks.md)
