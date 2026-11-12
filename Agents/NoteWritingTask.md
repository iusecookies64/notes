Read @Agents/NoteWritingGuidelines.md for note writing guidelines.

---

# Task
So, I am in the process of generating notes for my course subjects. We will generate full notes for every module for every subject one by one. I have not gone through the lectures, but have collected the list of topics for every lesson in each module (week) in a json file. Along with the list of topics, I have also included transcripts of the the lecture that sort of goes over the weeks topics (not exhaustive coverage). This is MSc curriculum, hence you have to keep the depth accordingly (you have to use your judgement for it as what exactly is taught I am not aware), you have to go through the topics and transcript for the week and then first generate a plan of what all topics and subtopics should be covered in the note, what to be taught in every subtopic etc. then once the plan is approved, you will launch subagents that each will be responsible for writing a particular section. Each subagent should generate 2 files, one for content, one for skeleton index, and you will use a simple script to combine the file in the correct order and put in output file. The agents should write the note following the guidelines.

#### Source Materials In:
@tempp/Trimester IV/Deep Learning

#### Output File:
@content/MSC DSAI/Trimester 4/Week 1 - Deep Learning Foundations.md

#### Annotated JSON Blueprint:
```json
{
    "Modules": [
    {
        "Title": "<string: Week Module Title (e.g. 'Week 1: Deep Learning Foundations')>",
        "Modules": [
        {
            "Title": "<string: Lesson Submodule Title (e.g. 'Lesson 1: Foundations of Deep Learning')>",
            "Modules": [
            /* Recursive submodules if present (typically empty: []) */
            ],
            "Topics": [
            {
                "Title": "<string: Topic / Content Item Title (e.g. 'Deep Learning vs Traditional ML')>"
            }
            ]
        }
        ],
        "Topics": [
        /* Direct week-level topics (e.g., Week Overview, Live Sessions, Lecture Recordings) */
        {
            "Title": "<string: Topic Title (e.g. 'Week 1: Overview')>"
        }
        ]
    }
    ]
}
```

#### Key Specifications 

Field Path                             │ Type                                   │ Description
────────────────────────────────────────┼────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────
Modules                                │ Array<Module>                          │ Top-level list containing only weekly modules (Week 0 to Week 13).
Module.Title                           │ string                                 │ Display name of the week or lesson.
Module.Modules                         │ Array<Module>                          │ Child submodules (e.g., lessons within a week). Follows identical recursive schema.
Module.Topics                          │ Array<Topic>                           │ Content items directly belonging to this module level, ordered as displayed on the LMS.
Topic.Title                            │ string                                 │ Display title of the topic/content item (videos, readings, practice quizzes, etc.).
