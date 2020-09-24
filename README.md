# Intruder Code Test

## Introduction

Welcome to the Intruder code test.

We recommend that the test should take 4-5 hours. It would be great if you could 
let us know how much time you spent on the test. There is no right or wrong amount of time, 
this info will simply help us with context when reviewing the results.

Your task is to write new Python code that parses the `example.nessus` XML file, stores
the results in the database and then displays the results in the Vue.js front-end.

Feel free to amend the existing code -- if you do so, please add a comment explaining
the reason for your changes.

## Pre-Requisites

Before starting this code test you should ensure that you have the following environment 
setup.

 * Python 3.7
 * NodeJS v12.18.4
 * NPM 6.14.6

## Story Specification

The goal is to give all authenticated users the ability to upload a xml nessus file 
(`example.nessus`) via a webform and then display the results in a "nice way". 

You will have to take a look at the XML structure, decide which information you 
want to extract and how you want to store the information in the database (i.e. 
design the models). Finally, you should pick whatever format of presentation 
you think is best suited to display the results in the front-end.
