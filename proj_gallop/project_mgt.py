# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:34:22 2019

@author: Arjun Sengupta
@description: This module provides classes and functions for creating projects
              and tasks
"""


class Project:

    def __init__(self, name, created_by):
        """
        Constructor for initializing a project
        """
        self.name = name
        self.__created_by = created_by
        self.tasks = {}

    def get_project_name(self):
        """
        Returns the project name
        """
        return self.name

    def set_project_name(self, name):
        """
        Sets the project name
        """
        self.name = name

    def get_project_creator(self):
        """
        Returns the name of the project creator
        """
        return self.__created_by

    def create_task(self, name, description, created_by,
                    assigned_to, due_date):
        """
        Creates a task in the project
        """
        new_task = Task(name, description, created_by, assigned_to, due_date)
        if len(self.tasks) == 0:
            self.tasks[0] = new_task
        else:
            task_id = max(self.tasks.keys()) + 1
            self.tasks[task_id] = new_task

    def __repr__(self):
        """
        Returns a string representation of the Project object
        """
        obj_string = self.get_project_name()
        return obj_string


class Task:

    def __init__(self, name, description, created_by, assigned_to, due_date):
        """
        Constructor for initializing a task
        """
        self.name = name
        self.description = description
        self.__created_by = created_by
        self.assigned_to = assigned_to
        self.due_date = due_date

    def get_task_name(self):
        """
        Returns the task name
        """
        return self.name

    def set_task_name(self, name):
        """
        Sets the task name
        """
        self.name = name

    def get_task_description(self):
        """
        Returns the task description
        """
        return self.description

    def set_task_description(self, description):
        """
        Sets the task description
        """
        self.description = description

    def get_task_creator(self):
        """
        Returns the name of the task creator
        """
        return self.__created_by

    def get_task_owner(self):
        """
        Returns the name of the task owner
        """
        return self.assigned_to

    def set_task_owner(self, assigned_to):
        """
        Sets the name of the task owner
        """
        self.assigned_to = assigned_to

    def get_task_due_date(self):
        """
        Returns the task due date
        """
        return self.due_date

    def set_task_due_date(self, due_date):
        """
        Sets the task due date
        """
        self.due_date = due_date

    def __repr__(self):
        """
        Returns a string representation of the Task object
        """
        obj_string = self.get_task_name() + " | " + self.get_task_owner()
        return obj_string
