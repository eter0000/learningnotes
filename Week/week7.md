# Merge Sort
  * 合併排序作法：
    * 將數列對分成左子數列、右子數列，分別對左子數列、右子數列作上一個步驟 ⇒ 遞迴(Recursive)
    * 直到左子數列、右子數列被分割成只剩一個元素為止，將僅剩的一個元素作為遞迴的結果回傳
    * 對回傳的左子數列、右子數列依大小排列合併，再將合併的結果作為遞迴的結果回傳
  
  * 合併作法：：將左子數列及右子數列依大小合併成一個新的數列
    * 若左子數列的數值都已填到新的數列 ⇒ 將右子數列中未填過的最小值填入新數列
    * 若右子數列的數值都已填到新的數列 ⇒ 將左子數列中未填過的最小值填入新數列
    * 將左子數列及右子數列中，未填過的最小值填到新的數列  
  
  * 時間複雜度(Time Complexity)
    * Best Case：Ο(n log n)
    * Worst Case：Ο(n log n)
    * Average Case：Ο(n log n)
    
  * [機器人排序影片](https://www.youtube.com/watch?v=es2T6KY45cA&feature=youtu.be)

  <img src="https://www.c-programming-simple-steps.com/images/xmerge-sort-visual.png.pagespeed.ic.SdExk04KbD.webp">
  
# Heap Sort 補充資料
  * https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html
  
# Merge Sort & Heap Sort比較
  * 可以參考[比較Merge Sort和 Heap Sort.md](https://github.com/eter0000/learningnotes/blob/master/HW2/Heap_sort%E8%88%87Merge_sort%E4%B9%8B%E6%AF%94%E8%BC%83.md)
