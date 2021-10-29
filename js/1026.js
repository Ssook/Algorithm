// 출처 : https://www.acmicpc.net/problem/1026
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
    const n = parseInt(inputs[0])
    let a = []
    let b = []
    inputs[1].split(' ').forEach(data => {
        a.push(parseInt(data));
    })
    inputs[2].split(' ').forEach(data => {
        b.push(parseInt(data));
    })


    // console.log(a);
    a = a.sort((a, b) => a - b);
    b = b.sort((a, b) => b - a);
    // console.log(a);
    // console.log(b);
    let answer = 0;
    for (let i = 0; i < n; i++) {
        answer += a[i] * b[i];
    }
    console.log(answer);
}