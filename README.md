# **SkillSwap – Skill Sharing & Mentorship Platform**

SkillSwap is a **Django-based web application** built on a *give-and-take learning model*, where users can both **teach and learn skills** from each other.  
The platform connects learners with suitable instructors, enables **session scheduling**, and promotes **peer-to-peer knowledge sharing** through 1-on-1 sessions.

---

## **📌 Project Overview**

SkillSwap addresses a common challenge:

> Many people want to learn new skills, and many already have valuable skills to teach — **SkillSwap bridges this gap**.

Instead of one-way learning, SkillSwap creates a **collaborative learning ecosystem** where users exchange knowledge through structured learning sessions.

---

## **🛠️ Tech Stack**

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Forms:** Django Forms & Crispy Forms
- **Database:** SQLite
- **Authentication:** Django Authentication System
- **ORM:** Django ORM
- **UI:** Responsive UI using reusable templates
- **Media Handling:** Profile picture upload & management

---

## **🧠 Core Django Concepts Implemented**

- Django Models & Relationships (Foreign Keys)
- ModelForms with **custom validation**
- CRUD operations
- Django ORM queries
- Django Messages framework
- Role-based logic (Learner vs Instructor)
- Template inheritance & reusable components

---

## **🚀 Key Features**

### **🔐 User Authentication & Profiles**
- User registration and login using Django authentication
- Profile management including:
  - Bio
  - Education
  - Specialization
  - LinkedIn URL
  - Profile picture
- Personalized dashboard with user-specific actions

---

### **🎓 Skill Management**
- Add skills you can **teach**
- Add skills you want to **learn**
- Edit and delete skills
- Validation prevents:
  - Duplicate skills
  - Teaching and learning the same skill

---

### **🤝 Smart Skill Matching**
- Learners are matched with instructors based on overlapping skills
- View detailed instructor profiles with:
  - Skills offered
  - Experience level
  - Education & specialization
  - Reviews and ratings

---

### **📅 Session Requests & Scheduling**
- Learners can send session requests to instructors
- Instructors can:
  - Accept or reject requests (with reason)
  - Schedule sessions with date, time, and Google Meet link
- Both users can view upcoming sessions

---

### **🔔 Notifications**
- Real-time notifications for:
  - Session requests
  - Acceptance or rejection
  - Session scheduling
  - Session cancellation
- Dedicated notifications page

---

### **⭐ Reviews & Ratings**
- Learners can submit reviews after session completion
- Ratings are displayed on instructor profiles
- Helps future learners make informed decisions

---

### **❌ Session Cancellation & Completion**
- Sessions can be cancelled by learner or instructor
- Cancellation reason is visible to both users
- Sessions can be marked as **completed**

---

## **✅ Summary**

SkillSwap demonstrates **end-to-end Django development**, covering:

- Authentication & authorization
- Database design & validation
- Role-based workflows
- User-centric UI design
- Real-world business logic implementation

This project serves as a strong portfolio example of building a **scalable, full-stack Django web application**.
