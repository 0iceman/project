# -*- coding: utf-8 -*-
# © 2016 Elico Corp (www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Project Task Category",
    "summary": "Allow unique category for Tasks",
    "version": "8.0.1.0.1",
    "category": "Project Management",
    "website": "www.elico-corp.com",
    "author": "Elico Corp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "project",
    ],
    "data": [
        'views/project_task_view.xml',
    ],
}
