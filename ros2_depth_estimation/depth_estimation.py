import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import argparse
from transformers import pipeline
from PIL import Image as PILImage
import numpy as np


class DepthEstimator(Node):
    def __init__(self, input_topic: str, output_topic: str):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, output_topic, 10)
        self.bridge = CvBridge()
        self.listener = self.create_subscription(Image, input_topic, self.image_callback, 10)
        self.estimator = pipeline(task="depth-estimation", model="Intel/dpt-large")

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        pil_image = PILImage.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
        depth_image = 1 / (np.array(self.estimator(pil_image)['depth'])/100 + 1e-6)
        self.publisher_.publish(self.bridge.cv2_to_imgmsg(np.array(depth_image, dtype=np.float32), encoding='32FC1'))



def main(args=None):
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_topic', type=str, required=True, help='Input topic name')
    parser.add_argument('-o', '--output_topic', type=str, default='/camera/depth', help='Output topic name')
    cmdline_args = parser.parse_args()

    # run the node
    rclpy.init(args=args)
    image_publisher = DepthEstimator(cmdline_args.input_topic, cmdline_args.output_topic)
    rclpy.spin(image_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
