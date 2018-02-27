## Description
A small practice of building an interpreter for a subset of Pascal instructions. Follow the tutorial from [Ruslan's Blog](https://ruslanspivak.com/lsbasi-part1/).

## Contents
### Part 1 - 6 Build a Calculator Interpreter
Introduced a simple command-line Calculator. Together with basic concepts of `Grammar`, `Lexer`, `Interpreter`.

[Design](python_commandline_calculator_interpreter/calc_v5_design.md) of a *syntax-directed* calculator interpreter contains more details of these concepts.

This repo include source code of Command-line Calculator Interpreter in [Python](\python_commandline_calculator_interpreter) and [Java](\commandline_calculator_interpreter).


### Part 7 Build an Simple Pascal Interpreter
**Syntax-directed interpreter** usually make a single pass over the input, the interpreter is able to evaluate an expression as soon as the parser recognized a certain language construct.

**Intermediate representation (IR)** is a data structure used to represent the input language to the interpreter. Tree is a very suitable data structure for an IR.

The Interpreter adopts [**Visitor Pattern**](https://en.wikipedia.org/wiki/Visitor_pattern) to traverse the AST produced by parser. 




## Logs


## Others
