# Red Black Tree
* 規則 :
  * 每個節點不是紅就是黑的
  * 根總是黑色的
  * 若節點是紅色的, 則其子節點必為黑色, 反之不必為真(亦即若節點是黑色, 則其子節點可為紅也可為黑), 這條規則其實也是在說明就垂直方向來看, 紅色節點不可以相連
  *  每個空子節點都是黑色的: 所謂的空子節點指的是, 對非葉節點而言, 本可能有, 但實際沒有的那個子節點. 譬如一個節點只有右子節點, 那麼其空缺的左子節點就是空子節點
  * 從根節點到葉節點或空子節點的每條路徑(簡單路徑), 必須包含相同數目的黑色節點(這些黑色節點的數目也稱為黑色高度)
  * 最長path(路徑)不會超過最短path的兩倍


<img src="https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-2.png">

* 旋轉 :
  * [Red Black Tree: Rotation(旋轉)](http://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html)

* 上課影片: [Red Black Tree Animation](https://youtu.be/rcDF8IqTnyI)

# 參考資料
  * [Red-Black Tree (紅黑樹)](https://yotsuba1022.gitbooks.io/data-structure-note/content/1.4.3-red-black-tree.html)
  * [Tree rotation](https://en.wikipedia.org/wiki/Tree_rotation)
