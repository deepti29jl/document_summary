## Team 

Deepti Sharma (deeptis2@illinois.edu)

## Topic 

Document Summarization for LinkedIn Profile data

## Introduction

In our professional life we meet new people in meetings, conferences or other professional gatherings. But quite often, we do not have the background of the person we meet. For formal gatherings, however, we do receive email invites and have the opportunity to look them up before we meet. However, that requires some work on the attendees behalf but event that requires the person to visit the web page. 

What if we dynamically generate a professional summary that is succinct and captures the key elements of career. This summary can be shared with wider audience for initial introductions.

We can leverage the data users have on their LinkedIn Profiles and apply the right Text retrieval algorithms to generate a professional summary for users benefits.

#### Data Source 
LinkedIn data feed

### Software Setup 

 Python (recommended version 3.6)
 
 Chrome Browser and Web Driver
 
#### Dependencies
 
 pip install metapy

 pip install beautifulsoup4

 pip install selenium
 
 Make sure that the most recent version of Chrome is installed on your machine  (To check/update Chrome, go to the menu and select Help > About Google Chrome. Or, download and install it from here: https://www.google.com/chrome/)
 Then, download the matching version of ChromeDriver from here: https://sites.google.com/a/chromium.org/chromedriver/ and add it to your system path.
 
### Code Organization

    data
        lemur-stopwords.txt (used by tokenizer)
        LinkedIn-Connections.htm (scraped content ofmy own network connections webpage to collect samples of LinkedIn profile URL)
        urls_10.txt  (sample file, contain 10 URLs for testing)
        urls_100.txt (sample file, contains 100 URLs for testing)
        urls_full_list.txt (All connection URLs extracted from LinkedIn-connections.htm )
    
    summarizer
        __init__.py
        entity.py (contains class: Person, to store profile data)
        parser.py (contains class: LIProfile Parser for html parsing)
        processor.py (contains class: TextProcessor for sentence extraction, tokenization and summarization implementaion)
        scraper.py (contains clas: LIScraper for scraping linkedin profile data from the web)
    
    temp 
        <contains programmatically generated file>
    
    main.py
        THIS IS THE MAIN PROGRAM
    
    README.md 
        Documentation


#### main.py
 This is the launcher program for the project, stored at the ROOT level


```bash
$ python main.py -h
usage: main.py [-h] [--tempdir TEMPDIR] [--url URL] [--file FILE]
               [--scrape SCRAPE]

optional arguments:
  -h, --help            show this help message and exit
  --tempdir TEMPDIR, -t TEMPDIR
                        Directory where temp and output files can be stored
  --url URL, -u URL     LinkedIn Profile URL to parse and summarize
  --file FILE, -f FILE  Input file with URLs for LinkedIn profile, one per
                        line
  --scrape SCRAPE, -s SCRAPE
                        Linked Network HTML file for downloading connections
                        URLs for an individual

```

### Sample Usage 

#### Parse and extract summary by passing a URL

```bash
[Sun Jan 19 16:56:08] deeptisharma@Course_Project $ python main.py -u https://www.linkedin.com/in/thisisdeepti/
Page has already been downloaded: https://www.linkedin.com/in/thisisdeepti/ Content: temp//0bf21e07bfe727c19450fc0f3c35be6d_bio.html
******************************************************
Full biography:
https://www.linkedin.com/in/thisisdeepti/
Deepti Sharma
About:
'Top 50 Tech Leaders' 2019 Award Winner InterCon Dubai. Passionate about engineering, innovation and solving business problems. Successfully built high-performing teams from ground up and led them to success. Traversed organizational journey from inception, early setup to post merger stage. Expertise in AdTech, MarTech, Big Data & ML Systems in Retail, Healthcare and Finance domains. Software Architecture - Distributed Systems - Predictive Analytics Platforms - Enterprise Applications - Engineering Innovation - Product Development (Ideation to Sunset) - Hiring - Operations Planning - Product Strategy - Growth Strategy - Startups
WorkExperience:
- Founder @ Quanvy ( Jun 2019 - Present, 7 months ) 
- Co-Founder @ BuzzinBows ( Feb 2019 - Sep 2019, 8 months ) 
- Director @ Visa ( Nov 2017 - Jan 2019, 1 year 3 months ) 
- Lead Software Engineer @ Visa ( Nov 2016 - Oct 2017, 1 year ) 
- Senior Staff Engineer @ Visa ( May 2015 - Oct 2016, 1 year 6 months ) 
- Solutions Architect @ KloudGin ( Sep 2014 - Mar 2015, 7 months ) 
- Big Data Architect @ InsightsOne (merged with Apigee, later acquired by Google) ( Apr 2012 - Aug 2014, 2 years 5 months ) 
- Software Development Engineer 2 @ Microsoft ( Oct 2010 - Mar 2012, 1 year 6 months ) 
- Technical Yahoo @ Yahoo! ( Nov 2009 - Oct 2010, 1 year ) 
- Technical Yahoo @ Yahoo! ( Jun 2005 - Nov 2009, 4 years 6 months ) 
- Intern @ i2 Technologies ( Jan 2005 - Jun 2005, 6 months ) 
Education:
- Birla Institute of Technology and Science , B.E (Hons.) Computer Science
Certificates:
- IBM Microservices Specialization @ Coursera
Awards:
- Top 50 Tech Leaders @ InterCon ( Oct 2019 ) 
- For Shipping a critical Bing component @ Microsoft ( 2011 ) 
- Karamveer Award - Ad Systems @ Yahoo! ( 2008 ) 
- U Rock Award - Going Above and Beyond @ Yahoo! ( 2006 ) 
Groups:
- IoT World Series
- Software & Technology Professionals: Managers | HR | Recruiters | Blockchain | Investors (BIG)
- Big Data, Analytics, IoT (Internet of Things) & Blockchain
- Cloud Computing
- Bing Microsoft
- Digital Marketing
- Yahoo Employees and Alumni Group
- Hadoop Users
- Marketing, Sales, Social Media, Advertising, PR, Digital & Technology Innovators by SOLUTIONSpeople
- Augmented Reality ▶️
- TDWI: Analytics and Data Management Discussion Group
- Harvard Business Review
- Yahoo Alums
- Design Thinking
******************************************************
Summary:
https://www.linkedin.com/in/thisisdeepti/
'Top 50 Tech Leaders' 2019 Award Winner InterCon Dubai
Passionate about engineering, innovation and solving business problems
Successfully built high-performing teams from ground up and led them to success
Traversed organizational journey from inception, early setup to post merger stage
******************************************************
$ 

```

#### Pass a list of URLs to parse and generate summary

Input file => urls_10.txt

#### urls_10.txt
This file contains 10 LinkedIn URLs to crawl

```text
https://www.linkedin.com/in/pranay-chauhan-b18a92b0/
https://www.linkedin.com/in/imran-khan-45964a199/
https://www.linkedin.com/in/aadish-jain-733615197/
https://www.linkedin.com/in/harsham/
https://www.linkedin.com/in/nath-masturkar/
https://www.linkedin.com/in/animesh-das-662b9b113/
https://www.linkedin.com/in/deanlindal/
https://www.linkedin.com/in/syed-hussain-56a2b2110/
https://www.linkedin.com/in/salila-khilani-b36b661/
https://www.linkedin.com/in/abdul%E2%9C%85-bari-015834ab/
```

Now let's run the command

```bash

$ python main.py -f data/urls_10.txt 
Page has already been downloaded: https://www.linkedin.com/in/pranay-chauhan-b18a92b0/ Content: temp//e43f058d2b3cad939db3860e3e1453a2_bio.html
Page has already been downloaded: https://www.linkedin.com/in/imran-khan-45964a199/ Content: temp//711b2e5e05df933dd7acbc508f655eae_bio.html
Page has already been downloaded: https://www.linkedin.com/in/aadish-jain-733615197/ Content: temp//f8711319c390378d9cb85afc9848af90_bio.html
Page has already been downloaded: https://www.linkedin.com/in/harsham/ Content: temp//0ac6422cf5bdb79711d73d24a0248e98_bio.html
Page has already been downloaded: https://www.linkedin.com/in/nath-masturkar/ Content: temp//9b0d6cf9062a70c63ee4696137024245_bio.html
Page has already been downloaded: https://www.linkedin.com/in/animesh-das-662b9b113/ Content: temp//cfa6eec32d81429d431e78896201a89a_bio.html
Page has already been downloaded: https://www.linkedin.com/in/deanlindal/ Content: temp//28baf73818e7a5910baa68620e48a610_bio.html
Page has already been downloaded: https://www.linkedin.com/in/syed-hussain-56a2b2110/ Content: temp//ca8d09368d98cff87b3b449aeedc6d22_bio.html
Page has already been downloaded: https://www.linkedin.com/in/salila-khilani-b36b661/ Content: temp//f4bb47bc8c878848fad5737139d96e8d_bio.html
Page has already been downloaded: https://www.linkedin.com/in/abdul%E2%9C%85-bari-015834ab/ Content: temp//e7b78e6ebbbf5d25174aa60ff637406e_bio.html
Generating summary for content in temp//e43f058d2b3cad939db3860e3e1453a2_bio_parsed.txt
Summary saved in file temp//e43f058d2b3cad939db3860e3e1453a2_bio_summary.txt Summarize size: 359 characters 
Generating summary for content in temp//711b2e5e05df933dd7acbc508f655eae_bio_parsed.txt
Summary saved in file temp//711b2e5e05df933dd7acbc508f655eae_bio_summary.txt Summarize size: 252 characters 
Generating summary for content in temp//f8711319c390378d9cb85afc9848af90_bio_parsed.txt
Summary saved in file temp//f8711319c390378d9cb85afc9848af90_bio_summary.txt Summarize size: 62 characters 
Generating summary for content in temp//0ac6422cf5bdb79711d73d24a0248e98_bio_parsed.txt
Summary saved in file temp//0ac6422cf5bdb79711d73d24a0248e98_bio_summary.txt Summarize size: 248 characters 
Generating summary for content in temp//9b0d6cf9062a70c63ee4696137024245_bio_parsed.txt
Summary saved in file temp//9b0d6cf9062a70c63ee4696137024245_bio_summary.txt Summarize size: 240 characters 
Generating summary for content in temp//cfa6eec32d81429d431e78896201a89a_bio_parsed.txt
Summary saved in file temp//cfa6eec32d81429d431e78896201a89a_bio_summary.txt Summarize size: 429 characters 
Generating summary for content in temp//28baf73818e7a5910baa68620e48a610_bio_parsed.txt
Summary saved in file temp//28baf73818e7a5910baa68620e48a610_bio_summary.txt Summarize size: 385 characters 
Generating summary for content in temp//ca8d09368d98cff87b3b449aeedc6d22_bio_parsed.txt
Summary saved in file temp//ca8d09368d98cff87b3b449aeedc6d22_bio_summary.txt Summarize size: 328 characters 
Generating summary for content in temp//f4bb47bc8c878848fad5737139d96e8d_bio_parsed.txt
Summary saved in file temp//f4bb47bc8c878848fad5737139d96e8d_bio_summary.txt Summarize size: 77 characters 
Generating summary for content in temp//e7b78e6ebbbf5d25174aa60ff637406e_bio_parsed.txt
Summary saved in file temp//e7b78e6ebbbf5d25174aa60ff637406e_bio_summary.txt Summarize size: 409 characters 
```

#### Execution Workflow


1. Check if the URL has already been crawled. First time visit, go to step2. Else skip to Step 5.
2. Use selenium web driver to launch the browser (Chrome) and extract the page source.

        Main class: summarize/scraper.py: LIScraper
3. Save this content into a temp_file.
        
        Filename convention: <TEMP_DIR>/<URL_MD5_HASH>_bio.html
4. Generate a Done file to mark that the URL has been crawled
    
        Done file: <TEMP_DIR>/<URL_MD5_HASH>_bio.done 
5. If the page has already been parsed, skip tho step 8
6. Parse the web page and generate a biography. 

        Main class: summarize/parser.py: LIProfileParser
7. Save the content to a file:

        Bio file: <TEMP_DIR>/<URL_MD5_HASH>_bio_parsed.txt
8. Repeat steps 2 to 7 for all URLs in the input file
9. Save generated files details to an Interim file 
        
        Interim file: temp/scraper_output.txt
10. Leveraging Interim file information, generate a summary of the Text for all listed files
        
        Main class: summarize/Processor.py : TextProcessor
11. Save the summary for future reference

        Summary File: <TEMP_DIR>/<URL_MD5_HASH>_bio_summary.txt
12. Repeat steps 10 and 11 for all parsed bio listed in the Interim File 

### Text Summarization Implementations Details

#### File: summarizer/processor.py Class: TextProcessor

We use metapy for text tokenization and stopwords removal

```python
    
    def __init__(self, top_n=5):
        self.document = metapy.index.Document()
        self.tokenizer = metapy.analyzers.ICUTokenizer(suppress_tags=True)
        self.tokenizer = metapy.analyzers.LengthFilter(self.tokenizer, min=2, max=30)
        self.tokenizer = metapy.analyzers.ListFilter(self.tokenizer, \
                                                "data/lemur-stopwords.txt",\
                                                metapy.analyzers.ListFilter.Type.Reject)
        self.top_N = top_n
```

First we split sentences from the overall text. This is a naive implementation of sentence splitter. Advance methods can be used to identify sentence boundary

```python
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
```
Then we generate tokens for each sentence. 
```python
    def tokenize(self, text):
        if (text is None or text == ''):
            return []

        self.document.content(text)
        self.tokenizer.set_content(self.document.content())

        tokens = [token for token in self.tokenizer]
        return tokens
```
While generating tokens for sentence, we also update word frequency table (frequency_map) in the calling function

```python
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
```
Once all sentences have been tokenized, we generate a score for each sentence using Word Matrix

    Sentence Score = Sum (freq of all tokens)/number_of_tokens
    
Code reference

```python
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
```

After scoring all the sentences, we calculate the average score. The sentences that score above the average value, will be shortlisted for summary. to keep the limit on length, a topN=5 default limit has been set for # sentences to be used for summary to keep it short.

Here is the main function for full text summarization implementation

```python
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
```

This is a simple Frequency Driven approach and there are many other techniques to achieve the same objectives such as Latent Semantic Approach, Bayesian Topic Models etc. 
