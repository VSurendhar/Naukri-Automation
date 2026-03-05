# 🚀 Naukri Profile Auto-Updater

> Automate your Naukri profile summary updates daily — stay at the top of recruiter searches without lifting a finger.

---

## 📌 Why This Project?

When employers search for candidates on Naukri, they typically focus on the **top N profiles** returned by the platform's ranking algorithm. One of the key signals Naukri uses to rank profiles is **how recently the profile was updated**.

Manually updating your profile every morning is tedious — and easy to forget. This project automates that entire process using a Python script powered by **Selenium** and **python-dotenv**, so your profile stays fresh and visible to recruiters every single day.

---

## ⚙️ How It Works

1. **Launches a browser** (via Selenium WebDriver)
2. **Navigates to** [naukri.com](https://www.naukri.com)
3. **Logs in** using your credentials stored securely in a `.env` file
4. **Finds the Profile Summary section** on your profile page
5. **Rotates to the next summary variant** (from your 3 pre-defined versions)
6. **Saves the update** — triggering Naukri's "recently updated" signal
7. **Uploads your Resume** — This acts as a secondary "profile updated" signal. By re-uploading the resume file, you double the signals sent to Naukri's ranking algorithm, ensuring maximum visibility.

> 💡 The summary rotation ensures each update is genuinely different from the last, which prevents Naukri's algorithm from treating it as a duplicate update.

---

## 📄 Dynamic Resume Fetching

The script is designed to be fully automated and maintainable without hardcoding specific filenames. Instead of pointing to a single file, it uses a **Dynamic Folder Strategy**:

- It looks into a designated folder (e.g., `~/Desktop/Personal/resume`).
- It automatically identifies and selects the **first file** found in that directory.
- This allows you to update your resume file in that folder without ever having to modify the script's source code.


---

## 📁 Project Structure

```
NaukriAutomation/
├── .venv/                      # Python virtual environment
├── .env                        # Your credentials and profile summaries (never commit this!)
├── chromedriver                # ChromeDriver binary bundled with the project
├── cron.log                    # Log file generated after each cron run
├── main.py                     # Main Python automation script
└── run_naukri_automation.sh    # Shell script to run the automation
```

---

## 🔐 Setting Up Your `.env` File

Create a file named `.env` in the root of the project directory with the following five variables:

```env
NAUKRI_EMAIL=your_email@example.com
NAUKRI_PASSWORD=your_secure_password
PROFILE_SUMMARY_1="Experienced software engineer with 5+ years building scalable web applications using Python, Django, and React. Passionate about clean code and agile development."
PROFILE_SUMMARY_2="Software engineer with half a decade of hands-on experience crafting robust web solutions. Proficient in Python, Django, and React with a strong focus on performance and maintainability."
PROFILE_SUMMARY_3="Versatile software engineer skilled in Python, Django, and React, with over five years of experience delivering high-quality, scalable applications in fast-paced environments."
```

> ⚠️ **Important:** Keep your `.env` file private. Never push it to GitHub or any public repository. Add `.env` to your `.gitignore`.

### Why Three Summaries?

Each summary should convey the same core message about your skills and experience — but worded differently. Even changing **a single word** is enough to signal a fresh update to Naukri's algorithm. The script rotates between these three variants each time it runs, keeping your updates authentic.

---

## 🐍 Running the Script Manually

### Prerequisites

```bash
pip install selenium python-dotenv
```

> ChromeDriver is bundled directly in the project folder, so no additional driver setup is needed.

### Run via Python

```bash
python3 main.py
```

### Run via Shell Script

Make the shell script executable (only needed once):

```bash
chmod +x run_naukri_automation.sh
```

Then run it:

```bash
./run_naukri_automation.sh
```

### `run_naukri_automation.sh` — Shell Script Contents

```zsh
#!/bin/zsh
set -e

# Load env vars
source ~/.zshrc

# Go to project folder
cd ~/CodingProjects/PythonProjects/NaukriAutomation/

# Activate venv
source .venv/bin/activate

# Run script
python3 main.py
```

---

## ⏰ Scheduling with Cron on macOS

To run this automation every morning automatically, you can set up a **cron job** using `crontab`.

### Step 1 — Open the Crontab Editor

```bash
crontab -e
```

### Step 2 — Add a Cron Job

The following example schedules the script to run every day at **8:00 AM**:

```cron
0 8 * * * /bin/zsh ~/CodingProjects/PythonProjects/NaukriAutomation/run_naukri_automation.sh >> ~/CodingProjects/PythonProjects/NaukriAutomation/cron.log 2>&1
```

> 📂 Replace the path above with the actual absolute path to your `run_naukri_automation.sh` file if it differs from the one shown.

**Cron syntax breakdown:**

| Field  | Value | Meaning        |
|--------|-------|----------------|
| Minute | `0`   | At minute 0    |
| Hour   | `8`   | At 8:00 AM     |
| Day    | `*`   | Every day      |
| Month  | `*`   | Every month    |
| Weekday| `*`   | Every weekday  |

### Step 3 — Grant Terminal Full Disk Access (macOS)

On macOS, cron jobs may be blocked by system permissions. To fix this:

1. Open **System Settings** → **Privacy & Security** → **Full Disk Access**
2. Click the **+** button and add `/usr/sbin/cron`
3. Restart your terminal

### Step 4 — Verify the Cron Job is Set

```bash
crontab -l
```

You should see your scheduled job listed.

---

## 📋 Tips for Best Results

- **Run in the morning** — Naukri search rankings tend to favour recently updated profiles, and recruiters are most active in the morning.
- **Keep summaries professional** — All three variants should genuinely reflect your skills and experience.
- **Test the script manually first** — Before connecting it to cron, run it once to confirm it logs in and updates correctly.
- **Use a virtual environment** — Isolate your dependencies using `python3 -m venv venv` to avoid conflicts.

---

## 🛡️ Security Notes

- Your `.env` file contains sensitive credentials. **Never share it or commit it to version control.**
- Add the following to your `.gitignore`:
  ```
  .env
  cron.log
  ```

---

## 🧰 Dependencies

| Library         | Purpose                            |
|-----------------|------------------------------------|
| `selenium`      | Browser automation                 |
| `python-dotenv` | Load credentials from `.env` file  |

Install all at once:

```bash
pip install selenium python-dotenv
```

---

## 📝 Note

This project is for personal use. Please use it responsibly and in accordance with [Naukri's Terms of Service](https://www.firstnaukri.com/freshersmnj/mynaukri.php/Show/termsAndConditions).

---

---

⭐ **If this project saved you some time, feel free to give it a star — it's free. I won't charge you for that.**

---

*Built with ❤️ to save you 2 minutes every morning — and keep your career opportunities flowing.*