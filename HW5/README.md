# HW5 - BFS & DFS
* DFS 就像試探著走迷宮，從起點開始、任意選一點與起點相鄰的點行走，行走過的點會被標記起來，再將下一個點視為起點、繼續選擇與該點相鄰的點行走，直到發現所有的點都已被標記過，即相鄰此點的所有點都已經走過了，則退回上一個分叉路口，繼續探訪，直到所有的點都被標記過了，則搜索完畢

  <img src="https://kopu.chat/wp-content/uploads/2017/09/dfs.png">
  
* BFS 以某個頂點作為起始點，一開始拜訪該頂點、再接著拜訪該頂點的所有相鄰頂點，接下來再拜訪下一層的頂點，直到所有的頂點皆拜訪過為止

  <img src="https://kopu.chat/wp-content/uploads/2017/09/bfs.png">
  
* 想了解更多可以到我的HW5，以下是連結 :
  * [BFS & DFS.py](https://github.com/eter0000/learningnotes/blob/master/HW5/BFS_06170210.py)
  * [流程圖、學習歷程、BFS和DFS的原理與比較.ipynb](https://github.com/eter0000/learningnotes/blob/master/HW5/%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81BFS%E5%92%8CDFS%E7%9A%84%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.ipynb)
  
* 參考網站 : https://kopu.chat/2017/09/22/%E5%AF%A6%E4%BD%9Cgraph%E8%88%87dfs%E3%80%81bfs%E8%B5%B0%E8%A8%AA/
