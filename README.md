# who-ghosted-me  

Python scripting can make life a lot easier when it comes to automating repetitive daily tasks that eat up hours of your week. It’s great for digging through data, spotting patterns, and pulling out insights that help drive decisiong making. But sometimes, it’s just as useful for checking if your ex-girlfriend’s dog’s Instagram page still follows you.

# what this script does
This script compares your Instagram followers and following lists from the official JSON data export (instructions below) and tells you who isn’t following you back.

# how it does this?
1. The script Reads both files (followers, and following) and extracts usernames from each.

2. Compares them to find accounts you follow that don’t follow you back.

3. Prints that list right in your terminal.

4. In short: two files go in, three lists come out — followers, following, and the painful truth.

### 📥 How to Download Your Instagram Data

1. Tap your **profile picture** in the bottom right to go to your profile.  
2. Tap **☰ (more options)** in the top right → **Your activity**.  
3. Under **Information you shared with Instagram**, tap **Download your information**.  
4. Enter your **email address** (if prompted), then tap **Request a download**.  
5. For **Select information**, choose **Select types of information**.  
6. Scroll down and check **Followers and following**.  
7. Under **Select file options**, set:  
   - **Format:** JSON  
   - **Date range:** All time *(important)*  
8. Tap **Submit request**.  
9. Wait for the email titled **Your Instagram Data** (usually arrives within an hour).  
10. Tap **Download data** and follow the instructions to download your ZIP file.  
11. Once downloaded, **unzip** it — you’ll see folders like:  
    ```
    connections/
        followers_and_following/
            followers_1.json
            following.json
    ```

---

### 🧰 How to Run the Script

1. Make sure **Python 3.7+** is installed.  
2. Place this project folder in the same directory as your downloaded `connections` folder.  
3. Open a terminal and run:
   ```bash
   python who_ghosted_me.py
