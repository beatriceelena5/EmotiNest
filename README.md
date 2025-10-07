# EmotiNest

---

## 1. Introduction

### Project Overview
**EmotiNest** is a web application designed to help users monitor and improve their **mental well-being**. Users can log daily entries to track their emotional state, stress levels, sleep quality, and other metrics. The platform also offers self-assessment tests for mental health conditions like **ADHD, anxiety, and depression**. Through data visualization, users can analyze their mental health trends and set personal improvement goals.

### Target Audience
EmotiNest is designed for anyone who wants to **track their mental health**, understand emotional patterns, and set goals for improvement.

---

## 2. Features

- **User Authentication:** Secure login, logout, and registration.  
- **Home Page:** Displays an overview of the user’s progress and allows users to set and track personal goals.  
- **Daily Forms:** Track emotional state, stress level, sleep quality, and more. Users can submit only one form per day.  
- **Statistics:** Visual representation of daily, weekly, and monthly trends using interactive graphs.  
- **Self-Assessment Tests:** Tests for ADHD, anxiety, depression, and job burnout, providing personalized feedback and recommendations.

---

## 3. Detailed Component Design

- **Backend:** Flask (Python), SQLite for database management.  
- **Frontend:** HTML, CSS, JavaScript (Chart.js for graphs).  
- **Deployment:** Docker  

---

## 4. Running the Application

### Steps
1. **Build the Docker Image:**  
   ```bash
   docker build -t emotinest .
   ```
2. **Run the Container:**  
   ```bash
   docker run -dp 5000:5000 emotinest
   ```
3. **Access the Application:**  
   [http://localhost:5000](http://localhost:5000)

---

## 5. Team Contributions

### Beatrice Elena Sălăvăstru
- Implemented user authentication (login, signup, logout).  
- Developed the **Home Page** logic for displaying user statistics (stress levels, energy, water intake, etc.).  
- Built the **Statistics Page** with data visualization for weekly data trends.  
- Integrated and validated user input forms.  
- Configured **Docker** for deployment.  
- Debugged and improved the deployment process.

### Irina Daniela Munteanu
- Implemented the **Goal Management Feature** (adding, deleting, and listing goals) on the Home Page.  
- Integrated tests for **ADHD, anxiety, depression, and job burnout**.  
- Created and validated the **Daily Tracking Form** (stress, sleep, happiness levels).  
- Worked on **responsiveness** and design consistency across components.  
- Debugged and improved the deployment process.

Together, we collaboratively built the project's foundation, including the database schema and primary structure.  
We also worked extensively on styling to ensure a **responsive**, **visually appealing**, and **user-friendly** design.  
By contributing equally to different sections and supporting each other, the **workload was balanced** and effort evenly distributed.

---

## 6. Challenges Encountered

During development, several challenges required creative solutions:

- **Docker Configuration:** Managing port conflicts and environment mismatches. Solved by fine-tuning container configurations and ensuring proper port assignments.  
- **Form Validation:** Ensuring all daily form fields were properly filled and validated. Implemented robust validation logic and clear feedback to users.  
- **Page Linking:** Navigating the complexities of linking pages correctly. Achieved smooth navigation through systematic debugging and testing.  
- **Data Accuracy:** Ensuring that daily form data was accurately captured and reflected in statistics. Refined database queries and improved error handling for reliable, meaningful data presentation.

---
