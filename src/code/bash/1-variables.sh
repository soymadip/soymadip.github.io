#!/bin/bash

# Simple Variable Assignment
# Note: Do not put spaces around the equals sign!
NAME="Gemini"
VERSION=1.0

# Using Variables
echo "Hello, I am $NAME version $VERSION."

# Arithmetic Expansion with (( ... ))
# This is the modern and preferred way to do integer math in Bash.
((PRICE = 10 + 5))
echo "The total price is: $PRICE"

# Default Values
# If USER_INPUT is unset or null, it defaults to 'default_user'
USER_INPUT=""
FINAL_USER="${USER_INPUT:-default_user}"
echo "Current user: $FINAL_USER"

# Command Substitution
# Capturing the output of a command into a variable
CURRENT_DATE=$(date +%Y-%m-%d)
echo "Today's date is: $CURRENT_DATE"
