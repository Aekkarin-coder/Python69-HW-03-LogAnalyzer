def analyze_user_activity(log_file_path: str) -> dict:
    #your code here
    action_counts = {}
    session_times = {}  # user_id -> login value (duration)
    users = set()

    with open(log_file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            timestamp, user_id, action, value = line.split()
            value = int(value)

            action_counts[action] = action_counts.get(action, 0) + 1
            users.add(user_id)

            if action == 'login':
                session_times[user_id] = value

    average_session_time = (
        sum(session_times.values()) / len(session_times)
        if session_times else 0.0
    )
    most_active_user = (
        max(session_times, key=session_times.get) if session_times else None
    )

    return {
        'action_counts': action_counts,
        'average_session_time': average_session_time,
        'most_active_user': most_active_user,
        'total_users': len(users),
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
