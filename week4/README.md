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
