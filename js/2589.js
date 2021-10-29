// 출처 : https://www.acmicpc.net/problem/2589
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on("line", function (line) {
    input.push(line)
}).on("close", function () {
    solution(input);
    process.exit();
});

function solution(inputs) {
    let n = parseInt(inputs[0].split(' ')[0])
    let m = parseInt(inputs[0].split(' ')[1])

    let graph = [];
    for (let i = 1; i < n + 1; i++) {
        graph.push(inputs[i].split(''));
    }
    let answer = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (graph[i][j] == 'L') {
                answer.push(bfs([i, j]));
            }
        }
    }

    console.log(Math.max(...answer));
    function bfs(start) {
        let queue = [start];
        let visit = [];
        let costs = [0];
        let moves = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        let maxCount = -1;
        for (let i = 0; i < n; i++) {
            let line = [];
            for (let j = 0; j < m; j++) {
                line.push(0);
            }
            visit.push(line);
        }
        visit[start[0]][start[1]] = 1;

        while (queue.length > 0) {
            let position = queue.shift();
            let cost = costs.shift();

            let x = position[0];
            let y = position[1];
            maxCount = Math.max(cost, maxCount)
            moves.forEach(move => {
                if (x + move[0] >= 0 && x + move[0] < n && y + move[1] >= 0 && y + move[1] < m && graph[x + move[0]][y + move[1]] == 'L' && visit[x + move[0]][y + move[1]] == 0) {
                    queue.push([x + move[0], y + move[1]]);
                    costs.push(cost + 1);
                    visit[x + move[0]][y + move[1]] = 1;
                }
            })

        }

        return maxCount;
    }
}