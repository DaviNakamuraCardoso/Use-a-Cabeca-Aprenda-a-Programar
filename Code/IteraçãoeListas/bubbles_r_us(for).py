
scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]
costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

numbers_of_scores = len(scores)
solution_numbers = list(range(numbers_of_scores))

def bubble_sort(scores,numbers):
    swapped = True

    while swapped == True:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] < scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

high_score = 0
for i in range(len(scores)):
    print('Bubble solution #' + str(i), scores[i])
    if scores[i] > high_score:
        high_score = scores[i]
    
print('Bubbles tests:', i + 1)
print('Highest bubble score:', high_score)

highest_bubbles = []
for i in range(len(scores)):
    if high_score == scores[i]:
        highest_bubbles.append(i)

print('Solutions with highest score: ', highest_bubbles)
cost = 100.0
most_effective = 0
for i in range(len(highest_bubbles)):
    index = highest_bubbles[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]
print('Most effective solution: ', most_effective, 'with a cost of', cost)    

        
bubble_sort(scores, solution_numbers)
print('Top solutions: ')
for i in range(len(scores)):
    print(str(i+1) + ')','Bubble solution #' + str(solution_numbers[i]), 'score:', scores[i])













