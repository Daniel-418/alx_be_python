task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: \'{}\' is a high priority task that requires immediate attention today"
                    .format(task))
        else:
            print("Note: \'{}\' is a high priority task. Consider completing it when you have free time."
                    .format(task))
    case "medium":
        if time_bound == "yes":
            print("Reminder: \'{}\' is a medium priority task that requires immediate attention today"
                    .format(task))
        else:
            print("Note: \'{}\' is a medium priority task. Consider completing it when you have free time."
                    .format(task))
    case "low":
        if time_bound == "yes":
            print("Reminder: \'{}\' is a low priority task that requires immediate attention today"
                    .format(task))
        else:
            print("Note: \'{}\' is a low priority task. Consider completing it when you have free time."
                    .format(task))
