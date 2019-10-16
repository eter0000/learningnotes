# 簡介：Stack
* Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。

* 一般的Stack，會有以下幾個處理資料結構的功能：
  * Push(data)：把資料放進Stack。把書放進箱子。
  * Pop：把「最上面」的資料從Stack中移除。把位於箱子「最上面」的書拿出來。
  * Top：回傳「最上面」的資料，不影響資料結構本身。確認目前位於箱子「最上面」的是哪本書。
  * IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。確認箱子裡面有沒有書。
  * getSize：回傳Stack裡的資料個數，不影響資料結構本身。記錄目前箱子已經裝了多少本書。

<img src="https://github.com/eter0000/learningnotes/blob/master/week3/1571204568273.jpg" height=300 weight=600>

# Stack的應用：
* Stack最主要的功能是「記得先前的資訊」，所以時常用來處理需要「回復到先前的狀態」的問題，也稱為Back-Tracking問題，例如：
　 * 編輯器(如word、sublime等等)中的undo。
   * 網頁瀏覽器的「回到前一頁」功能。
   * 編譯器(compiler)中的Parsing。
     * 參考：Compiler Design - Top-Down Parser。
   * 任何遞迴(recursion)形式的演算法，都可以用Stack改寫，例如Depth-First Search(DFS，深度優先搜尋)。
     * 參考：GeeksforGeeks:Iterative Depth First Traversal of Graph。
   * 因為遞迴(recursion)使用了系統的Call Stack。
