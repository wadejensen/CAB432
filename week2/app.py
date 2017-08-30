import random
import nltk
from nltk import FreqDist

nltk.download('gutenberg')
from nltk.corpus import gutenberg

from flask import Flask
app = Flask(__name__)

@app.route("/")
def count_words():
        books = []
        for text in gutenberg.fileids():
                books.append(text)
        book = books[random.randint(0, len(books)-1)]
        title = ""
	referenceList = [['austen-emma.txt', 'Emma by Jane Austen'], ['austen-persuasion.txt', 'Persuasion by Jane Austen'], ['austen-sense.txt', 'Sense and Sensibility by Jane Austen'], ['The King James Bible'], ['blake-poems.txt', 'Poems by William Blake'], ['bryant-stories.txt', 'Stories by Kobe Bryant'], ['burgess-busterbrown.txt', 'The Adventures of Buster Bear by Thornton W. Burgess'], ['carroll-alice.txt', 'Alice\'s Adventures in Wonderland by Lewis Carroll'], ['chesterton-ball.txt', 'The Ball and the Cross by G.K. Chesterton'], ['chesterton-brown.txt', 'The Wisdom of Father Brown by G.K. Chesterton'], ['chesterton-thursday.txt', 'The Man Who Was Thursday by G.K. Chesterton'], ['edgeworth-parents.txt', 'The Parent\'s Assistant by Maria Edgeworth'], ['melville-moby_dick.txt', 'Moby Dick by Herman Melville'], ['milton-paradise.txt', 'Paradise Lost by John Milton'], ['shakespeare-caesar.txt', 'The Tragedie of Julias Caesar by William Shakespeare'], ['shakespeare-hamlet.txt', 'The Tragedie of Hamlet by William Shakespeare'], ['shakespeare-macbeth.txt', 'The Tragedie of Macbeth by William Shakespeare'], ['whitman-leaves.txt', 'Leaves of Grass by Walt Whitman']]

        for reference in referenceList:
                if reference[0] == book:
                        title = reference[1]
                        break

        tokens = gutenberg.words(book)
        tokens = [word.lower() for word in tokens if word.isalpha()]

        fdist = FreqDist(tokens)
        common = fdist.most_common(500)

        words = []
        for word, frequency in common:
                words.append(word)
        words.sort()

        highCount = common[0][1]

        html = "<html><head><title>Word Cloud</title></head><body><h1>Most common Words in " + title + "</h1>"

        for word in words:
                size = str(int(15 + fdist[word] / float(highCount) * 150))
                colour = str(hex(int(0.8 * fdist[word] / float(highCount) * 256**3)))
                colour = colour[-(len(colour) - 2):]
                while len(colour) < 6:
                        colour = "0" + colour
                span = '<span style="font-size: '
                span = span + size + 'px; color: '
                span = span + colour + '; display: inline-block">'
                span = span + word + '</span>'
                html = html + span
        html = html + "</body></html>"
        return html

if __name__ == "__main__":
    app.run()
