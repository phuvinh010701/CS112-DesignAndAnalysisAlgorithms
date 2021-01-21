import time
import random
# Quy hoạc động thường
def knapSack(W, w, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif j < w[i - 1]:
                K[i][j] = K[i - 1][j]
            else:
                K[i][j] = max(val[i - 1]
                              + K[i - 1][j - w[i - 1]],
                              K[i - 1][j])
    return K[n][W]

# Quy hoạt động + trace back
def knapSack_trace_back(W, w, val, n):
    Table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    trace_b = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                Table[i][j] = 0
            elif j < w[i - 1]:
                Table[i][j] = Table[i - 1][j]
            else:
                Table[i][j] = max(val[i - 1] + Table[i - 1][j - w[i - 1]],  Table[i - 1][j])
                Table[i][j] = val[i - 1] + Table[i - 1][j - w[i - 1]]
                if Table[i][j] > Table[i-1][j]:
                    trace_b[i][j] = 1
                else :
                    Table[i][j] = Table[i-1][j]
    ans = Table[n][W]
    id = W
    while ans == Table[n][id]:
        id -= 1
    id += 1
    way = n
    while (id>0):
        if trace_b[way][id]:
            print(w[way-1], val[way-1])
            id -= w[way-1]
        way -= 1
    return ans



# Backtracking
def knapSack_back_tracking(index,value,heavy,max_v, W, val, w):
    if max_v < value:   # nếu phương án tạo giá trị lớn hơn max thì gán lại
        max_v = value
    if index == n:  # nếu sử dụng hết các món thì break
        return max_v
    for i in range(index+1, n):
        if heavy + w[i] <= W:  #đệ quy tính từng phương án một. rồi so sánh gán lại giá trị max
            max_v =max(max_v, knapSack_back_tracking(i,value+val[i],heavy + w[i], max_v, W, val, w))
    return max_v



Pre_table = []
def knapSack1(W, w, val, n):
    Table = [0]*(W+1)
    sum_1_i=0
    for i in range(n):
        Pre_table=[]
        for u in range( min( sum_1_i+w[i]+1 , W + 1) ) :
            Pre_table.append(Table[u])
        for j in range(w[i], min(sum_1_i+w[i]+1,W + 1)):
            Table[j] = max(  val[i ] + Pre_table[j - w[i ]]  , Pre_table[j])
        sum_1_i += w[i]
    return Table[W]
# Test
val = [60, 100, 120, 10, 100]
wt = [10, 20, 30, 5, 5]
W = 50
n = len(val)

print(knapSack(W, wt, val, n))
print(knapSack1(W, wt, val, n))

# thực nghiệm
for n in range(25000, 1000000, 25000):
    val = []
    w = []
    W = W + 50
    for i in range(n):
        val.append(random.randint(1,n))
        w.append(random.randint(1, n))

    start_time = time.time()
    knapSack(W, w, val, n)
    end_time = time.time()
    print(W, end="  ")
    print(n, end = "  ")
    print("{:.3f}".format(end_time - start_time))
    # start_time1 = time.time()
    # knapSack1(W, w, val, n)
    # end_time1 = time.time()
    # print(W, end = "  ")
    # print(n, end = "  ")
    # print("{:.3f}   {}".format(end_time-start_time, end_time1 - start_time1))