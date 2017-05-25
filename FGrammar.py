import nltk
import sentence

class FGrammar(object):
    grammar = nltk.CFG.fromstring("""
       S -> IMPERATIVE | BACKGROUND | REQUEST | COMMAND
       IMPERATIVE -> NNP ACTION PP
       BACKGROUND -> ENTITY VBZ COLOR
       REQUEST -> HEAD ACTION PP
       COMMAND -> ENTITY PP
       NNP -> "Please" | "please"
       ACTION -> VB ENTITY
       VB -> "draw" | "want"
       ENTITY -> DT COLOR GRA | DT GRA
       DT -> "a" | "the" | "an" | "An" | "A" | "The"
       DIR -> "right" | "left" | "top" | "bottom" | "middle"
       GRA -> "circle" | "triangle" | "rectangle" | "square" | "star" | "OlympicSymbol" | "ladder" | "snowflake" | "smileface" | "dart"
       PP -> IN DIRECTION
       IN -> "on"
       DIRECTION -> DT DIR
       NN -> "background"
       VBZ -> "is"
       COLOR -> "blue" | "green" | "red" | "yellow" | "black" | "pink" | "skyblue"
       HEAD -> PRP VB TO
       ACTION -> VB ENTITY
       PP -> IN DIRECTION
       PRP -> "I"
       TO -> "to"
    """)

    #def filt(self,x):
    # return x.label() == 'GRA' or x.label() == 'DIR' or x.label() == 'COLOR'

#def parseTreeFromString(str):
   # return nltk.Tree.fromstring(str)
    #usermessage = "please draw a black triangle on the right"
    def Analysis(self,usermessage):
        #usermessage = self.usermessage
        #grammar = self.grammar
        sent = usermessage.split()
        rd_parser = nltk.ChartParser(self.grammar)

        for tree in rd_parser.parse(sent):
            return tree



            #for subtree in tree.subtrees(filter = self.filt):
              #print subtree

              #if (subtree.label() == 'GRA' and subtree.leaves() == ['circle'] ):
                   # return True
              #else:
                    #return False

            #print tree
            #trees.append(tree)
            #print tree.leaves()
            #print len(trees)
#print rd_parser.parse(sent)[0]
    #An = Analysis()
   # Analysis(An,"I want to draw a circle on the left.",grammar)
#tree = nltk.Tree.fromstring(demo_grammar)
#print tree
#for subtree in tree.subtrees(filter=filt):  # Generate all subtrees
        #if (subtree.label()=='GRA'):
            #if(['circle']==subtree.leaves()):
                #print "ha ha ha"
            #else:
                #print "there are something wrong."
                #print (subtree.leaves())
if __name__ == "__main__":

 fg = FGrammar()
 fg.Analysis(fg.usermessage)
 #target = open('tree.txt','w')
 #target.write(str(fg.Analysis(fg.usermessage)))
 #target.close()
 stc = sentence.Extracting(str(fg.Analysis(fg.usermessage)))
 print stc.ExtractColor()
 print stc.ExtractDir()
 print stc.ExtractGra()
#tree2 = rd_parser.parse(sent)
#tree3 = parseTreeFromString(tree2)
#tree3.draw()