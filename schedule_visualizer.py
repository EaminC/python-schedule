import matplotlib.pyplot as plt
import numpy as np

# 定义一个包含表格名和课程数据的字典
schedule_data = {
    "title": "2025 Spring Schedule",
    "courses": [
        {"name": "Statistics for Data Analysis II: Regressions", "days": ["Tuesday", "Thursday"], "start": 14.0, "end": 15.33, "location": "The Keller Center 1022", "color": "#FF9999"},
        {"name": "TA Session: Statistics for Data Analysis II: Regressions", "days": ["Friday"], "start": 15.0, "end": 16.83, "location": "Remote", "color": "#99CCFF"},
        {"name": "Analytical Politics II: Political Institutions", "days": ["Tuesday", "Thursday"], "start": 15.5, "end": 16.83, "location": "The Keller Center 0001", "color": "#99FF99"},
        {"name": "TA Session: Analytical Politics II: Political Institutions", "days": ["Friday"], "start": 13.5, "end": 14.83, "location": "Remote", "color": "#FFCC99"},
        {"name": "Principles of Microeconomics for Public Policy II", "days": ["Monday", "Wednesday"], "start": 15.0, "end": 16.33, "location": "The Keller Center 0001", "color": "#CCCCFF"},
        {"name": "TA Session: Principles of Microeconomics for Public Policy II", "days": ["Friday"], "start": 10.5, "end": 11.83, "location": "Remote", "color": "#FFCCFF"}
    ]
}

# 映射星期到 x 轴位置
day_to_pos = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4
}

# 计算时间轴的范围
min_start = min(course["start"] for course in schedule_data["courses"]) - 1
max_end = max(course["end"] for course in schedule_data["courses"]) + 1

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制每门课程的条块
for course in schedule_data["courses"]:
    for day in course["days"]:
        day_index = day_to_pos[day]
        ax.broken_barh([(day_index - 0.5, 1)], (course["start"], course["end"] - course["start"]),
                       facecolors=course["color"], edgecolor="black")
        course_info = f"{course['name']}\n{course['location']}"
        ax.text(day_index, (course["start"] + course["end"]) / 2, course_info,
                ha='center', va='center', fontsize=6, bbox=dict(facecolor='white', alpha=0.5))

# 设置 y 轴范围和标签
ax.set_ylim(max_end, min_start)
y_ticks = np.arange(min_start, max_end + 0.5, 0.5)
y_tick_labels = [f"{int(h)}:00" if h.is_integer() else f"{int(h)}:30" for h in y_ticks]
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_tick_labels)

# 设置 x 轴范围和标签
ax.set_xlim(-0.5, 4.5)
ax.set_xticks(np.arange(-0.5, 4.5, 1))
ax.set_xticklabels([" " * 40 + day for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]])

# 设置标题
ax.set_title(schedule_data["title"])

# 显示图表
ax.grid(True, axis='y', color='gray', linestyle='--', linewidth=0.7)
plt.grid(True)
plt.tight_layout()
plt.show()
