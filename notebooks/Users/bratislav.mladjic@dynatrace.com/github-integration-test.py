# Databricks notebook source
import os

output = os.popen('ping -c 5 github.com/bratislavml')

while True:
  line = output.readline()
  
  if line:
    print(line)
  else:
    break

output.close()