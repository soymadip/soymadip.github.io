---
id: 1-variables-and-arithmetic
title: Variables and Arithmetic
sidebar_label: Variables and Arithmetic
sidebar_position: 1
description: "How to handle variable assignment, arithmetic expansion, and command substitution in Bash."
source_filename: "1 - variables.sh"
---

# Variables and Arithmetic

## What to remember

- **Variable Assignment**: No spaces are allowed around the `=` sign.
- **Accessing Variables**: Use the `$` prefix to read a variable's value.
- **Arithmetic Expansion**: Use `(( ... ))` for integer math; it's faster and cleaner than legacy `expr`.
- **Default Values**: Use `${VAR:-default}` to provide a fallback value if a variable is unset or null.
- **Command Substitution**: Use `$(command)` to capture the output of any bash command.

## Assignment and Access

Bash variables are loosely typed. The key rule is to **avoid spaces around the assignment operator**.

```bash
# Assignment (NO spaces!)
NAME="Gemini"
VERSION=1.0

# Accessing
echo "Hello, I am $NAME version $VERSION."
```

```text
Hello, I am Gemini version 1.0.
```

## Arithmetic Expansion with `(( ... ))`

The `(( ... ))` syntax allows for natural-looking integer arithmetic. It supports common operators like `+`, `-`, `*`, `/`, and even post-increment/decrement.

```bash
((PRICE = 10 + 5))
echo "The total price is: $PRICE"
```

```text
The total price is: 15
```

## Default Fallbacks

Bash provides built-in syntax for setting a default value when a variable might be empty.

```bash
USER_INPUT=""
# If empty, use 'guest'
FINAL_USER="${USER_INPUT:-guest}"
echo "User: $FINAL_USER"
```

```text
User: guest
```

## Capturing Output with `$( ... )`

Command substitution allows you to assign the result of a command to a variable.

```bash
CURRENT_DATE=$(date +%Y-%m-%d)
echo "Today's date is: $CURRENT_DATE"
```

```text
Today's date is: 2026-04-08
```

:::tip Case Sensitivity
Variable names are case-sensitive. It is a common convention to use uppercase for environment variables (like `PATH` or `USER`) and lowercase or camelCase for local script variables.
:::
