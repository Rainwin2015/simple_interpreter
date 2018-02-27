# Design of v5 Calculator Interpreter
## Examples of input
1 + 2 + 3 - 4
1 + 2 * 3 - 4

## Operators and Precedence
| Precedence Level | Associativity | Operators |
| ---------------- | ------------- | --------- |
| 2 | left | `+`, `-` |
| 1 | left | `*`, `/` |

## Grammar
factor : INTEGER
term : factor ((MUL | DIV) factor)*
expr : term ((PLUS | MINUS) term)*

> For each level of precedence, define a new *non-terminal* (e.g. `term` and `expr`). The body of the *non-terminal* should contain arithmetic operators from that level and *non-terminal* for the next higher level of precedence.

> Each rule in grammar corresponds to a method in the Interpreter class. 
