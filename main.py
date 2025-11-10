from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def hello_world():
    """
    Displays a colorful hello world message.
    """
    console = Console()
    text = Text("Hello, World!", style="bold magenta")
    panel = Panel(text, title="[bold green]Greeting[/bold green]", border_style="green")
    console.print(panel)

def personalized_greeting():
    """
    Gets user's name and displays a personalized greeting.
    """
    console = Console()
    name = console.input("[bold yellow]What's your name? [/bold yellow]")
    text = Text(f"Hello, {name}!", style="bold blue")
    panel = Panel(text, title="[bold cyan]Personalized Greeting[/bold cyan]", border_style="cyan")
    console.print(panel)

if __name__ == "__main__":
    hello_world()
    personalized_greeting()