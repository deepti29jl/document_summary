import metapy

metapy.log_to_stderr()

class TextProcessor:

    keywords = {'About', 'WorkExperience', 'Education', 'Certificates', 'Awards', 'Groups'}
    document = None
    tokenizer = None
    top_N = 5
    frequency_map = dict()
    sentence_token_map = dict()

    def __init__(self, top_n=5):
        self.document = metapy.index.Document()
        self.tokenizer = metapy.analyzers.ICUTokenizer(suppress_tags=True)
        self.tokenizer = metapy.analyzers.LengthFilter(self.tokenizer, min=2, max=30)
        self.tokenizer = metapy.analyzers.ListFilter(self.tokenizer, \
                                                "data/lemur-stopwords.txt",\
                                                metapy.analyzers.ListFilter.Type.Reject)
        self.top_N = top_n

    def split_sentences(self, text):
        sentences = []
        if (text != None and text != ''):
            for line in text.split('\n'):
                if ('. ') in line and 'ltd. ' not in line.lower():
                    pieces = line.split('. ')
                    for piece in pieces:
                        sentences.append(piece)
                else:
                    sentences.append(line)

        return sentences

    def tokenize(self, text):
        if (text is None or text == ''):
            return []

        self.document.content(text)
        self.tokenizer.set_content(self.document.content())

        tokens = [token for token in self.tokenizer]

        return tokens


    def score_sentences(self, sentences):
        sentence_score_map = dict()
        if (len(sentences) != len(self.sentence_token_map)):
            print("Array length mismatch: " + str(len(sentences)) + " vs " + str(len(self.sentence_token_map)))
            return sentence_score_map

        for (index, words) in self.sentence_token_map.items():
            word_count = len(words)

            if (word_count ==  0):
                sentence_score_map[index] = 0
                continue

            # Look for keywords we have used as LABELS for certain sections of bio as they should not score high
            #  keywords = {'About', 'WorkExperience', 'Education', 'Certificates', 'Awards', 'Groups'}
            if (word_count == 2 and words[0] in self.keywords):
                sentence_score_map[index] = 0
                continue

            for word in self.frequency_map.keys():
                if (word in sentences[index].lower()):
                    if(index in sentence_score_map):
                        sentence_score_map[index] += self.frequency_map[word]
                    else:
                        sentence_score_map[index] = self.frequency_map[word]

            if (index in sentence_score_map):
                sentence_score_map[index] /= word_count
            else:
                sentence_score_map[index] = 0


        return sentence_score_map

    def summarize(self, text_data):

        if (text_data is None or text_data == ''):
            print("Blank text, nothing to summarize")
            return None

        sentences = self.split_sentences(text_data)

        if (len(sentences) < 2):
            print("Too few sentences for summarization!")
            return text_data

        index = 0

        self.frequency_map.clear()
        self.sentence_token_map.clear()

        for s in sentences:
            tokens = self.tokenize(s)
            self.sentence_token_map[index] = tokens
            index += 1

            if (len(tokens) > 0):
                for t in tokens:
                    if(t in self.frequency_map):
                        self.frequency_map[t] += 1
                    else:
                        self.frequency_map[t] = 1

        sentence_scores = self.score_sentences(sentences)
        average_score = 0.0

        for (index, score) in sentence_scores.items():
            average_score += score

        average_score = (average_score/len(sentences))

        summarized = []
        for (index, score) in sentence_scores.items():

            if score > average_score:
                summarized.append(sentences[index])

            # Also adding a limit to the top
            if(len(summarized) >= self.top_N):
                break;

        summary = "\n".join(summarized)

        return summary