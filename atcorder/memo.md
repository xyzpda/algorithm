python で 入力 を 受け取る 方法 は 以下 の 5 つ。

(1) 数字 が 1 つ  
入力 例： N  

```python
N = int(input())
```

(2) 数字 が 2 つ 以上 で 別々 に 受け取り
入力 例： A B

```python
A, B = map(int, input().split())
```

(3) 文字列 が 1 つ  
入力 例： S

```python
S = input()
```

(4) 文字列 が 2 つ 以上 で 別々 に 受け取り  
入力 例： S T

```python
S, T = map(str, input().split()) 
```

(5) リスト で 受け取り  
入力 例： A1 A2 … An

```python
A = list(map(int, input().split()))
```
