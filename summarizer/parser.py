import re
from summarizer.entity import Person
from bs4 import BeautifulSoup

#######################
# LinkedIn Profile Parser
#######################
class LIProfileParser:

    def __init__(self):
        pass

    def is_valid_tag(self, element):
        return ('bs4.element.Tag' in str(type(element)))

    def clean_text(self, text):
        #print('Before: \"' + text + '\"')
        cleaned_text = text.strip().replace('\n','').replace('\r','').replace('\t',' ').replace('  ', ' ')
        cleaned_text = re.sub(r'( )+',' ', cleaned_text)
        #print('After: \"' + cleaned_text + '\"')
        return cleaned_text

    def extract_title_subtitle_daterange(self, element, joinkey='@', rangefiller=' - Present'):

        list = element.find_all('h3', {'class': 'result-card__title'})
        list2 = element.find_all('h4', {'class': 'result-card__subtitle'})
        list3 = element.find_all('span', {'class': 'date-range'})

        output = []
        if (len(list) == len(list2)):
            index = 0
            for el in list:
                el_details = self.clean_text(el.text)
                el_details += ' ' + joinkey+' ' + self.clean_text(list2[index].text)

                if (len(list3) == len(list2)):
                    time = list3[index].find_all('time')
                    duration = list3[index].find('span')
                    time_range = None
                    if(len(time) == 1):
                        time_range = self.clean_text(time[0].text) + rangefiller
                    else:
                        for t in time:
                            if (time_range is None):
                                time_range = self.clean_text(t.text)
                            else:
                                time_range += ' - ' + self.clean_text(t.text)

                    el_details += ' ( ' + time_range
                    if (duration is not None):
                        el_details += ', ' + self.clean_text(duration.text)

                    el_details += ' ) '
                index += 1

                output.append(el_details)

        return output

    def scrape_profile(self, content, url):

        # Parse the content
        soup = BeautifulSoup(content, 'html.parser')

        title = soup.find('title')
        about = soup.find('section', {'class': 'summary'})
        exp = soup.find('section', {'class': 'experience'})
        edu = soup.find('ul', {'class': 'education__list'})
        certs = soup.find('section',{'class':'certifications'})
        awards = soup.find('section', {'class': 'awards'})
        groups = soup.find('section', {'class': 'groups'})

        person = Person()
        person.set_url(url)

        if (title != None):
            name = title.text.split('-')[0].strip()
            #print(name)
            person.set_name(self.clean_text(name))

        if(about != None and about.p != None):
            person.set_about(self.clean_text(about.p.text))

        if(exp != None):
        #    print('experience: ')
            exp_details = self.extract_title_subtitle_daterange(exp, '@')
            person.set_experiences(exp_details)

        if (edu != None):
        #    print('education: ')
            edu_details = self.extract_title_subtitle_daterange(edu,',')
            person.set_education(edu_details)

        if(certs != None):
        #    print('certifications: ')
            cert_details = self.extract_title_subtitle_daterange(certs)
            person.set_certificates(cert_details)

        if(awards != None):
        #    print('awards: ')
            awards_details = self.extract_title_subtitle_daterange(awards,rangefiller='')
            person.set_awards(awards_details)

        if(groups != None):
        #    print('groups: ')
            grp_list = groups.find_all('h3',{'class':'result-card__title'})
            g_list = []
            for item in grp_list:
                g_list.append(self.clean_text(item.text))
            person.set_groups(g_list)

    #    print(person.get_bio())

        return person.get_bio()

