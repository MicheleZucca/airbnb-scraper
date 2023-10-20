import calendar
from datetime import datetime
import datetime
from dateutil.parser import parse
from datetime import date

import re

week_day = ['Monday',
            'Tueasday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']


def get_current_deta():
    return datetime.date.today()


def generate_month_calendar_from_data_input(current_year, current_month, day_check_in, day_check_out):
    calendar_generate = calendar.Calendar(calendar.firstweekday())

    check_in = []
    check_out = []
    for calendar_data in calendar_generate.itermonthdays4(year=current_year, month=current_month):

        year, month, number_day, name_day = calendar_data[0], calendar_data[1], calendar_data[2], week_day[
            calendar_data[3]]
        current_deta = (year, month, number_day, name_day)
        if current_deta[3] == day_check_in and current_deta[0] == current_year and current_deta[1] == current_month:
            check_in.append(current_deta)
        if current_deta[3] == day_check_out and current_deta[1] == current_month:
            check_out.append(current_deta)

        if len(check_in) == 0 and len(check_out) > 0:
            check_out.pop()

    return check_in, check_out


def customize_link(link, year_, check_in_day, check_out_day):

    links = []
    for i in range(1, 13):
        check_in_list, check_out_list = generate_month_calendar_from_data_input(year_, i, check_in_day, check_out_day)
        if len(check_in_list) > len(check_out_list):
            check_in_list.pop(len(check_in_list) - 1)
        # check_in_list[i][0] = str(check_in_list[i][0])

        for k, date in enumerate(zip(check_in_list, check_out_list)):
            # print(check_in_list[k], date[0])
            year = str(date[0][0])
            month = str(date[0][1]) if len(str(date[0][1])) == 2 else '0' + str(date[0][1])
            day = str(date[0][2]) if len(str(date[0][2])) == 2 else '0' + str(date[0][2])
            check_in_date = year + '-' + month + '-' + day
            tmp = parse(check_in_date).date()
            if get_current_deta() > tmp:
                break


            year = str(date[1][0])
            month = str(date[1][1]) if len(str(date[1][1])) == 2 else '0' + str(date[1][1])
            day = str(date[1][2]) if len(str(date[1][2])) == 2 else '0' + str(date[1][2])
            check_out_date = year + '-' + month + '-' + day

            pattern = r'\d{4}-\d{2}-\d{2}'
            new_link = re.sub(pattern, f'&checkin={check_in_date}&checkout={check_out_date}', link)
            links.append(new_link)

    return links
'''


if __name__ == '__main__':
    year = 2023
    check_in_day = 'Friday'
    check_out_day = 'Sunday'

    #print('Today is: ', get_current_deta())

    links = customize_link('link', year, check_in_day, check_out_day)
'''