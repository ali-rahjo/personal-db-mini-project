import psycopg2
import argparse
from modules.contact import add_contact, list_contacts, update_contact, delete_contact
from modules.tasks import add_task, list_tasks, update_task, delete_task
from modules.reports import due_tasks_report, contact_tasks_report
from modules.database import create_tables

def main():
    print("starting the process")
    parser = argparse.ArgumentParser(description="Personal Database CLI")
    subparsers = parser.add_subparsers(dest="command")

    # database setup command
    parser_setup = subparsers.add_parser("setup")

    # contacts commands
    parser_contacts = subparsers.add_parser("contacts")
    contacts_subparsers = parser_contacts.add_subparsers(dest="subcommand")
    
    parser_contacts_add = contacts_subparsers.add_parser("add")
    parser_contacts_add.add_argument("name")
    parser_contacts_add.add_argument("phone")
    parser_contacts_add.add_argument("email")

    parser_contacts_list = contacts_subparsers.add_parser("list")

    parser_contacts_update = contacts_subparsers.add_parser("update")
    parser_contacts_update.add_argument("id")
    parser_contacts_update.add_argument("name")
    parser_contacts_update.add_argument("phone")
    parser_contacts_update.add_argument("email")

    parser_contacts_delete = contacts_subparsers.add_parser("delete")
    parser_contacts_delete.add_argument("id")

    # tasks commands
    parser_tasks = subparsers.add_parser("tasks")
    tasks_subparsers = parser_tasks.add_subparsers(dest="subcommand")
    
    parser_tasks_add = tasks_subparsers.add_parser("add")
    parser_tasks_add.add_argument("contact_id")
    parser_tasks_add.add_argument("description")
    parser_tasks_add.add_argument("due_date")
    parser_tasks_add.add_argument("status")

    parser_tasks_list = tasks_subparsers.add_parser("list")

    parser_tasks_update = tasks_subparsers.add_parser("update")
    parser_tasks_update.add_argument("id")
    parser_tasks_update.add_argument("contact_id")
    parser_tasks_update.add_argument("description")
    parser_tasks_update.add_argument("due_date")
    parser_tasks_update.add_argument("status")

    parser_tasks_delete = tasks_subparsers.add_parser("delete")
    parser_tasks_delete.add_argument("id")

    # reports commands
    parser_report = subparsers.add_parser("report")
    report_subparsers = parser_report.add_subparsers(dest="subcommand")
    
    parser_report_due_tasks = report_subparsers.add_parser("due_tasks")

    parser_report_contact_tasks = report_subparsers.add_parser("contact_tasks")
    parser_report_contact_tasks.add_argument("contact_id")

    args = parser.parse_args()

    if args.command == "setup":
        create_tables()
        print("Database setup complete.")

    elif args.command == "contacts":
        if args.subcommand == "add":
            add_contact(args.name, args.phone, args.email)
        elif args.subcommand == "list":
            list_contacts()
        elif args.subcommand == "update":
            update_contact(args.id, args.name, args.phone, args.email)
        elif args.subcommand == "delete":
            delete_contact(args.id)

    elif args.command == "tasks":
        if args.subcommand == "add":
            add_task(args.contact_id, args.description, args.due_date, args.status)
        elif args.subcommand == "list":
            list_tasks()
        elif args.subcommand == "update":
            update_task(args.id, args.contact_id, args.description, args.due_date, args.status)
        elif args.subcommand == "delete":
            delete_task(args.id)

    elif args.command == "report":
        if args.subcommand == "due_tasks":
            due_tasks_report()
        elif args.subcommand == "contact_tasks":
            contact_tasks_report(args.contact_id)
    print("end the process")

if __name__ == '__main__':
    main()
