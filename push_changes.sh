#!/bin/bash

# GitHub repository URL
repo_url="https://github.com/SalahAli2018/task1.git"
git init

# Add all files
git add .

# Commit changes
git commit -m "python:3.8-slim"

# Tag the initial commit (optional)
git tag -a v1.0.4 -m "Version 1.0.4"

# Add the remote repository
git remote add origin "$repo_url"

# Push to the master branch and tags
git push -u origin master --tags


