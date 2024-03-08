# ROS2 Depth Estimation

A very simple ros2 node for depth estimation using [`Intel/dpt-large`](https://huggingface.co/Intel/dpt-large).

The depth information is not aliged to any unit, it is just a relative value. It increases with depth and is usually between 0.5 and 10.


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

The first time you run the node, it will download the model (~1.4GB).

```bash
ros2 run ros2_depth_estimation depth_estimation -i /input_topic -o /output_topic
```

Arguments:
* `-i` or `--input-topic`: Input topic of type `sensor_msgs/msg/Image`.
* `-o` or `--output-topic`: Output topic of type `sensor_msgs/msg/Image` (encoding: `32FC1`).
