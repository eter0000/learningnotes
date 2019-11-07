## 比較Merge Sort和 Heap Sort
- 相同之處
  - 時間複雜度
    - 皆是O(nlogn)
* 相異之處
  * 空間複雜度
    * Merge需要暫時性的暫列存放每回合Merge後的結果[O(n)]，Heap為原地置換，不需使用暫存的輔助資料結構[O(1)]
  * 穩定性
    * Merge是穩定排序法， Heap是不穩定排序法
