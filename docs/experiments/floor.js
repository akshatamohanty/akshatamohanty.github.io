function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}

function run(name, midpointFn, inputs, answers, times) {
  const start = Date.now();
  const answers_floor = [];
  for (let input of inputs) {
    const [m, n] = input;
    const midpoint = midpointFn(m, n);
    answers_floor.push(midpoint);
  }
  const end = Date.now();
  answers.push(answers_floor);
  times.push({ name, time: end - start });
}

function runIterations(iterations) {
  const inputs = [];
  const answers = [];
  const times = [];
  for (let i = 0; i < iterations; i++) {
    const n = getRandomIntInclusive(1, 2 ** 15 - 2);
    const m = getRandomIntInclusive(n, 2 ** 15 - 1);
    inputs[i] = [n, m];
  }

  const fns = {
    // floor_add: (m, n) => Math.floor((m + n) / 2),
    // floor_subtract: (m, n) => n + Math.floor((m - n) / 2),
    // bitwise: (m, n) => (n + m) >> 1,
    // unsighed_bitwise: (m, n) => (n + m) >>> 1,
    // odd_even: (m, n) => {
    //   return (m + n) % 2 === 0 ? (m + n) / 2 : (m + n - 1) / 2;
    // },
    // not: (m, n) => ~~((n + m) / 2),
    // modulo: (m, n) => {
    //   const p = (m + n) / 2;
    //   return p - (p % 1);
    // },
  };

  // for (let fn of Object.keys(fns)) {
  //   run(fn, fns[fn], inputs, answers, times);
  // }

  start = Date.now();
  answers_floor = [];
  for (let input of inputs) {
    const [m, n] = input;
    const midpoint = Math.floor((m + n) / 2);
    answers_floor.push(midpoint);
  }
  end = Date.now();
  answers.push(answers_floor);
  times.push({ name: "bitwise", time: end - start });

  // start = Date.now();
  // answers_floor = [];
  // for (let input of inputs) {
  //   const [m, n] = input;
  //   const midpoint = n + Math.floor((m - n) / 2);
  //   answers_floor.push(midpoint);
  // }
  // end = Date.now();
  // answers.push(answers_floor);
  // times.push({ name: "floor (subtract)", time: end - start });

  // start = Date.now();
  // answers_floor = [];
  // for (let input of inputs) {
  //   const [m, n] = input;
  //   const midpoint = ~~((m + n) / 2);
  //   answers_floor.push(midpoint);
  // }
  // end = Date.now();
  // answers.push(answers_floor);
  // times.push({ name: "not", time: end - start });

  // let not_matching = 0;
  // for (let i = 0; i < inputs.length; i++) {
  //   const answerArr = answers.map((arr) => arr[i]);
  //   const isMatching = answerArr.every((val) => val === answerArr[0]);
  //   if (!isMatching) {
  //     not_matching++;
  //     console.log(answerArr);
  //   }
  // }

  console.log(`Iterations: ${iterations}`);
  // console.log(`Is Valid: ${not_matching === 0}\n`);
  times.sort((a, b) => a.time - b.time);
  times.forEach(({ name, time }) => console.log(`${name}: ${time}ms`));
  console.log("------------------------");
}

function main() {
  const iterations = [10000000];
  iterations.forEach(runIterations);
}

main();
