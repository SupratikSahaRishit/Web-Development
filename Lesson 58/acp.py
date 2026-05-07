test_dict = {'Sentosa' : 2, 'Island' : 2, 'is' : 2, 'beautiful' :  1}
print("The original dictionary : " + str(test_dict))
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("Frequency of K is : " + str(res))