# Merge Sort 簡介
### 拆分
 * 把大陣列切一半變成兩個小陣列
 * 把切割好的陣列再各自切一半
 * 重複上步驟直到每個小陣列只剩一個元素
### 合併
 * 排序兩個只剩一個元素的小陣列並合併
 * 把兩邊排序好的小陣列合併並排序成一個陣列
 * 重複步驟二直到所有小陣列都合併成一個大陣列  

### 示意圖

<img src='https://github.com/eter0000/learningnotes/blob/master/images/msort.png' weight=300 height=500>

### 參考網站
 * [初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)
 * [Merge Sort - Wikipedia](https://en.wikipedia.org/wiki/Merge_algorithm)
 
# 流程圖
<img src='https://github.com/eter0000/learningnotes/blob/master/images/mer.png'>
 
## 學習過程
 * 一開始的想法是從「比較」和「合併」這個部分開始著手，所以我先把list分成兩部分：L和R
 * 再來給定他們各自的index(l、r、m)
 * 我想說要讓它在某種條件下重複執行，所以就用while迴圈
 * 再加上之前演習課老師有稍微提點，於是我就開始寫了

