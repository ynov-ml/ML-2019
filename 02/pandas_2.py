In [5]: pd.DataFrame({ 'A' : 1.,
               'B' : pd.Timestamp('20161209'),
               'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
               'D' : np.array([3] * 4, dtype='int32'),
               'E' : pd.Categorical(["test","train","test","train"]),
               'F' : 'hello' })
Out[5]: 
   A          B  C  D      E      F
0  1 2016-12-09  1  3   test  hello
1  1 2016-12-09  1  3  train  hello
2  1 2016-12-09  1  3   test  hello
3  1 2016-12-09  1  3  train  hello

In [6]: 
