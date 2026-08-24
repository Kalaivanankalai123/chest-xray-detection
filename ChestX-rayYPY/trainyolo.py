from ultralytics import YOLO

# Initialize a YOLOv8 model with pre-trained weights (yolov8n.pt)
model = YOLO('yolo11n.pt')  # Load a pre-trained model (YOLOv8 nano)

# Set up training parameters
model.train(
    data='datasets/data.yaml',  # Path to the dataset YAML file
    epochs=10,                  # Number of epochs
    imgsz=440,                  # Image size (640x640 in this case)
    batch=2                    # Batch size
    #device=1                    # Use GPU 0 (set device=-1 for CPU)
)
