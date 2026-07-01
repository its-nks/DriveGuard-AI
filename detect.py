"""
detect.py
Road Damage Detection using YOLOv8
Member 4 - DriveGuard AI
"""

from ultralytics import YOLO

# Load trained YOLO model
model = YOLO("best.pt")


def detect_damage(image_path):
    """
    Detect road damages from an input image.

    Args:
        image_path (str): Path to the input road image.

    Returns:
        YOLO detection results
    """

    results = model.predict(source=image_path, conf=0.25, save=True)

    return results


if __name__ == "__main__":
    image = "sample.jpg"  # Replace with your test image
    detect_damage(image)
