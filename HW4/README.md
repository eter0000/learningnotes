# HW4 - Hash Table
* 雜湊表（Hash table，也叫哈希表），是根據鍵（Key）而直接查詢在內存存儲位置的資料結構，也就是說，它通過計算一個關於鍵值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄，這加快了查找速度。這個映射函數稱做雜湊函數，存放記錄的數組稱做雜湊表
* 例如:為了查找電話簿中某人的號碼，可以創建一個按照人名首字母順序排列的表（即建立人名x到首字母F(x)的一個函數關係），在首字母為W的表中查找「王」姓的電話號碼，顯然比直接查找就要快得多。這裡使用人名作為關鍵字，「取首字母」是這個例子中雜湊函數的函數法則F()，存放首字母的表對應雜湊表，關鍵字和函數法則理論上可以任意確定。

  <img src="http://vhanda.in/blog/images/2012/07/19/normal-hash-table.png">
  
* 想了解更多可以到我的HW4，以下是連結 :
  * [Hash Table.py](https://github.com/eter0000/learningnotes/blob/master/HW4/hash_table_06170210.py)
  * [流程圖與學習歷程與Hash原理解釋.ipynb](https://github.com/eter0000/learningnotes/blob/master/HW4/%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%E5%8E%9F%E7%90%86%E8%A7%A3%E9%87%8B.ipynb)
  
* 參考網站 : https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
