# lib/cli.py

import click
from config import Session
from models import Project, Task

# Initialize the session
session = Session()

# CLI Menu for interacting with the user
@click.group()
def cli():
    """Task Manager CLI"""
    pass

# Project commands
@click.command()
@click.argument("name")
@click.argument("description")
def create_project(name, description):
    """Create a new project"""
    Project.create(session, name, description)
    click.echo(f"Project '{name}' created successfully!")

@click.command()
@click.argument("project_id", type=int)
def delete_project(project_id):
    """Delete a project"""
    Project.delete(session, project_id)
    click.echo(f"Project {project_id} deleted successfully!")

@click.command()
def list_projects():
    """List all projects"""
    projects = Project.get_all(session)
    if projects:
        for project in projects:
            click.echo(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")
    else:
        click.echo("No projects found.")

@click.command()
@click.argument("project_id", type=int)
def find_project_by_id(project_id):
    """Find a project by ID"""
    project = Project.find_by_id(session, project_id)
    if project:
        click.echo(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")
    else:
        click.echo("Project not found.")

@click.command()
@click.argument("name")
def find_project_by_name(name):
    """Find a project by name"""
    projects = Project.find_by_name(session, name)
    if projects:
        for project in projects:
            click.echo(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")
    else:
        click.echo("No project found with that name.")

# Task commands
@click.command()
@click.argument("description")
@click.argument("project_id", type=int)
def create_task(description, project_id):
    """Create a new task"""
    Task.create(session, description, project_id)
    click.echo(f"Task '{description}' created successfully for Project ID {project_id}.")

@click.command()
@click.argument("task_id", type=int)
def delete_task(task_id):
    """Delete a task"""
    Task.delete(session, task_id)
    click.echo(f"Task {task_id} deleted successfully!")

@click.command()
def list_tasks():
    """List all tasks"""
    tasks = Task.get_all(session)
    if tasks:
        for task in tasks:
            click.echo(f"ID: {task.id}, Description: {task.description}, Completed: {task.completed}, Project ID: {task.project_id}")
    else:
        click.echo("No tasks found.")

@click.command()
@click.argument("task_id", type=int)
def find_task_by_id(task_id):
    """Find a task by ID"""
    task = Task.find_by_id(session, task_id)
    if task:
        click.echo(f"ID: {task.id}, Description: {task.description}, Completed: {task.completed}, Project ID: {task.project_id}")
    else:
        click.echo("Task not found.")

@click.command()
@click.argument("description")
def find_task_by_description(description):
    """Find tasks by description"""
    tasks = Task.find_by_description(session, description)
    if tasks:
        for task in tasks:
            click.echo(f"ID: {task.id}, Description: {task.description}, Completed: {task.completed}, Project ID: {task.project_id}")
    else:
        click.echo("No tasks found with that description.")

# Add all commands to the CLI group
cli.add_command(create_project)
cli.add_command(delete_project)
cli.add_command(list_projects)
cli.add_command(find_project_by_id)
cli.add_command(find_project_by_name)

cli.add_command(create_task)
cli.add_command(delete_task)
cli.add_command(list_tasks)
cli.add_command(find_task_by_id)
cli.add_command(find_task_by_description)

if __name__ == "__main__":
    cli()
