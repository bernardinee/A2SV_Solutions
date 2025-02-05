if __name__ == '__main__':
   scores = []
   students = []
   for _ in range(int(input())):
       name = input()
       score = float(input())
       students.append([name, score])
       scores.append(score)
   
   second_lowest = sorted(set(scores))[1]
   names = sorted(name for name, score in students if score == second_lowest)
   
   for name in names:
       print(name)