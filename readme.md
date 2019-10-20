Game_Comment_Clean
====================

#### commentWeb
用来辅助手动标记评论的web可视化应用

#### gameComment_clean_jupyter
我们先从渠道**应用宝**里面获取了很多游戏的数据，其中包括评论、用户评分。这些评论有内容简短、重复出现等特点。因此我们先进行了预处理

- 处理评论内容html 反转义内容、繁体转简体、去除标点符号
- 并选出长度大于5 的评论
- 去除重复三次以上的评论

接下来我们手动标记了1000条评论数据（这个样本有点少，至少要10000条的），0代表无用评论，1代表普通评论。分类模型选用了**逻辑回归方法**，但是如何表达样本数据使其适用分类模型是重要考虑得。我们尝试了四种表示方法

自己对过滤垃圾评论的尝试，比如tf-idf、余弦相似度，效果不是很好，可以忽略
* gameComment_useless_clean
* gameComment_useless_clean2
* gameComment_useless_clean3
* gameComment_useless_clean4

gameComment_useless_clean_word2vec 用word2、CNN方法进行分类
- 词袋模型，就是基于样本预料集的词频矩阵，各样本维度相同，元素是对应词的词频
- tf-idf，利用tf-idf 优化词袋模型，只用认为是样本关键词来表示样本，而不是全部词汇
- word2vec，用向量表示每个词汇，求出样本全部词汇的平均值向量表示该样本
- 端到端方式，利用卷积神经网络CNN学习语法特征

practice_comment_word2vec是用来训练word2vec语料库