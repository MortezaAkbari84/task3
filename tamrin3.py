
suspects = ['A', 'B', 'C', 'D']

answer_A = [0, 0, 1]
answer_B = [0, 0, 0]
answer_C = [1, 0, 0]
answer_D = [0, 1, 0]
# answer_A[3] is always true
# beetwin A[1] & C[1] one of them is always false and is not related to whom the theaf is
# beetwin D[2] & C[3] one of them is always false and is not related to whom the theaf is
truth_count = 3

for i in suspects :
    if i == 'A' :
        answer_B[0] = 1 ; truth_count += 1
        answer_B[2] = 1 ; truth_count += 1
        answer_C[1] = 1 ; truth_count += 1
        answer_D[2] = 1 ; truth_count += 1
        
        if truth_count == 6 :
            print("theaf is ", i)
        else :
            truth_count = 3
        
    if i == 'C' :
        answer_B[0] = 1 ; truth_count += 1
        answer_B[2] = 1 ; truth_count += 1
        answer_C[1] = 1 ; truth_count += 1
        answer_B[1] = 1 ; truth_count += 1
        
        if truth_count == 6 :
            print("theaf is ", i)
        else :
            truth_count = 3
    
    if i == 'D' :
        answer_D[0] = 1 ; truth_count += 1
        answer_B[2] = 1 ; truth_count += 1
        answer_C[1] = 1 ; truth_count += 1
        answer_B[1] = 1 ; truth_count += 1
        
        if truth_count == 6 :
            print("theaf is ", i)
        else :
            truth_count = 3

    if i == 'B' :
        answer_B[0] = 1 ; truth_count += 1
        answer_B[1] = 1 ; truth_count += 1
        answer_A[1] = 1 ; truth_count += 1
        
        if truth_count == 6 :
            print("theaf is ", i)
        else :
            truth_count = 3















