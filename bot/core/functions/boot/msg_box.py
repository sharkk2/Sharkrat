from colorama import Fore, Style

def msg_box(msg, indent=1, width=None, title=None):
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + box)