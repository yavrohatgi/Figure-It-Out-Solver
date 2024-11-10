import { exit } from "process";
import { createInterface } from "readline";

// Create an interface for reading input from the console
const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

/**
 * Prompts the user to provide a correctness score for a given guess.
 * @param {*} currentGuess - The current guess that the user is providing a correctness score for.
 * @returns {Promise<number>} - A promise that resolves to the correctness score provided by the user.
 */
async function getCorrectnessFromUser(currentGuess) {
  return new Promise((resolve) => {
    rl.question(
      `Guess: ${JSON.stringify(currentGuess)}\nEnter correctness score: `,
      (answer) => {
        resolve(parseInt(answer));
      }
    );
  });
}

const correctness = await getCorrectnessFromUser({
  1: 1,
  2: 1,
  3: 1,
});

console.log(`Correctness: ${correctness}`);
exit(0);
