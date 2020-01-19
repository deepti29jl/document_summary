##################
# Person Data
##################
class Person:
    bio = None
    summary = ''
    name = ''
    url = ''
    about = ''
    experiences = []
    education = []
    certificates = []
    awards = []
    groups = []

    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_url(self, url):
        self.url = url

    def set_about(self, about):
        self.about = about

    def set_experiences(self, experiences):
        self.experiences = experiences

    def add_experience(self, experience):
        self.experiences.append(experience)

    def set_education(self, education):
        self.education = education

    def add_education(self, education):
        self.education.append(education)

    def set_certificates(self, certs):
        self.certificates = certs

    def add_certificate(self, cert):
        self.certificates.append(cert)

    def set_awards(self, awards):
        self.awards = awards

    def add_award(self, award):
        self.awards.append(award)

    def set_groups(self, groups):
        self.groups = groups

    def add_group(self, group):
        self.groups.append(group)

    def set_bio(self, bio):
        self.bio = bio

    def get_bio(self):
        if(self.bio is None):
            self.create_bio()

        return self.bio

    def set_summary(self, summary):
        self.summary = summary

    def get_summary(self):
        return self.summary

    def create_bio(self):
        self.bio = self.url
        self.bio += "\n" + self.name
        self.bio += '\nAbout:\n' + self.about
        self.bio += '\nWorkExperience:'

        index = 1

        for exp in self.experiences:
            self.bio += '\n- ' + exp
            index += 1
        self.bio += '\nEducation:'
        index = 1
        for edu in self.education:
            self.bio += '\n- ' + edu
            index += 1
        self.bio += '\nCertificates:'
        index = 1
        for cert in self.certificates:
            self.bio += '\n- ' + cert
            index += 1
        self.bio += '\nAwards:'
        index = 1
        for award in self.awards:
            self.bio += '\n- ' + award
            index += 1
        self.bio += '\nGroups:'
        index = 1
        for grp in self.groups:
            self.bio += '\n- ' + grp
            index += 1
