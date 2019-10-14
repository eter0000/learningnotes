# Linked List 
### 簡介
  * Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點，若實際打開每個node的內部，至少會包含(1)data來代表資料，與(2)pointer指向下一個node。

### [比較：Array與Linked list](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
  #### Array
   * 優點 : random access：只要利用index即可在O(1)時間對Array的資料做存取。
   * 較Linked list為節省記憶體空間：因為Linked list需要多一個pointer來記錄下一個node的記憶體位置。
     * 假設node之data項目為1byte的char，但是pointer項目卻要4bytes，這樣的資料結構就多花了4倍的記憶體空間在與真正要處理的資料無關的部分上，是個沒有效率的做法。
  
