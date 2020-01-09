# HW1 - Quick Sort
* 快速排序作法：
  * 選定一個基準值(Pivot)
  * 將比基準值(Pivot)小的數值移到基準值左邊，形成左子串列
  * 將比基準值(Pivot)大的數值移到基準值右邊，形成右子串列
  * 分別對左子串列、右子串列作上述三個步驟 ⇒ 遞迴(Recursive)　直到左子串列或右子串列只剩一個數值或沒有數值
  
* 分割(Partition)：將數列依基準值分成三部份(快速排序作法中，第2,3步驟)
  * 左子數列：比基準值小的數值
  * 中子數列：基準值
  * 右子數列：比基準值大的數值
  * 快速排序法的效率和基準值(Pivot)的選擇息息相關，每次選擇的基準值(Pivot)愈接近數列的平均值或中位數愈好
  
* 基準值(Pivot)的選擇
  * 固定位置：第一個數值、最後一個數值、中間的數值
    * 基準值可能選到最小或最大的數值，使左、右子串列其中的一個大小為0
  * 亂數選擇：
    * 基準值可能選到最小或最大的數值，使左、右子串列其中的一個大小為0
  * 中位數：
    * 數值依大小排列，位置在最中間的數值不容易計算，增加複雜度
  *　三選一：第一個、最後一個、中間的數值的中位數
  
* 時間複雜度(Time Complexity)
  * Best Case：Ο(n log n)
    * 第一個基準值的位置剛好是中位數，將資料均分成二等份
  * Worst Case：Ο(n2)　
    * 當資料的順序恰好為由大到小或由小到大時有分割跟沒分割一樣
  *　Average Case：Ο(n log n)
  
* 空間複雜度(Space Complexity)：Ο(log n) ~ Ο(n)
  * 快速排序法的空間複雜度依實作方式而不同
  * 遞迴呼叫需要額外的堆疊空間 ⇒ 因遞迴的深度而異
  * Best Case： Ο(log n)
    * 遞迴呼叫的深度為log n
  * Worst Case： Ο(n)
    * 遞迴呼叫的深度為n-1

*　穩定性(Stable/Unstable)：不穩定(Unstable)
  
 <img src="https://pic.pimg.tw/emn178/1333181106-1205952279_n.png">

* 參考網站
  * [Comparison Sort: Quick Sort(快速排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)
  * [[演算法] 快速排序法(Quick Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Quick/Quick.php)
