## 比較Merge Sort和 Heap Sort
- 相同之處
  - 時間複雜度
    - 皆是O(nlogn)
* 相異之處
  * 空間複雜度
    * Merge需要暫時性的暫列存放每回合Merge後的結果[O(n)]，Heap為原地置換，不需使用暫存的輔助資料結構[O(1)]
  * 穩定性
    * Merge是穩定排序法， Heap是不穩定排序法
- 小結
  * 雖然這兩個排序法的平均時間複雜度一樣，但在資料筆數為上億筆時，Merge sort會比Heap sort還來的快一些
  * 兩種排序法各有所長，若你想省記憶體空間，那Heap sort就會比較適合你；若你跑大筆的數據，想節省時間，那Merge sort會達到你想要的成效(當然我是假設只有這兩個排序法在做比較)
  
  <img src='https://github.com/eter0000/learningnotes/blob/master/images/com.jpg' weight=450 height=450>
參考資料
  * [Analysis of Algorithms](http://www-cs-students.stanford.edu/~rashmi/projects/Sorting.pdf)
