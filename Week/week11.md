# Hash Table
* Hash function原理解釋
  * 對不同的文字、字串、數字經過特定的函式或演算法，轉換成不同的樣貌，且有兩個特色：
     * 無法反推出原本的訊息
     * 雜湊值會隨輸入的值不同而改變
  * 資料庫的應用：
     * 利於檢索和管理
  * 密碼學的應用：
     * 對資料進行編碼，進而達到保護資料的效果

* Hash Table
  * 雜湊函數運算出來的雜湊值，根據鍵(key)儲存在數據結構中，存放這些記錄的數組就稱為就稱為Hash Table
  * 也可稱作 HashMap，是 Dictionary 類別中雜湊表的一種實作
  * 概念大概是：當要把資料放到雜湊表時，先給定一個 key 和存放的 value，並將 key 的每個字元轉換成 ASCII Code 或 Unicode Code 並相加，這個相加的值即是 hash 鍵值，在 table 陣列上對應到存放的 value
  * 而不同的值，有時在雜湊表裡會有相同的對應位置，稱作衝突(collision)，可因應的方法有：
    * 可透過 link list來儲存 value，需要額外的串列鏈結空間，不過為較簡單的方法
    * 修改 hash function 降低重複位置的發生

* 可以到我的介紹了解更多 : [Hash Table.md](https://github.com/eter0000/learningnotes/blob/master/HW4/%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%E5%8E%9F%E7%90%86%E8%A7%A3%E9%87%8B.ipynb)

# 參考資料
  * [Hash Table](https://en.wikipedia.org/wiki/Hash_table)
  * [[演算法]雜湊表](https://carlos-studio.com/2018/01/21/%E6%BC%94%E7%AE%97%E6%B3%95-%E9%9B%9C%E6%B9%8A%E8%A1%A8hash-table/)
