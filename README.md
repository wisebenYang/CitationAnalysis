期刊和会议论文的citation counting的分布情况 -- TheDistributionOfJournalAndConrference.py

不同类别的期刊和会议的比较 + 同一类别的期刊和会议之间的差异比较 -- DifferenceBetweenJournlsAndConferences.py

计算不同年份的期刊会议的引用权重分配情况 --  weightOfDifferentYear.py

使用本文提出的方法对期刊会议进行分类的结果 -- verify.py
  -- 这个文件中包含两个主要的函数，verifyJour 和 verifyConf。 这两个函数都是需要先将不同期刊会议在不同年份的引用次数给分别出来，然后再用这些数据来计算对应期刊会议的weighting citation counting。我们在源代码中将不同年份奇卡会议分别出来的函数给注释掉，因为我们已经获取了这些数据，可以直接使用。但是在没有这些数据的时候，就需要使用这些函数来计算这些数据。

计算期刊会议的weighting citation counting。使用本文的方法对CCF推荐的期刊会议进行排名，并提取前十个前会议 -- topTen

使用三种不同的方法处理确实的数据集 -- 
   - Method1.py:使用随机概率的方法；
   - Method2.py:使用投票规则的方法；
   - Method3.py：之间删除确实的数据集；

   
