import requests

#res = requests.get("http://127.0.0.1:3000/api/(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ Catalan) (NNS restaurants)) (CC and) (NP (JJ trendy) (NNS bars))))))))")
res = requests.get("http://127.0.0.1:3000/api/tree")
print(res.json())