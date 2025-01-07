```markdown
# 2025 Spring Schedule Visualizer

This project provides a visual representation of the class schedules for the 2025 Spring semester. It uses Python and Matplotlib to create a graphical week-by-week view that helps visualize when and where classes take place.

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

![2025 Spring Schedule](link_to_image_here)

Replace `link_to_image_here` with the actual link to your image for the schedule visualization.

## Customization

You can customize the schedule by modifying the `schedule_data` dictionary in the script. This allows you to add or change courses, times, and locations as needed.

## Contribution

Contributions are welcome! If you have a feature request or bug report, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
