# 簡介：Stack
* Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。

* 一般的Stack，會有以下幾個處理資料結構的功能：
  * Push(data)：把資料放進Stack。把書放進箱子。
  * Pop：把「最上面」的資料從Stack中移除。把位於箱子「最上面」的書拿出來。
  * Top：回傳「最上面」的資料，不影響資料結構本身。確認目前位於箱子「最上面」的是哪本書。
  * IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。確認箱子裡面有沒有書。
  * getSize：回傳Stack裡的資料個數，不影響資料結構本身。記錄目前箱子已經裝了多少本書。

<img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/Stack/intro/f1.png?raw=true" height=300 weight=600>

# Stack的應用：
* Stack最主要的功能是「記得先前的資訊」，所以時常用來處理需要「回復到先前的狀態」的問題，也稱為Back-Tracking問題，例如：
　 * 編輯器(如word、sublime等等)中的undo。
   * 網頁瀏覽器的「回到前一頁」功能。
   * 編譯器(compiler)中的Parsing。
     * 參考：Compiler Design - Top-Down Parser。
   * 任何遞迴(recursion)形式的演算法，都可以用Stack改寫，例如Depth-First Search(DFS，深度優先搜尋)。
     * 參考：GeeksforGeeks:Iterative Depth First Traversal of Graph。
   * 因為遞迴(recursion)使用了系統的Call Stack。
   
# 簡介 : Queue
 * Queue是具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。
<img src='https://github.com/eter0000/learningnotes/blob/master/week4/queue.png' height=200 weight=300>

 * 一般的Queue，會有以下幾個處理資料結構的功能：
   * Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。
      * 在Queue中新增資料又稱為enqueue。
   * Pop：把front所指向的資料從Queue中移除，並更新front。
      * 從Queue刪除資料又稱為dequeue。
   * getFront：回傳front所指向的資料。
   * getBack：回傳back所指向的資料。
   * IsEmpty：確認Queue裡是否有資料。
   * getSize：回傳Queue裡的資料個數。

# 參考資料
 * [Stack: Intro(簡介)](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)
 * [Queue: Intro(簡介)，並以Linked list實作](https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)
