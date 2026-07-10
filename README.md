# 🚀 Model Rocket Data Collection

Rocket.py - Utilizes basic kinematic equations to model the height and velocity of a model rocket. To simulate noise in data collection, Gaussian noise is added to the list of heights. 

Rocketry.py - Uses a butter filter from scipy to filter data and reduce noise, especially when solving for velocity


## ✨ Features
* Kinematic physics calculations
* Graphical visualization of height and velocity
* Added Gaussian noise to simulate realistic noise in data collection
* Butter filter to filter out certain frequencies

## 📈 Graphs
Normalized Cutoff Frequency of .1 * sampling rate
<img width="636" height="557" alt="Screenshot 2026-07-10 155503" src="https://github.com/user-attachments/assets/5cd161a4-3f0b-4d81-bfe6-613ac4977730" />





## 📦 Installation

Necessary Libraries

```bash
pip install numpy
pip install matplotlib
pip install scipy


