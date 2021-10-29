// 출처 : https://www.acmicpc.net/problem/14502
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

const getCombinations = function (arr, selectNumber) {
    const results = [];

    if (selectNumber === 1) return arr.map((value) => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    })

    return results;
}


function solution(input) {
    const n = input[0].split(' ')[0]
    const m = input[0].split(' ')[1]
    let answers = []
    let answer = 0;
    let graph = []
    for (let i = 1; i < input.length; i++) {
        let l = input[i].split(' ')
        for (let j = 0; j < l.length; j++) {
            l[j] = parseInt(l[j]);
        }
        graph.push(l)
    }
    const arr = []
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (graph[i][j] == 0) {
                arr.push([i, j])
            }
        }
    }
    const combArr = getCombinations(arr, 3)

    // 모든 조합에 대해 전염병 돌리기
    for (let i = 0; i < combArr.length; i++) {
        let combi = combArr[i];
        let copyGraph = JSON.parse(JSON.stringify(graph))

        // 벽세움
        for (let j = 0; j < combi.length; j++) {
            // console.log(combi[j])
            copyGraph[combi[j][0]][combi[j][1]] = 1
        }
        // 
        let queue = []
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (copyGraph[i][j] == 2) {
                    queue.push([i, j])
                }
            }
        }
        // console.log("!!");
        // console.log(copyGraph);
        // console.log(queue);
        let moves = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (queue.length > 0) {
            position = queue.shift();
            // console.log(position)
            x = position[0];
            y = position[1];
            copyGraph[x][y] = 2
            moves.forEach(move => {
                if (x + move[0] >= 0 && x + move[0] < n && y + move[1] >= 0 && y + move[1] < m && copyGraph[x + move[0]][y + move[1]] == 0) {
                    copyGraph[x + move[0]][y + move[1]] = 2;
                    queue.push([x + move[0], y + move[1]]);
                }
            });
        }

        // console.log(graph)
        // console.log(copyGraph)
        // 0개수 세기
        let count = 0;
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (copyGraph[i][j] == 0) {
                    count++;
                }
            }
        }
        // answers.push(count)
        answer = Math.max(count, answer)
    }


    console.log(answer)
}