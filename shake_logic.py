import sys, os, re

def filesToDict(listOfFiles):
	'''
	>>> filesToDict(['testRead1.txt','testRead2.txt']) == {'testRead1.txt': 'one\\ntwo\\n', 'testRead2.txt': 'three\\nfour\\nthree\\n'}
	True

	'''
	resultsDict = {}
	for filename in listOfFiles:
		fileHandler = open(filename, 'r')
		fileContents = fileHandler.read()
		fileHandler.close()
                x = filename.split("/")
                if len(x) > 1: filename = x[-1]
		resultsDict[filename]=fileContents
	return resultsDict

	# alternative, more pythonic solution:
	#return {f: open(f).read() for f in listOfFiles }

def freqAnalyzer(fullWorksDict, keyword):
	'''
	>>> freqAnalyzer({'testRead1.txt': 'one\\ntwo\\n', 'testRead2.txt': 'three\\nfour\\nthree\\n'}, 'tHree') == {'testRead1.txt': 0, 'testRead2.txt': 2}
	True

	>>> freqAnalyzer(filesToDict(['testRead1.txt','testRead2.txt']), 'tHree') == {'testRead1.txt': 0, 'testRead2.txt': 2}
	True

	'''
	resultsDict = {}
	for title in fullWorksDict.keys():
		text = fullWorksDict[title]
		text = text.lower()
		keyword = keyword.lower()
		freq = text.count(keyword)
		resultsDict[title] = freq
	return resultsDict

	# alternative, more pythonic solution:
	#return {opusName: content.lower().count(keyword.lower()) for opusName, content in fullWorksDict.items()}

def allWordsFromString(str):
        """
        Pull out all words from a string, ignore punctuation, force to lower case.
        >>> sorted(list(allWordsFromString('a b c a')))
        ['a', 'b', 'c']
        >>> sorted(list(allWordsFromString('C a.b.C.d; c ')))
        ['a', 'b', 'c', 'd']
        """
        return set(re.findall("\w+", str.lower()))

def allWordsFromStrings(*strs):
        """
        >>> sorted(list(allWordsFromStrings('a b c a', 'z y', ' a ')))
        ['a', 'b', 'c', 'y', 'z']
        """
        return reduce(lambda s1, s2: s1.union(s2),
                      map(allWordsFromString, strs))

def allPlayWords(corpus):
        return allWordsFromStrings(*(corpus.values()))

def main():
        '''
        This main() takes one argument - a word - and prints map from play name to
        number of occurrences of that word.
        '''
	arguments = sys.argv[1:]

	if len(sys.argv) <= 1:
		print "wrong usage"
		sys.exit(1)
        else:
                word = sys.argv[1]
                corpus = filesToDict(["data/{f}".format(f=f) for f in os.listdir("data")])
                for k, v in freqAnalyzer(corpus, word).iteritems():
                        print("{k}: {v}".format(v=v, k=k))

if __name__ == "__main__":
	main()
