# Letter

Dear editer,

​	您好，我们是来自今年美国大学生数学建模大赛中的一只队伍，我们选择了 Wordle 数据分析和预测这道题目。本组的三个组员都是 Wordle 游戏的狂热粉丝，我们体验过 Wordle 的各个难度、变体，并且亲自编写过 Wordle 游戏以及自动求解程序。正因如此，我们对 Wordle 游戏的统计结果分析充满兴趣，我们很好奇在这些数据背后隐藏着怎样的规律。

​	首先，我们对 Wordle 的游玩人数数据进行了整体分析。我们发现从 2022 年 1 月 7 日至今的这段时间中，Wordle 游玩困难模式的玩家人数不断上升。截至 2022 年 2 月前后，Wordle 的每日游玩人数爆发式增长。在这之后，游玩人数便开始缓慢下降。根据我们的模型预测，在 2023 年 3 月 1 日，Wordle 的游玩人数应该在 11782 至 24424 这个区间。

​	其次，我们对数据中的 359 个单词对应的结果百分比数据进行了也进行了深入地分析。首先，我们使用 K-means 聚类算法对这些数据进行了分类，以此尝试找到相似结果的单词之间的联系。聚类算法的分类效果是令人欣喜的。除了个别特殊的数据，我们分类出的每一个聚类中的数据在百分比数据上差距基本小于 10%。在聚类的基础上，我们抛开了已有的百分比数据，仅仅从单词本身的性质出发开始挖掘同一类单词之间的联系。我们构建了一个神经网络，通过输入单词的元音个数、不同字母个数、在日常生活中的使用频率等数据，模型可以输出单词对应的聚类编号。这样做的原因是，我们希望能够通过深度学习发现同组单词之间的潜在联系，从而能够对未知结果的单词进行科学的分类，从而预测出单词的百分比结果。我们对在 2023 年 3 月 1 日以 eerie 为结果的游戏数据预测是，在一步、两步、三步、...、六步、七步以及以上的玩家百分比为 $0\%, 2\%, 11\%, 28\%, 32\%, 21\%, 5\%$。我们认为这个数据是相当准确的，它符合我们设计的预测模型，同时用经验进行解释也具有相当的合理性。

​	另外，我们构建了一个模型来判断单词的难度。我们使用信息熵理论计算出了当前游戏模式下的最优策略，并将玩家可能选择的策略分成了三类。我们使用梯度下降法和随机模拟拟合出了三种玩家的比例，并且根据三种玩家的期望猜测数量定义了单词的三种难度：简单，中等，和困难。经过模型的预测，我们判断单词 eerie 的难度是中等。

​	基于对已有数据的分析，我们对 Wordle 今后的持续维护提出一些建议。我们观察到:不论单词难度如何，玩家经过一次尝试就命中答案的百分比显著下降。这表明玩家可能已经形成了固定的答题策略，或者已经对自动求解的网站形成了依赖。我们认为有以下三种可能的解决方案：一，扩大备选词库；二，针对性地寻找在当前最优策略下表现不佳的单词；三，开发新的游戏模式，例如绿色和黄色的字母均显示为黄色来增加玩家需要处理的信息。其次，我们认为可以使用我们的模型分析近期单词猜测正确率的走势来调整接下来选择的单词的难易程度，以优化玩家体验。

​	希望我们的分析和建议能够帮助到您。祝您能够设计出更加精彩有趣的谜题。



Hello, we are a team from this year's American College Mathematical Modeling Competition. We have chosen Wordle Data Analysis and prediction as the topic. The three members of this team are all avid fans of Wordle games. We have experienced various difficulties and variations of Wordle, and have written Wordle games and automatic solving programs by ourselves. For this reason, we were interested in analyzing the statistical results of Wordle's games, and we wondered what kind of patterns might lie behind the data.

First, we analyzed Wordle's total number of visitors. We've seen an increase in the number of Wordle players playing Hard mode over the period from January 7, 2022 to today. By February 2022, the number of daily visitors to Wordle had exploded. After that, the number of people playing began to slowly decline. Our model predicts that the number of visitors to Wordle on March 1, 2023 should range from 11,782 to 24,424.

Secondly, we have carried out an in-depth analysis of the result percentage data corresponding to 359 words in the data. First, we classified the data using the K-means clustering algorithm in an attempt to find associations between words with similar results. The classification effect of clustering algorithm is pleasing. Except for a few special data, the difference in percentage data of each cluster we classified was basically less than 10%. On the basis of clustering, we discard the existing percentage data and start to dig the relationship between the same kind of words only from the nature of the words themselves. We build a neural network. By inputting data such as the number of vowels, the number of different letters, and the frequency of use in daily life, the model can output the cluster number corresponding to the word. The reason for this is that we want to be able to discover potential associations between the same group of words through deep learning, so that we can scientifically classify words with unknown outcomes and thus predict word percentage outcomes. Our forecast for the game's data as a result of eerie on March 1, 2023, is that in one, two, three,... Steps, six, seven, and percentage of players more than $0 \ % and \ % 2, 11 \ % and \ %, 32 \ %, 21 \ % and \ % $5. We think this data is quite accurate, it is in line with the forecast model we designed, and the empirical explanation is quite reasonable.

In addition, we built a model to judge the difficulty of words. We use information entropy theory to calculate the optimal strategy for the current game mode, and divide the possible strategies into three categories. We used gradient descent and random simulation to fit the proportions of three types of players, and defined three levels of difficulty for words: easy, medium, and hard, based on the expected number of guesses of the three types of players. After the prediction of the model, the difficulty of judging the word eerie is medium.

Based on the analysis of the available data, we propose some suggestions for the ongoing maintenance of Wordle in the future. We observed a significant drop in the percentage of players who hit the answer after a single attempt, regardless of the difficulty of the word. This suggests that players may have developed a fixed strategy or become dependent on an automated website. We think there are three possible solutions as follows: first, expand the alternative word base; Second, targeted to find the words that do not perform well under the current optimal strategy; Third, develop new game modes, such as green and yellow letters in yellow to increase the amount of information players need to process. Second, we think we can use our model to analyze the recent trend in word guess accuracy to adjust the difficulty of the next word selection to optimize the player experience.

We hope our analysis and suggestions will help you. Good luck designing more interesting puzzles.



Team XXXXX

date