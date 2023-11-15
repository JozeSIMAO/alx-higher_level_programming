#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const incren0 = number++;

  theFunction(incren0);
};
