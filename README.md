# README

First draft content about new bot focus on `AWS Solution Architect Trainer Bot`

The bot will focus UX/UI on Trainer Bot including:

- Course study model: 
  - SR learning model to help on learning slowly and consistently
- Practice model for prepare a certificate examination:
    - **Exam Mode**
      In exam simulation mode, you complete one full-length practice exam and answer all 65 questions within the allotted time. You are then presented with a pass / fail score report showing your overall score and performance in each knowledge area to identify your strengths and weaknesses.
    - **Training Mode**
  When taking the practice exam in training mode, you will be shown the answers and explanations for every question after clicking “check”. Upon completion of the exam, the score report will show your overall score and performance in each knowledge area.
    - **Knowledge Reviews**
  Now that you have identified your strengths and weaknesses, you get to dive deep into specific areas with our knowledge reviews. You are presented with a series of questions focussed on a specific topic. There is no time limit and you can view the answer to each question as you go through them.
  - **Final Exam Simulator**
  The exam simulator randomly selects 65 questions from our pool of over 500 unique questions – mimicking the real AWS exam environment. The practice exam has the same format, style, time limit and passing score as the real AWS exam

## Implementation ideal   

We can reuse the SR system for course study learning model but we need more on UX including:

- Instead of just pickup the cards: we create review session and learning new session
- A knowledge repo == A study course , a session == a deck. Each session including many cards relative its topic. 

The reminder on noat.cards bot should be modified to archive 2 different things bellow: 

- Remember the last check point ? and resume from the last check point when people want to continue learning from the last check point 
- Apply review the old knowledge follow SR concept. 
- Verifying knowledge on a session by quiz test which including quiz questions defined/assigned for the session and auto ranking the knowledge belong the session based on grade score of quiz test.


## Implementation in action

### Modeling the schema of knowledge repo 

```yaml
type: noatcards
contents:
  - file: "01_aws_compute.md"
    test:
      - file: "01_aws_compute_quiz.md"
```
