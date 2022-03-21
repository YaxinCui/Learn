## 论文摘要阅读

### A Cross-Lingual Joint Aspect/Sentiment Model for Sentiment Analysis

摘要

- 跨语言联合实体/情感情感分析模型
- 情感资源很匮乏、所以要尝试跨语言
- 现有跨语言方法依赖机器翻译的质量
- 现有情感分析集中在文档级别中，在细粒度上缺乏依赖
- 为了解决这些问题，本文开发了一种新的跨语言联合体/情感（CLJAS）模型，利用从源语言学习到的知识在目标语言中进行特定于体的情感分析。
- 实验证明有效果

结论

- 作者提出了一直无监督跨语言实体/情感联合模型，进行情感分析
- CLJAS可以获取跨语言对齐词向量知识

### A Multi-Layer Network for Aspect-Based Cross-Lingual Sentiment Classification
摘要
- 用多层网络进行基于实体的跨语言情感分析
- 使用了attention
- 使用了POS信息
- 使用了形容词信息
- 在mBERT上做使用
- 效果还可以，我这边也应该做一个实验，看看效果怎么样


### An Adaptive Hybrid Framework for Cross-domain Aspect-based Sentiment Analysis
- 用自适应混合框架进行跨领域基于实体的情感分析
- 通过对抗获得领域不变性特征
- 通过半监督获得目标领域的标签，更好地得到领域不变性
- 使用自适应均值教师网络，抑制生成伪标签过程的噪声
- 效果很好

### Anchored Model Transfer and Soft Instance Transfer for Cross-Task Cross-Domain Learning: A Study Through Aspect-Level Sentiment Classification
- 用锚定模型迁移和软实体迁移，进行跨任务、跨领域学习，一个方面集情感分类研究
- 监督学习面临着缺乏数据的问题，迁移学习提供了一个有效方法去解决这些问题，使得跨领域、跨任务之间共享知识。
- 作者提出了AMT(Anchored Model Transfer)和Soft Instance Transfer(SIT)，能提供一个通用框架。
- 作者通过实验证明了模型有效性
- AMT允许通过锚定参数共享层从辅助任务中学习其他精细和相关信息
- SIT允许传输与ASC任务域相关的实例，以扩大ASC数据集
- ASC任务

### Aspect-Level Cross-lingual Sentiment Classification with Constrained SMT
- 基于SMT约束的实体级跨语言情感分类
- SMT：统计机器翻译
- 现有跨语言情感分类任务，大多都是基于文档的。
- 实体级跨语言有额外的困难，我们认为亚句子的自定单位，必须映射语言中。
- 作者提出基于限制级SMT方法，通过服务于子句单元的边界，来进行跨语言。
- 效果，提高了4-8%个点。


### Cross-Cultural Examination on Content Bias and Helpfulness of Online Reviews: Sentiment Balance at the Aspect Level for a Subjective Good
- 在线评论内容偏见和帮助性的跨文化检验：主观良好方面的情绪平衡
- 作者发现，不同文化背景的人对评价关注的点不同。西方人更关心服务，日本人更关心价格，西方人更关心物有所值。


### Cross-domain aspect extraction for sentiment analysis: A transductive learning approach
- 情绪分析的跨领域方面提取：一种跨领域学习方法
- 作者提出了CD—ALPHN（Cross-Domain Aspect Label Propagation through Heterogeneous Networks），跨域实体标签传播异构网络
- 作者通过labeled aspects, unlabeled aspects, and linguistic features等特征，构建了一张网络，把标签传播到无标签数据上。
- 效果很好。
- 通过异构网络提供不同领域之间特征空间的统一表示
- 通过跨领域迁移学习，使标签得到传播

### Cross-Domain End-To-End Aspect-Based Sentiment Analysis with Domain-Dependent Embeddings
- 基于领域相关嵌入的跨域端到端方面情感分析
- 在细粒度上，寻找领域不变性特征，实现领域自适应存在挑战
- 作者利用领域特征向量和多任务学习策略，来获取领域不变知识。
- 效果很好。
- 模型通过学习领域知识，共享非领域知识。

### Cross-Domain Review Generation for Aspect-Based Sentiment Analysis
- 情感分析中的跨领域评论生成
- 作者提出了一种新的do-main自适应范式，称为跨域评论生成（cross-domain review generation，CDRG）
- 能够在源域标签评论的基础上生成具有细粒度注释的目标域评论。
- 为了实现目的，分为两步。第一步是用mask抹去领域特征属性，第二部是使用预训练模型获得目标领域评论。
- 实现了SOTA。
- 具体任务为E2E-ABSA和AE任务。


### Cross-lingual Aspect-based Sentiment Analysis with Aspect Term Code-Switching
- 使用aspect term code-switching进行跨语言情感分析
- 为此，我们提出了一种无对齐标签投影方法，通过翻译系统获得目标语言的高质量伪标签数据，从而可以在目标语言中预先提供更准确的任务特定知识。
- 作者创建了一个方面代码转换机制，用代码转换的双语句子来增加训练数据。
- 实验效果很好，实验效果与我做的实验结果很相似。

