// 출처 : https://www.acmicpc.net/problem/2206
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// visit에 해당 좌표에 방문했을 때의 부순 벽의 개수를 기록
const input = [];
rl.on("line", function (line) {
    input.push(line)
}).on("close", function () {
    solution(input);
    process.exit();
});

function solution(inputs) {
    const n = inputs[0].split(' ')[0]
    const m = inputs[0].split(' ')[1]
    let graph = []
    let answer = -1;
    for (let i = 0; i < n; i++) {
        let arr = inputs[i + 1].split('')

        graph.push(arr)
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            graph[i][j] = parseInt(graph[i][j]);
        }
    }

    let queue = [[0, 0]]
    let counts = [1];
    let breakWalls = [0];
    let visit = [];
    for (let i = 0; i < n; i++) {
        line = []
        for (let i = 0; i < m; i++) {
            line.push(99999);
        }
        visit.push(line);
    }

    visit[0][0] = 1
    let moves = [[-1, 0], [0, -1], [1, 0], [0, 1]];
    while (queue.length > 0) {
        let position = queue.shift();
        let count = counts.shift();
        let breakWall = breakWalls.shift();
        let curX = position[0];
        let curY = position[1];
        // console.log(curX + ',' + curY);
        if (curX == n - 1 && curY == m - 1) {
            answer = count;
            break
        }
        moves.forEach(move => {
            if (curX + move[0] >= 0 && curX + move[0] < n && curY + move[1] >= 0 && curY + move[1] < m && visit[curX + move[0]][curY + move[1]] > breakWall) {
                // 벽을 부수어야 하는 경우
                if (graph[curX + move[0]][curY + move[1]] == 1) {
                    // 이미 하나 부순 경우는 스킵하고
                    if (breakWall == 0) {
                        visit[curX + move[0]][curY + move[1]] = breakWall;
                        queue.push([curX + move[0], curY + move[1]]);
                        counts.push(count + 1);
                        breakWalls.push(breakWall + 1);
                    }
                }
                // 그냥 빈칸
                else {
                    visit[curX + move[0]][curY + move[1]] = breakWall;
                    queue.push([curX + move[0], curY + move[1]]);
                    counts.push(count + 1);
                    breakWalls.push(breakWall);
                }
            }
        })
    }

    console.log(answer);
}