#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

##def read_data(filename):
##    rows = read_csv(filename)
##    data = ()
##    age_title = ()
##    rep_title = ()
##    for rep in rows[0][1:5]:
##        rep_title += (int(rep),)
####    print(rep_title)
##    for row in rows[1:5]:
##        age_title += (int(row[0]),)
##        data += (row[1:],)
####    print(age_title)
####    print(data)
##    return create_table(data, age_title, rep_title)


def read_data(filename):
    rows = read_csv(filename)
    data = ()
    age_title = ()
    rep_title = ()
    for rep in rows[0][1:]:
        rep_title += (int(rep),)
    for row in rows[1:]:
        age_title += (int(row[0]),)
        filler = ()
        for num in row[1:]:
            filler += (int(num),)
        data += (filler,)
##    print(data)
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# print("## Q1 ##")
### Sit-up score of a 24-year-old who did 10 sit-ups.
##print(type(access_cell(situp_table, 24, 10)) )   # 0
##
### Push-up score of a 18-year-old who did 30 push-ups.
##print(access_cell(pushup_table, 18, 30))   # 16
##
### Run score of a 30-year old-who ran 12 minutes (720 seconds)
##print(access_cell(run_table, 30, 720))     # 36
##
### Since our run.csv file does not have data for 725 seconds, we should
### get None if we try to access that cell.
##print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    if pushup > 60:
        pushup = 60
    if pushup < 1:
        return 0
    return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    if situp >60:
        situp = 60
    if situp < 1:
        return 0
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run < 510:
        run = 510
    elif run >1100:
        run = 1100
    elif run % 10 != 0:
        run = run + 10 -(run % 10)
    return access_cell(run_table, age, run)

# print("## Q2 ##")
##print(pushup_score(pushup_table, 18, 61))   # 25
##print(pushup_score(pushup_table, 18, 70))   # 25
##print(situp_score(situp_table, 24, 0))      # 0
##
##print(run_score(run_table, 30, 720))        # 36
##print(run_score(run_table, 30, 725))        # 35
##print(run_score(run_table, 30, 735))        # 35
##print(run_score(run_table, 30, 500))        # 50
##print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
##    print(score)
    if score < 51:
        return "F"
    elif score <= 60:
        return "P"
    elif score <= 74:
        return "P$"
    elif score <= 84:
        return "S"
    elif score >= 85:
        return "G"

# print("## Q3 ##")
##print(ippt_award(50))     # F
##print(ippt_award(51))     # P
##print(ippt_award(61))     # P$
##print(ippt_award(75))     # S
##print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_table = get_pushup_table(ippt_table)
    p_score = pushup_score(pushup_table, age, pushup)
    situp_table = get_situp_table(ippt_table)
    s_score = situp_score(situp_table, age, situp)
    run_table = get_run_table(ippt_table)
    r_score = run_score(run_table, age, run)
    total = p_score + s_score + r_score
    award = ippt_award(total)
    return (total, award)

# print("## Q4 ##")
##print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
##print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
##print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
##print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
##print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        rate_p = rate_pushup
        rate_s = rate_situp
        rate_r = rate_run
        final_pushup = days//rate_p + pushup
        final_situp = days//rate_s + situp
        final_run = run - days//rate_r
        result = ippt_results(ippt_table, age, final_pushup, final_situp, final_run)
        return (final_pushup, final_situp, final_run, result)

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
##print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        rate_p = rate_pushup
        rate_s = rate_situp
        rate_r = rate_run
        
        c_pushup = pushup
        c_situp = situp
        c_run = run
        new_pushup = pushup
        new_situp = situp
        new_run = run
        
        current_score = ippt_results(ippt_table, age, pushup, situp, run)
        pushup_table = get_pushup_table(ippt_table)
        p_score = pushup_score(pushup_table, age, pushup)
        situp_table = get_situp_table(ippt_table)
        s_score = situp_score(situp_table, age, situp)
        run_table = get_run_table(ippt_table)
        r_score = run_score(run_table, age, run)
        while days > 0:
            while pushup_score(pushup_table, age, new_pushup) == p_score:
                new_pushup += 1
            change_pushup = new_pushup - c_pushup
            days_p = change_pushup * rate_p
            
            while situp_score(situp_table, age, new_situp) == s_score:
                new_situp += 1
            change_situp = new_situp - c_situp
            days_s = change_situp * rate_s
            
            while run_score(run_table, age, new_run) == r_score:
                new_run += 1
            change_run = new_run - c_run
            days_r = change_run * rate_r

            next_point = min(days_p,days_s,days_r)
            print(days_p,days_s,days_r)
            print(next_point)
            if next_point > days:
                break
            elif next_point == days_p:
                c_pushup = new_pushup
                p_score = pushup_score(pushup_table, age, new_pushup)
            elif next_point == days_s:
                c_situp = new_situp
                s_score = situp_score(situp_table, age, new_situp)
            elif next_point == days_r:
                c_run = new_run
                r_score = run_score(run_table, age, new_run)
            days -= next_point
            print(days)
        print(days)
        
        result = ippt_results(ippt_table, age, c_pushup, c_situp, c_run)
        return (c_pushup, c_situp, c_run, result)


    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

##print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
##print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))


tp_bonus = make_tp_bonus(999999,8,9) 
print(tp_bonus(ippt_table, 18, 1, 55, 941, 10))
