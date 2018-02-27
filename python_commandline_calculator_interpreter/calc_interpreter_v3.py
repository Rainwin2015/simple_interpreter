# Additional features :
# - handles multiple sequence of operations

# Online Materials :
# https://ruslanspivak.com/lsbasi-part3/

# Token types :
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

# Class token :
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    ############
    # Lexer code
    ############

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        """
            add one to self.pos.
            set current_char variable.
            set None to current_char if eof is encountered.
        """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None    # indicate eof
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer / Scanner
        breaking a sentence apart into tokens.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                # advance() function call is inside self.integer() function
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            self.error()
        return Token(EOF, None)

    ###########################
    # Parser / Interpreter code
    ###########################

    def eat(self, token_type):
        """Compare the current_token type with the given token_type :
        - if they match, then assign the current_token to be get_next_token().
        - o.w., raise an exception.
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value
        """
        token = self.current_token
        # expacting current token to be an integer
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """Expression parser / Interpreter

        """
        self.current_token = self.get_next_token()
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result

def main():
    while True:
        try:
            text = input('calc3> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
