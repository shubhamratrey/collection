import requests
from bs4 import BeautifulSoup


class Chhattisgarh10thBoardResult2021:

    def __init__(self, roll_number, debug=False):
        self.DEBUG = debug
        self.ROLL_NUMBER = roll_number
        self.BASE_URL = 'https://results.cg.nic.in/2021results/Res_X_Main_Show21.aspx'
        self.RESPONSE_TEXT = ''
        self.RESULT_DATA = {}
        self.BEAUTIFUL_SOUP = None
        if self.DEBUG:
            print()
            for i in self.__dict__:
                print(i, ':', self.__dict__[i])
            print("------")
        self.set_response_text()
        self.init_beautiful_soup()
        self.set_result_data()

    @property
    def payload(self):
        return {'ctl00$ContentPlaceHolder1$txt_roll_no': self.ROLL_NUMBER}

    def set_response_text(self):
        if not self.ROLL_NUMBER:
            if self.DEBUG:
                print("EMPTY ROLL_NUMBER")
        resp = requests.post(self.BASE_URL, data=self.payload)
        if resp.status_code == 200:
            self.RESPONSE_TEXT = resp.text

    def init_beautiful_soup(self):
        if not self.RESPONSE_TEXT:
            if self.DEBUG:
                print("EMPTY RESPONSE_TEXT")
        self.BEAUTIFUL_SOUP = BeautifulSoup(self.RESPONSE_TEXT, 'lxml')

    def result_lxml_table(self):
        try:
            return self.BEAUTIFUL_SOUP.find_all('form')[0].find_all('table')
        except IndexError:
            return None

    @property
    def is_debug(self):
        return self.DEBUG

    @property
    def roll_number(self):
        return self.ROLL_NUMBER

    @property
    def student_name(self):
        """
        Student's Name
        :return:
        """
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        return str(table[2].find_all('tr')[2].contents[1].text)

    @property
    def father_name(self):
        """
        Student Father's Name
        :return:
        """
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        return str(table[2].find_all('tr')[3].contents[1].text)

    @property
    def mother_name(self):
        """
        Student Mother's Name
        :return:
        """
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        return str(table[2].find_all('tr')[4].contents[1].text)

    @property
    def school_code(self):
        """
        Student School Code
        :return:
        """
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        return int(table[2].find_all('tr')[5].contents[1].text)

    @property
    def center_code(self):
        """
        Student Center code
        :return:
        """
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        return int(table[2].find_all('tr')[6].contents[1].text)

    @property
    def result(self):
        """
        Student result
        :return: Dict
        """
        if not self.RESULT_DATA:
            if self.DEBUG:
                print("EMPTY RESULT_DATA")
        return self.RESULT_DATA

    @property
    def science_result(self):
        """
        Student's Science Result
        :return:
        """
        return self.result.get('SCIENCE')

    @property
    def english_result(self):
        """
        Student's English Result
        :return:
        """
        return self.result.get('ENGLISH')

    @property
    def hindi_result(self):
        """
        Student's Hindi Result
        :return:
        """
        return self.result.get('HINDI')

    @property
    def mathematics_result(self):
        """
        Student's Mathematics Result
        :return:
        """
        return self.result.get('MATHEMATICS')

    @property
    def information_technology_result(self):
        """
        Student's Information Technology Result
        :return:
        """
        return self.result.get('INFORMATION_TECHNOLOGY')

    @property
    def social_science_result(self):
        """
        Student's Social Science Result
        :return:
        """
        return self.result.get('SOCIAL_SCIENCE')

    @property
    def grand_total(self):
        """
        Student's GRAND_TOTAL
        :return:
        """
        return self.result.get('GRAND_TOTAL')

    @property
    def division(self):
        """
        Student's DIVISION
        :return:
        """
        return self.result.get('DIVISION')

    def get_sub_doc(self, theory, practical, other_activity, total, remarks):
        return {
            'THEORY': theory,
            'PRACTICAL': practical,
            'OTHER_ACTIVITY': other_activity,
            'TOTAL': total,
            'REMARKS': remarks
        }

    def valid_subjects(self):
        return {
            'SCIENCE': 'SCIENCE',
            'ENGLISH  (GENERAL)': 'ENGLISH',
            'HINDI    (SPECIAL)': 'HINDI',
            'MATHEMATICS': 'MATHEMATICS',
            'INFORMATION TECHNOLOGY': 'INFORMATION_TECHNOLOGY',
            'SOCIAL SCIENCE': 'SOCIAL_SCIENCE'
        }

    def set_result_data(self):
        table = self.result_lxml_table()
        if not table:
            if self.DEBUG:
                print("EMPTY TABLE")
        subject_data, grand_total, division = dict(), 0, ''
        for item in table[3].find_all('tr'):
            if item.contents[0].text in self.valid_subjects().keys():
                subject_name = str(item.contents[0].text)
                theory_marks = int(item.contents[1].text)
                practical_marks = int(item.contents[2].text)
                other_activity = str(item.contents[3].text)
                total_marks = int(item.contents[4].text)
                remarks = str(item.contents[5].text)

                subject_data[self.valid_subjects().get(subject_name)] = self.get_sub_doc(theory=theory_marks,
                                                                                         practical=practical_marks,
                                                                                         other_activity=other_activity,
                                                                                         total=total_marks,
                                                                                         remarks=remarks)
            elif item.contents[0].text == 'GRAND TOTAL':
                grand_total = item.contents[4].text
            elif item.contents[0].text == 'RESULT':
                division = item.contents[1].text
        data = {'ROLL_NUMBER': self.ROLL_NUMBER,
                'STUDENT_NAME': self.student_name,
                'FATHERS_NAME': self.father_name,
                'MOTHERS_NAME': self.mother_name,
                'CENTER_CODE': self.center_code,
                'SCHOOL_CODE': self.school_code,
                'SCIENCE': subject_data.get('SCIENCE', {}),
                'ENGLISH': subject_data.get('ENGLISH', {}),
                'HINDI': subject_data.get('HINDI', {}),
                'MATHEMATICS': subject_data.get('MATHEMATICS', {}),
                'INFORMATION_TECHNOLOGY': subject_data.get('INFORMATION_TECHNOLOGY', {}),
                'SOCIAL_SCIENCE': subject_data.get('SOCIAL_SCIENCE', {}),
                'GRAND_TOTAL': grand_total,
                'DIVISION': division}

        self.RESULT_DATA = data
