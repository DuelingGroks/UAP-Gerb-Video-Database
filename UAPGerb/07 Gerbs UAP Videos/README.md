README for “07 Gerbs UAP Video Analyses” Folder
----------------------------------------------

Overview
--------
This folder contains 37 (and possibly more) video analyses and transcripts by researcher Gerb on the topic of UAP (Unidentified Aerial Phenomena) and alleged special access programs. Each .md file in this folder corresponds to one of Gerb’s videos. Our goal is to collect, refine, and preserve these transcripts and associated metadata in a clear, consistent format.

By maintaining this archive on GitHub, anyone who wishes to contribute corrections, updates, and references can fork the repository and submit pull requests. This ensures community-driven accuracy and transparency regarding Gerb’s video analyses.

File Structure & Naming
-----------------------
Each video has its own .md file, named as follows:

```
  01 Title_of_Video.md
  02 Title_of_Video.md
  ...
  37 Title_of_Video.md
```
Example names:
  01 Wilson_Davis_Memo_Documentary.md
  02 SAP_Secrecy_Exposé.md

Please keep the numbering consistent so that Video #1 always has the filename prefix “01,” Video #2 is “02,” and so on.

Standard Template
-----------------
Below is the recommended layout for each transcript .md file.
```yaml
---
title: "Video Title Here"
video_id: "01"
date_published: "YYYY-MM-DD"
youtube_url: "https://..."
transcript_source: "Part AI / Part Human Corrections"
transcript_status: "In Progress"
contributors:
  - "Gerb"
  - "YourGitHubHandle"
---
```
1. Video Overview
   Include a short summary (one or two paragraphs) about what the video covers: key individuals, the main topic or research angle, and why it is relevant.

2. Show Notes
   List any important links, references, or disclaimers, for example:
   ```markdown
   ## Show Notes
   - References:
     - [Link to memo in Congressional Record](https://...)
     - [Interview with James Rigney](https://...)
   - Related Topics (Obsidian Backlinks):
     - [[Special_Access_Programs]]
     - [[UFO_Reverse_Engineering]]
   ```
3. Background / Context
   Provide more detailed backstory for the video. This helps newcomers understand its significance.

4. Transcript
   This is the core of the file. Indicate how it was produced (AI, manual corrections, etc.). Provide timestamps and speaker labels.
```markdown
   ## Transcript
   ### Transcription Method
   Initial transcript generated with Adobe Premiere auto-transcription, then manually checked by contributors.

   ### Transcript (with Timestamps + Speakers)
   00:00:00 – 00:00:38, Gerb
   > In 2018, a mysterious document...

   (Continue with the rest of the transcript here.)
```
   If the transcript is very long, break it up into subsections or multiple time blocks.

5. Analysis or Commentary (Optional)
   Keep this separate from the raw transcript so that the historical record remains pristine.

6. Changelog (Optional)
   You may add a simple list to note major changes:

```markdown
   ## CHANGELOG
   - 2025-03-09: Created initial transcript (by Gerb)
   - 2025-03-10: Fixed name spelling (by TURFPTAx)
```

How to Contribute
-----------------
1. Fork this repository on GitHub.
2. Clone your fork and create a new branch:
```markdown
   git checkout -b transcript-fixes-video01
```
3. Edit the relevant .md file (e.g., 01 Wilson_Davis_Memo_Documentary.md).
4. Commit and push your changes to your fork.
5. Open a Pull Request from your fork’s branch back into the main repository.

In your Pull Request description, please include:
- Which video(s) you updated
- What corrections or additions you made
- Any references or sources for your changes

By contributing, you affirm that your changes are based on the actual content of Gerb’s video or credible references. Please respect each other’s contributions and abide by the repository’s license and code of conduct.

License and Disclaimer
----------------------
- No Official Affiliation: This project is not officially affiliated with Gerb or any related entity. We are volunteers archiving public, fair-use content for historical and research purposes.
- Non-Commercial / Educational: All transcripts and analyses are intended purely for archival, educational, and commentary purposes.
- Open Source: Unless otherwise indicated, all content is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License (or whichever license this project chooses).

Contact
-------
For questions, open an Issue in the GitHub repository or email the repository maintainer if contact info is provided.

Happy transcribing and exploring!
