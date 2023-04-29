from flask import Flask
from flask_restful import Api, Resource
from nltk.tree import *


app = Flask(__name__)
api = Api()

trees = {
    "paraphrases": [
        {
            "tree": "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))"
        },
        {
            "tree": "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars)) (, ,) (NP (JJ Catalan) (NNS restaurants)) (CC and) (NP (NNS clubs))))))))"
        },
        {
            "tree": "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ Catalan) (NNS restaurants)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ trendy) (NNS bars))))))))"
        },
        {
            "tree": "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ Catalan) (NNS restaurants)) (CC and) (NP (JJ trendy) (NNS bars))))))))"
        },
        {
            "tree": "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ Catalan) (NNS restaurants)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (NNS clubs))))))))"
        }
    ]
}

class Main(Resource):
    def get(self, tree):
        #return tree
        return Tree.fromstring(f"{tree}")


#api.add_resource(Main, "/api/courses")
api.add_resource(Main, "/paraphrase?tree=<tree>")
api.init_app(app)

if __name__=="__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
