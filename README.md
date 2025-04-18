🔥 Project Overview
💡 Project Name: "Employee API – CI/CD Pipeline with Docker & Jenkins"
🧠 Tech Stack:
Language: Python (Flask)

Tools: Docker, GitHub, Jenkins

App: A RESTful API for employee management

Goal: Automate build, test, and deployment using Jenkins pipeline


✅ Jenkins Setup – Step-by-Step Guide
🔹 Step 1: Launch an AWS EC2 Ubuntu Instance
Select Ubuntu 20.04

Allow ports: 22, 5000, 8080

SSH into it

🔹 Step 2: Install Jenkins and Docker
# Update packages
sudo apt update

# Install Java
sudo apt install openjdk-11-jdk -y

# Install Jenkins
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Install Docker
sudo apt install docker.io -y
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins


🔹 Step 3: Access Jenkins Dashboard
Go to: http://<EC2-IP>:8080

Get initial password:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword



🔹 Step 4: Create a Pipeline Job
Click New Item

Choose Pipeline

Scroll down to Pipeline Script, and paste the Jenkinsfile code above.

Save

🔹 Step 5: Push Your Code to GitHub
Create a GitHub repo like employee-api, and push your code:
git init
git remote add origin https://github.com/your-username/employee-api.git
git add .
git commit -m "Initial commit"
git push -u origin master

🔹 Step 6: Run Your Pipeline
Go to Jenkins > your project > click Build Now

After build success, access your app:
👉 http://<EC2-IP>:5000/employees


