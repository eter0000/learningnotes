# 流程圖
<img src='https://github.com/eter0000/learningnotes/blob/master/images/heap.png'>

# 學習過程
* 一開始的想法是利用for迴圈由後往前比較上去:
  * 如果第2*w+1項 > 第w項，那就互換
  * 如果第2*w+2項 > 第w項，那就互換
  * 在用另外一個for迴圈執行到len(nums)-1的長度時，就算是跑完了
* 於是我就開始寫了，第一次寫出來的樣子是
<img src='https://github.com/eter0000/learningnotes/blob/master/images/heap1.jpg' weight=500 height=200>
 
 * 再把它加上`def`和`calss`應該就行吧? 於是我就讓它跑，執行出來的結果長這樣
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/heap2.jpg' >
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/heap222.jpg'>
 
 * 它跟我說 list index out of range，但我上面明明給定它判別式了，怎麼還會出包? 於是我跟同學討論了一下，找出問題所在，問題就在於我執行一次之後，會把第一個值pop掉，那nums的長度就不一樣了，後來找到還有`try`這個語法，它可以容錯誤值，在有錯誤值的性況下照常執行，而對錯誤值就會在`except`裡處理。於是我就在執行迴圈的判別式前，多打一行`try`，之後在回傳進newlist值的前一行再多一行`ecxept`，我是用`pass`來忽略錯誤值，它就長這樣
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/heap3.jpg'>
 
 * 跑出來的樣子是
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/heap4.jpg'>
 
 * 跑出來的結果是有排序沒有錯，但它是descending的，我要的是漸增的結果才對啊，我才發現我的heap是把最大值交換到第一位，之後取出第一位，所以會有這樣的結果是正常的，所以我在最後return 回來的值改成`newlist[::-1]`，讓它從最後一位讀回來
 
 <img src='https://github.com/eter0000/learningnotes/blob/master/images/heap5.jpg'>
 
 * 太棒了，總算完工了!
