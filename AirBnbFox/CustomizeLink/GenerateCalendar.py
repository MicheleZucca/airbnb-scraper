import calendar
import datetime

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

        year, month, number_day, name_day = calendar_data[0], calendar_data[1], calendar_data[2], week_day[calendar_data[3]]
        current_deta = (year, month, number_day, name_day)
        if current_deta[3] == day_check_in and current_deta[0] == current_year and current_deta[1] == current_month:
            check_in.append(current_deta)
        if current_deta[3] == day_check_out and current_deta[1] == current_month:
            check_out.append(current_deta)

        if len(check_in) == 0 and len(check_out) > 0:
            check_out.pop()
            '''
        if len(check_in) > len(check_out) and len(check_out) != 0:
            check_in.pop(len(check_in) - 1)
            '''

    return check_in, check_out

if __name__ == '__main__':

    year = 2023
    check_in_day = 'Friday'
    check_out_day = 'Sunday'


    print('Today is: ', get_current_deta())

    #clear list
    for i in range(1, 13):

        checkin, checkout = generate_month_calendar_from_data_input(2023, i, check_in_day, check_out_day)

        if len(checkin) > len(checkout):
            checkin.pop(len(checkin)-1)
            
        print(checkin)
        print(checkout)



