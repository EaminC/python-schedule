import matplotlib.pyplot as plt
import numpy as np

# 你的 schedule_data，原样保留
schedule_data = {
    "title": "2025 Spring Schedule",
    "courses": [
        {
            "name": "Topics in Machine Learning: Distributed and Federated Learning",
            "days": ["Tuesday", "Thursday"],
            "start": 9.5, "end": 10.8333,
            "location": "Ryerson Phys Lab 255",
            "color": "#FF9999",
        },
        {
            "name": "Complexity Theory",
            "days": ["Tuesday", "Thursday"],
            "start": 14.0, "end": 15.3333,
            "location": "Eckhart Hall 202",
            "color": "#99CCFF"
        },
        {
            "name": "Meet with Kexin's Group",
            "days": ["Monday"],
            "start": 14.0, "end": 15.0,
            "location": "John Crerar Library 208",
            "color": "#99FF99"
        },
        {
            "name": "Meet with Junchen's Group",
            "days": ["Monday"],
            "start": 23.5, "end": 24.0,
            "location": "Zoom",
            "color": "#FFCC99",
            "link": "https://uchicago.zoom.us/j/4015085138?pwd=eu5znzc3mmg3btfiq2e3ejzqsxlwqt09"
        },
        {
            "name": "Meet with vllm's Group",
            "days": ["Tuesday"],
            "start": 23.5, "end": 24.0,
            "location": "Zoom",
            "color": "#CCCCFF",
            "link": "https://uchicago.zoom.us/j/4015085138?pwd=eU5ZNzc3Mmg3bTFiQ2E3ejZqSXlWQT09"
        },
    ]
}

day_to_pos = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4
}

# 时间范围计算，加入最大不超过24点的逻辑
min_start = min(course["start"] for course in schedule_data["courses"]) - 1
max_end = min(max(course["end"] for course in schedule_data["courses"]) + 1, 24)  # 限制最大不超过24

fig, ax = plt.subplots(figsize=(10, 6))

for course in schedule_data["courses"]:
    for day in course["days"]:
        day_index = day_to_pos[day]
        ax.broken_barh([(day_index - 0.5, 1)], (course["start"], course["end"] - course["start"]),
                       facecolors=course["color"], edgecolor="black")
        
        # 处理可选 link
        if "link" in course:
            course_info = f"{course['name']}\n{course['location']}\n{course['link']}"
        else:
            course_info = f"{course['name']}\n{course['location']}"

        ax.text(day_index, (course["start"] + course["end"]) / 2, course_info,
                ha='center', va='center', fontsize=6, bbox=dict(facecolor='white', alpha=0.5))

# Y轴设置
ax.set_ylim(max_end, min_start)
y_ticks = np.arange(min_start, max_end + 0.5, 0.5)
y_tick_labels = [f"{int(h)}:00" if h.is_integer() else f"{int(h)}:30" for h in y_ticks]
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_tick_labels)

# X轴设置
ax.set_xlim(-0.5, 4.5)
ax.set_xticks(np.arange(-0.5, 4.5, 1))
ax.set_xticklabels([" " * 40 + day for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]])

# 标题和网格
ax.set_title(schedule_data["title"])
ax.grid(True, axis='y', color='gray', linestyle='--', linewidth=0.7)
plt.grid(True)
plt.tight_layout()
plt.show()