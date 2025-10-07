Aici este fișierul `README.md` în format Markdown, păstrând toate informațiile originale.

````markdown
# EmotiNest

---

## 1. Introduction

### Project Overview
**EmotiNest** is a web application designed to help users monitor and improve their **mental well-being**. Users can log daily entries to track their emotional state, stress levels, sleep quality, and other metrics. The platform also offers self-assessment tests for mental health conditions like **ADHD, anxiety, and depression**. Through data visualization, users can analyze their mental health trends and set personal improvement goals.

### Target Audience
EmotiNest is designed for anyone who wants to **keep track their mental health**, understand emotional patterns, and set goals for improvement.

---

## 2. Features

* **User Authentication:** Secure login, logout, and registration.
* **Home Page:** Displays an overview of the user’s progress. Allows users to set and track personal goals.
* **Daily Forms:** Track emotional state, stress level, sleep quality, and more. Users can submit only one form per day.
* **Statistics:** Visual representation of daily, weekly, and monthly trends using interactive graphs.
* **Self-Assessment Tests:** Tests for **ADHD, anxiety, depression, and job burnout**. Provides personalized feedback and recommendations.

---

## 3. Detailed Component Design

* **Backend:** Flask (Python), SQLite for database management.
* **Frontend:** HTML, CSS, JavaScript (Chart.js for graphs).
* **Deployment:** Docker

---

## 4. Running the application

### Steps

1.  **Build the Docker Image:**
    ```bash
    docker build -t emotinest .
    ```
2.  **Run the Container:**
    ```bash
    docker run -dp 5000:5000 emotinest
    ```
3.  **Access the Application:**
    ```
    http://localhost:5000
    ```

---

## 5. Team Contributions

### Beatrice Elena Sălăvăstru
* User authentication (login, signup, logout).
* Home Page: Developed the logic and implementation for displaying user statistics (e.g., stress levels, energy, water intake, etc.).
* Statistics page with data visualization for weekly data trends.
* Integration of forms and their validation.
* Docker setup for deployment.
* Debugging and improving the deployment process.

### Irina Daniela Munteanu
* Home Page: Built and implemented the goal management feature (adding, deleting, and listing goals).
* Integration of tests for ADHD, anxiety, depression, and job burnout.
* Forms Page: Created and validated the daily tracking form (e.g., stress, sleep, happiness levels).
* Worked on the responsiveness and design consistency of various components.
* Debugging and improving the deployment process.

We collaboratively built the project's foundation, including the database schema and primary structure. Additionally, we worked extensively on styling to ensure a responsive, visually appealing, and user-friendly design. By working side by side and contributing to each other's sections, the workload was distributed equitably, and the level of effort was approximately equal for both team members.

---

## 6. Challenges Encountered

During the development process, we encountered a number of challenges that required creative solutions. One of the key hurdles was managing **port conflicts and environment mismatches** while setting up **Docker**, which we addressed by fine-tuning container configurations and ensuring proper port assignments. Another issue was ensuring all fields in the daily form were filled out and **validated correctly**. To tackle this, we implemented more robust validation logic and provided clear feedback to users. Navigating the complexities of **linking pages correctly** also proved tricky, but through careful debugging and testing, we ensured smooth navigation throughout the application. Lastly, we worked hard to make sure the data from the daily form was **accurately captured and reflected in the statistics page**. By refining database queries and introducing better error handling, we were able to ensure reliable and meaningful data presentation.
````
