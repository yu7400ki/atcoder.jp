input()

A = list(map(int,input().split()))

def dec_to_bin(x):	#10進数を2進数へ変換
	return bin(int(x))

def consecutive_zero(x):
	return len(x) - x.rfind("1") - 1	#後ろから0がいくつ連続するかを返す

a_list = []
for a in A:
	a_list.append(dec_to_bin(a))	#Aの要素すべてに対してdec_to_binを実行

l = []
for a in a_list:
	l.append(consecutive_zero(a))	#a_listの要素すべてに対してconsecutive_zeroを実行

print(min(l))	#lの最小値を出力