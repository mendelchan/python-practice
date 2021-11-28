URL: https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one


def breakingRecords(scores):
    
    num_min = scores[0]
    num_max = scores[0]
    
    count_min = 0 
    count_max = 0 
    
    for score in scores:
        if score > num_max:
            count_max += 1
            num_max = score 
             
        if score < num_min:
            count_min += 1 
            num_min = score 
    
    return [count_max, count_min]


# Call the function on test cases 
a = [1, 2, 3, 4, 5]
b = [10, 24, 24, 10, 9, 25]
c = [13, 20, 9, 25, 34, 55]

print(breakingRecords(a))
print(breakingRecords(b))
print(breakingRecords(c))