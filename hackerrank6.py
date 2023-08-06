def matchstrings(strings,queries):
    dic = {}
    for string in strings:
        if string in dic:
            dic[string] += 1
        else:
            dic[string] = 1

    results = []
    for query in queries:
        if query in dic:
            results.append(dic[query])
        else:
            results.append(0)

    return results 
           
strings = ['aba','baba','aba','xzxb']
queries = ['aba','xzxb','ab']
print(matchstrings(strings,queries))