# 2025 Spring Schedule Visualizer

This project provides a visual representation of the class schedules. It uses Python and Matplotlib to create a graphical week-by-week view that helps visualize when and where classes take place.

## Features

- **Visual Schedule**: Easily see your entire class schedule in a weekly layout.
- **Course Details**: Hover over any course block to see details such as course name and location.
- **Color-Coded**: Each course has a unique color for quick identification.

## Prerequisites

Before you run this project, you'll need to have Python installed along with the following Python libraries:
- matplotlib
- numpy

You can install these packages using pip:

```bash
pip install matplotlib numpy
```

## Running the Script

To run the script, simply execute the Python file from your terminal or command prompt:

```bash
python schedule_visualizer.py
```
## Code Structure

- `schedule_data`: A dictionary containing the course schedule, including the course name, days of the week, start and end times, locations, and colors.
- `day_to_pos`: A dictionary mapping weekdays to their respective positions on the x-axis of the plot.
- `matplotlib`: Used to create the visual representation of the schedule.

## Visualization

Here is what the schedule visualization looks like:

<img width="1434" alt="image" src="https://github.com/user-attachments/assets/133d0b0a-1bee-4a89-bb93-bcdc419e3dc5" />



## Customization

You can customize the schedule by modifying the `schedule_data` dictionary in the script. This allows you to add or change courses, times, and locations as needed.

example
```json
{
  "title": "2025 Spring Schedule",
  "courses": [
    {
      "name": "Statistics for Data Analysis II: Regressions",
      "days": ["Tuesday", "Thursday"],
      "start": 14.0,
      "end": 15.33,
      "location": "The Keller Center 1022",
      "color": "#FF9999"
    },
    {
      "name": "TA Session: Statistics for Data Analysis II: Regressions",
      "days": ["Friday"],
      "start": 15.0,
      "end": 16.83,
      "location": "Remote",
      "color": "#99CCFF"
    },
    {
      "name": "Analytical Politics II: Political Institutions",
      "days": ["Tuesday", "Thursday"],
      "start": 15.5,
      "end": 16.83,
      "location": "The Keller Center 0001",
      "color": "#99FF99"
    },
    {
      "name": "TA Session: Analytical Politics II: Political Institutions",
      "days": ["Friday"],
      "start": 13.5,
      "end": 14.83,
      "location": "Remote",
      "color": "#FFCC99"
    },
    {
      "name": "Principles of Microeconomics for Public Policy II",
      "days": ["Monday", "Wednesday"],
      "start": 15.0,
      "end": 16.33,
      "location": "The Keller Center 0001",
      "color": "#CCCCFF"
    },
    {
      "name": "TA Session: Principles of Microeconomics for Public Policy II",
      "days": ["Friday"],
      "start": 10.5,
      "end": 11.83,
      "location": "Remote",
      "color": "#FFCCFF"
    }
  ]
}
```


## Contribution

Contributions are welcome! If you have a feature request or bug report, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
