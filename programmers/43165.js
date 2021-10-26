function solution(numbers, target) {
    var answer = 0;

    function dfs(level, sum) {
        if (level == numbers.length) {
            if (sum == target) {
                answer++;
            }
            return
        }

        dfs(level + 1, sum + numbers[level]);
        dfs(level + 1, sum - numbers[level]);

    }

    dfs(0, 0);
    return answer;
}

solution([1, 1, 1, 1, 1], 3)