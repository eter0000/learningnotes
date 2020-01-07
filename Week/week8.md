# Binary Tree
  * 最廣義的樹(Tree)對於樹上的node之child數目沒有限制，因此，每個node可以有多個child
  
  <img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/BinaryTree_fig/Intro/f1.png?raw=true">
  
  * 若限制node只能有兩個child，等價於「樹上的每一個node之degree皆為2」，此即稱為Binary Tree(二元樹)，並稱兩個child pointer為left child和right child
  
  <img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/BinaryTree_fig/Intro/f2.png?raw=true">
  
  * [Tree in Data Structure](https://www.tutorialride.com/data-structures/trees-in-data-structure.htm)
  * [Introduction to Tree Data Structure](https://www.youtube.com/watch?v=ikPPdBDZnz4#action=share)
# Full & Complete Binary Tree
  * Full Binary Tree
    * 所有internal node都有兩個subtree(也就是兩個child pointer)
    * 所有leaf node具有相同的level(或相同的height)
    
    * 若一棵Full Binary Tree的leaf node之level為n，整棵樹共有2n−1個node
      * 例如，若leaf node的level為4， 整棵樹共有15個node，並且，每個node與其child有以下關係：
          * 第i個node的left child之index為 2i
          * 第i個node的right child之index為 2i+1
          * 除了root之parent為NULL之外，第i個node的parent之index為 ⌊i2⌋

    <img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/BinaryTree_fig/Intro/f3.png?raw=true">

  * Complete Binary Tree
    * 若一棵樹的node按照Full Binary Tree的次序排列(由上至下，由左至右)，則稱此樹為Complete Binary Tree
    * 下圖的樹共有10個node，且這十個node正好填滿Full Binary Tree的前十個位置，則此樹為Complete Binary Tree
    
    <img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/BinaryTree_fig/Intro/f4.png?raw=true">

# 參考網站
  * [Binary Tree: Intro(簡介)](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
