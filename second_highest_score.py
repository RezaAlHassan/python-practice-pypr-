
# Online Python - IDE, Editor, Compiler, Interpreter

if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10 :
        arr = map(int, input().split())
        # Convert the map object to a list
        scores_list = list(arr)
        # Remove duplicates by converting the list to a set and then back to a list
        unique_scores = list(set(scores_list))
        # Sort the unique scores in descending order
        unique_scores.sort(reverse=True)
        runner_up_score = unique_scores[1]  # The runner-up score is the second element
        print(runner_up_score)