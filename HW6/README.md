# HW6 - Dijkstra & Kruskal Algorithm
* Dijkstra演算法 :
  * 初使時令 S={V0},T={其餘頂點}，T中頂點對應的距離值
  * 若存在<V0,Vi>，為<V0,Vi>弧上的權值
  * 若不存在<V0,Vi>，為無窮
  * 從T中選取一個其距離值為最小的頂點W，加入S
  * 對T中頂點的距離值進行修改：若加進W作中間頂點，從V0到Vi的距離值比不加W的路徑要短，則修改此距離值
  * 重複上述步驟，直到S中包含所有頂點，即S=V為止

  <img src="https://img-blog.csdn.net/20130921194526562?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWF0cml4X2xhYm9yYXRvcnk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast">
  
* Kruskal演算法 :
  * 設連通網N=(V,{E})，令最小生成樹
    * 初始狀態為只有n個頂點而無邊的非連通圖T=(V,{NULL})，每個頂點自成一個連通分量
    * 在E中選取代價最小的邊，若該邊依附的頂點落在T中不同的連通分量上，則將此邊加入到T中；否則，捨去此邊，選取下一條代價最小的邊
    * 依此類推，直至T中所有頂點都在同一連通分量上為止
    
    <img src="https://img-blog.csdn.net/20130921173459156">
    
 * 想了解更多可以到我的HW6，以下是連結 :
    * [Dijkstra & Kruskal.py](https://github.com/eter0000/learningnotes/blob/master/HW6/Dijkstra_06170210.py)
    * [流程圖、學習歷程、Dijkstra與Kruskal原理說明.ipynb](https://github.com/eter0000/learningnotes/blob/master/HW6/%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81Dijkstra%E8%88%87Kruskal%E5%8E%9F%E7%90%86%E8%AA%AA%E6%98%8E.ipynb)
  
  * 參考網站 : https://www.itread01.com/content/1548612012.html
