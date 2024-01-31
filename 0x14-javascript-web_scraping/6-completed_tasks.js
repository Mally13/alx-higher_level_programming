#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id
 */
const request = require('request');
const { argv } = process;

// Check if both URL and file path are provided as arguments
if (argv.length !== 3) {
  console.error('Usage: ./6-completed-tasks.js <URL>');
  process.exit(1);
}

request.get(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body);
  const tasks = {};
  results.forEach(userTask => {
    if (userTask.completed) {
      if (tasks[userTask.userId]) {
        tasks[userTask.userId]++;
      } else {
        tasks[userTask.userId] = 1;
      }
    }
  });
  console.log(tasks);
});
