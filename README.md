**SkillSwap – Skill Sharing & Mentorship Platform**
SkillSwap is a Django-based web application built on a give-and-take learning model, where users can both teach and learn skills from each other.
The platform connects learners with suitable instructors, enables session scheduling, and promotes peer-to-peer knowledge sharing.

**Project Overview**
SkillSwap aims to solve a common problem: Many people want to learn new skills, and many already have valuable skills to teach — SkillSwap bridges this gap. Instead of one-way learning, SkillSwap creates a collaborative learning ecosystem where users exchange knowledge through 1-on-1 sessions.

**Tech Stack**

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Forms: Django Forms & Crispy Forms

Database: SQLite

Authentication: Django Auth System

ORM: Django ORM

Clean UI with reusable templates

File upload handling (profile pictures)

**Core Concepts Implemented**

Django Models & Relationships (Foreign Keys)

ModelForms and custom validations

CRUD operations

Django ORM queries

Messages framework for user feedback

Role-based logic (Learner vs Instructor)
🚀 Key Features
🔐 User Authentication & Profiles

User registration and login using Django authentication

**Profile management with:**

Bio

Education

Specialization

LinkedIn URL

Profile picture

Dashboard showing personalized actions and status

**Skill Management**

Add skills you can teach

Add skills you want to learn

Edit and delete skills

Validation prevents:

Duplicate skills

Teaching and learning the same skill

**Smart Skill Matching**
Learners are matched with instructors based on overlapping skills

View detailed instructor profiles including:

Skills they teach

Experience level

Education and specialization

Reviews and ratings

**Session Requests & Scheduling**

Learners can send session requests to instructors

Instructors can:

Accept or reject requests (with reason)

Schedule sessions with date, time, and Google Meet link

Both learners and instructors can view upcoming sessions

**Notifications**

Notification system for:

Session requests

Acceptance or rejection

Session scheduling

Session cancellation

Dedicated notifications page for users

**Reviews & Ratings**

Learners can submit reviews and ratings after session completion

Reviews are displayed on instructor profiles

Helps future learners make informed decisions

**Session Cancellation & Completion**

Sessions can be cancelled by learner or instructor

Cancellation reason is visible to the opposite user

Sessions can be marked as completed after successful learning

