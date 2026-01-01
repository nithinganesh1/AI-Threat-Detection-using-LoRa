import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")  

# Class group mapping
GROUP_MAP = {
    "Animal": [0, 1, 2, 5, 6, 7],
    "Human": [3],
    "Weapon": [8, 10],
    "Fire": [9]
}

# Reverse lookup: class_id -> group_name
CLASS_TO_GROUP = {}
for group, ids in GROUP_MAP.items():
    for i in ids:
        CLASS_TO_GROUP[i] = group

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO inference
    results = model(frame, conf=0.4, verbose=False)

    for r in results:
        boxes = r.boxes
        if boxes is None:
            continue

        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            # Check if class belongs to any group
            if cls_id not in CLASS_TO_GROUP:
                continue

            group_label = CLASS_TO_GROUP[cls_id]

            # Bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Color by group
            if group_label == "Animal":
                color = (0, 255, 0)
            elif group_label == "Human":
                color = (255, 0, 0)
            elif group_label == "Weapon":
                color = (0, 0, 255)
            elif group_label == "Fire":
                color = (0, 165, 255)
            else:
                color = (255, 255, 255)

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Label text
            label = f"{group_label} {conf:.2f}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
