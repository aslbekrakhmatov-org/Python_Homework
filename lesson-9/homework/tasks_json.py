import json
import csv
with open("tasks.json", 'r') as file:
    data = json.load(file)

ID_list=[]
tasks_list = []
status_list = []
priority_list = []
for item in data:
    ID_list.append(item['id'])
    tasks_list.append(item["task"])
    status_list.append (item["completed"])
    priority_list.append(int(item['priority']))

print(f"IDs - {ID_list}")
print(f"Tasks - {tasks_list}")
print(f"Statuses - {status_list}")
print(f"Priorities - {priority_list}")

for x in data:
    if x["id"] == 5:
        x['completed'] = True

with open("tasks.json", 'w') as file:
    json.dump(data, file, indent=2)

total_tasks = len(ID_list)
completed_tasks=0
pending_tasks = 0
for item in data:
    if item["completed"]:
        completed_tasks+=1
    else:
        pending_tasks+=1
avrg_pr = sum(priority_list)/total_tasks

print(f"Total tasks - {total_tasks}")
print(f"Completed tasks - {completed_tasks}")
print(f"Pending tasks - {pending_tasks}")
print(f"Average priority - {avrg_pr}")

with open("tasks.csv", 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "task", "completed", "priority"])
    writer.writeheader()
    writer.writerows(data)