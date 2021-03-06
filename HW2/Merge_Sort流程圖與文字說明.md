# 流程圖
<img src='https://github.com/eter0000/learningnotes/blob/master/images/mer.png'> 

# 學習過程
 * 一開始的想法是從「比較」和「合併」這個部分開始著手，所以我先把list分成兩部分：L和R，再來給定他們各自的index(l、r、m)，我想說要讓它在某種條件下重複執行，所以就用while迴圈，再加上之前演習課老師有稍微提點，於是我就開始寫了
 
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/m_sort2.jpg'>

 * 結果跑出來
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/msort3.jpg'>
 
 * 他說我index out of range，這時我才想到我忘記考慮到如果其中一邊跑完的情況，於是我就再加入條件:如果index超過它的長度時，要把另外一組剩下的直接補上，除此之外我發現我也忘記設l+1 跟 r+1，所以也一起加上去
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/pmsort.jpg'>
 

 * 跑出來的樣子是
 
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/pmsort1.jpg'>
 
 * 首先我先看沒錯誤，表示我程式碼沒問題，但還不知道跑出來的結果是否是我要的，於是我仔細的左右比對模擬，對完之後，太好了!
 終於跑出我想要的結果了，大家都說頭過身就過，「比較」跟「合併」的部分弄好了，下一個目標就是用迴圈去跑它了
 
 * 於是我就開始想到底要怎麼設迴圈，但是再多設用一個迴圈也不曉得要設在哪裡，讓我卡關很久。後來我想到，既然是要讓它一直切割直到剩下一個元素，那就必須先切完，再由下而上執行回來，用到遞迴的觀念，所以我想到在切割完的地方再跑一次merge_sort，這樣就可以一直切一直切，切到不能在切時，再一起整合，於是就變成
 
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/msort44.jpg'>

 * 但現實總是殘酷的
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/msort5.jpg'>
 
 * 看到之後我整個傻眼，我打那麼多不就是在定義merge_sort嗎?怎麼會跟我說我沒有定義它?後來想想，不對喔，如果只是單純的def這樣寫是沒錯，但我是放在`class`裡，要呼叫自己時應該要在前面再加上`self.`，應該這樣就對了吧?應該吧?
 
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/msort6.jpg'>
 
 * 歐買尬，終於跑出來了，謝謝天，謝謝地，謝謝!
 

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
