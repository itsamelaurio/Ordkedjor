from Digraph import Digraph
from BFS import BFS


def main():
    with open("5000.txt") as f:
        words = [w.strip() for w in f.readlines()]
    g = Digraph(len(words))
    turnIntoGraph(g, words)

    test(g, words)


def turnIntoGraph(g, words):

    for wordX in words:
        for wordY in words:
            if(wordX != wordY):
                ok = False
                temp = wordY
                for letter in wordX[-4:]:
                    if letter in temp:
                        temp = temp.replace(letter, '', 1)
                        ok = True
                    else:
                        ok = False
                        break
                if(ok):
                    g.addedge(words.index(wordX), words.index(wordY))


def test(g, words):
    with open("5000test.txt") as f:
        for line in f.readlines():
            start = line[0:5]
            goal = line[6:11]

            bfs = BFS(g, words.index(start))
            print(bfs.dist_to(words.index(goal)))
            # ... sök väg från start till goal här


main()
