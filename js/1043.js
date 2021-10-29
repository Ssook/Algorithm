// 출처 : https://www.acmicpc.net/problem/1043
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
    const n = parseInt(inputs[0].split(' ')[0]);
    const m = parseInt(inputs[0].split(' ')[1]);


    let check = []
    for (let i = 0; i < n + 1; i++) {
        check.push(0)
    }
    let people = []
    inputs[1].split(' ').forEach(data => {
        people.push(parseInt(data));
    })
    if (people.shift() == 0) {
        console.log(m);
        return;
    }
    for (let p = 0; p < people.length; p++) {
        check[people[p]] = 1;
    }

    let parties = []
    let graph = []
    for (let i = 0; i < n + 1; i++) {
        let line = [];
        for (let j = 0; j < n + 1; j++) {
            line.push(0);
        }
        graph.push(line);
    }

    for (let i = 2; i < m + 2; i++) {
        let party = inputs[i].split(' ');
        party.shift();
        party = party.map(data => {
            return parseInt(data);
        })
        parties.push(party);
    }

    // 그래프 그리기
    for (let i = 0; i < parties.length; i++) {
        for (let j = 0; j < parties[i].length; j++) {
            for (let k = j + 1; k < parties[i].length; k++) {
                graph[parties[i][j]][parties[i][k]] = 1;
                graph[parties[i][k]][parties[i][j]] = 1;
            }
        }
    }

    // bfs로 소문 다 퍼트리기
    for (let i = 0; i < people.length; i++) {
        let start = people[i];
        let queue = [start];
        while (queue.length > 0) {
            let cur = queue.shift();
            check[cur] = 1;

            for (j = 1; j < n + 1; j++) {
                if (graph[cur][j] == 1 && check[j] == 0) {
                    queue.push(j);
                }
            }
        }
    }

    let answer = 0;
    for (let i = 0; i < m; i++) {
        let flag = true;
        for (let j = 0; j < parties[i].length; j++) {
            if (check[parties[i][j]] == 1) {
                flag = false;
            }
        }

        if (flag) {
            answer++;
        }
    }
    console.log(answer);
}