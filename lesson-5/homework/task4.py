def enrolment_stats(univer_stats):
    student_num = []
    student_tutions = []
    for x in univer_stats:
        student_num.append(x[1])
        student_tutions.append(x[2])
    return student_num, student_tutions

def mean(stats_mean):
    student_mean = round((sum(stats_mean)/len(stats_mean)), 2)
    return student_mean

def median(stats_median):
    if len(stats_median)%2 == 0:
        student_median = (stats_median[len(stats_median)/2] + stats_median[len(stats_median/2 +1)])/2
    else:
        student_median = stats_median[len(stats_median)//2+1]
    return student_median

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

statistics = enrolment_stats(universities)
num_students = statistics[0]
tutions_students = statistics[1]
mean_num = mean(num_students)
mean_tutions = mean(tutions_students)
median_num = median(num_students)
median_tutions = median(tutions_students)
print(f"    Total students: {sum(num_students)} \n\
    Total tuition: $ {sum(tutions_students)} \n\n\
    Student mean: {mean_num} \n\
    Student median: {median_num} \n\n\
    Tution mean: $ {mean_tutions} \n\
    Tution median: $ {median_tutions}")

# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849