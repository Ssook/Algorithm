// 출처 : https://www.acmicpc.net/problem/2096

// 메모리 제한 때매 못푼다함
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

    let dMin = [0, 0, 0];
    let dMax = [0, 0, 0];
    for (let i = 1; i < n + 1; i++) {
        let line = [];
        let arr = inputs[i].split(' ');
        for (let j = 0; j < 3; j++) {
            line.push(parseInt(arr[j]))
        }

        let temp0 = Math.max(dMax[0] + line[0], dMax[1] + line[0]);
        let temp1 = Math.max(dMax[0] + line[1], dMax[1] + line[1], dMax[2] + line[1]);
        let temp2 = Math.max(dMax[1] + line[2], dMax[2] + line[2]);

        dMax[0] = temp0;
        dMax[1] = temp1
        dMax[2] = temp2;

        let mTemp0 = Math.min(dMin[0] + line[0], dMin[1] + line[0]);
        let mTemp1 = Math.min(dMin[0] + line[1], dMin[1] + line[1], dMin[2] + line[1]);
        let mTemp2 = Math.min(dMin[1] + line[2], dMin[2] + line[2]);

        dMin[0] = mTemp0;
        dMin[1] = mTemp1;
        dMin[2] = mTemp2;

    }


    console.log(Math.max(...dMax), Math.min(...dMin));
}