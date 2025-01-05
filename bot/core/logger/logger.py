
from datetime import datetime
import config


ANSI_COLORS = {
    "black": "\033[38;5;232m",    
    "red": "\033[31m", 
    "green": "\033[32m", 
    "yellow": "\033[33m", 
    "blue": "\033[34m",  
    "magenta": "\033[35m", 
    "cyan": "\033[36m",  
    "white": "\033[37m", 
    "gray": "\033[90m", 
    "reset": "\033[0m",
    "bold": "\033[1m",
    "red2": "\033[38;5;174m",        
    "green2": "\033[38;5;28m",      
    "yellow2": "\033[38;5;220m",  
    "sky_blue": "\033[38;5;111m",     
    "purple2": "\033[38;5;183m",       
    "turquoise": "\033[38;5;80m",      
    "peach": "\033[38;5;209m",          
    "purple": "\033[38;5;54m",     
    "green3": "\033[38;5;142m",          
    "silver": "\033[38;5;250m"           
}

class logger:
    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_timestamp():
        # Get the current time and format it in 12-hour format with AM/PM
        return datetime.now().strftime("%I:%M:%S %p")

    @staticmethod
    def _format_message(level, message, color):
        timestamp = logger._get_timestamp()
        # Format the log message with gray timestamp, uncolored brackets, and bold colored level
        return (f"{ANSI_COLORS['gray']}{timestamp}{ANSI_COLORS['reset']} "
                f"[{ANSI_COLORS['reset']}{ANSI_COLORS['bold']}{color}{level}{ANSI_COLORS['reset']}] {message}")

    @staticmethod
    def info(message):
        color = ANSI_COLORS.get(config.INFO_COLOR, ANSI_COLORS["reset"])
        print(logger._format_message("info", message, color))

    @staticmethod
    def error(message):
        color = ANSI_COLORS.get(config.ERROR_COLOR, ANSI_COLORS["reset"])
        print(logger._format_message("error", message, color))
        
    @staticmethod
    def debug(message):
        color = ANSI_COLORS.get(config.DEBUG_COLOR, ANSI_COLORS["reset"])
        print(logger._format_message("debug", message, color))
        
    @staticmethod
    def fatal(message):
        color = ANSI_COLORS.get(config.FATAL_COLOR, ANSI_COLORS["reset"])
        print(logger._format_message("fatal", message, color))
    
        
    @staticmethod
    def warning(message):
        color = ANSI_COLORS.get(config.WARNING_COLOR, ANSI_COLORS["reset"])
        print(logger._format_message("warning", message, color))
