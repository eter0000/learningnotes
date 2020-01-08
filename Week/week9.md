# Binary Search Tree
 * 定義 : 
   * 左子樹不為空，則左子樹的所有節點的鍵值(Key)小於根節點的鍵值
   * 右子樹不為空，則右子樹的所有節點的鍵值(Key)大於根節點的鍵值
   * 左右子樹也都是二元搜索樹
   * 節點不會有重複的鍵值
 
 * 有時會遇到特殊狀況 : 
   * 沒有鍵值，而用值(Value)來比較
   * 允許重複的資料，此時會出現等於的情況，則將定義1.改成小於等於或者定義2.改成大於等於
   
  <img src="https://pic.pimg.tw/emn178/1357012343-3927431965.png"> 
  
 * 原版通常會有以下介面 : 
   * add: 加入資料(或insert)
   * remove: 移除資料(或delete)
   * containsKey: 判斷是否包含鍵值
   * get: 取出資料
 
 * 無鍵值的介面通常會有 : 
   * add: 加入資料。(或insert)
   * remove: 移除資料。(或delete)
   * contains: 判斷是否包含資料

* 詳細內容可以到我的介紹[BST.md](https://github.com/eter0000/learningnotes/blob/master/HW3/Binary%20Search%20Tree%20%E6%96%B0%E5%A2%9E%E3%80%81%E5%88%AA%E9%99%A4%E3%80%81%E6%9F%A5%E8%A9%A2%E3%80%81%E4%BF%AE%E6%94%B9%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.md)
* [Binary Search Tree上課影片](https://youtu.be/7vw2iIdqHlM)
# 參考資料
  * [Binary Search Tree: Search(搜尋資料)、Insert(新增資料)](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)
