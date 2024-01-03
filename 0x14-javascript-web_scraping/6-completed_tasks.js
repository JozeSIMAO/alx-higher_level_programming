#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});
