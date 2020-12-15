# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:38:19 2019

@author: Arjun Sengupta
@description: This module contains functions to initialize the application
"""


import proj_gallop.ui as ui
import proj_gallop.project_mgt as proj


# Dictionary to store sample users for authentication.
# Username is the key
# Password is the value
users = {
        "Tom": "tom_password",
        "Jane": "jane_password"
        }

# Variable to store a logged in user's username
logged_in_user = ""

# Create work directory to store project data
"""work_directory = os.getcwd() + "\\" + "work_dir"
if os.path.isdir(work_directory) is False:
    os.mkdir(work_directory)
"""

# Create sample projects
project_dict = {}

proj1 = proj.Project("Product Development", "John A")
project_dict[0] = proj1
proj2 = proj.Project("Marketing Website", "Jane B")
project_dict[1] = proj2
proj3 = proj.Project("Hiring", "Ellis")
project_dict[2] = proj3

# Create sample tasks in projects
proj1.create_task("Okta integration",
                  "Integrate app with Okta",
                  "Roy",
                  "Harun",
                  "23-Nov-2019")
proj1.create_task("REST API dev",
                  "Build REST APIs",
                  "Roy",
                  "John",
                  "21-Dec-2019")
proj2.create_task("SEO strategy",
                  "Present SEO strategy",
                  "Morgan",
                  "Toni",
                  "08-Dec-2019")
proj2.create_task("Ecommerce platform",
                  "Choose ecommerrce platform",
                  "Morgan",
                  "Dan",
                  "08-Dec-2019")
proj3.create_task("Tech support hire",
                  "Interview Jarvis",
                  "Dana",
                  "Alice",
                  "11-Nov-2019")


# Entry point of application
def launch_application():
    """
    Starts the application
    """
    ui.login_page()


# Check if the user is valid
def is_user_valid(username, password):
    """
    Validates user
    """
    global users
    if username is not None and username in users.keys():
        if password == users[username]:
            return True
    else:
        return False


# Log in a user
def login_user(username, password, login_page):
    """
    Log in the user if the user is valid
    """
    login_page.destroy()
    if is_user_valid(username, password) is True:
        global logged_in_user
        logged_in_user = username
        ui.general_actions_page()
    else:
        ui.login_failed_page()
        
# Return all projects
def get_all_projects():
    """
    Returns a list of all projects
    """
    return project_dict
        
def create_new_project(project_name, created_by):
    """
    Creates a new project
    """
    projectid = max(project_dict.keys()) + 1
    new_project = proj.Project(project_name, created_by)
    project_dict[projectid] = new_project
    
def get_all_tasks(project_id):
    """
    Returns all tasks of a project
    """
    project = project_dict[int(project_id)]
    return project.tasks

def add_task_to_project(project_id, task_name, task_description,
                        task_created_by, task_assigned_to,
                        task_due_date):
    """
    Adds a task to a project
    """
    project = project_dict[int(project_id)]
    project.create_task(task_name, task_description, task_created_by,
                        task_assigned_to, task_due_date)