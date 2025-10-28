# 🌐 Al Yamamah Community

> A blog, news, and event platform for **Al Yamamah University**, enhanced with **YU AI** — an intelligent chatbot for university-related questions.  
> Built using **Django**, **Tailwind CSS**, and **OpenAI’s API**, this project connects students, staff, and clubs in one smart digital community.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2%2B-green?logo=django)
![TailwindCSS](https://img.shields.io/badge/Frontend-TailwindCSS-38bdf8?logo=tailwind-css)
![OpenAI](https://img.shields.io/badge/OpenAI-Integration-black?logo=openai)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧠 Overview

**Al Yamamah Community** is a web platform designed for **Al Yamamah University** to bring together blogs, news, and events into one space — supported by an AI assistant named **YU AI**.  

It aims to **empower communication** across the university by allowing users to:
- Publish and moderate **blogs** 📝  
- Post and view **events and announcements** 📅  
- Read the latest **university news** 📰  
- Chat with **YU AI** for general university questions 🤖  

This project blends **technology**, **community**, and **AI** to create a more connected digital campus.

---

## ✨ Features

- 📰 **News Hub** — Post, edit, and view university updates  
- 📅 **Event Management** — Manage and link related events and blogs  
- 🧠 **YU AI Assistant** — Answer general questions about Al Yamamah University  
- ✍️ **Blog System** — With moderation, descriptions, and author pages  
- 🏫 **Club Pages** — Connect posts and members to student clubs  
- 👤 **Writer Profiles** — Simple author pages with social links  
- 🌙 **Dark Mode** — Optional dark/light theme toggle  
- 📧 **Email System** — Moderator notifications and password resets  

---

## 🚀 Getting Started

### 🧩 Dependencies
Make sure you have the following installed:
- Python **3.9+**
- Django **4.2+**
- Node.js (for Tailwind)
- `django-tailwind`
- `openai` (Python SDK)
- A valid **OpenAI API Key**

---

### ⚙️ Installation

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/Al-Yamamah-Community.git
cd Al-Yamamah-Community
````

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```python
SECRET_KEY="your_django_secret_key"
OPENAI_API_KEY="your_openai_api_key"
```

---

### 🧪 Running the Project

#### Start Django

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Run Tailwind (in a separate terminal)

```bash
python manage.py tailwind install
python manage.py tailwind start
```

Then open your browser at:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🛠️ Common Issues

| Issue                | Solution                                                  |
| -------------------- | --------------------------------------------------------- |
| Django not found     | Ensure it’s installed with `pip install django`           |
| Tailwind not working | Run `python manage.py tailwind start` in another terminal |
| AI not responding    | Verify your `OPENAI_API_KEY` is active in `.env`          |
| Database errors      | Run `python manage.py migrate` and try again              |

You can also use:

```bash
python manage.py check
```

to verify your Django setup.

---

# 🗺️ Project Roadmap — Personal Website

Last Updated: 2025/10/28

Current Version: v1.5

Status: Active Development 🚧

- [ ] Make all the profile pictures user's profile picture. 
- [ ] Contact page
## ✅ Recent Fixes

- Fixed **blog UI bugs** on both the **Blog Page** and **Index Page**.
    
- Added **author-only edit/delete** functionality for posts.
    
- Implemented **re-approval queue** for all post updates.
    

## 🎯 Version 1.5 — Foundation Build

Goal: Establish the website’s base features, improve usability, and prepare for scalable community tools.

Duration: ~2 weeks

### 🧩 Core Improvements

#### 🧠 General Enhancements

- [ ] 🌓 Implement **Dark Mode** with theme persistence
    
- [ ] 🧩 Improve **AI Knowledge Base** with richer internal data
    
- [ ] 🔗 Connect **AI Assistant** with live **news and events** APIs
    
- [ ] 🗞️ Sync **News or blogs** and **Events** with mutual linking
    
- [ ] 📅 **Rewrite the calendar** with a clean, interactive layout
    
- [x] 🔒 Add **blog moderation system** (hidden until approved)
    
- [ ] 📧 Integrate **email notifications** for moderators alerts + password reset
    
- [ ] 🏷️ Add **description fields** to blogs and news (SEO & summaries)
    
- [ ] 🔗 Allow **events to link** to related blogs or news items
    
- [x] ✍️ Added **Update & Delete** features for writers.
    
- [x] 🔄 Posts are **hidden on update** and require re-approval.
    
- [ ] Render Deployment
      
- [ ] Description for better card layout

- [ ] Contact page

### 🏫 Club Page

**Goal:** Introduce a structured page for campus clubs and members.

**Tasks**

- [x] Create **Club Page** displaying club name, logo, and activities
    
- [x] Connect **blogs & news** authored by club members to their club page
    
- [ ] Add **club membership roles** and social/contact links
    
- [x] Added **Header & Logo** fields for club customization.
    

### ✍️ Writer Page

**Goal:** Highlight contributors and their content.

**Tasks**

- [x] Build **Writer Page** with profile (photo, name, short bio, social links)
    
- [x] Display **list of posts** for the writer
    
- [x] Connect **writer** to **club (if any)**
    
- [x] Added **Profile Picture & Header** fields for writers.
    
- [ ] Create a "My Posts" Page for Writers
## 🔮 Version 1.2 — Community & AI Expansion (Planned)

**Goal:** Enhance interactivity, automation, and personalization.

**Focus Areas**

- [ ] Real-time **AI data updates** from blogs, news, and events
    
- [ ] Add **user dashboard** for writers and club admins
    
- [ ] Improve **moderation tools** and **admin analytics**
    

## 🧭 Future Vision

TBD

## 🤝 Contributing

Pull requests are welcome!

If you’d like to contribute, please open an issue first to discuss proposed changes.

## 🧰 Tech Stack

- **Backend:** Django
    
- **Frontend:** Tailwind CSS
    
- **AI:** Open AI Chat
    
- **Hosting:** PythonAnywhere, Note: Latter it'll be hosted on render
    

> _“Build small. Iterate fast. Ship proudly.”_

## 👨‍💻 Author

**Fayez Al-Qhatani**

* 🐦 X (Twitter): [@Fayez_Alshwayya](https://x.com/Fayez_Alshwayya)
* 🌐 Website: [fayezs.site](https://fayezshwayya.pythonanywhere.com/)
* 💻 GitHub: [FKQ7](https://github.com/FKQ7)

---

## 🧾 Version History

| Version | Date       | Description                          |
| ------- | ---------- | ------------------------------------ |
| `0.1`   | 2025/10/08 | Initial release — base website build |
| `1.5`   | 2025/10/08 | ... |


---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE.md](LICENSE.md) file for details.

---

> *“Building a smarter, more connected university — one line of code at a time.”* 💡

```