### Cross-Lingual Sentiment Quantification
- 跨语言情绪量化
- 情感量化是评论情感相对水平，比如积极、消极。
- 作者是第一个做跨语言情感量化任务的
- 作者的实验效果很好
- 作者展示了(Structural correspondence learning SCL)和(Distributional correspondence indexing: DCI)方法的有效性。
- 作者目前的分析水平在文档级，没有在细粒度水平。


### Exploring Distributional Representations and Machine Translation for Aspect-based Cross-lingual Sentiment Classification
- 探索分布式表示和机器翻译在跨语言实体级情感分类
- 作者比较了基于方面的CLSC的零镜头学习、双语单词嵌入、叠加去噪自动编码表示和机器翻译技术。
- 作者表明，基于分布式语义的模型可以获得与基于方面的CLSC机器翻译相当的结果。
- CLSA方法好像需要平行语料。

### Exploring Zero-shot Cross-lingual Aspect-based Sentiment Analysis using Pre-trained Multilingual Language Models
- 实验预训练多语言模型探索zero-shot跨语言基于实体的情感分析
- 作者使用了mBERT和XLMR进行了实验
- 作者做了Aspect Category Detection 和 Opinion Target Expression两个任务
- 实验结果表明XLMR的效果更好，更适合zero-shot

### Improving Word Embedding Coverage in Less-Resourced Languages Through Multi-Linguality and Cross-Linguality: A Case Study with Aspect-Based Sentiment Analysis
- 通过多语言性和跨语言性提高资源较少语言中的单词嵌入覆盖率：基于方面的情感分析案例研究
- 在这项工作中，我们提出了一种有效的方法，通过利用从不同语料库学习到的双语单词嵌入来提高资源较少语言中的单词嵌入覆盖率。
- 通过实验，验证了有效性

### Joint Multi-modal Aspect-Sentiment Analysis with Auxiliary Cross-modal Relation Detection
- 联合多模态实体情感分析和跨模态关系抽取
- 联合使用多模态ATE、多模态ASC任务
- 首次建立了文本-图像探测，更好地使用视觉信息

### Neural Attentive Network for Cross-Domain Aspect-Level Sentiment Classification
- 使用神经注意力网络进行跨领域实体级情感分类
- 该领域存在两个问题：一个是跨域构建健壮的文档建模；另一个是挖掘特定领域的方面，并利用情感词汇。
- 作者提出了NAACL，它能利用有监督的深层神经网络和无监督的概率生成模型的优点来加强表征学习。
- NAACL有两项任务，一个是领域分类器，用弱监督潜在Dirichlet分配模型（wsLDA），多视角注意机制来计算方面/词汇感知的文档表示。
- 方面级情感分类器，与领域分类器共享文档建模得到的向量。
- NAACL在分类准确率和F1评分方面优于比较的方法。
- 定性评估还表明，该模型能够合理地关注对判断输入文本情感极性非常重要的词语。

### Solving Data Sparsity for Aspect based Sentiment Analysis using Cross-linguality and Multi-linguality
- 使用跨语言和多语言来解决实体级情感分析问题
- 通过使用平行语料获得的双语词向量来解决数据稀疏问题。
- 使用了LSTM结构。
- 在多语言、跨语言上进行了使用，得到了最好的结果。
- 在英语、法语、印度语上做实验

### Unsupervised Cross-lingual Adaptation for Sequence Tagging and Beyond
- 在序列标记及其他任务上进行无监督跨语言自适应
- 跨语言自适应在mPTLM有两种实现方法，zero-shot和基于翻译。
- 作者提出了warmup-then-adaptation框架，以更好地利用翻译后的训练集，同时继承mPTLMs的跨语言能力。
- 作者不是简单地用机器翻译的数据扩充源语言训练数据，而是定制一种预热机制，从每种语言的翻译数据中提取多语言任务特定知识，并将其注入模型。
- 然后，对改进后的模型参数采用自适应方法，并以热启动方式进行跨语言迁移。
- 在九种目标语言的三种不同序列标记任务上的实验结果表明，我们的方法有利于mPTLMs的跨语言适应。
- NER、SRL（语义角色标注）、ABSA任务
- 作者展示了如何在序列标记任务中执行标签投影以实现基于翻译的方法，并开发了一种span-span映射策略来处理潜在的词序变化和对齐缺失问题。

### Cross-lingual Transfer Learning for Low-Resource Natural Language Processing Tasks
- 面向低资源自然语言处理任务的跨语言迁移学习
- 作者用了English, German, Chinese and Korean 作为例子
- 作者在NER、SA上两个重要自然语言处理任务做实验，证实了方法的有效性
