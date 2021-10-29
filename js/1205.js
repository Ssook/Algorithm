// 출처 : https://www.acmicpc.net/problem/1205
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
    let arr = inputs[0].split(' ');
    const n = parseInt(arr[0]);
    const newScore = parseInt(arr[1]);
    const p = parseInt(arr[2]);
    if (n == 0) {
        console.log(1);
        return;
    }

    let scores = [];
    arr = inputs[1].split(' ');
    arr.forEach(element => {
        scores.push(parseInt(element));
    });

    let r = n - 1;
    let l = 0;
    // 이분탐색으로 새 점수가 들어갈 인덱스를 구함
    let upperIndex = -1;
    while (r >= l) {
        let mid = parseInt((r + l) / 2);
        if (scores[mid] < newScore) {
            r = mid - 1;
        }
        else if (scores[mid] > newScore) {
            l = mid + 1;
        }

        else {
            upperIndex = mid;
            l = mid + 1
        }
    }


    let answer = Math.max(l, upperIndex);
    // p안에 못들면 -1
    if (answer >= p) {
        console.log(-1);
    } else {
        // 같은 게 없으면 그냥 인덱스가 정답
        if (upperIndex == -1) console.log(answer + 1);
        // 같은 게 있는 경우 정답보다 큰 값들을 카운팅
        else {
            count = 0;
            i = 0;
            while (scores[i] > newScore) {
                count++;
                i++;
            }
            console.log(count + 1)
        }

    }
}