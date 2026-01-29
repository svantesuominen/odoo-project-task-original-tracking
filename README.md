# Project Task Original Tracking

This module enhanced Odoo Project Tasks by tracking changes to the original deadline and planned hours (allocated time). It provides a clear view of how much a task has deviated from its initial plan.

## Features
- **Capture Original Data**: Automatically stores the first deadline and planned hours when they are set for the first time.
- **Extra Info Integration**: Adds an "Original Plan and Tracking" section to the standard **Extra Info** tab.
- **Deadline Comparison**: Calculates the number of days difference between the current deadline and the original one.
- **Planned Hours Comparison**: Shows the difference between current allocated hours and the original plan.
- **Remaining Original Hours**: Calculates `Original Plan - Spent Hours` to show the remaining original time budget.
- **Manager Access**: Original values can be manually overridden by users with **Project Administrator** permissions.

## Technical Details
- **Version**: 17.0.1.0.0
- **Authors**: Svante Suominen, Avoin.Systems & Google Antigravity
- **Dependencies**: `project`, `hr_timesheet`

## Installation
1. Ensure the `extra-addons` path is configured in your Odoo instance.
2. Update the Apps list.
3. Install "Project Task Original Tracking".
