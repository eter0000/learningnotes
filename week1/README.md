# Linked List 
## 簡介
  * Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點，若實際打開每個node的內部，至少會包含(1)data來代表資料，與(2)pointer指向下一個node。

## [比較：Array與Linked list](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
  ### Array
   #### 優點
    * random access：只要利用index即可在O(1)時間對Array的資料做存取。
    * 較Linked list為節省記憶體空間：因為Linked list需要多一個pointer來記錄下一個node的記憶體位置。
     * 假設node之data項目為1byte的char，但是pointer項目卻要4bytes，這樣的資料結構就多花了4倍的記憶體空間在與真正要處理的資料無關的部分上，是個沒有效率的做法。
  
   #### 缺點
    * 新增/刪除資料很麻煩：若要在第一個位置新增資料，就需要O(N)時間把矩陣中所有元素往後移動。同理，若要刪除第一個位置的資料，也需要O(N)時間把矩陣中剩餘的元素往前移動。
    * 若資料數量時常在改變，要時常調整矩陣的大小，會花費O(N)的時間在搬動資料(把資料從舊的矩陣移動到新的矩陣)。

   * 適用時機：
    * 希望能夠快速存取資料。
    * 已知欲處理的資料數量，便能確認矩陣的大小。
    * 要求記憶體空間的使用越少越好。
