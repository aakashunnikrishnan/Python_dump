if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_scores = sorted(set(arr), reverse=True)

    print(unique_scores[1] if len(unique_scores) > 1 else unique_scores[0])
