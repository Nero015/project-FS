import ply.lex as lex

tokens = [
    'STARTUML', 'ENDUML', 'EOL', 'COLON', 'RIGHT_ARROW_1', 'RIGHT_ARROW_2',
    'LBRACE', 'RBRACE', 'INHERIT', 'ID', 'STRING', 'STEREO', 'ACTOR', 
    'USECASE', 'ACTOR_TXT', 'USE_CASE_TXT'
]

t_STARTUML = r'@startuml'
t_ENDUML = r'@enduml'
t_COLON = r':'
t_RIGHT_ARROW_1 = r'->'
t_RIGHT_ARROW_2 = r'-->'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'
t_STRING = r'"[^"]*"'
t_STEREO = r'<<[^>]+>>'
t_EOL = r'\n'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


t_ACTOR = r'actor'
t_USECASE = r'usecase'
t_ACTOR_TXT = r':[a-zA-Z_][a-zA-Z0-9_]*'
t_USE_CASE_TXT = r'\([a-zA-Z_][a-zA-Z0-9_]*\)'


t_ignore = ' \t'


def t_error(t):
    print(f"Caractère invalide : {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
