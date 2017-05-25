import nltk


class Extracting(object):
    def __init__(self, demo_grammar):
        self.grammar = demo_grammar
        self.tree = nltk.Tree.fromstring(self.grammar)

    def FiltGra(self, x):
        return x.label() == 'GRA'

    def FiltDir(self, x):
        return x.label() == 'DIR'

    def FiltColor(self, x):
        return x.label() == 'COLOR'

    def ExtractGra(self):
        for subtree in self.tree.subtrees(filter=self.FiltGra):  # Generate all subtrees
            # "circle" | "triangle" | "rectangle" | "square" | "star" | "olympicSymbol"
            # print subtree.leaves()
            if (subtree.leaves() == ['circle']):
                graph = 'circle'
                return graph
            if (subtree.leaves() == ['triangle']):
                graph = 'triangle'
                return graph
            if (subtree.leaves() == ['rectangle']):
                graph = 'rectangle'
                return graph
            if (subtree.leaves() == ['square']):
                graph = 'square'
                return graph
            if (subtree.leaves() == ['star']):
                graph = 'star'
                return graph
            if (subtree.leaves() == ['OlympicSymbol']):
                graph = 'OlympicSymbol'
                return graph
            if (subtree.leaves() == ['snowflake']):
                graph = 'snowflake'
                return graph
            if (subtree.leaves() == ['smileface']):
                graph = 'smileface'
                return graph
            if (subtree.leaves() == ['dart']):
                graph = 'dart'
                return graph
            else:
                graph = ''
                return graph

    def ExtractDir(self):
        for subtree in self.tree.subtrees(filter=self.FiltDir):  # Generate all subtrees
            # "right" | "left" | "top" | "bottom" | "middle"
            # print subtree.leaves()
            if (subtree.leaves() == ['left']):
                direction = 'left'
                return direction
            if (subtree.leaves() == ['right']):
                direction = 'right'
                return direction
            if (subtree.leaves() == ['top']):
                direction = 'top'
                return direction
            if (subtree.leaves() == ['bottom']):
                direction = 'bottom'
                return direction
            if (subtree.leaves() == ['left']):
                direction = 'left'
                return direction
            else:
                direction = 'middle'
                return direction

    def ExtractColor(self):

        for subtree in self.tree.subtrees(filter=self.FiltColor):  # Generate all subtrees
            # "blue" | "green" | "red" | "yellow" | "black"
            # if(subtree.leaves()):

            if (subtree.leaves() == ['red']):
                color = 'red'
                return color
            if (subtree.leaves() == ['blue']):
                color = 'blue'
                return color
            if (subtree.leaves() == ['green']):
                color = 'green'
                return color
            if (subtree.leaves() == ['yellow']):
                color = 'yellow'
                return color
            if (subtree.leaves() == ['black']):
                color = 'black'
                return color
            if (subtree.leaves() == ['pink']):
                color = 'pink'
                return color
            if (subtree.leaves() == ['skyblue']):
                color = 'skyblue'
                return color
            else:
                color = 'black'
                return color
