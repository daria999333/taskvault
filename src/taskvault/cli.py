import typer
from rich.console import Console
from rich.table import Table

from taskvault.database import (
    add_task,
    complete_task,
    delete_task,
    get_all_tasks,
    init_db,
)

app = typer.Typer(help="TaskVault - A simple and efficient terminal task manager.")
console = Console()


@app.command("add")
def add_task_cli(
    title: str = typer.Argument(..., help="Task description or title"),
    priority: str = typer.Option("Medium", "--priority", "-p", help="Priority: High, Medium, Low"),
) -> None:
    """Add a new task to the vault."""
    init_db()
    task_id = add_task(title, priority)
    console.print(f"[bold green]Success![/bold green] Task #{task_id} added: '{title}' [dim]({priority})[/dim]")


@app.command("list")
def list_tasks_cli() -> None:
    """List all tasks in the vault."""
    init_db()
    tasks = get_all_tasks()

    if not tasks:
        console.print("[yellow]Your task vault is empty! Add a task using 'add' command.[/yellow]")
        return

    table = Table(title="📋 TaskVault Items", show_header=True, header_style="bold blue")
    table.add_column("ID", style="bold white", justify="center")
    table.add_column("Task", style="white")
    table.add_column("Priority", justify="center")
    table.add_column("Status", justify="center")

    for task in tasks:
        status_style = "bold green" if task["status"] == "Completed" else "bold yellow"
        priority_style = (
            "bold red"
            if task["priority"] == "High"
            else "bold cyan"
            if task["priority"] == "Medium"
            else "dim white"
        )

        table.add_row(
            str(task["id"]),
            task["title"],
            f"[{priority_style}]{task['priority']}[/{priority_style}]",
            f"[{status_style}]{task['status']}[/{status_style}]",
        )

    console.print(table)


@app.command("done")
def done_task_cli(task_id: int = typer.Argument(..., help="ID of the task to mark as completed")) -> None:
    """Mark a specific task as completed."""
    init_db()
    success = complete_task(task_id)
    if success:
        console.print(f"[bold green]Success![/bold green] Task #{task_id} marked as Completed.")
    else:
        console.print(f"[bold red]Error:[/bold red] Task with ID {task_id} not found.")


@app.command("remove")
def remove_task_cli(task_id: int = typer.Argument(..., help="ID of the task to delete")) -> None:
    """Delete a task from the vault."""
    init_db()
    success = delete_task(task_id)
    if success:
        console.print(f"[bold red]Deleted![/bold red] Task #{task_id} has been removed.")
    else:
        console.print(f"[bold red]Error:[/bold red] Task with ID {task_id} not found.")


if __name__ == "__main__":
    app()