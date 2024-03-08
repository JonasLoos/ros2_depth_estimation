# ROS2 Depth Estimation

using [`Intel/dpt-large`](https://huggingface.co/Intel/dpt-large).

## Installation

Install requirements:

```bash
pip install -r requirements.txt
```

Build:

```bash
colcon build --symlink-install --packages-select ros2_depth_estimation
```

## Usage

The first time you run the node, it will download the model.

```bash
ros2 run ros2_depth_estimation depth_estimation -i /input_topic -o /output_topic
```
