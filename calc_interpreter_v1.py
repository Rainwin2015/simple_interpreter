# Description : a simple calculator with these rules
# - only single digit integers are allowed in the input.
# - the only arithmetic operation supported is addition.
# - no whitespace characters are allowed anywhere in the input.

# Example input :
# 2+5

# Output :
# 7

# Token types
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type
        self.type = type
        #token value
        self.value = value

    def __str__(self):
        """String representation of class instance.
        Example :
            Token(INTEGER, 3)
        """
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

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the postion self.pos and decide what token to create based on this single character.
        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        """Compare the current token with the previous token
        - if they match, then eat the current token;
        - otherwise, raise an exception
        """
        # current token type meet expactation, advanced to the next token
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else :
            self.error()

    def expr(self):
        """Verify if the sequence of tokens does indeed correspond to the expacted sequence of tokens. i,e, "INTEGER -> PLUS -> INTEGER".

        Uses helper method eat() to verify the token type passed to the eat method matches the current token type.
        """
        self.current_token = self.get_next_token()
        left = self.current_token
        # expacting an interger token
        self.eat(INTEGER)

        # expacting an operator token
        op = self.current_token
        self.eat(PLUS)

        #expacting an integer token
        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = input('calc1> ')
        except EOFError:
            break

        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
