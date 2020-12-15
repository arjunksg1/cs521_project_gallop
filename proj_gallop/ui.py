# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:37:16 2019

@author: Arjun Sengupta
@description: This module provides functions to initialize UI pages
"""


import tkinter as tk
from tkinter import font
import proj_gallop.app as app


# Background color for all pages
#bgcolor = "#e4f7f4"
bgcolor = "#f0e9e9"


def login_page():
    """
    Initializes the login page
    """
    # Create tkinter window
    login_page = tk.Tk()
    login_page["bg"] = bgcolor
    login_page.geometry("600x400")
    login_page.resizable(width=False, height=False)
    login_page.title("Project Gallop")
    # Create login form
    login_form = tk.Frame(login_page,
                          width=450,
                          height=50,
                          pady=3,
                          bg=bgcolor).grid(row=0, columnspan=3)
    login_title_font = font.Font(family='Montserrat', size=15)
    tk.Label(login_form,
             text="Login",
             bg=bgcolor, 
             font=login_title_font).grid(row=0, column = 0)
    field_font = font.Font(family='Montserrat', size=10)
    tk.Label(login_form,
             text="Username",
             bg=bgcolor,
             font=field_font,
             pady=10).grid(row=1, column=0)
    tk.Label(login_form,
             text="Password",
             bg=bgcolor,
             font=field_font).grid(row=2, column=0)
    username = tk.Entry(login_form)
    username.grid(row=1, column=1)
    password = tk.Entry(login_form, show="*")
    password.grid(row=2, column=1)
    tk.Label(login_form, bg=bgcolor, pady=10).grid(row=3, columnspan=3)
    submit_button = tk.Button(login_form,
                              text="Log in",
                              bg="#b0a4a7",
                              relief="raised",
                              font=field_font,
                              command=lambda: app.login_user(username.get(), 
                                                              password.get(),
                                                              login_page)
                              ).grid(row=4, column=1)
    # Open the window
    login_page.mainloop()
    

def login_failed_page():
    """
    Initializes the login failed page
    """
    # Create tkinter window
    login_failed_page = tk.Tk()
    login_failed_page["bg"] = bgcolor
    login_failed_page.geometry("600x400")
    login_failed_page.resizable(width=False, height=False)
    login_failed_page.title("Project Gallop - Login Failed")
    # Create message
    field_font = font.Font(family='Montserrat', size=10)
    tk.Label(login_failed_page,
             text="Login failed",
             bg=bgcolor,
             font=field_font,
             pady=10).grid(row=1, column=0)
    submit_button = tk.Button(login_failed_page,
                              text="Return to Login page",
                              bg="#b0a4a7",
                              relief="raised",
                              font=field_font,
                              command=lambda: [login_failed_page.destroy(),
                                               app.launch_application()]
                              ).grid(row=4, column=1)
    print("login failed")
    

def projects_page():
    """
    Initializes the page displaying all projects
    """
    all_projects = app.get_all_projects()
    # Create tkinter window
    all_projects_page = tk.Tk()
    all_projects_page["bg"] = bgcolor
    all_projects_page.geometry("600x400")
    #all_projects_page.resizable(width=False, height=False)
    all_projects_page.title("Project Gallop - All Projects View")
    # Create project list
    header_font = font.Font(family='Montserrat', size=12)
    field_font = font.Font(family='Montserrat', size=8)
    tk.Label(all_projects_page,
             font=header_font,
             bg=bgcolor,
             text="Project Name").grid(row=0, column=0, columnspan=5)
    tk.Label(all_projects_page,
             font=header_font,
             bg=bgcolor,
             text="Project ID").grid(row=0, column=6)
    for j in all_projects.keys():
        project_name = all_projects[j].get_project_name()
        tk.Label(all_projects_page,
                 font=field_font,
                 bg=bgcolor,
                 text=project_name).grid(row=j+1, column=0, columnspan=5)
        tk.Label(all_projects_page,
                 font=field_font,
                 bg=bgcolor,
                 text=j).grid(row=j+1, column=6)
    tk.Label(all_projects_page,
             bg=bgcolor,
             text="Enter project ID to update a project: ")\
             .grid(row=j+3, column=0, columnspan=5)
    project_id = tk.Entry(all_projects_page)
    project_id.grid(row=j+4, column=1)
    tk.Button(all_projects_page,
              text="Edit",
              bg="#b0a4a7",
              command=lambda: all_tasks_page(project_id.get()))\
              .grid(row=j+5, column=1)
    tk.Label(all_projects_page,
             bg=bgcolor)\
             .grid(row=j+3, column=0, columnspan=5)
    
    create_new_project = tk.Button(all_projects_page,
                                   text="Add New Project",
                                   bg="#8b7db0",
                                   font=field_font,
                                   command=lambda:[all_projects_page.destroy(),
                                                   new_project_page()])\
                                   .grid(row=j+8, column=1)
    
    # Open window
    all_projects_page.mainloop()
        

def general_actions_frame(page):
    """
    Initializes a tkinter frame displaying buttons to create or update project
    """
    # Create tkinter frame
    welcome_message = "Welcome " + app.logged_in_user
    actions_frame = tk.Frame(page,
                             width=500,
                             height=100, 
                             bg=bgcolor).grid(row=0, columnspan=5)
    field_font = font.Font(family='Montserrat', size=10)
    tk.Label(actions_frame,
             text=welcome_message,
             font=field_font,
             bg=bgcolor).grid(row=0, column=0)
    create_new_project = tk.Button(actions_frame,
                                   text="Create New Project",
                                   bg="#8b7db0",
                                   font=field_font,
                                   command=lambda:[page.destroy(),
                                                   new_project_page()])\
                                   .grid(row=0, column=1)
    update_project = tk.Button(actions_frame,
                                   text="Update Existing Project",
                                   bg="#8b7db0",
                                   font=field_font,
                                   command=lambda: [page.destroy(),
                                                    projects_page()])\
                               .grid(row=0, column=2)
    view_projects = tk.Button(actions_frame,
                                   text="View All Projects",
                                   bg="#8b7db0",
                                   font=field_font,
                                   command=lambda: [page.destroy(),
                                                    projects_page()])\
                               .grid(row=0, column=3)
    

def general_actions_page():
    """
    Initializes a page displaying choices to create a project, 
    update a project, or view all existing projects
    """
    # Create tkinter window
    actions_page = tk.Tk()
    actions_page["bg"] = bgcolor
    actions_page.geometry("600x400")
    actions_page.resizable(width=False, height=False)
    actions_page.title("Project Gallop - Actions")
    general_actions_frame(actions_page)
    actions_page.mainloop()

def new_project_page():
    """
    Initializes a project creation page to create a new project
    """
    # Create tkinter window
    new_project_page = tk.Tk()
    new_project_page["bg"] = bgcolor
    new_project_page.geometry("600x400")
    new_project_page.resizable(width=False, height=False)
    new_project_page.title("Project Gallop - New Project")
    # Create project form
    project_form = tk.Frame(new_project_page,
                          width=450,
                          height=50,
                          pady=3,
                          bg=bgcolor).grid(row=0, columnspan=3)
    project_page_title_font = font.Font(family='Montserrat', size=15)
    tk.Label(project_form,
             text="Create a New Project",
             bg=bgcolor, 
             font=project_page_title_font).grid(row=0, column = 0)
    field_font = font.Font(family='Montserrat', size=10)
    tk.Label(project_form,
             text="Project Name",
             bg=bgcolor,
             font=field_font,
             pady=10).grid(row=1, column=0)
    project_name = tk.Entry(project_form)
    project_name.grid(row=1, column=1)
    tk.Label(project_form, bg=bgcolor, pady=10).grid(row=3, columnspan=3)
    submit_button = tk.Button(project_form,
                              text="Create",
                              bg="#b0a4a7",
                              relief="raised",
                              font=field_font,
                              command=lambda: [
                                      app.create_new_project(
                                      project_name.get(), app.logged_in_user
                                      ), 
                                      new_project_page.destroy(),
                                      projects_page()])\
                        .grid(row=4, column=1)
    new_project_page.mainloop()

def invalid_project_id():
    """
    Displays a message about an invalid project id
    """
    invalid_id_page = tk.Tk()
    invalid_id_page.geometry("600x400")
    invalid_id_page.title("Project Gallop - Invalid ID")
    invalid_id_page.resizable(width=False, height=False)
    # Display message
    tk.Label(invalid_id_page,
             text="Invalid Project ID. Choose a number from listed IDs",
             bg=bgcolor).grid(row=0, column=0, columnspan=10)
    # Launch window
    invalid_id_page.mainloop()


def all_tasks_page(project_id):
    """
    Initializes a page that displays all tasks for a project
    """
    # Validate project_id
    try:
        project_id = int(project_id)
    except ValueError:
        invalid_project_id()
    project_dict = app.get_all_projects()
    if project_id not in project_dict.keys():
        invalid_project_id()
    # Create tkinter window
    tasks_page = tk.Tk()
    tasks_page["bg"] = bgcolor
    tasks_page.geometry("600x400")
    tasks_page.title("Project Gallop - Tasks")
    # Retrieve tasks
    tasks = app.get_all_tasks(project_id)
    print(tasks)
    field_font = font.Font(family='Montserrat', size=10)
    task_font = font.Font(family='Montserrat', size=8)
    tk.Button(tasks_page,
              text="Add New Task",
              bg="#b0a4a7",
              font=field_font,
              command=lambda: add_task_page(project_id))\
              .grid(row=0, column=0)
    tk.Label(tasks_page,
             text="Task Name",
             bg=bgcolor,
             font=field_font).grid(row=1, column=0)
    tk.Label(tasks_page,
             text="Assigned To",
             bg=bgcolor,
             font=field_font).grid(row=1, column=1)
    for task_id in tasks.keys():
        task = tasks[task_id]
        tk.Label(tasks_page,
                 text=task.get_task_name(),
                 bg=bgcolor,
                 font=task_font).grid(row=task_id+5, column=0)
        tk.Label(tasks_page,
                 text=task.get_task_owner(),
                 bg=bgcolor,
                 font=task_font).grid(row=task_id+5, column=1)
    if len(tasks.keys()) == 0:
        row = 5
    else:
        row = len(tasks.keys()) + 5
    tk.Button(tasks_page,
              text="Refresh",
              bg="#b0a4a7",
              font=field_font,
              command=lambda: [tasks_page.destroy(),
                              all_tasks_page(project_id)])\
              .grid(row=row, column=0)
    tasks_page.mainloop()        
    
def add_task_page(project_id):
    """
    Initializes a task creation page
    """
    # Create tkinter window
    task_page = tk.Tk()
    task_page["bg"] = bgcolor
    task_page.geometry("600x400")
    task_page.title("Project Gallop - Add Task")
    # Input fields
    field_font = font.Font(family='Montserrat', size=8)
    tk.Label(task_page,
             text="Task Name: ",
             bg=bgcolor,
             font=field_font,
             pady=10).grid(row=0, column=0)
    tk.Label(task_page,
             text="Task Description: ",
             bg=bgcolor,
             font=field_font).grid(row=1, column=0)
    tk.Label(task_page,
             text="Assigned To: ",
             bg=bgcolor,
             font=field_font).grid(row=2, column=0)
    tk.Label(task_page,
             text="Due Date: ",
             bg=bgcolor,
             font=field_font).grid(row=3, column=0)
    task_name = tk.Entry(task_page)
    task_name.grid(row=0, column=1)
    task_description = tk.Entry(task_page)
    task_description.grid(row=1, column=1)
    task_owner = tk.Entry(task_page)
    task_owner.grid(row=2, column=1)
    task_due_date = tk.Entry(task_page)
    task_due_date.grid(row=3, column=1)
    tk.Button(task_page,
              text="Add Task",
              bg="#b0a4a7",
              font=field_font,
              command=lambda: [app.add_task_to_project(project_id,
                                                      task_name.get(),
                                                      task_description.get(),
                                                      app.logged_in_user,
                                                      task_owner.get(),
                                                      task_due_date.get()),
                                task_page.destroy()])\
              .grid(row=4, column=1)
    # Launch the window
    task_page.mainloop()
    
    