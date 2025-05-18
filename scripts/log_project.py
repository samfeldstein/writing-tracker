import csv

log = "log.csv"

def load_projects_from_csv():
    projects = set()
    try:
        with open(log) as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = row.get("project")
                if project:
                    projects.add(project.strip())
    except FileNotFoundError:
        pass
    return sorted(projects)

def log_project():
    projects = load_projects_from_csv()
    
    if not projects:
        return input("No existing projects found. Enter new project name: ")

    print("Select a project:")
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project}")

    while True:
        choice = input("Enter number or a new project: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(projects):
                return projects[index]
            else:
                print("Invalid number.")
        elif choice.strip():
            return choice.strip()
