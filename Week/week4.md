# Insertion Sort
* 插入排序作法：
   * 將資料分成已排序、未排序兩部份
   * 依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
   * 插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入
   * 比較時，若遇到的值比正處理的值大或相等，則將值往右移
   
* 時間複雜度(Time Complexity)
    * Best Case：Ο(1)
      * 當資料的順序恰好為由小到大時，每回合只需比較1次
    * Worst Case：Ο(n2)
      * 當資料的順序恰好為由大到小時，第i回合需比i次
    * Average Case：Ο(n2)
      * 第n筆資料，平均比較n/2次
      
 
 
 <img src="https://pic.pimg.tw/jialin128/1467563630-3020446577_n.png">

# 參考資料
  * [[演算法] 插入排序法(Insertion Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
  * [插入排序法 in python](http://jialin128.pixnet.net/blog/post/141019829-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88insertion-sort%EF%BC%89in-pytho)
