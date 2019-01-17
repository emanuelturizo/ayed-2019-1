import json


# TODO Complete!
def numpareimpar(lista,k,listapar,listaimpar):
    
    
    if len(lista)==0:
        return listapar+listaimpar
    else:
        if k%2!=0:
            listaimpar.append(k)
            return numpareimpar(lista[1:],k,listapar,listaimpar)
            
        if k%2==0:
            listapar.append(k)
            return numpareimpar(lista[1:],k,listapar,listaimpar)
        
    
    return listapar+listaimpar


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
