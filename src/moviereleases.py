import json
import datetime

import requests

apikey = "c1b8c43af9af6b592db8570437bf2e70"


class MovieReleases:
    def __init__(self, url):
        self.url = url

    def load(self):
        print "loading data..."

        resp = requests.get(self.real_url())
        if resp.status_code != 200:
            jsonBody = resp.json()
            message = jsonBody['status_message']
            print "loading data failed: [%s]" % message
            return "{ 'error': '%s'}" % message
        else:
            print "data loaded."
            datajson = """{ "data": %s }""" % resp.content
            return json.loads(datajson)

    def real_url(self):
        return self.url.replace("{API_KEY}", apikey)

    def fillDates(self, url_template, end_date):
        week = datetime.timedelta(days=7)
        lower_date = end_date - week

        return url_template \
            .replace("{LOWER_DATE}", lower_date.strftime("%Y-%m-%d")) \
            .replace("{UPPER_DATE}", end_date.strftime("%Y-%m-%d"))

    def lastWeeksReleases(self):
        today = datetime.datetime.today()
        searchUrl = self.fillDates(self.real_url(), today)

        data = requests.get(searchUrl).json()

        json_str = self.json_titles(data['results'])
        return json.loads(json_str)

    def json_titles(self, results):
        return_val = """{ "docs": ["""

        first = True
        for result in results:
            if "en" != result['original_language']:
                continue

            if not first:
                return_val += ","
            first = False

            title = result['original_title']
            return_val += """ { "title": "%s" }""" % title

        return_val += " ] }"
        return return_val

    def createEmail(self, data):
        email_body = "New movie releases:\n"
        for doc in data['docs']:
            email_body += "\t- %s\n" % doc['title']

        email_body += "\nYour Movie release check!"
        return MovieReleaseMail(email_body)


class MovieReleaseMail:
    def __init__(self, email_content):
        self.subject = "Movie releases"
        self.content = email_content
