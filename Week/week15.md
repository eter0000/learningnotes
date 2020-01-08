# Shortest Path
* Dijkstra's algorithm 是以某一節點為出發點，計算從該節點出發到所有其他節點的最短路徑
* 首先以某一節點當作出發點，在與其相連且尚未被選取的節點裡，選擇加入離出發點距離 最短的節點，並且透過新增的節點更新到達其他節點的距離
* 如此重覆加入新節點，直到所有的節點都被加入為止
* 演算過程如以下 : 
  
  <img src="http://1.bp.blogspot.com/-vPmM3H1AmDk/UYI6zFfXlJI/AAAAAAAAMmg/OKcvccPEMkg/s1600/2457-5.PNG">

* 可以參考我的[Dijkstra與Kruskal原理說明](https://github.com/eter0000/learningnotes/blob/master/HW6/%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81Dijkstra%E8%88%87Kruskal%E5%8E%9F%E7%90%86%E8%AA%AA%E6%98%8E.ipynb)

* [Printing Paths in Dijkstra’s Shortest Path Algorithm](https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/)

# 參考資料
  * http://puremonkey2010.blogspot.com/2013/05/alg-info-dijkstras-algorithm-shortest.html
  * https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
  * https://ithelp.ithome.com.tw/articles/10209593
