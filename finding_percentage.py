# count = int(input("enter the number of students : "))
# res=dict{}
# marks = []
# for i in range(count):
#     name = input()
#     marks1 = float(input())
#     marks2 = float(input())
#     marks3 = float(input())   
#     print(name,marks1,marks2,marks3)

if __name__ == '__main__':
    n = int(input(""))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("")
    marks = student_marks[query_name]
    print(format(sum(marks)/3,'.2f'))