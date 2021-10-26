
function solution(n, computers) {
    let answer = 0;
    let visit = []

    for (let i = 0; i < n; i++) {
        visit.push(0)
    }

    for (let i = 0; i < n; i++) {
        if (visit[i] == 0) {
            dfs(i);
            answer += 1
        }
    }
    function dfs(x) {
        visit[x] = 1;
        for (let i = 0; i < n; i++) {
            if (computers[x][i] == 1 && visit[i] == 0) {
                dfs(i);
            }
        }
    }

    // console.log(answer);
    return answer;
}

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])