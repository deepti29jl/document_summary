from summarizer.processor import TextProcessor
from summarizer.scraper import LIScraper
import argparse
import codecs
import os

class BulkProcessor:

    def process(self, input_file, working_dir):
        if (not (os.path.exists(input_file) and os.path.isfile(input_file))):
            print("File: " + input_file + " does not exist!")
            return
        if (os.path.getsize(input_file) == 0):
            print("File is empty!")
            return

        scraped_output_file = working_dir + "/scraper_output.txt"

        li_scraper = LIScraper()
        li_scraper.scrape_profiles(input_file, working_dir, scraped_output_file)

        in_fh = codecs.open(scraped_output_file, 'r', encoding='utf8')
        data = in_fh.readlines()
        in_fh.close()

        valid_inputs = {}
        text_proc = TextProcessor(top_n=7)

        for line in data:

            (url, prefix, data_file) = line.replace('\n','').split('\t')

            if(os.path.exists(data_file) and os.path.isfile(data_file)):
                size = os.path.getsize(data_file)
                if (size > 0):
                    valid_inputs[data_file] = {'url': url,'prefix': prefix}
                else:
                    print(data_file + " is blank!")
            else:
                print(data_file + " does not exist!")

        for (data_file, tuple) in valid_inputs.items():

            print("Generating summary for content in " + data_file)
            summary_file = working_dir + '/' + tuple['prefix'] + 'bio_summary.txt'

            fh = codecs.open(data_file, 'r', encoding='utf8')
            text_data = fh.read()
            fh.close()

            summary = text_proc.summarize(text_data)
            #print(summary)

            out_fh = codecs.open(summary_file, 'w', encoding='utf8')
            out_fh.write(summary)
            out_fh.close()

            print("Summary saved in file " + summary_file + " Summary size: " + str(len(summary)) + " characters ")


if __name__ == '__main__':

    working_dir ='temp/'
    html_file = 'data/LinkedIn-Connections.htm'
    urls_file = 'data/urls_10.txt'

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--tempdir", "-t", help="Directory where temp and output files can be stored")
    arg_parser.add_argument("--url", "-u", help="LinkedIn Profile URL to parse and summarize")
    arg_parser.add_argument("--file", "-f", help="Input file with URLs for LinkedIn profile, one per line")
    arg_parser.add_argument("--scrape", "-s", help="Linked Network HTML file for downloading connections URLs for an individual")

    # read arguments from the command line
    args = arg_parser.parse_args()

    if(args.tempdir):
        working_dir = args.tempdir
        if(not os.path.exists(working_dir)):
            print("Path " + working_dir + " does not exist!")
            exit(1)
        if(not os.path.isdir(working_dir)):
            print("Path " + working_dir + " is not a valid directory")
            exit(2)

    if(args.file):
        connections_file = args.file
        proc = BulkProcessor()
        proc.process(connections_file, working_dir)

    if(args.url):
        url = args.url
        li_scraper = LIScraper()
        bio = li_scraper.scrape_profile(url, working_dir)

        if (bio is None):
            print("Could not retrieve Bio for url " + url)
            exit(10)

        print("******************************************************")
        print("Full biography:\n" + bio)

        proc = TextProcessor()
        summary = proc.summarize(bio)

        if (summary is None):
            print("Could not extract summary from the text!!!")
            exit(20)

        print("******************************************************")
        print("Summary:\n" + summary)
        print("******************************************************")

    if(args.scrape):
        html_file = args.scrape
        urls_file = working_dir + "/urls.txt"
        li_scraper = LIScraper()
        li_scraper.scrape_connection_urls(html_file, urls_file)

