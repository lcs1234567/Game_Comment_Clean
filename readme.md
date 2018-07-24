Game_Comment_Clean
====================

#### gameComment_useless_clean4
1. 计算余弦相似度
- 获得 dataFrame 数据集
```
content_clear 
--------------
玩到31不能玩了
```
- 分词
```
import jieba
def jieba_word(x):
   return [ ''.join(i) for i in  jieba.cut(x)]

jieba_word 
--------------------
[玩到,31,不能,玩,了]
```
- 生成词典
```
from gensim import corpora
words = [x for x in df['jieba_word']]
d = corpora.Dictionary(words)
```
- 构建词频向量，词频矩阵
```
# 词频向量
word_count = [d.doc2bow(word) for word in type_words]
# 词频矩阵
# corpus2dense 稠密矩阵 csc 稀疏矩阵
corpus_matrix = corpus2csc(word_count, len(d))
```
- 计算余弦相似度
```
acorpus_matrix_T = corpus_matrix.T
# 此时 计算两种的 夹角余弦
similarities = cosine_similarity(acorpus_matrix_T)
```
2. 取出和 i 条评论最相似的评论 max(similarities[i,:]) 的 index
- similarities 是一个对称矩阵，和无向图的矩阵表示类似
- 对角线赋值为0，对角线=向量本身和本身夹角余弦值=1
- 切片，取similarities 第i行
- 对max的列值
```
    # 对角线 赋值 0
    np.fill_diagonal(similarities, 0)
    
    # 测试评论在 最后一行
    test_cosine_similarity = similarities[-1,:]
    
    # 选出 max 余弦值，即最相似的评论
    like_content_index = np.where(test_cosine_similarity == max(test_cosine_similarity))[0][0]
```
3. 自动分类
- 手动分类一部分
- 根据 相似度 给待分类评论分类
    - 比如 手动分类300条评论 df_mark_type
    - 一条待分类评论 df_test_type
    - df_test_type 和 df_mark_type 计算余弦值矩阵
    - 根据最相识的评论给类别type
    - 扩大 df_mark_type
    - 循环以上步骤，尝试分类30000 条评论
- 编写 python 分类函数 实践效果
    - df_result 写入 mysql, python web 展示

    ```
    from sqlalchemy import create_engine
    engine = create_engine("mysql+pymysql://root:eXYhzAWjyvy8grwM@127.0.0.1:3306/game_process?charset=utf8mb4")
    collect_test_type[['id','source','game_name','user_name','comment_time','content','score','type','emotion']].to_sql('s_lcs_game_classifbycosine_comments_qq', 
        con=engine, if_exists='replace', index=False)
    ```

#### commentWeb
1. 这是展示过滤 无用游戏评论的效果