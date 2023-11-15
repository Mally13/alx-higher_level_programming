#!/usr/bin/node

const fs = require('fs').promises;
const { argv } = process;

async function readAndConcatenateFiles (file1, file2) {
  const dataA = await fs.readFile(file1, 'utf8');
  const dataB = await fs.readFile(file2, 'utf8');
  return `${dataA}${dataB}`;
}

async function writeToFile (file, content) {
  try {
    await fs.writeFile(file, content, 'utf8');
  } catch (err) {
    console.error(err);
  }
}

async function main () {
  const file1 = argv[2];
  const file2 = argv[3];
  const outputFile = argv[4];

  try {
    const concatenatedString = await readAndConcatenateFiles(file1, file2);
    await writeToFile(outputFile, concatenatedString);
  } catch (err) {
    console.error('Error:', err);
  }
}

main();
