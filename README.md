# AI Threat Detection using LoRa

This project detects **Animals, Humans, Weapons, and Fire** in real time using a trained **YOLO (Ultralytics)** model. Detection alerts can be transmitted to remote locations using **LoRa communication**.

---

## 🔍 Detected Categories

* **Animal** (deer, elephant, giraffe, tiger, wild boar, zebra)
* **Human**
* **Weapon** (handgun, rifle)
* **Fire**

---

## 📁 Project Structure

```
AI-Threat-Detection-using-LoRa/
├── app.py
├── data.yaml
├── runs/detect/train/weights/best.pt
├── images/
├── labels/
├── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nithinganesh1/AI-Threat-Detection-using-LoRa.git
cd AI-Threat-Detection-using-LoRa
```

### 2️⃣ Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 3️⃣ Run Detection

```bash
python app.py
```

The system starts **live camera detection** using the trained model.

---

## 📌 Model Info

* Framework: **Ultralytics YOLO**
* Trained model path:

```
runs/detect/train/weights/best.pt
```

---

## 📡 Use Cases

* Forest and wildlife monitoring
* Border and security surveillance
* Remote alert systems using LoRa


