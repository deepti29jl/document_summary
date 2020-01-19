import codecs
import hashlib
import os
import time
from summarizer.parser import LIProfileParser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_filename_prefix(url):
    hash_object = hashlib.md5(url.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig + "_"

#######################
# LinkedIn Scraper
#######################
class LIScraper:

    driver = None
    parser = None

    def __init__(self):
        self.parser = LIProfileParser()

    def download(self, url, filename):
        if (self.driver == None):
            self.driver = webdriver.Chrome()

        self.driver.get(url)
        timeout = 3
        loaded = False
        try:
            self.driver.find_element_by_class_name("education")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "education")))
            loaded = True
        except:
            print("Exception occurred while loading page!")
            loaded = False
        finally:
            if(loaded == True):
                print("Page loaded")
            else:
                print("Cannot download webpage!")
                return None

        content = self.driver.page_source

        with codecs.open(filename, 'w', encoding='utf8') as new_file:
            # Parse the content
            soup = BeautifulSoup(content, 'html.parser')

            # Ensure response is valid html
            data = soup.prettify()

            new_file.write(data)
            new_file.close()

        return new_file

    def scrape_connection_urls(self, in_filename, out_filename):
        in_file = codecs.open(in_filename, 'r', encoding='utf8')
        content = str(in_file.read())
        in_file.close()

        # Parse the content
        soup = BeautifulSoup(content, 'html.parser')
        tag = 'mn-connection-card__picture'

        connections = soup.find_all('a',{'class':tag})
        #print(str(len(connections)))

        out_file = codecs.open(out_filename, 'w', encoding='utf8')
        url_count = 0
        for conn in connections:
            url = conn.attrs['href']
            line = url + '\n'
            out_file.write(line)
            url_count += 1

        out_file.close()
        print("Collected " + str(url_count) + " URLs from the page. Output file: " + out_filename)


    def scrape_profile(self, url, output_path):

        prefix = get_filename_prefix(url)
        data_file_path = output_path + "/" + prefix + "bio.html"
        done_file_path = output_path + "/" + prefix + "bio.done"

        if (os.path.exists(data_file_path) and os.path.exists(done_file_path)):
            print("Page has already been downloaded: " + url + " Content: " + data_file_path)
        else:
            print("Downloading web page: " + url + " Content: " + data_file_path)
            return_value = self.download(url, data_file_path)
            if (return_value is None):
                return None

            open(done_file_path, 'a').close()
            time.sleep(10)

        in_file = codecs.open(data_file_path, 'r', encoding='utf8')
        content = str(in_file.read())
        in_file.close()

        bio = self.parser.scrape_profile(content, url)

        return bio

    def scrape_profiles(self, url_input_file, temp_path, bio_output_file):
        in_file = codecs.open(url_input_file, 'r', encoding='utf8')
        data = in_file.readlines()
        in_file.close()

        output_list_file = codecs.open(bio_output_file, 'w', encoding='utf8')

        for line in data:
            url = line.replace('\n','').strip()
            prefix = get_filename_prefix(url)
            out_file_path = temp_path + "/" + prefix + "bio_parsed.txt"

            bio = self.scrape_profile(url, temp_path)

            if (bio is None):
                print("Could not get Bio for url: " + url + " Skipping...")
                continue

            out_file = codecs.open(out_file_path, 'w', encoding='utf8')
            out_file.write(bio)
            out_file.close()

            output_list_file.write(url + '\t' + prefix + '\t' + out_file_path + "\n")

        output_list_file.close()

    def close(self):
        if (self.driver != None):
            self.driver.close()

