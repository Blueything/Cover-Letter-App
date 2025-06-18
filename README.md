# 📝 Cover Letter Generator App

Generate customized, professional cover letters instantly — tailored to the **company**, **role**, and **technologies** you're applying for. Built with **Streamlit** and **FPDF**, this app helps streamline your job application workflow with clean formatting and PDF export.

![Cover Letter Demo](./assets/cover-letter-preview.png)

---

## 🎯 Purpose

Job hunting is time-consuming. This app simplifies one key part: **creating tailored cover letters** for every job application. With a few inputs, you can instantly generate a polished, PDF-ready cover letter aligned with your resume and job target.

---

## 🚀 Features

- 🧠 Smart text templating based on role, company, and tech stack
- 📄 Real-time **PDF generation** using `fpdf`
- 🔗 Auto-linked **LinkedIn** and **email**
- 🧑 Personal details auto-filled (name, phone, university, etc.)
- 🖥️ Interactive UI using **Streamlit**
- 📥 One-click PDF **download button**

---

## 🧰 Tech Stack

| Layer        | Technologies                        |
|--------------|-------------------------------------|
| Frontend     | Streamlit                           |
| PDF Engine   | FPDF (Python)                       |
| Language     | Python 3.x                          |
| Hosting      | Streamlit Cloud / Localhost         |

---

## 📦 Folder Structure

```plaintext
/
├── app.py                    # Main Streamlit app
├── assets/
│   └── cover-letter-preview.png
├── requirements.txt          # Python dependencies
└── README.md
